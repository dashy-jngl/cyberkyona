from .joshiplz import Joshiplz


def setup(bot: Red):
    bot.add_cog(Joshiplz(bot))
