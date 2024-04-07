#from redbot.core.bot import Red

from .joshiplz import Joshiplz


async def setup(bot):
    await bot.add_cog(Joshiplz(bot))
