#from redbot.core.bot import Red

from .plz import Plz


def setup(bot):
    bot.add_cog(Plz(bot))
