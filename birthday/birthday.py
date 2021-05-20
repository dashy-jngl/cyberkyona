import discord
import random
from redbot.core import commands
from redbot.core.utils.chat_formatting import pagify
from random import choice
from redbot.core.i18n import Translator, cog_i18n
from typing import List
from collections import defaultdict

class Birthday(commands.Cog):
    """Show joshi birthdays"""

    def __init__(self, bot):
        self.bot = bot

    def format_help_for_context(self, ctx: commands.Context) -> str:
        pre_processed = super().format_help_for_context(ctx)
        return f"{pre_processed}\n\nCog Version: {self.__version__}"



    @commands.command()
    async def birthday(self, ctx: commands.Context, ask: str):
        """ - simpRate MotherFuckers!"""
        birthdays = {
        "momo": "22.03.00",
        "22.03.00": ["momo ", "not momo "],
        "kyona": "22.03.01",
        "22.03.01": "kyona"
        }
        msg = " "

        if ask in birthdays[key]:
            bd = birthdays[ask]
            await ctx.send(bd[0])
            await ctx.send(bd[1])
        else await ctx.send("no entries found")
#        item = ask
#        for key in birthdays.keys():
#            if item in birthdays[key]:
#                bd = birthdays[key]
#                await ctx.send(bd[0])

#        await ctx.send(birthdays[[ask].0])

