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

mayu_path = "/home/dashy9000/data/.mayu"    #
hardy_path = "/home/dashy9000/data/.hardy"  # 303430784771948544
dashy_path = "/home/dashy9000/data/.dashy"  #
cryo_path = "/home/dashy9000/data/.cryo"    # 302168981903769602
asuka_path = "/home/dashy9000/data/.asuka"  #
tiger_path = "/home/dashy9000/data/.tiger"  # 574149508989190154
light_path = "/home/dashy9000/data/.light"  #
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


class Spam(BaseCog):
    '''
    #JoshiSpam!
    '''
    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop)
     
    @commands.command()
#    @commands.cooldown(1, 60, commands.BucketType.guild)
    async def spam(
        self,
        ctx: commands.Context,  
        channel: Optional[discord.TextChannel],
        text: str,
        files: list,
        mentions: discord.AllowedMentions = None,
    ):
        if not channel:
            channel = ctx.channel
        if not text and not files:
            await ctx.send_help()
            return

        # preparing context info in case of an error
        if files != []:
            error_message = (
                "Has files: yes\n"
                f"Number of files: {len(files)}\n"
                f"Files URL: " + ", ".join([x.url for x in ctx.message.attachments])
            )
        else:
            error_message = "Has files: no"

        # sending the message
        for x in range(0,amount):
            time.sleep(1)
            try:
                await channel.send(text, files=files, allowed_mentions=mentions)
            except:
                await ctx.send("<:jungleKyonaLook:695168285586751509>")
        return
        
    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())

    __del__ = cog_unload
