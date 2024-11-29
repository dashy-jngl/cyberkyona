#from redbot.core.bot import Red

from .plz2 import Plz2


async def setup(bot):
    await bot.add_cog(Plz2(bot))
