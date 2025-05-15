# file: stardom.py
from __future__ import annotations

import discord
from redbot.core import commands
import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator


class StardomCog(commands.Cog):
    """Cog for scraping Stardom schedule and posting match details."""

    SCHEDULE_URL = "https://wwr-stardom.com/schedule"

    def __init__(self, bot):
        self.bot = bot

    def get_card_links(self) -> list[str]:
        r = requests.get(self.SCHEDULE_URL)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        return [
            a["href"]
            for a in soup.find_all("a", class_="btn", string="対戦カード")
        ]

    def parse_card(self, url: str, translate: bool = False) -> tuple[str, list[dict]]:
        r = requests.get(url); r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")

        # Title + date
        base = soup.select_one("h1.match_head_title").get_text(strip=True)
        date_el = soup.select_one("p.date")
        title = f"{date_el.get_text(strip=True)} {base}" if date_el else base

        # Start time
        ticket = soup.select_one("a.btnstyle4")
        if ticket and ticket.get("href"):
            try:
                r2 = requests.get(ticket["href"]); r2.raise_for_status()
                soup2 = BeautifulSoup(r2.text, "html.parser")
                for div in soup2.find_all("div", class_="data_bg2"):
                    if "本戦開始時間" in div.get_text():
                        ts = div.parent.find("span", class_="time")
                        if ts:
                            title = f"({ts.get_text(strip=True)}) {title}"
                        break
            except requests.RequestException:
                pass

        matches: list[dict] = []
        for wrap in soup.select("div.match_cover div.match_wrap"):
            mtype_el = wrap.select_one("h2.sub_content_title1")
            mtype = mtype_el.get_text(strip=True) if mtype_el else "Match"

            # detect two-team “row” style
            row = wrap.find("div", class_="match_block_row")
            if row:
                teams = [
                    [n.get_text(strip=True) for n in row.select("div.leftside h3.name")],
                    [n.get_text(strip=True) for n in row.select("div.rightside h3.name")],
                ]
            else:
                # N-way “column” style: 1 ul per team
                col = wrap.find("div", class_="match_block_column") or []
                uls = col.select("ul.match_block_3col")
                teams = [
                    [n.get_text(strip=True) for n in ul.select("h3.name")]
                    for ul in uls
                ]

            matches.append({"type": mtype, "teams": teams})

        # optional translation
        if translate:
            translator = GoogleTranslator(source="ja", target="en")
            originals = [title] + [m["type"] for m in matches]
            for m in matches:
                for team in m["teams"]:
                    originals += team
            seen: dict[str, None] = {}
            for t in originals:
                if t and t not in seen:
                    seen[t] = None
            originals = list(seen.keys())
            translations = translator.translate_batch(originals)
            mapping = dict(zip(originals, translations))

            title = mapping.get(title, title)
            for m in matches:
                m["type"] = mapping.get(m["type"], m["type"])
                m["teams"] = [
                    [mapping.get(p, p) for p in team] for team in m["teams"]
                ]

        return title, matches

    def pad_center(self, text: str, width: int) -> str:
        """Center-pad text by character count."""
        l = len(text)
        if l >= width:
            return text
        space = width - l
        left = space // 2
        return " " * left + text + " " * (space - left)

    @commands.command()
    async def stardom(self, ctx, *args):
        """
        Usage:
          !stardom            → next show in Japanese
          !stardom e          → next show in English
          !stardom 2 -e       → 2nd show in English
        """
        # parse flags/number
        n = 1
        translate = False
        for a in args:
            la = a.lower()
            if la in ("e", "-e", "--english"):
                translate = True
            else:
                try:
                    n = int(a)
                except ValueError:
                    pass

        links = self.get_card_links()
        if not links:
            return await ctx.send("🚫 No upcoming shows found.")
        if n < 1 or n > len(links):
            return await ctx.send(f"🚫 Only found {len(links)} show(s).")

        title, matches = self.parse_card(links[n - 1], translate=translate)
        embed = discord.Embed(title=title, color=discord.Color.blurple())

        for m in matches:
            teams = m["teams"]
            # how many teams?
            tcount = len(teams)
            rows   = max(len(t) for t in teams)
            # compute widths for each team column
            w_data = [max((len(p) for p in t), default=0) for t in teams]
            w_sep  = len("vs")

            # build top border
            parts = []
            for i in range(tcount):
                parts.append("─" * w_data[i])
                if i < tcount - 1:
                    parts.append("─" * w_sep)
            top = "┌" + "┬".join(parts) + "┐"

            # build rows
            body: list[str] = []
            mid_row = rows // 2
            for r in range(rows):
                cells = []
                for i in range(tcount):
                    val = teams[i][r] if r < len(teams[i]) else ""
                    cells.append(self.pad_center(val, w_data[i]))
                    if i < tcount - 1:
                        sep = "vs" if r == mid_row else ""
                        cells.append(self.pad_center(sep, w_sep))
                body.append("│" + "│".join(cells) + "│")

            # bottom border
            parts = []
            for i in range(tcount):
                parts.append("─" * w_data[i])
                if i < tcount - 1:
                    parts.append("─" * w_sep)
            bottom = "└" + "┴".join(parts) + "┘"

            # stitch it and add field
            block = "```\n" + top + "\n" + "\n".join(body) + "\n" + bottom + "\n```"
            embed.add_field(name=m["type"], value=block, inline=False)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(StardomCog(bot))
