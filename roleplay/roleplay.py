import discord
from redbot.core import commands
from random import choice
from typing import List
from typing import Optional


dance:List[str] = [
    ("https://tenor.com/view/utamihayashishita-utami-gif-19094685"),
    ("https://gfycat.com/selfreliantcapitalbird-nao-yamaguchi-natsu-sumire-hana-kimura-kagetsu"),
    ("https://gfycat.com/aggravatingfinishedarmyworm-stardom-world-saya-kamitani-momo-watanabe"),
    ("https://tenor.com/view/alfie-fisher-stardom-saya-kamitani-dance-gif-19427727"),
    ("https://tenor.com/view/session-moth-martina-goth-ott-over-the-top-wrestling-aaw-gif-14328463"),
    ("https://thumbs.gfycat.com/ClosedGloomyHectorsdolphin.webp"),
    ("https://cdn.discordapp.com/attachments/797764263640563732/799909574206554142/sayadance.gif"),
    ("https://media1.tenor.com/images/0c6fd21d5bc52340ad5d22453932ccb9/tenor.gif?itemid=16765682"),
    ("https://media.discordapp.net/attachments/763850139215069225/797947714369355816/himedance2.gif"),
    ("https://imgur.com/ORcqiyg"),
    ("https://media.discordapp.net/attachments/546875050628874251/791360873196945408/dab789ad623c6aa92693f415b519b3e7_2.gif"),
    ("https://media.discordapp.net/attachments/727434367118475367/744905678120026212/1454196076470.gif"),
    ("https://media.discordapp.net/attachments/559545867590303747/757017950350737428/Starlight_Kid_Dancing.gif"),
    ("https://cdn.discordapp.com/attachments/797764263640563732/798071770799931422/2020-12-22_15-01-06_unknown.gif"),
    ("https://cdn.discordapp.com/attachments/797764263640563732/798072395067686922/2020-12-23_00-09-44_ramudance.gif"),
    ("https://cdn.discordapp.com/attachments/797764263640563732/798075438358331412/2020-12-24_00-13-25_AcrobaticSourAntarcticfurseal-size_restricted_1.gif"),
    ("https://cdn.discordapp.com/attachments/797764263640563732/798076756883669021/2021-01-06_20-14-56_ezgif-6-d415603be2fc.gif"),
    ("https://cdn.discordapp.com/attachments/797764263640563732/798101971990478899/2020-10-15_07-32-04_qqDance.gif"),
]
flip: List[str] = [
    ("https://cdn.discordapp.com/attachments/798071153801166909/798071294360813608/2020-12-22_01-24-00_tumblr_8bd10ca21a9cc71945e0a62901742655_8860684d_540.gif"),
    ("https://cdn.discordapp.com/attachments/798071153801166909/798071654579306526/2020-12-22_04-29-10_tumblr_puq8q5M8kS1qi3b4no5_400.gif"),
]
fu: List[str] = [
    ("https://cdn.discordapp.com/attachments/798074269925507083/798074300073508904/2020-12-31_10-39-30_avd9b-9reok.gif"),
    ("https://cdn.discordapp.com/attachments/798074269925507083/798074339193782312/2020-12-31_18-58-43_ezgif.com-video-to-gif.gif"),
    ("https://cdn.discordapp.com/attachments/798074269925507083/798075318136209448/2020-12-23_04-16-47_aqfyx-obvsu.gif"),
    (""),
]
hi: List[str] = [
    ("https://tenor.com/view/riho-aew-all-elite-wrestling-aew-dynamite-gatoh-move-gif-17745924"),
    ("https://tenor.com/view/riho-all-elite-wrestling-gatoh-move-choco-pro-cute-gif-17744360"),
    ("https://tenor.com/view/stardom-giulia-gif-19057013"),
    ("https://tenor.com/view/stardom-alfie-fisher-hiroyo-matsumoto-gif-19681678"),
    ("https://media.discordapp.net/attachments/559545867590303747/791787393380384818/Hi_Mina.gif"),
    ("https://media.discordapp.net/attachments/559545867590303747/768305958794559528/Hi_Kyona.gif"),
    ("https://gfycat.com/raggedbaredog"),
    ("https://gfycat.com/joyfuldrearyhyena"),
    ("https://media.discordapp.net/attachments/559545867590303747/752051219291308092/1597275384650.gif"),
    ("https://media.discordapp.net/attachments/559545867590303747/758459373311492146/HI_AZM.gif"),
    ("https://cdn.discordapp.com/attachments/797764466745016322/798070661955977266/2020-12-21_20-38-34_Flirty_Miyu.gif"),
    ("https://cdn.discordapp.com/attachments/797764466745016322/798072294592610374/2020-12-22_23-21-06_ami2x-95rdl.gif"),
    ("https://cdn.discordapp.com/attachments/797764466745016322/798073006609399838/2020-12-27_12-39-49_Its_Yuka.gif"),
    ("https://cdn.discordapp.com/attachments/797764466745016322/798073672182005820/2020-12-28_04-12-27_MayuWave.gif"),
    ("https://cdn.discordapp.com/attachments/797764466745016322/798073729812660254/2020-12-28_20-49-59_EnragedFatalAcornweevil-size_restricted.gif"),
    ("https://cdn.discordapp.com/attachments/797764466745016322/798074151541407758/2020-12-30_11-57-55_Tsukasa_Fujimoto_Hitting_the_AYYYEEE.gif"),
    ("https://cdn.discordapp.com/attachments/797764466745016322/798076316305326080/2021-01-04_08-18-48_20210104_031758.gif"),
    ("https://cdn.discordapp.com/attachments/797764466745016322/798076406457696286/2021-01-03_07-54-16_tumblr_2f6ad2719ea8bbc384792704ecf9f6e3_b9dbecfa_400.gif"),
    ("https://cdn.discordapp.com/attachments/797764466745016322/798076896846807040/2021-01-07_12-17-43_20200922_122400.gif"),
    ("https://cdn.discordapp.com/attachments/797764466745016322/798077478923927572/2021-01-09_02-27-04_thechampsayshi.gif"),
    #(""),
    #(""),
]
hugs: List[str] = [
    ("https://cdn.discordapp.com/attachments/797764291540680714/798074381733593138/2021-01-01_01-11-47_a2zt5-lwci1.gif"),
    ("https://cdn.discordapp.com/attachments/797764291540680714/798075181791838268/2020-12-23_23-00-24_20201223_162904.gif"),
    ("https://cdn.discordapp.com/attachments/797764291540680714/798073701044060191/2020-12-28_20-44-23_tenor_-_2020-12-28T154409.093.gif"),
    ("https://media.discordapp.net/attachments/559545867590303747/790779937904263169/tenor_-_2020-12-21T212436.031.gif"),
    ("https://cdn.discordapp.com/attachments/727060162145157191/798076794527416370/20201105_034326.gif"),
    ("https://cdn.discordapp.com/attachments/797764291540680714/798640432418390086/2020-05-25_09-19-49_me-yaaGqaamhY-V37g6nBpWuM4sSoriginal_319289752.jpg"),
    #("https://tenor.com/view/alfie-fisher-stardom-osaka-cinderella-giulia-syuri-gif-19789405"),
    #(""),
    ("https://cdn.discordapp.com/attachments/797764291540680714/799824636086583326/2020-10-28_05-37-30_Io_hugs_asuka.jpg"),
    ("https://cdn.discordapp.com/attachments/797764291540680714/799824647645822996/2020-10-09_12-30-03_dash_hug.jpg"),
]
kick: List[str] = [
    ("https://gfycat.com/joyoustinyislandcanary"),
    ("https://cdn.discordapp.com/attachments/797764349543841813/798070623648874496/2020-12-21_19-53-05_ladyC.cleans.ruaka.gif"),
    ("https://cdn.discordapp.com/attachments/797764349543841813/798071676808986624/2020-12-22_06-18-39_mikakicka2.gif"),
    ("https://cdn.discordapp.com/attachments/797764349543841813/798072156314402836/2020-12-22_20-48-43_tumblr_3a7d5dbe405d17cbecc8a08520783870_8f7262c5_540.gif"),
    ("https://cdn.discordapp.com/attachments/797764349543841813/798073635482763305/2020-12-28_04-11-27_5-18-2019_10-49-09_AM.gif"),
    ("https://cdn.discordapp.com/attachments/797764349543841813/798075225317048320/2020-12-23_23-41-37_HirotaFurafuraDon.gif"),
    #(""),
]
kiss: List[str] = [
    ("https://imgur.com/r/WrestleWithThePlot/exQw1PI"),
]
lol: List[str] = [
    ("https://cdn.discordapp.com/attachments/798070972006924298/798071044099145778/2020-12-21_23-18-08_Maika_lol.gif"),
    ("https://cdn.discordapp.com/attachments/798070972006924298/798075381260484658/2020-12-24_00-11-38_miyu_laugh.gif"),
]
no: List[str] = [
    ("https://cdn.discordapp.com/attachments/798071059437191168/798071918971977799/2020-12-22_19-01-54_tumblr_prfn2pbrfc1rz10qqo9_r1_540.gif"),
]
slap:List[str] = [
    ("https://gfycat.com/shoddycapitalhorsefly-natsuko-tora-jungle-kyona-stardom"),
    ("https://gfycat.com/threadbareordinarygander-momo-watanabe-io-shirai-stardom"),
    ("https://gfycat.com/ampleveneratedeelelephant"),
    ("https://gfycat.com/digitalsociablehake-stephanie-mcmahon-mr-mcmahon-ted-dibiase"),
    ("https://gfycat.com/anotherdefianthorse-melina-slap"),
    #(""),
]
sleep: List[str] = [
    ("https://tenor.com/view/alexa-bliss-sleep-sleeps-sleeping-tired-gif-13510907"),
    ("https://tenor.com/view/sasha-banks-sleep-sleeps-sleeping-dead-gif-13691399"),
    ("https://tenor.com/view/bayley-sleep-sleeps-sleeping-tired-gif-19115530"),
    ("https://tenor.com/view/bayley-knocked-out-sleep-sleeps-sleeping-gif-14001950"),
    ("https://tenor.com/view/alexa-bliss-tired-sleepy-sleep-sleeps-gif-12017341"),
    ("https://cdn.discordapp.com/attachments/797764479886426122/798838456419745802/2020-04-06_05-59-33_Screenshot_546.png"),
    ("https://cdn.discordapp.com/attachments/797764479886426122/799824253368926259/2020-03-15_06-23-19_Tam_sleeps.jpg"),
    ("https://cdn.discordapp.com/attachments/797764479886426122/799824278845259796/2020-10-22_00-12-28_sleepy_maika.jpg"),
]
test: List[str] = [
    ("https://gfycat.com/raggedbaredog"),
]

#embed vars
footer = "❤️🤼‍♀️ Be happy with Pro-Wrestling 🤼‍♀️❤️"
 
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
    async def sendEmbed(self, ctx: commands.Context, imgurl, msg, user, user2: Optional[discord.Member],):

        # Build Embed
        embed = discord.Embed()
        embed.set_footer(text=footer)
        embed.set_image(url=imgurl)
        
        embed.description = f"**{user.mention} hugs {user2.mention}**"
        await ctx.send(embed=embed)

        #check member
        if not user2:
            embed.description = f"**{user.mention} {msg}**"
            await ctx.send(embed=embed)
        #set message author
        else:
            embed.description = f"**{user.mention} {msg} {user2.mention}**"
            await ctx.send(embed=embed)
            

    @commands.command(aliases=["takeitback"])
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

        #set image
        images = choice(test)

        #check member
        if not user:
            author = self.bot.user
            user = ctx.message.author
            msg = " Tests the System"
            await self.sendEmbed(ctx, images, msg, author)
        #set message author
        else:
            author = ctx.message.author
            msg = " Tests "
            await self.sendEmbed(ctx, images, msg, author, user)