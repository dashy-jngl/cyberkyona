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
        """ - PP MotherFuckers!"""
        
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
###
            elif user.id == 713995207384760370: #cyberKyona
                user = ctx.message.author
                bot_msg: List[str] = [
                    (f"{ctx.author.name} She'll ban you you know."),
                    (f"Sorry motherfucker, im not THAT crazy! {ctx.author.name}"),
                    ("<a:tamNoYukEw:698479875610378280>"),
                    ("<:thatsNotWrestlingGgr:707427714940010539>"),
                ]
                await ctx.send(f"{choice(bot_msg)}")
###                
            else:
                await ctx.send("**" + user.name + "'s** size is:\n" + "**" + msg + "**")
        else:
            await ctx.send("**" + ctx.message.author.name + "'s** size is:\n" + "**" + msg + "**")


    @commands.command()
    async def simp(self, ctx: commands.Context, user: discord.Member = None) -> None:
        """ - simpRate MotherFuckers!"""
        
        msg = " "
        simprate = random.randint(50, 100)
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
