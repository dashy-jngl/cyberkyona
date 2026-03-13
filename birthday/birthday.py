import discord
from redbot.core import commands
from datetime import datetime, date, timezone
from typing import Dict, List, Optional, Tuple
import aiohttp
import asyncio
import re

API_URL = "https://joshitori.com/api/wrestlers"
IMAGE_BASE = "https://joshitori.com"
CACHE_TTL = 86400  # 1 day in seconds

PINK = discord.Color.from_rgb(255, 105, 180)


class Birthday(commands.Cog):
    """Show joshi birthdays from the Joshitori database."""

    __version__ = "2.0.0"

    def __init__(self, bot):
        self.bot = bot
        self._cache: List[dict] = []
        self._cache_time: float = 0

    def cog_unload(self):
        pass

    # ── data layer ──────────────────────────────────────────

    async def _fetch_wrestlers(self) -> List[dict]:
        """Fetch all wrestlers from Joshitori API with caching."""
        now = asyncio.get_event_loop().time()
        if self._cache and (now - self._cache_time) < CACHE_TTL:
            return self._cache

        async with aiohttp.ClientSession() as session:
            async with session.get(API_URL, timeout=aiohttp.ClientTimeout(total=30)) as resp:
                resp.raise_for_status()
                data = await resp.json()

        # filter to wrestlers with real birthdays
        valid = []
        for w in data:
            bd = w.get("birthday", "")
            if bd and not bd.startswith("0001"):
                valid.append(w)

        self._cache = valid
        self._cache_time = now
        return valid

    UNKNOWN_YEAR = 1900  # sentinel for known month/day but unknown year

    @staticmethod
    def _parse_birthday(bd_str: str) -> Optional[date]:
        """Parse ISO birthday string to date."""
        if not bd_str or bd_str.startswith("0001"):
            return None
        try:
            return datetime.fromisoformat(bd_str.replace("Z", "+00:00")).date()
        except (ValueError, TypeError):
            return None

    @classmethod
    def _year_known(cls, bd: date) -> bool:
        """Check if the birth year is actually known (not a sentinel)."""
        return bd.year != cls.UNKNOWN_YEAR

    @staticmethod
    def _get_image(wrestler: dict) -> Optional[str]:
        """Get the best image URL for a wrestler."""
        local = wrestler.get("image_local", "")
        if local:
            return f"{IMAGE_BASE}{local}"
        return wrestler.get("image") or None

    @staticmethod
    def _get_aliases(wrestler: dict) -> List[str]:
        """Get alias names (excluding the main name)."""
        aliases = wrestler.get("aliases") or []
        main = wrestler.get("name", "")
        return [a["alias"] for a in aliases if a.get("alias") and a["alias"] != main]

    @staticmethod
    def _age(born: date, today: date) -> int:
        """Calculate age in years."""
        age = today.year - born.year
        if (today.month, today.day) < (born.month, born.day):
            age -= 1
        return age

    # ── activity filter ─────────────────────────────────────

    ACTIVE_YEARS = 2  # default: only show wrestlers active in last 2 years
    MIN_MATCHES = 50  # minimum matches to show up in results
    BYPASS_PROMOS = {
        "world wonder ring stardom",
        "marigold",
        "actwres girl'z",
        "world wrestling entertainment",
        "all elite wrestling",
        "tokyo joshi pro wrestling",
    }

    @staticmethod
    def _is_active(wrestler: dict, today: date, years: int = 2) -> bool:
        """Check if wrestler had a match within the last N years."""
        lmd = wrestler.get("last_match_date", "")
        if not lmd or lmd.startswith("0001"):
            return False
        try:
            last = datetime.fromisoformat(lmd.replace("Z", "+00:00")).date()
            cutoff = today.replace(year=today.year - years)
            return last >= cutoff
        except (ValueError, TypeError):
            return False

    # ── matching helpers ────────────────────────────────────

    def _find_by_date(
        self, wrestlers: List[dict], month: int, day: int, show_all: bool = False, today: Optional[date] = None
    ) -> List[Tuple[dict, date]]:
        """Find wrestlers born on a given month/day."""
        if today is None:
            today = date.today()
        results = []
        for w in wrestlers:
            bd = self._parse_birthday(w.get("birthday", ""))
            if bd and bd.month == month and bd.day == day:
                if not show_all and not self._is_active(w, today, self.ACTIVE_YEARS):
                    continue
                if not show_all and w.get("match_count", 0) < self.MIN_MATCHES:
                    if w.get("promotion", "").lower() not in self.BYPASS_PROMOS:
                        continue
                results.append((w, bd))
        results.sort(key=lambda x: x[0].get("elo", 0), reverse=True)
        return results

    def _find_by_name(
        self, wrestlers: List[dict], query: str, show_all: bool = False, today: Optional[date] = None
    ) -> List[Tuple[dict, date]]:
        """Search wrestlers by name or alias (case-insensitive partial match)."""
        if today is None:
            today = date.today()
        q = query.lower().strip()
        results = []
        seen_ids = set()

        for w in wrestlers:
            if w["id"] in seen_ids:
                continue
            bd = self._parse_birthday(w.get("birthday", ""))
            if not bd:
                continue
            if not show_all and not self._is_active(w, today, self.ACTIVE_YEARS):
                continue

            if not show_all and w.get("match_count", 0) < self.MIN_MATCHES:
                if w.get("promotion", "").lower() not in self.BYPASS_PROMOS:
                    continue

            # check main name
            if q in w["name"].lower():
                results.append((w, bd))
                seen_ids.add(w["id"])
                continue

            # check aliases
            for alias in self._get_aliases(w):
                if q in alias.lower():
                    results.append((w, bd))
                    seen_ids.add(w["id"])
                    break

        results.sort(key=lambda x: x[0].get("elo", 0), reverse=True)
        return results

    # ── date parsing ────────────────────────────────────────

    _DATE_RE = re.compile(
        r"^(\d{1,2})[./\-](\d{1,2})$"
    )

    def _parse_date_arg(self, arg: str) -> Optional[Tuple[int, int]]:
        """Try to parse DD.MM or DD/MM or DD-MM → (month, day)."""
        m = self._DATE_RE.match(arg.strip())
        if not m:
            return None
        day, month = int(m.group(1)), int(m.group(2))
        if 1 <= month <= 12 and 1 <= day <= 31:
            return (month, day)
        return None

    # ── embed builders ──────────────────────────────────────

    FOREVER_AGE = 22  # all wrestlers are 22 forever

    def _build_wrestler_embed(self, wrestler: dict, bd: date, today: date) -> discord.Embed:
        """Build a detail embed for a single wrestler."""
        promo = wrestler.get("promotion", "")
        aliases = self._get_aliases(wrestler)

        name_line = wrestler["name"]
        if aliases:
            name_line += f" ({', '.join(aliases[:3])})"

        if self._year_known(bd):
            bd_str = f"{bd.strftime('%d.%m.%Y')} · Age {self.FOREVER_AGE}"
        else:
            bd_str = f"{bd.strftime('%d.%m')}.??"

        desc = bd_str
        if promo:
            desc += f" · {promo}"

        embed = discord.Embed(
            title=f"🎂 Happy Birthday — {name_line}",
            description=desc,
            color=PINK,
        )

        img = self._get_image(wrestler)
        if img:
            embed.set_thumbnail(url=img)

        return embed

    def _build_date_embeds(
        self, results: List[Tuple[dict, date]], month: int, day: int, today: date
    ) -> List[discord.Embed]:
        """Build one embed per wrestler for a date lookup."""
        if not results:
            date_str = f"{day:02d}.{month:02d}"
            embed = discord.Embed(
                title=f"🎂 Birthdays — {date_str}",
                description="No birthdays found for this date!",
                color=PINK,
            )
            return [embed]

        return [self._build_wrestler_embed(w, bd, today) for w, bd in results[:20]]

    def _build_search_embeds(self, results: List[Tuple[dict, date]], query: str, today: date) -> List[discord.Embed]:
        """Build one embed per wrestler for search results."""
        return [self._build_wrestler_embed(w, bd, today) for w, bd in results[:20]]

    # ── commands ────────────────────────────────────────────

    @commands.command()
    async def birthday(self, ctx: commands.Context, *, ask: str = ""):
        """
        Show joshi birthdays (active wrestlers only).

        Usage:
          !birthday          → today's birthdays
          !birthday 22.03    → birthdays on March 22
          !birthday tam      → search by name/alias
          !birthday all      → today's birthdays (include retired/inactive)
          !birthday all 22.03 → all birthdays on March 22
          !birthday all tam  → search all wrestlers by name
        """
        ask = ask.strip()
        today = date.today()

        # check for "all" flag
        show_all = False
        if ask.lower().startswith("all"):
            show_all = True
            ask = ask[3:].strip()

        try:
            wrestlers = await self._fetch_wrestlers()
        except Exception as e:
            return await ctx.send(f"❌ Couldn't reach joshitori.com: {e}")

        if not ask:
            # today's birthdays
            results = self._find_by_date(wrestlers, today.month, today.day, show_all, today)
            embeds = self._build_date_embeds(results, today.month, today.day, today)
            for embed in embeds:
                await ctx.send(embed=embed)
            return

        # try parsing as date
        parsed = self._parse_date_arg(ask)
        if parsed:
            month, day = parsed
            results = self._find_by_date(wrestlers, month, day, show_all, today)
            embeds = self._build_date_embeds(results, month, day, today)
            for embed in embeds:
                await ctx.send(embed=embed)
            return

        # otherwise, name search
        results = self._find_by_name(wrestlers, ask, show_all, today)
        if not results:
            # if filtered and nothing found, hint about "all"
            if not show_all:
                all_results = self._find_by_name(wrestlers, ask, True, today)
                if all_results:
                    return await ctx.send(
                        f"No active wrestlers found for \"{ask}\" — but found {len(all_results)} "
                        f"result{'s' if len(all_results) != 1 else ''} with `!birthday all {ask}`"
                    )
            return await ctx.send(f"No results for \"{ask}\" <:dashsrs:763999844724899841>")

        embeds = self._build_search_embeds(results, ask, today)
        for embed in embeds:
            await ctx.send(embed=embed)

    @commands.command()
    async def bdcheck(self, ctx: commands.Context):
        """Post today's birthdays as an announcement."""
        today = date.today()

        try:
            wrestlers = await self._fetch_wrestlers()
        except Exception:
            return

        results = self._find_by_date(wrestlers, today.month, today.day, False, today)
        if not results:
            return

        for w, bd in results:
            promo = w.get("promotion", "")
            img = self._get_image(w)

            if self._year_known(bd):
                desc = f"Turning **{self.FOREVER_AGE}** today! · {promo}"
            else:
                desc = f"Happy Birthday! · {promo}"

            embed = discord.Embed(
                title=f"🎂 Happy Birthday {w['name']}!",
                description=desc,
                color=PINK,
            )
            if img:
                embed.set_thumbnail(url=img)
            embed.set_footer(text="joshitori.com")

            await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Birthday(bot))
