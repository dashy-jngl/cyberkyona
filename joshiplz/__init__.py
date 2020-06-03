from .joshiplz import Joshiplz


def setup(bot: Red):
    bot.add_cog(joshiplz(bot))
