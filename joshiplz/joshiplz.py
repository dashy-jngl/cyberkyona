# Post animal pics by Eslyium#1949 & Yukirin#0048

# Discord
import discord

# Red
from redbot.core import commands
from .errors import RetryLimitExceeded


# Libs
import aiohttp
import os
import random

#import aiohttp
import asyncio
import discord
import io
import logging
import os
from typing import Awaitable, Callable

BaseCog = getattr(commands, "Cog", object)


class Joshiplz(BaseCog):
    #JoshiSpam!
    
    # 8MB; not using 1024 because not sure how exactly Discord does it, erring on small side
    SIZE_LIMIT = 1000 * 1000 * 8
    # number of times we can fail to get an acceptable image before giving up
    RETRY_LIMIT = 10
    
#    def __init__(self, bot):
#        self.bot = bot
#        self.__session = aiohttp.ClientSession()
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.__session = aiohttp.ClientSession()

    def cog_unload(self) -> None:
        if self.__session:
            asyncio.get_event_loop().create_task(self.__session.close())



    @commands.command()
    async def joshi(self, ctx: commands.Context) -> None:
        """Get a random bird."""

        await ctx.trigger_typing()

        async def fetcher() -> str:
            url = "http://dash.pallas.feralhosting.com/.joshi?count=1"
            async with self.__session.get(url) as response:
                return (await response.json())[0]

        try:
            file = await self.__get_image_carefully(fetcher)
            await ctx.send(file=file)
        except (aiohttp.ClientError, RetryLimitExceeded):
            #log.warning("API call failed; unable to get bird picture")
            await ctx.send("I was unable to get a bird picture.")

    async def __get_image_carefully(self, fetcher: Callable[[], Awaitable[str]]) -> discord.File:
        for x in range(Joshiplz.RETRY_LIMIT):
            try:
                img_url = await fetcher()
                filename = os.path.basename(img_url)
                async with self.__session.head(img_url) as size_check:
                    if size_check.content_length is None or size_check.content_length > Randimals.SIZE_LIMIT:
                        continue
                    async with self.__session.get(img_url) as image:
                        return discord.File(io.BytesIO(await image.read()), filename=filename)
            except aiohttp.ClientError:
                continue
        raise RetryLimitExceeded()
        
        
#    def cog_unload(self):
#        self.bot.loop.create_task(self.session.close())

#    __del__ = cog_unload
