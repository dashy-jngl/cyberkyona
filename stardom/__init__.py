from .stardom import StardomCog

async def setup(bot):
    n = StardomCog(bot)
    await bot.add_cog(n)
