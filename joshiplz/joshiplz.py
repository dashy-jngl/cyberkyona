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
            index = random.randrange(1, len(files))
#            file = path+"/"+files[index]
#            fp = path
            await ctx.send(file=discord.File(path+"/"+files[index]))
            
        except:
            await ctx.send("Nope")
            
    @commands.command()
#    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def joshiplz(self, ctx, amount : int = 5):
        """Throws a dog bomb!

        Defaults to 5, max is 10"""
        results = []
        if amount > 10 or amount < 1:
            amount = 5
        try:
            for x in range(0,amount):
                path ='/home/dash/data/.joshi'
                files = os.listdir(path)
                index = random.randrange(1, len(files))
#               file = path+"/"+files[index]
#               fp = path
                await ctx.send(file=discord.File(path+"/"+files[index]))
            await ctx.send('<:hikariHeart:706347703088447508>')     
        
        except:
            await ctx.send("oop")

    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())

    __del__ = cog_unload
