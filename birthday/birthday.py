import discord
from redbot.core import commands

from typing import List
from collections import defaultdict

from datetime import date

class Birthday(commands.Cog):
    """Show joshi birthdays"""

    def __init__(self, bot):
        self.bot = bot

    def format_help_for_context(self, ctx: commands.Context) -> str:
        pre_processed = super().format_help_for_context(ctx)
        return f"{pre_processed}\n\nCog Version: {self.__version__}"



    @commands.command()
    async def birthday(self, ctx: commands.Context, ask: str = "none"):
        """ displays birthdays for a given date or supplies birthdates for a given joshi"""
        birthdays = {
        "momo": ["22.03.00"],
        "22.03.00": ["momo ", "not momo "],
        "20.05": ["Nao Yamaguchi"],
        }

        if ask == "none":
            today = date.today()
            day = today.strftime("%d")
            month = today.strftime("%m")
            ask = day +"."+ month
            await ctx.send(ask)

        try:
            bd = birthdays[ask]
            for i in range(len(bd)):
                await ctx.send(bd[i])
        except:
            await ctx.send("<a:konamishrug:845007847926136912>"+"<:giuliaKiss:845008239027290175>")


