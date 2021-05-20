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

    @commands.command()
    async def birthday(self, ctx: commands.Context, user: discord.Member = None) -> None:
        """ - simpRate MotherFuckers!"""
        
        msg = " "
        simprate = random.randint(75, 200)
        simpmood = random.randint(1, 300)
        simpmax = random.randint(2, 10)
        if simpmood == 1:
            simprate = simprate + 9000
        if simpmood > 270:
            simprate = random.randint(200, 300)
        if simpmood == 233:
            simprate = simprate * simpmax
        simp = str(simprate)
        if user:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                bot_msg: List[str] = [
                    ("I only simp for Kyona"),
                    ("I only simp for Asuka"),
                    ("I only simp for Io"),
                    ("I only simp for Taya"),
                ]
                await ctx.send(f"{choice(bot_msg)}")
            else:
                await ctx.send("**" + user.name + "'s** simprate is:\n\n" + "**" +  simp +"%**")
        else:
            await ctx.send("**" + ctx.message.author.name + "'s** simprate is:\n\n" + "**" +  simp +"%**")
    
