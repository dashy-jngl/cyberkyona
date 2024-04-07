from .birthday import Birthday

async def setup(bot):
    n = Birthday(bot)
    bot.add_cog(n)
