# Post animal pics by Eslyium#1949 & Yukirin#0048

# Discord
import discord

# Red
from redbot.core import commands

# Libs
import aiohttp
import os
import random

BaseCog = getattr(commands, "Cog", object)


class Joshiplz(BaseCog):
    #JoshiSpam!

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop)
     
     
    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def joshi(self, ctx):
        #1x joshi!
        try:
            fp = random.choice(os.listdir("/home/dash/dwnlds/.joshi/"))
            await bot.send_file(ctx.message.channel, "randomimagefoldername/{}".format(fp))
        except:
            await ctx.send("Nope")

"""
    @commands.command()
    @commands.cooldown(1, 120, commands.BucketType.guild)
    async def cats(self, ctx, amount : int = 5):
        #Throws a cat bomb!

        #Defaults to 5, max is 10
        results = []
        if amount > 10 or amount < 1:
            amount = 5
        try:
            for x in range(0,amount):
                async with self.session.get(self.catapi) as r:
                    api_result = await r.json()
                    results.append(api_result['file'])
            await ctx.send("\n".join(results))
        except:
            await ctx.send("API Error")
"""

    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())

    __del__ = cog_unload
