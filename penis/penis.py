import discord
import random
from redbot.core import commands
from redbot.core.utils.chat_formatting import pagify


class Penis(commands.Cog):
    """Penis related commands."""

    def __init__(self, bot):
        self.bot = bot

    def format_help_for_context(self, ctx: commands.Context) -> str:
        """
            Thanks Sinbad!
        """
        pre_processed = super().format_help_for_context(ctx)
        return f"{pre_processed}\n\nCog Version: {self.__version__}"


    @commands.command()
    async def penis(self, ctx: commands.Context, user: discord.Member = None) -> None:
        """
            pp
        """
        msg = " "
        length = random.randint(0, 30)
        msg = "8{}D".format("=" * length)
        if user:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                bot_msg: List[str] = [
                    _("Bigger than yours!"),
                    _("If i told you i'd have to fuck you!"),
                    _("haha sorry motherfucker!"),
                    _("You wish!"),
                ]
                await ctx.send(f"{ctx.author.mention} {choice(bot_msg)}")

            else:
                await ctx.send(user.mention + msg)
        else:
            await ctx.send(ctx.message.author.name+"**'s size is:**\n" + msg)
