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

mayu_path = "/home/dashy9000/data/.mayu"    #
hardy_path = "/home/dashy9000/data/.hardy"  # 303430784771948544
dashy_path = "/home/dashy9000/data/.dashy"  #
cryo_path = "/home/dashy9000/data/.cryo"    # 302168981903769602
asuka_path = "/home/dashy9000/data/.asuka"  #
tiger_path = "/home/dashy9000/data/.tiger"  # 574149508989190154
light_path = "/home/dashy9000/data/.light"  #
ksup_path = "/home/dashy9000/data/.ksup"    # 404141277358325771

joshi_path = [
    (
        "/home/dashy9000/data/.joshi"
    ),
    (
        "/home/dashy9000/data/.wwe"
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
    async def joshiplz(self, ctx: commands.Context, amount : int = 2, user: discord.Message.author = None):
        """ - Throws a Joshi bomb!

        Defaults to 5, max is 25"""
        results = []
        if amount > 25:
            amount = 25
        if amount < 1:
            amount = 1
        user = ctx.message.author
        try:
            for x in range(0,amount):
                if user.id == 338135974158794752: #dashy
                    spice = random.randrange(0,100)
                    if spice > 40: 
                        path = dashy_path
                        files = os.listdir(path)
                        index = random.randrange(1, len(files))
                        await ctx.send(file=discord.File(path+"/"+files[index]))
                    elif spice < 41:
                        path = choice(joshi_path)
                        files = os.listdir(path)
                        index = random.randrange(1, len(files))
                        await ctx.send(file=discord.File(path+"/"+files[index]))
                elif user.id == 303430784771948544: #hardy
                    spice = random.randrange(0,100)
                    if spice > 40: 
                        path = hardy_path
                        files = os.listdir(path)
                        index = random.randrange(1, len(files))
                        await ctx.send(file=discord.File(path+"/"+files[index]))
                    elif spice < 41:
                        path = choice(joshi_path)
                        files = os.listdir(path)
                        index = random.randrange(1, len(files))
                        await ctx.send(file=discord.File(path+"/"+files[index]))
                elif user.id == 302168981903769602: #frog
                    spice = random.randrange(0,100)
                    if spice > 40: 
                        path = cryo_path
                        files = os.listdir(path)
                        index = random.randrange(1, len(files))
                        await ctx.send(file=discord.File(path+"/"+files[index]))
                    elif spice < 41:
                        path = choice(joshi_path)
                        files = os.listdir(path)
                        index = random.randrange(1, len(files))
                        await ctx.send(file=discord.File(path+"/"+files[index]))    
                elif user.id == 404141277358325771: #ksup
                    spice = random.randrange(0,100)
                    if spice > 40: 
                        path = ksup_path
                        files = os.listdir(path)
                        index = random.randrange(1, len(files))
                        await ctx.send(file=discord.File(path+"/"+files[index]))
                    elif spice < 41:
                        path = choice(joshi_path)
                        files = os.listdir(path)
                        index = random.randrange(1, len(files))
                        await ctx.send(file=discord.File(path+"/"+files[index]))    
                elif user.id == 574149508989190154: #tigr
                    spice = random.randrange(0,30)
                    if spice > 40: 
                        path = tiger_path
                        files = os.listdir(path)
                        index = random.randrange(1, len(files))
                        await ctx.send(file=discord.File(path+"/"+files[index]))
                    elif spice < 41:
                        path = choice(joshi_path)
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
