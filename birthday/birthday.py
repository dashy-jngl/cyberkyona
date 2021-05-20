import discord
import random
from redbot.core import commands
from redbot.core.utils.chat_formatting import pagify
from random import choice
from redbot.core.i18n import Translator, cog_i18n
from typing import List

class Birthday(commands.Cog):
    """Show joshi birthdays"""

    def __init__(self, bot):
        self.bot = bot

    def format_help_for_context(self, ctx: commands.Context) -> str:
        pre_processed = super().format_help_for_context(ctx)
        return f"{pre_processed}\n\nCog Version: {self.__version__}"

    birthdays = {
    "momo": "22.03.00",
    "22.03.00": "momo",
    "kyona": "22.03.01",
    "22.03.01": "kyona",
    }

    @commands.command()
    async def birthday(self, ctx: commands.Context, ask: str):
        """ - simpRate MotherFuckers!"""
        
        msg = " "

        await ctx.send(birthday[ask])
    
