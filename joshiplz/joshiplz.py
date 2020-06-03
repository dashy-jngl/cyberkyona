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
    async def joshi(self, ctx):
        #1x joshi!
        try:
            path ='/home/dash/data/.joshi'
            files = os.listdir(path)
            index = random.randrange(0, len(files))
#            file = path+"/"+files[index]
#            fp = path
            await channel.send(file=discord.File('/home/dash/data/.joshi/0cw20v7v_198_l.jpg'))
            
        except:
            await ctx.send("Nope")

    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())

    __del__ = cog_unload
