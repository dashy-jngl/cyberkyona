import discord
from redbot.core import commands

from typing import List
from collections import defaultdict

from datetime import date

class Birthday(commands.Cog):
    """Show joshi birthdays"""

    def __init__(self, bot):
        self.bot = bot

    def format_help_for_context(self, ctx: commands.Context) -> str:
        pre_processed = super().format_help_for_context(ctx)
        return f"{pre_processed}\n\nCog Version: {self.__version__}"



    @commands.command()
    async def birthday(self, ctx: commands.Context, ask: str = "none"):
        """ displays birthdays for a given date or supplies birthdates for a given joshi"""
        birthdays = {
#       jan
        "03.01":  ["Hyper Misao", "Akane Fujita"],
        "04.01": ["Takumi Iroha", "Ayako Sato"],
        "05.01": ["Misaki Ohata"],
        "06.01": ["Jacqueline"],
        "07.01": ["Honori Hana", "Devil Masami", "Melanie Cruise/Mel"],
        "08.01": ["Bull Nakano"],
        "09.01": ["Ruby Riott", "Maya Yukihi"],
        "12.01": ["Raquel Gonzalez"],
        "14.01": ["Kacy Catanzaro"],
        "15.01": ["Kelly Kelly"],
        "16.01": ["Candy Okutsu"],
        "18.01": ["Uno Matsuya", "Tequila Saya"],
        "20.01": ["Rina Amikura"],
        "24.01": ["Saki Akai"],
        "26.01": ["Sasha Banks", "Waka Tsukiyama", "Taylor Wilde"],
        "27.01": ["Zoey Stark"],
        "30.01": ["Becky Lynch", "Natsuko Tora"],
#       feb
        "01.02": ["Saori Anou"],
        "02.02": ["Isla Dawn", "Yuki Miyazaki"],
        "07.02": ["Haruka Umesaki"],
        "08.02": ["Syuri"],
        "09.02": ["Madusa/Alundra Blayze", "AKARI"],
        "12.02": ["SAKI"],
        "13.02": ["Sumika Yanagawa"],
        "14.02": ["Mio Shirai"],
        "15.02": ["LuFisto"],
        "18.02": ["Hikari Noa"],
        "19.02": ["Mayu Iwatani"],
        "20.02": ["Yuki Kamifuku"],
        "21.02": ["Giulia"],
        "25.02": ["Maria Kanellis"],
        "26.02": ["Kaori Yoneyama", "Yappy"],
        "27.02": ["Rin Kadokura"],
        "28.02": ["Yoshiko Hasegawa/Yoppy"],
#       mar
        "01.03": ["Maria", "Tenille Dashwood"],
        "02.03": ["Manami Toyota"],
        "05.03": ["Jordynne Grace"],
        "12.03": ["Rina Yamashita"],
        "14.03": ["Shotzi Blackheart"],
        "16.03": ["Mizuki"],
        "17.03": ["Miyu Yamashita"],
        "18.03": ["Moka Miyamoto", "Mari"],
        "19.03": ["Kyoko Kimura", "AJ Lee"],
        "20.03": ["Nao Kakuta", "Ami Miura"],
        "21.03": ["Killer Kelly"],
        "22.03": ["Tam Nakano", "Momo Watanabe", "Bea Pristley"],
        "24.03": ["Maika", "Ryo Mizunami", "Lacey Evans", "Lana"],
        "31.03": ["Sareee/Sarray"],
#       apr
        "01.04": ["Kurumi Hiiragi"],
        "03.04": ["Tasha Steelz"],
        "04.04": ["Jungle Kyona", "Chelsea Green", "Yumi Ohka"],
        "05.04": ["Charlotte Flair"],
        "06.04": ["Arisa Nakajima", "Momo Kohgo"],
        "09.04": ["Bianca Belair"],
        "12.04": ["Sakura Hirota", "Shizuku Tsukada"],
        "14.04": ["Ram Kaichow", "Marina Shafir", "Lita"],
        "16.04": ["Mia Yim"],
        "17.04": ["Mikoto Shindo"],
        "18.04": ["Yuuki Mashiro"],
        "20.04": ["Tae Honma"],
        "21.04": ["Nikki Cross", "Heidi Katrina"],
        "22.04": ["Hikaru Shimizu", "Kyoko Inoue"],
        "23.04": ["Jamie Hayter", "Britt Baker", "Mei Hoshizuki"],
        "24.04": ["Ibuki Hoshi"],
        "27.04": ["Arisu Endo"],
        "30.04": ["Thekla"],
#       may
        "02.05": ["Zoe Lucas"],
        "05.05": ["Saki Kashima"],
        "06.05": ["Dakota Kai", "Piper Niven/Viper"],
        "07.05": ["Natsuki Taiyo"],
        "08.05": ["Io Shirai"],
        "10.05": ["Mitsuru Konno"],
        "11.05": ["Totoro Satsuki"],
        "12.05": ["Kaho Kobayashi"],
        "13.05": ["Scarlett Bordeaux"],
        "16.05": ["Yuzuki Aikawa/Yuzupon"],
        "17.05": ["Marika Kobashi", "Misa Matsui"],
        "19.05": ["Saya Iida", "Reika Saiki"],
        "20.05": ["Nao Yamaguchi", "Kayden Carter"],
        "21.05": ["Leva Bates"],
        "25.05": ["Nao Ishikawa"],
        "27.05": ["Natalya"],
        "28.05": ["Himeka", "Kyuri"],
        "29.05": ["Nia Jax"],
        "30.05": ["Mei Suruga", "Mio Momono"],
        "31.05": ["Maika Ozaki"],
#   jun
        "03.06": ["Jade Cargill"],
        "04.06": ["Riho", "Red Velvet"],
        "05.06": ["Priscilla Kelly/Gigi Dolan"],
        "07.06": ["Nodaka Tenma", "Noa Igarashi"],
        "08.06": ["Liv Morgan"],
        "10.06": ["Mika Iwaka", "Deonna Purrazzo"],
        "11.06": ["Hikaru Shida", "Sonoko Kato"],
        "15.06": ["Bayley"],
        "16.06": ["Andras Miyagi/Michiko Miyagi"],
        "23.06": ["Brandi Rhodes", "Jessie Mckay/Billie Kay"],
        "24.06": ["Kagetsu"],
        "27.06": ["Kimber Lee"],
        "29.06": ["Serena Deeb"],
        "30.06": ["Su Yung"],
#       jul
        "01.07": ["Chihiro Hashimoto"],
        "02.07": ["Leon"],
        "07.07": ["Mochi Miyagi"],
        "08.07": ["Shanna"],
        "09.07": ["Mizuka Arai", "Tay Conti"],
        "11.07": ["Big Swole"],
        "13.07": ["Mahiro Kiryu", "Akira Hokuto"],
        "15.07": ["Konami", "Anna Jay"],
        "18.07": ["Mandy Rose"],
        "19.07": ["Natsumi Maki/Natsupoi", "Shoko Nakajima", "Yuu"],
        "22.07": ["Maki Itoh", "Thunder Rosa"],
        "24.07": ["Tomoka Inaba", "Torrie Wilson"],
        "25.07": ["Jaguar Yokata"],
        "26.07": ["Yoshiko", "Tessa Blanchard"],
        "28.07": ["Xia Li", "Riko Kawahata", "Lioness Asuka"],
        "29.07": ["Chie Koishikawa"],
        "30.07": ["Lulu Pencil", "Tsukasa Fujimoto"],
#       aug
        "02.08": ["Yuna Mizumori"],
        "03.08": ["Nanami", "Nyla Rose", "Sayuri"],
        "06.08": ["Natsu Sumire"],
        "07.08": ["Kris Statlander"],
        "08.08": ["Shayna Baszler"],
        "09.08": ["Alexa Bliss"],
        "11.08": ["Sena Shiori", "Hanan", "Kay Lee Ray"],
        "12.08": ["Kris Wolf"],
        "13.08": ["Momo Tani"],
        "15.08": ["Ruaka"],
        "17.08": ["Indi Hartwell", "Paige", "Ayano Irie"],
        "18.08": ["Starlight Kid"],
        "21.08": ["Miku Aono"],
        "24.08": ["DASH Chisako"],
        "27.08": ["Jazz"],
        "28.08": ["Yuko Sakurai"],
        "31.08": ["Ember Moon", "Mickie James"],
#       sep
        "02.09": ["Unagi Sayaka", "Sayaka Obihiro"],
        "03.09": ["Hana Kimura", "Allie"],
        "04.09": ["Amazing Kong/Awesome Kong"],
        "07.09": ["Molly Holly"],
        "08.09": ["Miyuki Takase"],
        "10.09": ["Sarah Logan"],
        "14.09": ["Utami Hayashishita", "Penelope Ford", "Mai Sakurai"],
        "16.09": ["Madeline", "Suzu Suzuki", "YuuRI", "Kiera Hogan"],
        "19.09": ["Eva Marie"],
        "23.09": ["Kairi Sane/Kairi Hojo"],
        "24.09": ["Misa Kagura"],
        "25.09": ["Aja Kong"],
        "26.09": ["Asuka/Kana"],
        "27.09": ["Rika Tatsumi", "Kakeru Sekiguchi"],
        "28.09": ["Jinny"],
        "29.09": ["Hazuki", "Candice LeRae"],
        "30.09": ["Candice Michelle"],
#       oct
        "01.10": ["AZM"],
        "02.10": ["Mii"],
        "04.10": ["Emi Sakura"],
        "11.10": ["Rhea Ripley"],
        "13.10": ["Arisa Hoshiki"],
        "14.10": ["Stacy Keibler"],
        "16.10": ["Xia Brookside"],
        "17.10": ["Nina Samuels"],
        "19.10": ["Sayuri Namba", "Miu Watanabe", "Toni Storm", "Hamuko Hoshi", "Asashi"],
        "21.10": ["Banny Oikawa"],
        "22.10": ["Taya Valkyrie/Franky Monet", "Cutie Suzuki"],
        "23.10": ["Aoife Valkyrie", "Carmella", "Yurika Oka"],
        "24.10": ["AKINO"],
        "25.10": ["Yuki Aino"],
        "25.10": ["Rydeen Hagane"],
        "27.10": ["ASUKA/Veny", "Leyla Hirsch"],
        "28.10": ["Mayumi Ozaki"],
#       nov
        "01.11": ["Plum Mariko"],
        "03.11": ["Dawn Marie"],
        "04.11": ["Tokiko Kirihara"],
        "06.11": ["Hiroyo Matsumoto"],
        "08.11": ["Sayaka", "Candy Floss"],
        "10.11": ["Peyton Royce/Cassie Lee"],
        "11.11": ["Yuna Manase", "Session Moth Martina", "Chie Ozora", "Dump Matsumoto"],
        "12.11": ["Ayumi Hayashi"],
        "13.11": ["Act Yasukawa"],
        "15.11": ["Tegan Nox"],
        "17.11": ["Meiko Satomura", "Mercedes Martinez", "Lady C"],
        "19.11": ["Risa Sera"],
        "21.11": ["Nikki Bella", "Brie Bella", "Rin Rin"],
        "22.11": ["Nagisa Nozaki"],
        "23.11": ["Aliyah", "Rina Shingaki"],
        "24.11": ["Beth Phoenix"],
        "26.11": ["Rhythm", "Ivory"],
        "27.11": ["Suzume"],
        "28.11": ["Saya Kamitani"],
        "29.11": ["Rosemary"],
        "30.11": ["Naomi"],
        "01.12": ["Hanako Nakamori"],
        "03.12": ["Mirai Maiumi"],
        "04.12": ["Itsuki Aoki", "Dynamite Kansai"],
        "05.12": ["Raku"],
        "07.12": ["Tsubasa Kuragaki"],
        "08.12": ["Chigusa Nagayo"],
        "17.12": ["Riko Kaiju"],
        "18.12": ["Trish Stratus"],
        "23.12": ["Nanae Takahashi"],
        "25.12": ["KAZUKI"],
        "26.12": ["Mina Shirakawa"],
        "27.12": ["Zelina Vega/Thea Trinidad", "Yuka Sakazaki", "Chyna"],
        "28.12": ["Hina", "Rina", "Haruna Neko", "Rachael Ellering"],
#       a
        "akane": ["Akane Fujita: 03.01.93"],
        "ayako": ["Ayako Sato: 04.01.86"],
        "": [""],
#       b
        "becky": ["Becky Lynch: 30.01.87"],
        "": [""],
        "bull": ["Bull Nakano: 08.01.68"],
        "": [""],
#       c
        "candy": ["Candy Okutsu: 16.01.75", "Candy Floss: 08.11.99"],
        "": [""],
#       d
        "devil": ["Devil Masami: 07.01.62"],
        "": [""],
#       e
        "": [""],
        "": [""],
#       f
        "": [""],
        "": [""],
#       g
        "": [""],
        "": [""],
#       h
        "haruka": ["Haruka Umesaki: 07.02.01"],
        "": [""],
        "heidi": ["Ruby Riott/Heidi Lovelace: 09.01.91"],
        "hinori": ["Honori Hana: 07.01.00"],
        "hyper": ["Hyper Misao: 03.01.90"],
        "": [""],
        "": [""],
        "": [""],
#       i
        "isla": ["Isla Dawn: 02.02.94"],
        "": [""],
#       j
        "jacqueline": ["Jacqueline: 06.01.64"],
        "": [""],
#       k
        "kacy": ["Kacy Catanzaro: 14.01.90"],
        "kelly": ["Kelly Kelly: 15.01.87"],
#       l
        "": [""],
        "": [""],
#       m
        "": [""],
        "maya": ["Maya Yukihi: 09.01.??"],
        "mel": ["Melanie Cruise/Mel: 07.01.87"],
        "melanie": ["Melanie Cruise/Mel: 07.01.87"],
        "misaki": ["Misaki Ohata: 05.01.89"],
        "misao": ["Hyper Misao: 03.01.90"],
#       n
        "natsuko": ["Natsuko Tora: 30.01.91"],
        "": [""],
#       o
        "": [""],
        "": [""],
#       p
        "": [""],
        "": [""],
#       q
        "": [""],
        "": [""],
#       r
        "raquel": ["Raquel Gonzalez: 12.01.91"],
        "rina": ["Rina Amikura: 20.01.95", "", ""],
        "ruby": ["Ruby Riott/Heidi Lovelace: 09.01.91"],
#       s
        "saki": ["Saki Akai: 24.01.87", "", ""],
        "saori": ["Saori Anou: 01.02.91"],
        "": [""],
        "sasha": ["Sasha Banks: 26.01"],
#       t
        "takumi": ["Takumi Iroha: 04.01.93"],
        "taylor": ["Taylor Wilde: 26.01.86"],
        "": [""],
        "tequila": ["Tequila Saya: 18.01.84"],
#       u
        "uno": ["Uno Matsuya: 18.01.84"],
        "": [""],
#       v
        "": [""],
        "": [""],
#       w
        "waka": ["Waka Tsukiyama: 26.01.92"],
        "": [""],
#       x
        "": [""],
        "": [""],
#       y
        "": [""],
        "yuki": ["Yuki Miyazaki: 02.02.79"],
#       z
        "zoey": ["Zoey Stark: 27.01.94"],
        "": [""],
        }

        if ask == "none":
            today = date.today()
            day = today.strftime("%d")
            month = today.strftime("%m")
            ask = day +"."+ month
            await ctx.send(ask + " JST")

        try:
            bd = birthdays[ask]
            for i in range(len(bd)):
                await ctx.send(bd[i])
        except:
            await ctx.send("<a:konamishrug:845007847926136912>"+"<:giuliaKiss:845008239027290175>")


