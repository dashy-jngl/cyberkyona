from .simp import Simp

def setup(bot):
    n = Simp(bot)
    bot.add_cog(n)
