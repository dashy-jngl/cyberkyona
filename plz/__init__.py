#from redbot.core.bot import Red

from .plz import Plz


async def setup(bot):
    await bot.add_cog(Plz(bot))
