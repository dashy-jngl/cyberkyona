from .who import Who


async def setup(bot):
    await bot.add_cog(Who(bot))
