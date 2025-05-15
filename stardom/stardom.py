from __future__ import annotations
import discord
from redbot.core import commands
import requests
from bs4 import BeautifulSoup
from wcwidth import wcswidth
from deep_translator import GoogleTranslator

class StardomCog(commands.Cog):
    SCHEDULE_URL = "https://wwr-stardom.com/schedule"

    def __init__(self, bot):
        self.bot = bot

    # … your get_card_links() and parse_card() go here …

    # Helpers to build the ASCII table
    def disp_len(self, s: str) -> int:
        return wcswidth(s)

    def pad_center(self, text: str, width: int) -> str:
        length = self.disp_len(text)
        if length >= width:
            return text
        space = width - length
        left = space // 2
        return " " * left + text + " " * (space - left)

    def format_match_table(self, left: list[str], right: list[str], w1: int, w2: int, w3: int) -> str:
        lines: list[str] = []
        # top border
        lines.append(f"┌{'─'*w1}┬{'─'*w2}┬{'─'*w3}┐")
        rows = max(len(left), len(right))
        for i in range(rows):
            l = left[i] if i < len(left) else ""
            r = right[i] if i < len(right) else ""
            mid = "vs" if i == rows // 2 else ""
            lines.append(
                "│"
                + self.pad_center(l, w1)
                + "│"
                + self.pad_center(mid, w2)
                + "│"
                + self.pad_center(r, w3)
                + "│"
            )
        # bottom border
        lines.append(f"└{'─'*w1}┴{'─'*w2}┴{'─'*w3}┘")
        return "\n".join(lines)

    @commands.command()
    async def stardom(self, ctx, n: int = 1, *, flags=""):
        translate = "-e" in flags.split()
        links = self.get_card_links()
        if n < 1 or n > len(links):
            return await ctx.send(f"Only found {len(links)} show(s).")

        title, raw_matches = self.parse_card(links[n-1], translate=translate)

        # Compute uniform column widths
        w2 = self.disp_len("vs")
        w1 = max(
            (self.disp_len(name) for m in raw_matches for name in m["left"]),
            default=0,
        )
        w3 = max(
            (self.disp_len(name) for m in raw_matches for name in m["right"]),
            default=0,
        )

        embed = discord.Embed(title=title)
        for m in raw_matches:
            table = self.format_match_table(m["left"], m["right"], w1, w2, w3)
            # wrap in a code block so Discord preserves the monospace
            embed.add_field(name=m["type"] or "Match", value=f"```\n{table}\n```", inline=False)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(StardomCog(bot))
