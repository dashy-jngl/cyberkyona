from redbot.core.bot import Red

from .joshiplz import Joshiplz


def setup(bot: Red):
    bot.add_cog(Joshiplz())
