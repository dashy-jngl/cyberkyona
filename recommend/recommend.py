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
    ("**Giula vs. Kagestsu - Stardom New Years Stars 2020.01.11** https://m.bilibili.com/video/BV11T4y1g7uM"),
    ("**Arisa Hoshiki vs. Konami - Stardom Cinderella 2019 2019.04.29** https://m.bilibili.com/video/BV1r4411i7zu"),
    ("**Toni Storm vs. Konami - Stardom 2019.05.06 Golden Week Stars 2019 Day** https://m.bilibili.com/video/BV1F4411j79T"),
    ("**Momo Watanabe vs. Io Shirai - 23.05.2018 Stardom Gold Star** https://m.bilibili.com/video/BV11W411w75L"),
    ("**Io Shirai vs. Mayu Iwatani - Stardom 2016 Gold May** https://m.bilibili.com/video/BV1NW411M71q"),
    ("**Toni Storm vs Io Shirai - Stardom** https://m.bilibili.com/video/BV15x411E7S2"),
    ("**大江户队(Hazuki & Kagetsu) vs. Queen's Quest (Io Shirai & Momo Watanabe) - stardom 2018** https://m.bilibili.com/video/BV1Ss411P7K3"),
    ("**Io Shirai vs. Kairi Hojo - Stardom The Highest 2017.03.20** https://m.bilibili.com/video/BV13x411B77G"),
    ("**Exploding Bat Death Match: Io Shirai and Tam Nakano vs. Kagestsu and Natsu Sumire - Stardom 2018.04.01** https://m.bilibili.com/video/BV1VW411M7ys"),
    ("**Kairi Hojo vs. Act Yasukawa - Stardom** https://m.bilibili.com/video/BV14W411j7Q4"),
    ("**Kairi Hojo vs Santana Garrett - Stardom 2016.05.15** https://m.bilibili.com/video/BV17x411G7tX"),
    ("**Kairi Hojo vs. Meiko Satomura - Stardom** https://m.bilibili.com/video/BV14W411j7Zw"),
    ("**Kairi Hojo vs. Toni Storm - Stardom ** https://m.bilibili.com/video/BV1mW411E71q"),
    #("**** "),
    
]
sendai: List[str] = [
    ("**Dash Chisako vs. Sareee - 2019.07.07 Sendai Girls** https://m.bilibili.com/video/BV1Z4411C7Rs"),
    ("**Meiko Satomura vs.Toni Storm - 2019.07.27 Sendai Girls, Sendai UK** https://m.bilibili.com/video/BV14J41117po"),
    ("**Meiko Satomura vs.Sareee - 2019.04.16 Sendai Girls** https://m.bilibili.com/video/BV1Y4411A7iu"),
    ("**Tag: DASH Chisako and Meiko Satomura and Syuri vs. Sakura Hirota and Chihiro Hashimoto and Yuu** https://www.youtube.com/watch?v=EdxRCoIv5EE")
]
agz: List[str] = [
    ("**Miyuki Takase vs Himeka Arita - AGZ 2019.11.06** https://m.bilibili.com/video/BV1s54y1s72x"),
    ("**Miyuki Takase vs Tae Honma - AGZ 2019.11.03** https://www.bilibili.com/video/BV1Wy4y1m74B"),
    ("**Miyuki Takase vs Nagisa Nozaki - AGZ 2020.03.05**  https://www.bilibili.com/video/BV1Tv41147Ni"),
    ("**Giulia vs Saori Anou - AGZ 2019.7.21** https://www.bilibili.com/video/BV1th411y7SG "),
    ("**Saori Anou vs Reika Saiki AGZ 2019.8.14 ** https://www.bilibili.com/video/BV1Zf4y1r7qQ"),
]
ice: List[str] = [
    ("**Tsukasa Fujimoto vs. Maya Yukihi - 2019.08.03 Ice Ribbon New Ice Ribbon #974 ~ Osaka Ribbon 2019 III** https://m.bilibili.com/video/BV1x7411k73E"),
    ("**Tsukasa Fujimoto vs.sareee - 2019.09.14 Ice-Ribbon #992** https://m.bilibili.com/video/BV1Nt4y1v7AA"),
    ("**Risa Sera vs. Rina Yamashita - 2020 Ice Ribbon Yokohama Bunka Gymnasium** https://www.dailymotion.com/video/x7wrnh4"),
    ("**Giula vs. Maya Yukihi - 2019.05.25 Ice Ribbon Osaka Ribbon 2019** https://m.bilibili.com/video/BV1qt411E7Aj"),
    ("**Tsukasa Fujimoto vs. Maya Yuhiki - 2018.12.31 Ice Ribbon RibbonMania ** https://m.bilibili.com/video/BV1V54y1m7zQ"),
    ("**Suzu Suzuki vs. Maya Yukihi - 2020.08.09 Ice Ribbon New Ice Ribbon #1057 ~ Ice Ribbon Yokohama Bunka Gymnasium Final** https://m.bilibili.com/video/BV1rh411976b"),
]
indy: List[str] = [
    ("**Kagetsu vs. Meiko Satomura - 2020.02.24 Kagestsu Produce** https://m.bilibili.com/video/BV19E411u79u"),
]
wwe: List[str] = [
    ("**Charlotte Flair Vs IO Shirai Vs Rhea Ripley - NXT** https://www.dailymotion.com/video/x7ucx0n"),
    ("**Io Shirai vs. Candice Lerae - NXT** https://www.dailymotion.com/video/x7wmzax"),
    ("**Last Woman Standing: Rhea Ripley vs. Raquel Gonzales - NXT** https://www.dailymotion.com/video/x7yizta"),
    ("**Rhea Ripley vs. Shayna Bazsler - NXT** https://www.dailymotion.com/video/x7y67pi"),
    ("**Steel Cage: Rhea Ripley vs. Mercedes Martines - NXT** https://www.dailymotion.com/video/x7w20gy"),
    ("**Asuka vs. Bayley - NXT** https://www.dailymotion.com/video/x656jeb"),
    ("**Ember Moon vs. Asuka - NXT** https://www.dailymotion.com/video/x5xiing"),
]
tjp: List[str] = [
    ("**Yuka Sakazaki vs. Mizuki - 2020.11.07 TJPW Wrestle Princess** https://m.bilibili.com/video/BV1wy4y1z76y"),
    #("**** "),
]
wave: List[str] = [
    ("**Kana vs Kana (Sakura Hirota) - Wave 2015** https://www.youtube.com/watch?v=oBc04ILjeCM"),
]
marv: List[str] = [
    ("**** "),
]
sead: List[str] = [
    ("**Arisa Nakajima (c) vs. Rina Yamashita, SEAdLINNNG New Leaf! (10.03.2020)** https://youtu.be/qjGE9NEMAIc"),
]
oz: List[str] = [
    ("**Hiroyo Matsumoto vs. Hikari Shida - OZ Academy Plum Hanasaku 2017.08.20** https://m.bilibili.com/video/BV1f441177F8"),
    ("**Mayumi Ozaki and Maya Yuhiki vs Rina Yamashita and Yoshiko - OZ Academy Flower Bloom In Yokohama 2018** https://m.bilibili.com/video/BV1Nt411Z7HB"),
]

termlist = [
    (stardom),
    (agz),
    #(marv),
    #(wwe),
    (sendai),
    (indy),
    (ice),
    (tjp),
    #(wave),
    (sead),
    (oz),
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
                await ctx.send(f"{ctx.author.mention}{choice(bot_msg)}{choice(agz)}")    
            elif promo == "sendai":
                await ctx.send(f"{ctx.author.mention}{choice(bot_msg)}{choice(sendai)}")    
            elif promo == "wave":
                await ctx.send(f"{ctx.author.mention}{choice(bot_msg)}{choice(wave)}")    
            elif promo == "ice":
                await ctx.send(f"{ctx.author.mention}{choice(bot_msg)}{choice(ice)}")
            elif promo == "Ice":
                await ctx.send(f"{ctx.author.mention}{choice(bot_msg)}{choice(ice)}")                
            elif promo == "indy":
                await ctx.send(f"{ctx.author.mention}{choice(bot_msg)}{choice(indy)}")    
            #elif promo == "marv":
                #await ctx.send(f"{ctx.author.mention}{choice(bot_msg)}{choice(marv)}")    
            elif promo == "sead":
                await ctx.send(f"{ctx.author.mention}{choice(bot_msg)}{choice(sead)}")
            elif promo == "tjp":
                await ctx.send(f"{ctx.author.mention}{choice(bot_msg)}{choice(tjp)}")
            elif promo == "oz":
                await ctx.send(f"{ctx.author.mention}{choice(bot_msg)}{choice(oz)}")                
            
            else:
                list = choice(termlist)
                await ctx.send(ctx.author.mention + msg + choice(list))
        else:
            list = choice(termlist)
            await ctx.send(ctx.message.author.mention + msg + choice(list))