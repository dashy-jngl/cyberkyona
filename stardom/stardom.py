import discord
from redbot.core import commands
import requests
from bs4 import BeautifulSoup
from wcwidth import wcswidth
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
        # find all "対戦カード" buttons
        return [a["href"] for a in soup.find_all("a", class_="btn", string="対戦カード")]

    def parse_card(self, url: str, translate=False) -> tuple[str, list[dict]]:
        r = requests.get(url)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")

        # Title + date
        base = soup.select_one("h1.match_head_title").get_text(strip=True)
        date_el = soup.select_one("p.date")
        if date_el:
            date_str = date_el.get_text(strip=True)
            title = f"{date_str} {base}"
        else:
            title = base

        # Append time from ticket page
        ticket = soup.select_one("a.btnstyle4")
        if ticket and ticket.get("href"):
            try:
                r2 = requests.get(ticket["href"])
                r2.raise_for_status()
                soup2 = BeautifulSoup(r2.text, "html.parser")
                for div in soup2.find_all("div", class_="data_bg2"):
                    if "本戦開始時間" in div.get_text():
                        ts = div.parent.find("span", class_="time")
                        if ts:
                            title += f" ({ts.get_text(strip=True)})"
                        break
            except requests.RequestException:
                pass

        # Collect matches
        matches = []
        for wrap in soup.select("div.match_cover div.match_wrap"):
            mtype = wrap.select_one("h2.sub_content_title1")
            mtype = mtype.get_text(strip=True) if mtype else ""
            row = wrap.find("div", class_="match_block_row")
            if row:
                left = [n.get_text(strip=True) for n in row.select("div.leftside h3.name")]
                right = [n.get_text(strip=True) for n in row.select("div.rightside h3.name")]
            else:
                col = wrap.find("div", class_="match_block_column")
                uls = col.select("ul.match_block_3col") if col else []
                left = [n.get_text(strip=True) for n in uls[0].select("h3.name")] if len(uls) > 0 else []
                right = [n.get_text(strip=True) for n in uls[1].select("h3.name")] if len(uls) > 1 else []
            matches.append({"type": mtype, "left": left, "right": right})

        # Optional: translate
        if translate:
            translator = GoogleTranslator(source="ja", target="en")
            # batch all strings
            originals = [title] + [m["type"] for m in matches]
            for m in matches:
                originals += m["left"] + m["right"]
            # unique preserve order
            seen = {}
            for t in originals:
                if t and t not in seen:
                    seen[t] = None
            originals = list(seen.keys())
            translated = translator.translate_batch(originals)
            mapping = dict(zip(originals, translated))

            title = mapping.get(title, title)
            for m in matches:
                m["type"] = mapping.get(m["type"], m["type"])
                m["left"] = [mapping.get(n, n) for n in m["left"]]
                m["right"]= [mapping.get(n, n) for n in m["right"]]

        return title, matches

    @commands.command()
    async def stardom(self, ctx, n: int = 1, *, flags=""):
        """Post the nth Stardom show match card. Use -e to translate."""
        translate = "-e" in flags.split()
        links = self.get_card_links()
        if n < 1 or n > len(links):
            return await ctx.send(f"Only found {len(links)} show(s).")

        title, matches = self.parse_card(links[n-1], translate=translate)

        embed = discord.Embed(title=title)
        for m in matches:
            # build a single string for this match
            lines = []
            rows = max(len(m["left"]), len(m["right"]))
            for i in range(rows):
                l = m["left"][i] if i < len(m["left"]) else ""
                r = m["right"][i] if i < len(m["right"]) else ""
                vs = " vs " if i == rows // 2 else ""
                lines.append(f"{l}{vs}{r}")
            embed.add_field(name=m["type"] or "Match", value="\n".join(lines), inline=False)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(StardomCog(bot))
