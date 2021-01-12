import discord
from redbot.core import commands
from random import choice
from redbot.core.i18n import Translator, cog_i18n
from typing import List

bot_msg = [
    ("I suggest: "),
]

stardom: List[str] = [
    ("**Giulia vs. Syuri - 2020.12.20 Stardom Osaka Dream Cinderella** https://m.bilibili.com/video/BV1Bf4y1C7QP"),
    ("**Momo vs. Utami - 2020.12.20 Stardom Osaka Dream Cinderella** https://m.bilibili.com/video/BV1By4y1U7h6"),
    ("**Konami vs.Giulia - 2020.11.15 Stardom Sendai Cinderella** https://m.bilibili.com/video/BV19a4y1s7zU"),
    ("**Mayu Iwatani vs. Saki Kashima 2020.03.08 Stardom No People Gate** https://m.bilibili.com/video/BV17E411T7DX"),
    ("**Momo Watanabe vs. Mayu vs. Konami - 2020.07.12 Stardom New Summer Day 2** https://m.bilibili.com/video/BV1JC4y1b7Bu"),
    ("**Kagetsu vs. Mayu Iwatani - 2019.21.24 Stardom End of Year Climax ** https://m.bilibili.com/video/BV1BJ411p7Uh"),
    ("**HZK vs. Arisa Hoshiki - 2019.07.24 Stardom** https://m.bilibili.com/video/BV12z4y1R7Tz"),
    ("**Arisa Hoshiki vs. Tam Nakano - 2019.06.16 Stardom** https://m.bilibili.com/video/BV1x441137ec"),
    ("**Mayu Iwatani vs. Syuri - 2020.10.03 Stardom Yokohama Cinderella** https://m.bilibili.com/video/BV1vD4y1R7vw"),
    ("**Momo Watanabe vs.Mayu Iwatani - 2020.01.19 Stardom 9th Anniversary in Korakuen** https://m.bilibili.com/video/BV1x7411r7BB"),
    ("**Kagetsu & Mayu Iwatani vs. Momo Watanabe & Jungle Kyona - 2020. Stardom ** https://m.bilibili.com/video/BV1Q7411n74E"),
    ("**Kairi Hojo vs. Jungle Kyona - 2017.02.23 Stardom** https://www.dailymotion.com/video/x7tcj5z"),    
    ("**Momo Watanabe vs. Jungle Kyona - 2019.03.03 Stardom World in Nagoya** https://m.bilibili.com/video/BV1ib411v7ws" ),    
    (""),    
    (""),    
    (""),
]
sendai: List[str] = [
    ("**Dash Chisako vs. Sareee - 2019.07.07 Sendai Girls** https://m.bilibili.com/video/BV1Z4411C7Rs"),
]
agz: List[str] = [
    ("agz matches go here"),
]
ice: List[str] = [
    ("**Tsukasa FUjimoto vs. Maya Yukihi - 2019.08.03** https://m.bilibili.com/video/BV1x7411k73E"),
]
indy: List[str] = [
    ("**Tsukasa FUjimoto vs. Maya Yukihi - 2019.08.03** https://m.bilibili.com/video/BV1x7411k73E"),
]
termlist = [
    (stardom),
    (agz),
]
class Recommend(commands.Cog):

    __author__ = ["Airen", "JennJenn", "TrustyJAID", "dasha"]
    __version__ = "1.0.0"

    def __init__(self, bot):
        self.bot = bot

    def format_help_for_context(self, ctx: commands.Context) -> str:
        
        pre_processed = super().format_help_for_context(ctx)
        return f"{pre_processed}\n\nCog Version: {self.__version__}"

    @commands.command(aliases=["rc"])
    async def recommend(self, ctx: commands.Context, promo = None) -> None:
        """
            - Recommends matches from WWC user submissions!

            `promo` the promotion you would like to see
        """

        msg = " "
        if promo:

            if promo == "stardom":
                await ctx.send(f"{ctx.author.mention}{choice(bot_msg)}{choice(stardom)}")
            
            elif promo == "agz":
                await ctx.send(f"{ctx.author.mention} {choice(bot_msg)}{choice(agz)}")    
            
            else:
                list = choice(termlist)
                await ctx.send(ctx.author.mention + msg + choice(list))
        else:
            list = choice(termlist)
            await ctx.send(ctx.message.author.mention + msg + choice(list))
