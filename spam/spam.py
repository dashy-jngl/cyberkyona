# make JoshiPlz

# Discord
import discord

# Red
from redbot.core import commands
from redbot.core.utils.tunnel import Tunnel



# Libs
import os
import random
#import urllib.request
from random import choice
import time

from typing import Optional

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
        time.sleep(1)
        path = choice(joshi_path)
        fileses = os.listdir(path)
        index = random.randrange(1, len(fileses))
        filelist = [
        (files),
        (discord.File(path+"/"+fileses[index])),
        ]
        # sending the message
        try:
            await channel.send(text, files=fileses, allowed_mentions=mentions)
        except discord.errors.HTTPException as e:
            author = ctx.author
            if not ctx.guild.me.permissions_in(channel).send_messages:
                try:
                    await ctx.send(
                        _("I am not allowed to send messages in ") + channel.mention,
                        delete_after=2,
                    )
                except discord.errors.Forbidden:
                    await author.send(
                        _("I am not allowed to send messages in ") + channel.mention,
                        delete_after=15,
                    )
                    # If this fails then fuck the command author
            elif not ctx.guild.me.permissions_in(channel).attach_files:
                try:
                    await ctx.send(
                        _("I am not allowed to upload files in ") + channel.mention, delete_after=2
                    )
                except discord.errors.Forbidden:
                    await author.send(
                        _("I am not allowed to upload files in ") + channel.mention,
                        delete_after=15,
                    )
            else:
                log.error(
                    f"Unknown permissions error when sending a message.\n{error_message}",
                    exc_info=e,
                )
    @commands.command(name="spam")
    async def _spam(
        self, 
        ctx: commands.Context,        
        channel: Optional[discord.TextChannel], 
        amount : int = 3,
        *, 
        text: str = ""
    ):
        """
        Make the bot say what you want in the desired channel.

        If no channel is specified, the message will be send in the current channel.
        You can attach some files to upload them to Discord.

        Example usage :
        - `!say #general hello there`
        - `!say owo I have a file` (a file is attached to the command message)
        """
        for  x in range(0,amount):
            files = await Tunnel.files_from_attatch(ctx.message)
            await self.spam(ctx, channel, text, files)
            await ctx.send(fileses=discord.File(path+"/"+fileses[index]))
        return

        
    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())

    __del__ = cog_unload
