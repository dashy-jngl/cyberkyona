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
            fp = random.choice(os.listdir("http://dash.pallas.feralhosting.com/.joshi/"))
            await bot.send_file(ctx.message.channel, "randomimagefoldername/{}".format(fp))
        except:
            await ctx.send("Nope")

    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())

    __del__ = cog_unload
