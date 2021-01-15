from .roleplay import Roleplay


def setup(bot):
    n = Roleplay(bot)
    bot.add_cog(n)
