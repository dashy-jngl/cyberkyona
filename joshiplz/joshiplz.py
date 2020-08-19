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

mayu_path = "/home/dashy9000/data/.mayu"
hardy_path = "/home/dashy9000/data/.hardy"
dashy_path = "/home/dashy9000/data/.dashy"
frog_path = "/home/dashy9000/data/.frog"
asuka_path = "/home/dashy9000/data/.asuka"
tiger_path = "/home/dashy9000/data/.tiger"
light_path = "/home/dashy9000/data/.light"

joshi_path = [
    (
        "/home/dash/datay9000/.joshi"
    ),
    (
        "/home/dash/datay9000/.wwe"
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
            await ctx.send("<:jungleKyonaLook:695168285586751509>")
            
    @commands.command()
#    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def joshiplz(self, ctx: commands.Context, amount : int = 3, user: discord.Message.author = None):
        """ - Throws a Joshi bomb!

        Defaults to 3, max is 12"""
        results = []
        if amount > 12:
            amount = 12
        if amount < 1:
            amount = 1
        user = ctx.message.author
        try:
            for x in range(0,amount):
                if user.id == 338135974158794752: #dashy
                    path = dashy_path
                    files = os.listdir(path)
                    index = random.randrange(1, len(files))
                    await ctx.send(file=discord.File(path+"/"+files[index]))
                else:
                    path = choice(joshi_path)
                    files = os.listdir(path)
                    index = random.randrange(1, len(files))
                    await ctx.send(file=discord.File(path+"/"+files[index]))
            return     
        
        except:
            await ctx.send("<:jungleKyonaLook:695168285586751509>")

    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())

    __del__ = cog_unload
