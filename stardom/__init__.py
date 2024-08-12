from .stardom import Stardom

def setup(bot):
    n = Stardom(bot)
    bot.add_cog(n)
