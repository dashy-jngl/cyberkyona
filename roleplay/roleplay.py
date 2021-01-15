import discord
from redbot.core import commands, Config
from random import randint
from random import choice
import aiohttp
import logging

log = logging.getLogger("Roleplay")  # Thanks to Sinbad for the example code for logging
log.setLevel(logging.DEBUG)

console = logging.StreamHandler()

if logging.getLogger("red").isEnabledFor(logging.DEBUG):
    console.setLevel(logging.DEBUG)
else:
    console.setLevel(logging.INFO)
log.addHandler(console)

BaseCog = getattr(commands, "Cog", object)


class Roleplay(BaseCog):
    """Interact with people!"""

    def __init__(self):
        self.config = Config.get_conf(self, identifier=842364413)
        default_global = {
            "hugs": [
                ("https://media.discordapp.net/attachments/559545867590303747/790779937904263169/tenor_-_2020-12-21T212436.031.gif")
            ],

        }
        self.config.register_global(**default_global)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def hug(self, ctx, *, user: discord.Member):
        """Hugs a user!"""

        author = ctx.message.author
        images = choice(hugs)

        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} hugs {user.mention}**"
        embed.set_footer(text="Made with the help of nekos.life")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

