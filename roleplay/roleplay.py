import discord
from redbot.core import commands
from random import choice
from typing import List


insults: List[str] = [
    ("https://cdn.discordapp.com/attachments/797764291540680714/798074381733593138/2021-01-01_01-11-47_a2zt5-lwci1.gif"),

]


@cog_i18n(_)
class Insult(commands.Cog):

    __author__ = ["Airen", "JennJenn", "TrustyJAID", "dasha"]
    __version__ = "1.0.0"

    def __init__(self, bot):
        self.bot = bot

    def format_help_for_context(self, ctx: commands.Context) -> str:
        
        pre_processed = super().format_help_for_context(ctx)
        return f"{pre_processed}\n\nCog Version: {self.__version__}"

    @commands.command(aliases=["takeitback"])
    async def hugs(self, ctx: commands.Context, user: discord.Member = None) -> None:
        """
            - Insults motherfucker!

            `user` the user you would like to insult
        """

        msg = " "

        await ctx.send(choice(hugs))
