#from redbot.core.bot import Red

from .lewdplz import Lewdplz


def setup(bot):
    bot.add_cog(Lewdplz(bot))
