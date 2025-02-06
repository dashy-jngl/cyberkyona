from .simp import Simp

async def setup(bot):
    n = Simp(bot)
    await bot.add_cog(n)
