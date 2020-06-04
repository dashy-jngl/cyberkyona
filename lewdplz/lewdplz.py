# post lewds plz

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

joshipath = '/home/dash/data/.joshi'
lewdpath = '/home/dash/data/.lewd'

BaseCog = getattr(commands, "Cog", object)


class Lewdplz(BaseCog):
    #nsfwSpam!

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop)
     
    @commands.command()
    async def lewd(self, ctx):
        #1x joshi!
        path = lewdpath
        try:
#            path = nsfwpath
            files = os.listdir(path)
            index = random.randrange(1, len(files))
#            file = path+"/"+files[index]
#            fp = path
            await ctx.send(file=discord.File(path+"/"+files[index]))
            
        except:
            await ctx.send("Nope")
            
    @commands.command()
#    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def lewds(self, ctx, amount : int = 3):
        """Throws a dog bomb!

        Defaults to 5, max is 10"""
        results = []
        path = lewdpath
        if amount > 12:
            amount = 12
        if amount < 1:
            amount = 1
        try:
            for x in range(0,amount):
                files = os.listdir(path)
                index = random.randrange(1, len(files))
                await ctx.send(file=discord.File(path+"/"+files[index]))
            await ctx.send('<:ShidaUp:638771591840530443>')     
        
        except:
            await ctx.send("oop")

    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())

    __del__ = cog_unload
