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
    ("**DASH Chisako & Sendai Sachiko Vs  Io Shirai & Mayu Iwatani** https://www.youtube.com/watch?v=1s83jVycaRU"),
    #("**** "),
    #("**** "),
]
sendai: List[str] = [
    ("**Dash Chisako vs. Sareee - 2019.07.07 Sendai Girls** https://m.bilibili.com/video/BV1Z4411C7Rs"),
    ("**Meiko Satomura vs.Toni Storm - 2019.07.27 Sendai Girls, Sendai UK** https://m.bilibili.com/video/BV14J41117po"),
    ("**Meiko Satomura vs.Sareee - 2019.04.16 Sendai Girls** https://m.bilibili.com/video/BV1Y4411A7iu"),
    ("**Tag: DASH Chisako and Meiko Satomura and Syuri vs. Sakura Hirota and Chihiro Hashimoto and Yuu** https://www.youtube.com/watch?v=EdxRCoIv5EE"),
    ("**DASH Chisako vs Chihiro Hashimoto - Sendai Girls 2018.05.13** https://youtu.be/d2qpnM2x3RE"),
    ("**Kagetsu vs Chihiro Hashimoto - Sendai Girls February 16th 2020** https://www.dailymotion.com/video/k7cBgl4mNB5auivUiyC"),
    #("**** "),
    #("**** "),
]
agz: List[str] = [
    ("**Miyuki Takase vs Himeka Arita - AGZ 2019.11.06** https://m.bilibili.com/video/BV1s54y1s72x"),
    ("**Miyuki Takase vs Tae Honma - AGZ 2019.11.03** https://www.bilibili.com/video/BV1Wy4y1m74B"),
    ("**Miyuki Takase vs Nagisa Nozaki - AGZ 2020.03.05**  https://www.bilibili.com/video/BV1Tv41147Ni"),
    ("**Giulia vs Saori Anou - AGZ 2019.7.21** https://www.bilibili.com/video/BV1th411y7SG "),
    ("**Saori Anou vs Reika Saiki AGZ 2019.8.14 ** https://www.bilibili.com/video/BV1Zf4y1r7qQ"),
    ("**SAKI & Yuna Mizumori vs Kakeru Sekiguchi & Momo Kohgo - AGZ 2020.02.11** https://www.bilibili.com/video/BV1cv41147Yu/"),
    ("**Noa Igarashi & Yuko Sakurai vs Ayano Irie & Ranmaru - AGZ 2019.07.21 ** https://www.bilibili.com/video/BV1Xt4y1z78p/"),
    ("**Tequila Saya vs Hikari Shimizu - AGZ 2019.05.25** https://www.bilibili.com/video/BV19r4y1T7Kt/"),
    ("**Kakeru Sekiguchi & Miku Aono vs Mii & Rina Amikura - AGZ 2020.11.24** https://www.bilibili.com/video/BV16y4y1m75B/"),
    ("**Miyuki Takase & Himeka Arita vs Mari & SAKI - AGZ 2019.05.25** https://www.bilibili.com/video/BV1tU4y147qc/"),
    #("**** "),
    #("**** "),
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
    ("**Sareee & Yoshiko vs Zap I & Zap T from RJPW 2020** https://youtu.be/EkoNlVXwopE"),
    ("**Nixon Newell vs. Kimber Lee - WCPW True Legacy #7** https://youtu.be/mvBZ5zY1D_U"),
    ("**Sadie Gibbs [AEW] vs Kay Lee Ray [WWE NXTUK] - EVE** https://www.youtube.com/watch?v=oGIKgAS2aQ4&list=LL&index=2"),
    #("**** "),
]
wwe: List[str] = [
    ("**Charlotte Flair Vs IO Shirai Vs Rhea Ripley - NXT** https://www.dailymotion.com/video/x7ucx0n"),
    ("**Io Shirai vs. Candice Lerae - NXT** https://www.dailymotion.com/video/x7wmzax"),
    ("**Last Woman Standing: Rhea Ripley vs. Raquel Gonzales - NXT** https://www.dailymotion.com/video/x7yizta"),
    ("**Rhea Ripley vs. Shayna Bazsler - NXT** https://www.dailymotion.com/video/x7y67pi"),
    ("**Steel Cage: Rhea Ripley vs. Mercedes Martines - NXT** https://www.dailymotion.com/video/x7w20gy"),
    ("**Asuka vs. Bayley - NXT** https://www.dailymotion.com/video/x656jeb"),
    ("**Ember Moon vs. Asuka - NXT** https://www.dailymotion.com/video/x5xiing"),
    #("**** "),
    #("**** "),
]
tjp: List[str] = [
    ("**Yuka Sakazaki vs. Mizuki - 2020.11.07 TJPW Wrestle Princess** https://m.bilibili.com/video/BV1wy4y1z76y"),
    ("**Miyu Yamashita vs. Allysin Kay - SHINE Championship - TJP** https://youtu.be/jRAPC3mNrME"),
    #("**** "),
]
wave: List[str] = [
    ("**Kana vs Kana (Sakura Hirota) - Wave 2015** https://www.youtube.com/watch?v=oBc04ILjeCM"),
    ("**WAVE tournament final: Takumi vs Nagisa Nozaki vs Ryo Mizunami - Wave CTW 2019-07-15** https://youtu.be/R41Q6glbd8w"),
    ("**Takumi vs HIRO'e for the Regina di wave title. - Wave 2019.08.12** https://youtu.be/ljvY8JiP9qg"),
    ("**Luminous (Miyuki Takase & Haruka Umesaki) vs Yuu & Ami Miura - Wave 2020.11.1** https://youtu.be/Mxd3CZ1gcU4"),
    ("**HIRO'e vs Arisa Nakajima - Wave** https://youtu.be/w3Swv_O-giU"),
    ("**HIRO'e vs Tsukasa - Wave** https://youtu.be/XKExTXEA2_o"),
    ("**Sareee & Hibiki vs Rina Amikura & Rina Shingaki from WAVE** https://youtu.be/a5L4E4Flum4"),
    ("**Syuri vs Rin Kadokura from WAVE ** https://youtu.be/arzbiulGYcU"),
    ("**Tsukasa Fujimoto vs Haruka Umesaki - Wave** https://youtu.be/iBUH1D4tzHw"),
    ("**Takumi Iroha & Yuki Miyazaki vs Mio Momono & Yumi Ohka from September 6th 2020.** https://youtu.be/TOfwcZoeNnU"),
    ("**Takumi Iroha vs Yumi Ohka for the Regina di WAVE title from November 23rd 2019. Really good match.** https://youtu.be/Ox8PTsc1XeI"),
    ("**HIRO'e & Miyuki Takase vs Yuki Miyazaki & Nagisa Nozaki for the WAVE tag titles from June 28th 2018.** https://youtu.be/8ijKXOTSKJI"),
]
marv: List[str] = [
    ("**Syuri & Takumi vs Nyla Rose and ASUKA - Marvelous 2019.12.08** https://youtu.be/KF2eKFT6NjE"),
    ("**Mio vs Takumi- Marvelous 2019.11.03** https://youtu.be/ovQxvCKJeao"),
    ("**Takumi Iroha & Syuri vs Nagisa Nozaki & Chihiro Hashimoto - Marvelous** "),
    #("**** "),
]
sead: List[str] = [
    ("**Arisa Nakajima (c) vs. Rina Yamashita, SEAdLINNNG New Leaf! (10.03.2020)** https://youtu.be/qjGE9NEMAIc"),
    ("**Arisa Nakajima & Tsukasa Fujimoto vs Sareee & Nanae Takahashi. - Sead May 5th 2017** https://www.dailymotion.com/video/k1ybFIWXlxMGqGndRlP"),
    ("**Arisa Nakajima & Nanae Takahashi vs. Hiroyo Matsumoto & Ryo Mizunami** https://www.dailymotion.com/video/x5ggl8s"),
    #("**** "),
    #("**** "),
]
oz: List[str] = [
    ("**Hiroyo Matsumoto vs. Hikari Shida - OZ Academy Plum Hanasaku 2017.08.20** https://m.bilibili.com/video/BV1f441177F8"),
    ("**Mayumi Ozaki and Maya Yuhiki vs Rina Yamashita and Yoshiko - OZ Academy Flower Bloom In Yokohama 2018** https://m.bilibili.com/video/BV1Nt411Z7HB"),
    ("**Mayumi Ozaki vs  Saori Anou - Oz Acadmey** https://youtu.be/zNUTR9PEbsM"),
    ("**Hikaru Shida & Syuri vs. Hiroyo Matsumoto & Kagetsu 2017.01.25** https://www.dailymotion.com/video/x7qx2iw"),
    #("**** "),
    #("**** "),
    #("**** "),
]
retro: List[str] = [
    ("**Esther Moreno y Manami Toyota vs Aja Kong y Bison Kimura. 29-Abril-1991** https://youtu.be/z_pLjPK3ygI"),
    ("**Kana VS Meiko Satomura - 2-13-2011 (Triple Tails Osaka event)** https://www.youtube.com/watch?v=Qx1B35rVcnw"),
    ("**Debbie Malenko & Sakie Hasegawa vs Takako Inoue & Mariko Yoshida from Wrestlemarinepiad 1992** https://www.dailymotion.com/video/xwa9w0"),
    ("**Dynamite Kansai vs Manami Toyota WWWA Title match from December 4th 1995.** https://youtu.be/XypDvsj6t1Y"),
    ("**Aja Kong & Sakie Hasegawa vs Manami Toyota & Toshiyo Yamada. WWWA Tag Title 2/3 falls match from February 27th 1994.** https://youtu.be/Pov70LNERJM"),
    ("**Bull Nakano & Aja Kong vs Akira Hokuto & Shinobu Kandori. Hokuto & Kandori are bitter rivals and are forced to team together to face Nakano & Kong. An absolute classic, highly recommend.(BU113TPR00FJAYCE#2404)** https://youtu.be/cTMaGmB45xA"),
    ("**Manami Toyota vs. Aja Kong - March 26, 1995** https://youtu.be/OrE-o-L3RZ4"),
    ("**Combat Toyoda vs. Megumi Kudo (No-Rope Electrified Barbwire Deathmatch)** https://www.youtube.com/watch?v=BSdMiVV_fnQ"),
    ("**Dynamite Kansai, AKINO & GAMI vs Amazing Kong, Mayumi Ozaki & Ayako Hamada - Gaia** https://youtu.be/t4b57zLQpPU"),
    ("**Kana vs. Meiko Satomura (4/19/2010)** https://www.youtube.com/watch?v=Hhv86X56XGM&ab_channel=vrnamnchnm"),    
    #("**** "),
]
gatoh: List[str] = [
    ("**Antonio Honda vs An Chamu - Gatoh Move** https://www.youtube.com/watch?v=6x0xPriwE98"),
    ("**Mei Suruga vs An Chamu - Gatoh Move** https://www.youtube.com/watch?v=uTxzHBVUO8s"),
    ("**Chris Brookes & Yuna Mizumori vs Emi Sakura & Lulu Pencil - Gatoh Move** https://youtu.be/6dVBJmHRJPE?t=1503"),
    ("**Mei Suruga vs Ryo Mizunami - Gatoh Move** https://youtu.be/jbiWEMPet94?t=1133"),
    ("**Kirihara Tokiko VS Cherry - Gatoh Move** https://youtu.be/WPyW2_C1RWE?t=960"),
    ("**Emi Sakura vs Yuna Mizumori - Gatoh Move** https://youtu.be/ihR2AqPJ73Q?t=1129"),
    ("**Chie Koshikawa & Mei Suruga vs Kirihara Tokiko & Antonio Honda - Gatoh Move** https://youtu.be/QtZeqoeWC7w?t=1440"),
    ("**Hiroyo Matsumoto & Chon Shiryu vs Antonio Honda & Jaki Numazawa - Gatoh Move** https://www.youtube.com/watch?v=88MlL2SeKZ0"),
    ("**Mitsuru Konno & Mei Suruga vs Sayaka Obihiro & Yuna Mizumori - Gatoh Move** https://www.youtube.com/watch?v=NptxvmTou1I"),
    ("**Antonio Honda vs Obihiro Sayaka - Gatoh Move** https://youtu.be/u8DqNHclepQ?t=2640"),
    ("**Emi Sakura & Mei Suruga vs Mitsuru Konno & Tokiko Kirihara - Gatoh Move** "),
]
termlist = [
    (stardom),
    (agz),
    (marv),
    (wwe),
    (sendai),
    (indy),
    (ice),
    (tjp),
    (wave),
    (sead),
    (oz),
    (retro),
    (gatoh),
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
            `promo` - the promotion you, random if none selected
            current promotions:
            agz -AGZ
            gm -Gatoh move
            ice -Ice Ribbon
            indy -Misc
            marv -Marvelous
            oz -Oz Academy
            retro
            sead -Seadlinnng
            sendai -Sendai Girls
            stardom -Stardom
            tjp -Tokyo Joshi Pro Wrestling
            wave -Wave Pro Wrestling
            wwe -<:asukaDerp:643500197183356958>
        """

        msg = " "
        if promo:

            if promo == "stardom":
                await ctx.send(f"{ctx.author.mention}{choice(bot_msg)}{choice(stardom)}")            
            elif promo == "agz":
                await ctx.send(f"{ctx.author.mention}{choice(bot_msg)}{choice(agz)}")
            elif promo == "gm":
                await ctx.send(f"{ctx.author.mention}{choice(bot_msg)}{choice(gatoh)}")    
            elif promo == "sendai":
                await ctx.send(f"{ctx.author.mention}{choice(bot_msg)}{choice(sendai)}")    
            elif promo == "wave":
                await ctx.send(f"{ctx.author.mention}{choice(bot_msg)}{choice(wave)}")    
            elif promo == "ice":
                await ctx.send(f"{ctx.author.mention}{choice(bot_msg)}{choice(ice)}")
            elif promo == "indy":
                await ctx.send(f"{ctx.author.mention}{choice(bot_msg)}{choice(indy)}")    
            elif promo == "marv":
                await ctx.send(f"{ctx.author.mention}{choice(bot_msg)}{choice(marv)}")    
            elif promo == "sead":
                await ctx.send(f"{ctx.author.mention}{choice(bot_msg)}{choice(sead)}")
            elif promo == "tjp":
                await ctx.send(f"{ctx.author.mention}{choice(bot_msg)}{choice(tjp)}")
            elif promo == "oz":
                await ctx.send(f"{ctx.author.mention}{choice(bot_msg)}{choice(oz)}")
            elif promo == "wwe":
                await ctx.send(f"{ctx.author.mention}{choice(bot_msg)}{choice(wwe)}")                
            
            else:
                list = choice(termlist)
                await ctx.send(ctx.author.mention + msg + choice(list))
        else:
            list = choice(termlist)
            await ctx.send(ctx.message.author.mention + msg + choice(list))