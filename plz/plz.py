import shutil  # To remove empty directories

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
