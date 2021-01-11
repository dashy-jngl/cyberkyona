import discord
from redbot.core import commands
from random import choice
from redbot.core.i18n import Translator, cog_i18n
from typing import List

bot_msg = [
    (" Simp!"),
]
termlist = [
    (stardom),
    (agz),
]
stardom: List[str] = [
    ("stardom matches go here"),
]
agz: List[str] = [
    ("agz matches go here"),
]

class Recommend(commands.Cog):

    __author__ = ["Airen", "JennJenn", "TrustyJAID", "dasha"]
    __version__ = "1.0.0"

    def __init__(self, bot):
        self.bot = bot

    def format_help_for_context(self, ctx: commands.Context) -> str:
        
        pre_processed = super().format_help_for_context(ctx)
        return f"{pre_processed}\n\nCog Version: {self.__version__}"

    @commands.command(aliases=["rc"])
    async def recommend(self, ctx: commands.Context, promo = None) -> None:
        """
            - Recommends matches from WWC user submissions!

            `promo` the promotion you would like to see
        """

        msg = " "
        if promo:

            if promo == "stardom":
                await ctx.send(f"{ctx.author.mention}{choice(bot_msg)}{choice(stardom)}")
            
            elif promo == "agz": #cyberKyona
                await ctx.send(f"{ctx.author.mention} {choice(bot_msg)}{choice(agz)}")    
            
            else:
                list = choice(termlist)
                await ctx.send(ctx.author.mention + msg + choice(list))
        else:
            list = choice(termlist)
            await ctx.send(ctx.message.author.mention + msg + choice(list))
