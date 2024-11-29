from rapidfuzz import process, fuzz  # For fuzzy matching
import discord
from redbot.core import commands
import os
import random
import aiohttp

base_path = "/home/dashy9000/data/joshifiles/"

# Define mappings for substitutions and choices
choices_map = {
    # "misa": ["misam", "misak"],
    # "momo": ["momok", "momow"],
    # "maika": ["maiker", "maikao"],
    # "saya": ["sayak", "sayai"],
    # "arisa": ["arisah", "arisan"],
    # "saki": ["sakik", "sakia", "SAKI"],
    # "mio": ["miom"],
    # "bby": ["maiker", "aoi", "unagi", "azm", "mayu", "rika", "momow"],
    # "dos": ["aj", "becky", "rhea", "mandy"],
    # "bblz": ["alexa", "rhea"],
    # "brzy": ["syuri", "sayai", "hyper"],
    # "mo": ["momoka", "himeka", "kaho", "miyuki"],
    # "ksup": ["hzk", "arisah", "momow", "kagetsu"],
    # "kray": ["kira", "konami", "misak", "tomoka", "shida", "jungle"],
}

substitutions = {
    # "asuka": "kana",
    # "coco": "momok",
    # "ez": "momok",
    # "iyo": "io",
    # "misao": "hyper",
    # "mii": "hibiscus",
    # "champ": "maiker",
    # "slk": "starlight",
    # "hikaru": "shida",
    # "miyagi": "andras",
    # "michiko": "andras",
    # "hazuki": "hzk",
    # "sarray": "sareee",
    # "bee": "suzume",
    # "kyona": "jungle",
    # "tora": "natsuko",
    # "poi": "natsupoi",
    # "natsumi": "natsupoi",
    # "sausage": "sasha",
    # "suasage": "sasha",
    # "ssj": "sasha",
    # "bobby": "bby",
    # "mooshty": "utami",
    # "moosh": "utami",
    # "parasite": "tam",
    # "roxie": "tam",
    # "walker": "sayak",
    # "dashy": "momow",
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

    def find_closest_match(self, search_terms: str):
        """Find the best matching folder using fuzzy search."""
        folder_names = os.listdir(base_path)

        # Split input into multiple terms (e.g., "maika ozaki" -> ["maika", "ozaki"])
        search_terms_list = search_terms.lower().split()

        # Score each folder by checking how well it matches all search terms
        results = []
        for folder in folder_names:
            folder_lower = folder.lower()
            # Calculate cumulative score for all search terms
            score = sum(fuzz.partial_ratio(term, folder_lower) for term in search_terms_list) / len(search_terms_list)
            results.append((folder, score))

        # Sort results by score (descending) and return the best match
        results.sort(key=lambda x: x[1], reverse=True)
        if results and results[0][1] > 60:  # Threshold for a match
            return results[0][0]  # Return the folder name
        return None

    def get_random_file(self, directory: str):
        """
        Recursively find a random file in the given directory.
        If a directory is empty, remove it.
        """
        try:
            items = os.listdir(directory)
            if not items:
                shutil.rmtree(directory)  # Remove empty directory
                return None

            # Filter files and directories
            files = [f for f in items if os.path.isfile(os.path.join(directory, f))]
            dirs = [d for d in items if os.path.isdir(os.path.join(directory, d))]

            if files:
                return os.path.join(directory, random.choice(files))
            elif dirs:
                # Recursively search in subdirectories
                subdir = random.choice(dirs)
                return self.get_random_file(os.path.join(directory, subdir))

        except Exception as e:
            print(f"Error accessing directory '{directory}': {e}")
            return None

    @commands.command()
    async def plz(self, ctx, *, ask: str = "mayu"):
        """Respond with a random file from a matching directory."""
        user = ctx.message.author

        # Restrict specific users if needed
        if user.id in [1518231553405091861, 7347683482016154001]:
            return

        # Resolve the input to a valid directory name
        ask = self.resolve_ask(ask)

        # Attempt to find a matching folder
        folder = self.find_closest_match(ask)
        if not folder:
            folder = "youtoo"  # Default folder if no match is found

        path = os.path.join(base_path, folder)

        # Get a random file, even from subdirectories
        random_file = self.get_random_file(path)
        if random_file:
            try:
                await ctx.send(file=discord.File(random_file))
            except Exception as e:
                await ctx.send("code better dash")
                print(f"Error: {e}")
        else:
            await ctx.send("No files found, or the directory is empty!")


    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())

    __del__ = cog_unload