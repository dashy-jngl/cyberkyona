import discord
import os
from redbot.core import commands
from random import choice
from typing import List
from typing import Optional

file_path = "/home/dashy9000/archive/roleplayData/"
path = "http://www.onlytams.com/roleplayData/"

footers: List[str] = [
    ("❤️🤼‍♀️ Be happy with Pro-Wrestling 🤼‍♀️❤️"),
    ("❤️🤼‍♀️ Made with help from joshistans everywhere 🤼‍♀️❤️"),
    ("❤️🤼‍♀️ Made with love 🤼‍♀️❤️"),
    ("❤️🤼‍♀️ Everyone is differnt... 🤼‍♀️❤️"),
]

BaseCog = getattr(commands, "Cog", object)
class Roleplay(commands.Cog):

    __author__ = ["Airen", "JennJenn", "TrustyJAID", "dasha"]
    __version__ = "1.0.0"

    def __init__(self, bot):
        self.bot = bot

    def format_help_for_context(self, ctx: commands.Context) -> str:
        
        pre_processed = super().format_help_for_context(ctx)
        return f"{pre_processed}\n\nCog Version: {self.__version__}"
    
    #send embed mention
    async def sendEmbedMention(self, ctx: commands.Context, imgurl, msg, footer, user, user2,):

        # Build Embed
        embed = discord.Embed()
        embed.set_footer(text=footer)
        embed.set_image(url=imgurl)
        
        embed.description = f"**{user.mention} {msg} {user2.mention}**"
        await ctx.send(embed=embed)

    #send embed No mention
    async def sendEmbedNoMention(self, ctx: commands.Context, imgurl, msg, footer, user,):

        # Build Embed
        embed = discord.Embed(color=discord.Color(value=16580705))
        embed.set_footer(text=footer)
        embed.set_image(url=imgurl)
        embed.description = f"**{user.mention} {msg}**"
        await ctx.send(embed=embed)
            

    @commands.command()
    async def hugs(self, ctx: commands.Context, user: Optional[discord.Member]):
        """
            hugs!!!!!!!
        """
        #check member
        if not user:
            author = self.bot.user
            user = ctx.message.author
        #set message author
        else:
            author = ctx.message.author
        #set image
        images = choice(hugs)

        await self.sendEmbed(ctx, author, user, images)

    @commands.command()
    async def slap(self, ctx: commands.Context, user: Optional[discord.Member]):
        """
            hugs!!!!!!!
        """
        #check member
        if not user:
            author = self.bot.user
            user = ctx.message.author
        #set message author
        else:
            author = ctx.message.author
        #set image
        images = choice(slap)

        await self.sendEmbed(ctx, images, author, user)

    @commands.command()
    async def test(self, ctx: commands.Context, user: Optional[discord.Member]):
        """
            test the dasha
        """

        #set directory
        directory = "test/"
        #set footer
        footer = choice(footers)
        #set author
        author = ctx.message.author
        #set image
        data_path = file_path + directory
        files = choice(os.listdir(data_path))
        images = path + directory + files
        #set messages
        msg = images
        msg2 = " Tests "
        #await ctx.send(f"{msg}")

        #check mention
        if not user:
            user = self.bot.user
            await self.sendEmbedNoMention(ctx, images, msg, footer, author)
        else:
            await self.sendEmbedMention(ctx, images, msg2, footer, author, user)

    @commands.command()
    async def testfile(self, ctx: commands.Context):
        """
            test the dasha
        """
        data_path = file_path + "test/"
        files = choice(os.listdir(data_path))
        await ctx.send(file=discord.File(file_path + "test/" + files))