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
        r = requests.get(self.SCHEDULE_URL); r.raise_for_status()
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
        if ticket and ticket["href"]:
            try:
                r2 = requests.get(ticket["href"]); r2.raise_for_status()
                soup2 = BeautifulSoup(r2.text, "html.parser")
                for div in soup2.find_all("div", class_="data_bg2"):
                    if "本戦開始時間" in div.get_text():
                        ts = div.parent.find("span", class_="time")
                        if ts:
                            title += f" ({ts.get_text(strip=True)})"
                        break
            except requests.RequestException:
                pass

        # Matches
        matches: list[dict] = []
        for wrap in soup.select("div.match_cover div.match_wrap"):
            mtype_el = wrap.select_one("h2.sub_content_title1")
            mtype = mtype_el.get_text(strip=True) if mtype_el else "Match"

            row = wrap.find("div", class_="match_block_row")
            if row:
                left = [n.get_text(strip=True) for n in row.select("div.leftside h3.name")]
                right = [n.get_text(strip=True) for n in row.select("div.rightside h3.name")]
            else:
                col = wrap.find("div", class_="match_block_column") or []
                uls = col.select("ul.match_block_3col") if col else []
                left = [n.get_text(strip=True) for n in (uls[0].select("h3.name") if len(uls)>0 else [])]
                right = [n.get_text(strip=True) for n in (uls[1].select("h3.name") if len(uls)>1 else [])]

            matches.append({"type": mtype, "left": left, "right": right})

        # Translate
        if translate:
            translator = GoogleTranslator(source="ja", target="en")
            originals = [title] + [m["type"] for m in matches]
            for m in matches:
                originals += m["left"] + m["right"]
            seen: dict[str, None] = {}
            for t in originals:
                if t and t not in seen:
                    seen[t] = None
            originals = list(seen.keys())
            translated = translator.translate_batch(originals)
            mapping = dict(zip(originals, translated))

            title = mapping.get(title, title)
            for m in matches:
                m["type"]  = mapping.get(m["type"], m["type"])
                m["left"]  = [mapping.get(x, x) for x in m["left"]]
                m["right"] = [mapping.get(x, x) for x in m["right"]]

        return title, matches

    @commands.command()
    async def stardom(self, ctx, n: int = 1, *, flags=""):
        """
        Post the nth Stardom show match card.
        Use -e to translate to English.
        """
        translate = "-e" in flags.split()
        links = self.get_card_links()
        if not links:
            return await ctx.send("🚫 No upcoming shows found.")
        if n < 1 or n > len(links):
            return await ctx.send(f"🚫 Only found {len(links)} show(s).")

        title, matches = self.parse_card(links[n-1], translate=translate)
        embed = discord.Embed(title=title, color=discord.Color.blurple())

        for m in matches:
            rows = max(len(m["left"]), len(m["right"]))
            left_block  = "\n".join(m["left"][i]  if i < len(m["left"])  else "" for i in range(rows))
            mid_block   = "\n".join("vs" if i == rows//2 else ""     for i in range(rows))
            right_block = "\n".join(m["right"][i] if i < len(m["right"]) else "" for i in range(rows))

            # Match type header
            embed.add_field(name=m["type"], value="\u200b", inline=False)
            # Three compact inline columns
            embed.add_field(name="\u200b", value=left_block,  inline=True)
            embed.add_field(name="\u200b", value=mid_block,   inline=True)
            embed.add_field(name="\u200b", value=right_block, inline=True)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(StardomCog(bot))
