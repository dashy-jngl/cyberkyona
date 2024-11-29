from rapidfuzz import process  # For fuzzy matching
import discord
from redbot.core import commands
import os
import random
import aiohttp

base_path = "/home/dashy9000/data/joshifiles/"

# Define mappings for substitutions and choices
choices_map = {
    "misa": ["misam", "misak"],
    "momo": ["momok", "momow"],
    "maika": ["maiker", "maikao"],
    "saya": ["sayak", "sayai"],
    "arisa": ["arisah", "arisan"],
    "saki": ["sakik", "sakia", "SAKI"],
    "mio": ["miom"],
    "bby": ["maiker", "aoi", "unagi", "azm", "mayu", "rika", "momow"],
    "dos": ["aj", "becky", "rhea", "mandy"],
    "bblz": ["alexa", "rhea"],
    "brzy": ["syuri", "sayai", "hyper"],
    "mo": ["momoka", "himeka", "kaho", "miyuki"],
    "ksup": ["hzk", "arisah", "momow", "kagetsu"],
    "kray": ["kira", "konami", "misak", "tomoka", "shida", "jungle"],
}

substitutions = {
    "asuka": "kana",
    "coco": "momok",
    "ez": "momok",
    "iyo": "io",
    "misao": "hyper",
    "mii": "hibiscus",
    "champ": "maiker",
    "slk": "starlight",
    "hikaru": "shida",
    "miyagi": "andras",
    "michiko": "andras",
    "hazuki": "hzk",
    "sarray": "sareee",
    "bee": "suzume",
    "kyona": "jungle",
    "tora": "natsuko",
    "poi": "natsupoi",
    "natsumi": "natsupoi",
    "sausage": "sasha",
    "suasage": "sasha",
    "ssj": "sasha",
    "bobby": "bby",
    "mooshty": "utami",
    "moosh": "utami",
    "parasite": "tam",
    "roxie": "tam",
    "walker": "sayak",
    "dashy": "momow",
}

BaseCog = getattr(commands, "Cog", object)

class Plz(BaseCog):
    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop)

    def resolve_ask(self, ask: str):
        """Resolve the input 'ask' to a directory or choice."""
        ask = ask.lower()

        # Check substitutions
        if ask in substitutions:
            ask = substitutions[ask]

        # Check choices map
        if ask in choices_map:
            ask = random.choice(choices_map[ask])

        return ask

    def find_closest_match(self, search_term: str):
        """Find the closest matching folder using fuzzy search."""
        folder_names = os.listdir(base_path)
        result = process.extractOne(search_term, folder_names)
        if result:
            match, score, *_ = result  # Handle additional return values
            if score > 60:  # Threshold for a match
                return match
        return None

    @commands.command()
    async def plz(self, ctx, ask: str = "mayu"):
        """Respond with a random file from a matching directory."""
        user = ctx.message.author

        # Restrict specific users if needed
        if user.id in [151823155340509186, 734768348201615400]:
            return

        # Resolve the input to a valid directory name
        ask = self.resolve_ask(ask)

        # Attempt to find a matching folder
        folder = self.find_closest_match(ask)
        if not folder:
            folder = "youtoo"  # Default folder if no match is found

        path = os.path.join(base_path, folder)

        try:
            files = os.listdir(path)
            if not files:
                raise FileNotFoundError("No files in directory.")

            index = random.randint(0, len(files) - 1)
            await ctx.send(file=discord.File(os.path.join(path, files[index])))
        except Exception as e:
            await ctx.send("code better dash")
            print(f"Error: {e}")

    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())

    __del__ = cog_unload
