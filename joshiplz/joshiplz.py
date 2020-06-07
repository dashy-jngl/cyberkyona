# make JoshiPlz

# Discord
import discord

# Red
from redbot.core import commands


# Libs
import os
import random
#import urllib.request
from random import choice

import aiohttp
#import asyncio
#import io
#import logging
#from typing import Awaitable, Callable

joshi_path = [
    (
        "/home/dash/data/.joshi"
    ),
    (
        "/home/dash/data/.wwe"
    ),
]                


BaseCog = getattr(commands, "Cog", object)


class Joshiplz(BaseCog):
    #JoshiSpam!

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop)
     
    @commands.command()
    async def joshi(self, ctx):
        """ - 1x joshi! """
        try:
            path = choice(joshi_path)
            files = os.listdir(path)
            index = random.randrange(1, len(files))
#            file = path+"/"+files[index]
#            fp = path
            await ctx.send(file=discord.File(path+"/"+files[index]))
            
        except:
            await ctx.send("Nope")
            
    @commands.command()
#    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def joshiplz(self, ctx, amount : int = 3):
        """ - Throws a Joshi bomb!

        Defaults to 3, max is 12"""
        results = []
        if amount > 12:
            amount = 12
        if amount < 1:
            amount = 1
        try:
            for x in range(0,amount):
                path = choice(joshi_path)
                files = os.listdir(path)
                index = random.randrange(1, len(files))
                await ctx.send(file=discord.File(path+"/"+files[index]))
            return     
        
        except:
            await ctx.send("oop")

    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())

    __del__ = cog_unload
