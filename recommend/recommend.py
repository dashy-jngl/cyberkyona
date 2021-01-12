import discord
from redbot.core import commands
from random import choice
from redbot.core.i18n import Translator, cog_i18n
from typing import List

bot_msg = [
    (", I suggest: "),
    (", What about?: "),
    (", I recommend: "),
    (", I think: "),
    (", I like: "),
]

stardom: List[str] = [
    ("**Giulia vs. Syuri - 2020.12.20 Stardom Osaka Dream Cinderella** https://m.bilibili.com/video/BV1Bf4y1C7QP"),
    ("**Momo vs. Utami Hayashishita - 2020.12.20 Stardom Osaka Dream Cinderella** https://m.bilibili.com/video/BV1By4y1U7h6"),
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
    ("**Kairi Hojo vs. Meiko Satomura - Stardom** https://m.bilibili.com/video/BV14W411j7Zw"),    
    ("**Mayu Iwatani vs. Jungle Kyona - 2020.07.24 Stardom Cinderella Summer in Nagoya** https://m.bilibili.com/video/BV11K4y1e7fx"),
    ("**Mayu Iwatani vs. Takumi Iroha - 2020.10.18 Stardom** https://m.bilibili.com/video/BV1J54y1r7Kh"),
    ("**Natsuko vs. Giula 2020.03.24 Stardom Cinderella 2020** https://m.bilibili.com/video/BV1Ff4y1i7qZ"),
    ("**Mayu Iwatani vs. Tam Nakano - 2020.09.19 Stardom** https://m.bilibili.com/video/BV1ta411c71E"),
    ("**AZM vs. Starlight Kid - 2020.10.03** https://m.bilibili.com/video/BV1sy4y1q7Rd"),
    ("**Momo Watanabe vs. Io Shirai - Stardom** https://m.bilibili.com/video/BV1WW41157wV"),
    ("**Momo Watanabe vs. Arisa Hoshiki - 2019.05.16 Stardom** https://m.bilibili.com/video/BV1L441157G3"),
    ("**Momo Watanabe vs. Toni Storm - 2019.05.04 -Stardom Golden Week Stars** https://m.bilibili.com/video/BV1F4411Y776"),
    ("**Mayu Iwatani vs. Utami Hayashishita -2020.11.15 Stardom Sendai Cinderella** https://m.bilibili.com/video/BV1nz4y1y764"),
    ("**Momo Watanabe & Utami Hayashishita vs. Jungle Kyona & Konami - 2019.07.15 Stardom World Big Summer In Nagoya** https://m.bilibili.com/video/BV1RE411D7r5"),
    #("**** "),
    
]
sendai: List[str] = [
    ("**Dash Chisako vs. Sareee - 2019.07.07 Sendai Girls** https://m.bilibili.com/video/BV1Z4411C7Rs"),
    ("**Meiko Satomura vs.Toni Storm - 2019.07.27 Sendai Girls, Sendai UK** https://m.bilibili.com/video/BV14J41117po"),
    ("**Meiko Satomura vs.Sareee - 2019.04.16 Sendai Girls** https://m.bilibili.com/video/BV1Y4411A7iu"),
]
agz: List[str] = [
    ("agz matches go here"),
]
ice: List[str] = [
    ("**Tsukasa Fujimoto vs. Maya Yukihi - 2019.08.03 Ice Ribbon New Ice Ribbon #974 ~ Osaka Ribbon 2019 III** https://m.bilibili.com/video/BV1x7411k73E"),
    ("**Tsukasa Fujimoto vs.sareee - 2019.09.14 Ice-Ribbon #992** https://m.bilibili.com/video/BV1Nt4y1v7AA"),
    ("**Risa Sera vs. Rina Yamashita - 2020 Ice Ribbon Yokohama Bunka Gymnasium** https://www.dailymotion.com/video/x7wrnh4"),
]
indy: List[str] = [
    ("**Kagetsu vs. Meiko Satomura - 2020.02.24 Kagestsu Produce** https://m.bilibili.com/video/BV19E411u79u"),
]
wwe: List[str] = [
    ("**** "),
]
tjp: List[str] = [
    ("**Yuka Sakazaki vs. Mizuki - 2020.11.07 TJPW Wrestle Princess** https://m.bilibili.com/video/BV1wy4y1z76y"),
    #("**** "),
]
wave: List[str] = [
    ("**** "),
]
marv: List[str] = [
    ("**** "),
]
wwe: List[str] = [
    ("**** "),
]
sead: List[str] = [
    ("**Arisa Nakajima (c) vs. Rina Yamashita, SEAdLINNNG New Leaf! (10.03.2020)** https://youtu.be/qjGE9NEMAIc"),
]

termlist = [
    (stardom),
    #(agz),
    #(marv),
    #(wwe),
    (sendai),
    (indy),
    (ice),
    (tjp),
    #(wave),
    (sead),
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
            elif promo == "sendai":
                await ctx.send(f"{ctx.author.mention} {choice(bot_msg)}{choice(sendai)}")    
            elif promo == "wave":
                await ctx.send(f"{ctx.author.mention} {choice(bot_msg)}{choice(wave)}")    
            elif promo == "ice":
                await ctx.send(f"{ctx.author.mention} {choice(bot_msg)}{choice(ice)}")    
            elif promo == "indy":
                await ctx.send(f"{ctx.author.mention} {choice(bot_msg)}{choice(indy)}")    
            elif promo == "marv":
                await ctx.send(f"{ctx.author.mention} {choice(bot_msg)}{choice(marv)}")    
            elif promo == "sead":
                await ctx.send(f"{ctx.author.mention} {choice(bot_msg)}{choice(sead)}")    
            
            else:
                list = choice(termlist)
                await ctx.send(ctx.author.mention + msg + choice(list))
        else:
            list = choice(termlist)
            await ctx.send(ctx.message.author.mention + msg + choice(list))