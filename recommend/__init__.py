from .recommend import Recommend


def setup(bot):
    n = Recommend(bot)
    bot.add_cog(n)
