from .birthday import Birthday

def setup(bot):
    n = Birthday(bot)
    bot.add_cog(n)
