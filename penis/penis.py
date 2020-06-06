import discord
import random
from redbot.core import commands
from redbot.core.utils.chat_formatting import pagify
from random import choice
from redbot.core.i18n import Translator, cog_i18n
from typing import List

class Penis(commands.Cog):
    """Penis related commands."""

    def __init__(self, bot):
        self.bot = bot

    def format_help_for_context(self, ctx: commands.Context) -> str:
        pre_processed = super().format_help_for_context(ctx)
        return f"{pre_processed}\n\nCog Version: {self.__version__}"


    @commands.command()
    async def penis(self, ctx: commands.Context, user: discord.Member = None) -> None:
        # pp
        
        msg = " "
        length = random.randint(0, 30)
        msg = "8{}D".format("=" * length)
        if user:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                bot_msg: List[str] = [
                    ("bigger than yours"),
                    ("if i told you i'd have to fuck you"),
                    ("haha sorry"),
                    ("you wish"),
                ]
                await ctx.send(f"{choice(bot_msg)} {ctx.author.name}")

            else:
                await ctx.send("**" + user.name + "'s** size is:\n" + "**" + msg + "**")
        else:
            await ctx.send("**" + ctx.message.author.name + "'s** size is:\n" + "**" + msg + "**")


    @commands.command()
    async def simp(self, ctx: commands.Context, user: discord.Member = None) -> None:
        # pp
        
        msg = " "
        simprate = random.randint(0, 100)
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
                await ctx.send("**" + user.name + "'s** Simprate is: /n" + "**" +  simp +"%**")
        else:
            await ctx.send("**" + ctx.message.author.name + "'s Simprate is: " + "**" +  simp +"%**")
