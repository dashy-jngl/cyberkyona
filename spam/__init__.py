#from redbot.core.bot import Red

from .spam import Spam


def setup(bot):
    bot.add_cog(Spam(bot))
