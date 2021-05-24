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

base_path = "/home/dashy9000/data/joshifiles/"

momo = [
#    ("momok"),
#    ("momot"),
    ("momow"),
]

saya = [
    ("sayak"),
    ("sayai"),
]

arisa = [
    ("arisah"),
#    ("arisan"),
]

BaseCog = getattr(commands, "Cog", object)


class Plz(BaseCog):
    #JoshiSpam!

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop)

    @commands.command()
    async def plz(self, ctx, ask: str, num: int = 1):

        if ask != "ASUKA" and ask != "SAKI":
            ask = ask.lower()

        if ask == "momo":
            ask = choice(momo)

        if ask == "arisa":
            ask = choice(arisa)

        if ask == "saya":
            ask = choice(saya)

        if ask == "miyagi" or ask == "michiko":
            ask = "andras"

        if ask == "hazuki":
            ask = "hzk"

        if ask == "kyona":
            ask = "jungle"

        if ask == "tora":
            ask = "natsuko"

        if ask == "poi" or ask == "natsumi":
            ask = "natsupoi"

        try:
            try:
                path = base_path + ask
                files = os.listdir(path)
            except:
                path = base_path + "momow"
                files = os.listdir(path)
            index = random.randrange(0, len(files))
            await ctx.send(file=discord.File(path+"/"+files[index]))
        except:
            await ctx.send("code better dash")


    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())

    __del__ = cog_unload
