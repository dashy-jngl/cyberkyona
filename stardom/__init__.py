from .stardom import StardomCog

def setup(bot):
    n = StardomCog(bot)
    bot.add_cog(n)
