
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
import time

import aiohttp
#import asyncio
#import io
#import logging
#from typing import Awaitable, Callable
from typing import Optional


mayu_path = "/home/dashy9000/data/.mayu"    # 465090995965526016
hardy_path = "/home/dashy9000/data/.hardy"  # 303430784771948544
dashy_path = "/home/dashy9000/data/.dashy"  #
asuka_path = "/home/dashy9000/data/.asuka"  # 174754160963485698
tiger_path = "/home/dashy9000/data/.tiger"  # 574149508989190154
ksup_path = "/home/dashy9000/data/.ksup"    # 404141277358325771
mo_path = "/home/dashy9000/data/.mo"        # 132091505237032960

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
            await ctx.send("<:dashsrs:763999844724899841>")

    @commands.command()
#    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def joshiplz(self, ctx: commands.Context, joshi: Optional[str], amount : int = 3):
        """ - Throws a Joshi bomb!
        Defaults to 3, max is 500"""
        if not amount:
            amount = 3
        results = []
        if amount > 6:
            amount = 6
        if amount < 1:
            amount = 1
        user = ctx.message.author
        if user.id == 404141277358325771: #ksup
            upath = ksup_path
        if user.id == 303430784771948544: #hardy
            upath = hardy_path
#        if user.id == 465090995965526016: #MM
#            upath = mayu_path
        if user.id == 132091505237032960: #mo
            upath = mo_path
        if user.id == 574149508989190154: #tigr
            upath = tiger_path
#        if user.id == 174754160963485698: #pz
#            upath = asuka_path
        if user.id == 338135974158794752: #dash
            upath = dashy_path

        try:
            for x in range(0,amount):
                time.sleep(1)
                spice = random.randrange(0,100)
                if joshi:
                    path = "/home/dashy9000/data/" + joshi
                    files = os.listdir(path)
                    index = random.randrange(1, len(files))
                    await ctx.send(file=discord.File(path+"/"+files[index]))
                else:
                    if spice > 40:
                        path = upath
                        files = os.listdir(path)
                        index = random.randrange(1, len(files))
                        await ctx.send(file=discord.File(path+"/"+files[index]))
                    else:
                        path = choice(joshi_path)
                        files = os.listdir(path)
                        index = random.randrange(1, len(files))
                        await ctx.send(file=discord.File(path+"/"+files[index]))
                return
#        else:
#            path = "/home/dashy9000/data/" + joshi
#            try:
#                for x in range(0,amount):
#                    time.sleep(1)
#                    files = os.listdir(path)
#                    index = random.randrange(1, len(files))
#                    await ctx.send(file=discord.File(path+"/"+files[index]))
#                return

        except:
            await ctx.send("<:dashsrs:763999844724899841>")

    @commands.command()
#    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def joshispam(self, ctx: commands.Context, amount : int = 3, user: discord.Message.author = None):
        """ - Throws a Joshi bomb!
        Defaults to 3, max is 500"""
        results = []
        if amount > 500:
            amount = 500
        if amount < 1:
            amount = 1
        user = ctx.message.author
        if user.id == 404141277358325771: #ksup
            upath = ksup_path
        if user.id == 303430784771948544: #hardy
            upath = hardy_path
#        if user.id == 465090995965526016: #MM
#            upath = mayu_path
        if user.id == 132091505237032960: #mo
            upath = mo_path
        if user.id == 574149508989190154: #tigr
            upath = tiger_path
#        if user.id == 174754160963485698: #pz
#            upath = asuka_path
        if user.id == 338135974158794752: #dash
            upath = dashy_path

        try:
            for x in range(0,amount):
                time.sleep(1)

                spice = random.randrange(0,100)
                if spice > 40:
                    path = upath
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
            await ctx.send("<:dashsrs:763999844724899841>")

    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())

    __del__ = cog_unload
