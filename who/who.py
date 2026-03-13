import discord
from redbot.core import commands
from datetime import datetime, date
from typing import List, Optional, Tuple
import aiohttp
import asyncio

API_URL = "https://joshitori.com/api/wrestlers"
IMAGE_BASE = "https://joshitori.com"
CACHE_TTL = 86400  # 24h

PINK = discord.Color.from_rgb(255, 105, 180)

# Tiers by max percentile (must be sorted by max_pct ascending)
TIERS = [
    (0.5, "Jotei 2", "\N{CROWN}"),
    (1, "Jotei 1", "\N{CROWN}"),
    (2, "Ace 3", "\N{HIGH VOLTAGE SIGN}"),
    (3.5, "Ace 2", "\N{HIGH VOLTAGE SIGN}"),
    (5, "Ace 1", "\N{HIGH VOLTAGE SIGN}"),
    (7.5, "Senshi 3", "\N{FIRE}"),
    (10, "Senshi 2", "\N{FIRE}"),
    (12.5, "Senshi 1", "\N{FIRE}"),
    (16.5, "Estrella 3", "\N{WHITE MEDIUM STAR}"),
    (22.5, "Estrella 2", "\N{WHITE MEDIUM STAR}"),
    (30, "Estrella 1", "\N{WHITE MEDIUM STAR}"),
    (40, "Young Lioness", "\N{CRESCENT MOON}"),
    (100, "Seedling", "\N{SEEDLING}"),
]


class Who(commands.Cog):
    """Look up joshi wrestler profiles from Joshitori."""

    __version__ = "1.0.0"

    def __init__(self, bot):
        self.bot = bot
        self._cache: List[dict] = []
        self._cache_time: float = 0

    # ── data layer ──────────────────────────────────────────

    async def _fetch_wrestlers(self) -> List[dict]:
        now = asyncio.get_event_loop().time()
        if self._cache and (now - self._cache_time) < CACHE_TTL:
            return self._cache

        async with aiohttp.ClientSession() as session:
            async with session.get(API_URL, timeout=aiohttp.ClientTimeout(total=30)) as resp:
                resp.raise_for_status()
                data = await resp.json()

        self._cache = data
        self._cache_time = now
        return data

    # ── helpers ─────────────────────────────────────────────

    @staticmethod
    def _get_image(wrestler: dict) -> Optional[str]:
        local = wrestler.get("image_local", "")
        if local:
            return IMAGE_BASE + local
        return wrestler.get("image") or None

    @staticmethod
    def _get_aliases(wrestler: dict) -> List[str]:
        aliases = wrestler.get("aliases") or []
        main = wrestler.get("name", "")
        return [a["alias"] for a in aliases if a.get("alias") and a["alias"] != main]

    @staticmethod
    def _get_tier(rank: int, total: int) -> Tuple[str, str]:
        """Get tier name and icon from rank percentile."""
        if total == 0:
            return "Seedling", "\N{SEEDLING}"
        pct = (rank / total) * 100
        for max_pct, name, icon in TIERS:
            if pct <= max_pct:
                return name, icon
        return "Seedling", "\N{SEEDLING}"

    def _find_by_name(self, wrestlers: List[dict], query: str) -> List[dict]:
        """Search by name or alias. Exact match prioritised, then partial."""
        q = query.lower().strip()
        exact = []
        partial = []
        seen = set()

        for w in wrestlers:
            if w["id"] in seen:
                continue

            names = [w["name"].lower()] + [a.lower() for a in self._get_aliases(w)]

            # exact match on any name/alias
            if q in names:
                exact.append(w)
                seen.add(w["id"])
                continue

            # partial match
            for n in names:
                if q in n:
                    partial.append(w)
                    seen.add(w["id"])
                    break

        # If there's an exact match, return only that
        if exact:
            return exact

        # Sort partial by ELO desc (most notable first)
        partial.sort(key=lambda w: w.get("elo", 0), reverse=True)
        return partial

    def _get_rank(self, wrestlers: List[dict], wrestler_id: int) -> Tuple[int, int]:
        """Get rank and total ranked wrestlers (sorted by ELO desc, 50+ matches only)."""
        ranked = sorted(
            [w for w in wrestlers if w.get("match_count", 0) >= 50],
            key=lambda w: w.get("elo", 0),
            reverse=True,
        )
        total = len(ranked)
        for i, w in enumerate(ranked):
            if w["id"] == wrestler_id:
                return i + 1, total
        return 0, total  # unranked

    def _build_embed(self, w: dict, rank: int, total: int) -> discord.Embed:
        aliases = self._get_aliases(w)
        name_line = w["name"]
        if aliases:
            name_line += " (" + ", ".join(aliases[:3]) + ")"

        embed = discord.Embed(title=name_line, color=PINK)

        # Profile info
        lines = []
        promo = w.get("promotion", "")
        if promo:
            lines.append("**Promotion:** " + promo)

        bd = w.get("birthday", "")
        if bd and not bd.startswith("0001"):
            try:
                d = datetime.fromisoformat(bd.replace("Z", "+00:00")).date()
                if d.year == 1900:
                    lines.append("**Birthday:** %02d.%02d.??" % (d.day, d.month))
                else:
                    lines.append("**Birthday:** " + d.strftime("%d.%m.%Y") + " (Age 22)")
            except (ValueError, TypeError):
                pass

        bp = w.get("birthplace", "")
        if bp:
            lines.append("**From:** " + bp)

        style = w.get("wrestling_style", "")
        if style:
            lines.append("**Style:** " + style)

        h = w.get("height", "")
        wt = w.get("weight", "")
        if h or wt:
            lines.append("**Size:** " + " \N{MIDDLE DOT} ".join(filter(None, [h, wt])))

        debut = w.get("debut_year", 0)
        if debut:
            lines.append("**Debut:** " + str(debut))

        embed.description = "\n".join(lines)

        # Stats
        elo = w.get("elo", 0)
        wins = w.get("wins", 0)
        losses = w.get("losses", 0)
        draws = w.get("draws", 0)
        matches = w.get("match_count", 0)
        win_rate = round(wins / (wins + losses) * 100) if (wins + losses) > 0 else 0

        if rank > 0:
            tier_name, tier_icon = self._get_tier(rank, total)
            rank_str = "%s %s (#%d of %d)" % (tier_icon, tier_name, rank, total)
        else:
            rank_str = "Unranked (<50 matches)"

        stats_lines = [
            "**ELO:** %.0f" % elo,
            "**Rank:** %s" % rank_str,
            "**Record:** %dW-%dL-%dD (%d matches)" % (wins, losses, draws, matches),
            "**Win Rate:** %d%%" % win_rate,
        ]
        embed.add_field(name="Stats", value="\n".join(stats_lines), inline=False)

        img = self._get_image(w)
        if img:
            embed.set_thumbnail(url=img)

        return embed

    # ── command ─────────────────────────────────────────────

    @commands.command()
    async def who(self, ctx: commands.Context, *, name: str = ""):
        """
        Look up a joshi wrestler profile.

        Usage:
          !who Suzu Suzuki
          !who tam
          !who 鈴木すず
        """
        name = name.strip()
        if not name:
            return await ctx.send("Usage: `!who <name>` — e.g. `!who Suzu Suzuki`")

        try:
            wrestlers = await self._fetch_wrestlers()
        except Exception as e:
            return await ctx.send("Could not reach joshitori.com: %s" % e)

        results = self._find_by_name(wrestlers, name)

        if not results:
            return await ctx.send('No wrestler found for "%s" <:dashsrs:763999844724899841>' % name)

        # Show up to 5 results
        for w in results[:5]:
            rank, total = self._get_rank(wrestlers, w["id"])
            embed = self._build_embed(w, rank, total)
            await ctx.send(embed=embed)

        if len(results) > 5:
            await ctx.send("*...and %d more results. Try a more specific name!*" % (len(results) - 5))
