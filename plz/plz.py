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
    ("momok"),
#    ("momot"),
    ("momow"),
]

maika = [
    ("maiker"),
#    ("momot"),
    ("maikao"),
]
saya = [
    ("sayak"),
    ("sayai"),
]

arisa = [
    ("arisah"),
    ("arisan"),
]

saki = [
    ("sakik"),
    ("sakia"),
    ("SAKI"),
]
mio = [
    ("miom"),
#    ("mios"),

]

BaseCog = getattr(commands, "Cog", object)


class Plz(BaseCog):
    #JoshiSpam!

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop)

    @commands.command()
    async def plz(self, ctx, ask: str = "mayu"):

        if ask != "ASUKA" and ask != "SAKI":
            ask = ask.lower()

        if ask == "arisa":
            ask = choice(arisa)

        if ask == "asuka":
            ask = "kana"

        if ask == "mio":
            ask = choice(mio)

        if ask == "momo":
            ask = choice(momo)

        if ask == "saya":
            ask = choice(saya)

        if ask == "saki":
            ask = choice(saki)
        
        if ask == "maika":
            ask = choice(maika)

        if ask == "coco" or ask == "ez" :
            ask = "momok"
        
        if ask == "iyo":
            ask = "io"

        if ask == "misao":
            ask = "hyper"
            
        if ask == "mii":
            ask = "hibiscus"

        if ask == "champ":
            ask = "utami"

        if ask == "slk":
            ask = "starlight"

        if ask == "hikaru":
            ask = "shida"

        if ask == "miyagi" or ask == "michiko":
            ask = "andras"

        if ask == "hazuki":
            ask = "hzk"

        if ask == "sarray":
            ask = "sareee"

        if ask == "bee":
            ask = "suzume"

        if ask == "kyona":
            ask = "jungle"

        if ask == "tora":
            ask = "natsuko"

        if ask == "poi" or ask == "natsumi":
            ask = "natsupoi"
            
        if ask == "sausage" or ask == "suasage" or ask == "ssj":
            ask = "sasha"

        if ask == "bobby" ask == "bby":
            ask = "mayu"
           
        if ask == "mo":
            ask = "momoka"
            
        if ask == "bubbles":
            ask = "alexa"
            
        if ask == "brzy":
            ask = "sayai"
            
        if ask == "feptom":
            ask = "unagi"
            
        if ask == "roxie":
            ask = "tam" 
            
        try:
            try:
                path = base_path + ask
                files = os.listdir(path)
            except:
                path = base_path + "maya"
                files = os.listdir(path)
            index = random.randrange(0, len(files))
            await ctx.send(file=discord.File(path+"/"+files[index]))
        except:
            await ctx.send("code better dash")


    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())

    __del__ = cog_unload
