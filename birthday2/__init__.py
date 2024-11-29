from .birthday import Birthday

async def setup(bot):
    n = Birthday(bot)
    await bot.add_cog(n)
