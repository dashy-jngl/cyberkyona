# Post animal pics by Eslyium#1949 & Yukirin#0048

# Discord
import discord

# Red
from redbot.core import commands


# Libs
import os
import random
#import urllib.request


import aiohttp
#import asyncio
#import io
#import logging
#from typing import Awaitable, Callable

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
            file = random.choice(os.listdir("/home/dash/data/.joshi"))
            await ctx.send(file=file)
            
        except:
            await ctx.send("Nope")

    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())

    __del__ = cog_unload
