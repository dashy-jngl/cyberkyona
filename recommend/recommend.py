import discord
from redbot.core import commands
from random import choice
from redbot.core.i18n import Translator, cog_i18n
from typing import List


stardom: List[str] = [
    ("Yo Mama so fat she sued Xbox 360 for guessing her weight."),
    

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
            - Insults motherfucker!

            `user` the user you would like to insult
        """

        msg = " "
        if promo:

            if promo == "stardom":
                user = ctx.message.author
                bot_msg = [
                    (
                        " Simp!"
                    ),
                    (
                        " You love itoh!"
                    ),
                    (
                        " Pay me motherfucker!"
                    ),
                    (
                        " Itoh-chan #1"
                    ),
                ]
                await ctx.send(f"{ctx.author.mention}{choice(bot_msg)}")
            
            elif promo == "agz": #cyberKyona
                user = ctx.message.author
                bot_msg = [
                    (
                        " I simp so hard for her!"
                    ),
                    (
                        " I love cyberKyona"
                    ),
                    (
                        " Pay me motherfucker!"
                    ),
                    (
                        " Kyona-chan #1"
                    ),
                ]
                await ctx.send(f"{ctx.author.mention} {choice(bot_msg)}")    
            
            else:
                await ctx.send(user.mention + msg + choice(stardom))
        else:
            await ctx.send(ctx.message.author.mention + msg + choice(stardom))
