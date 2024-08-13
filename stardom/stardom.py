import discord
from redbot.core import commands
import requests
from bs4 import BeautifulSoup
from io import BytesIO

class StardomCog(commands.Cog):
    """Cog for scraping Stardom schedule and posting match details with images."""

    def __init__(self, bot):
        self.bot = bot

    def scrape_stardom_schedule(self, event_index=0):
        """Scrape the Stardom schedule page and extract match details, show name, time, and images."""
        schedule_url = "https://wwr-stardom.com/schedule/"

        # Get the page content
        response = requests.get(schedule_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all show links within the <ul> with id 'upcoming-events-c6674bbda7f981637828f635a37cbeaa'
        upcoming_events = soup.find('ul', {'id': 'upcoming-events-c6674bbda7f981637828f635a37cbeaa'})

        if not upcoming_events:
            return None, None, [], []

        show_elements = upcoming_events.find_all('a', href=True)

        if len(show_elements) <= event_index:
            return None, None, [], []

        selected_show_element = show_elements[event_index]
        
        selected_show_link = selected_show_element['href']
        show_name = selected_show_element.find('span', {'class': 'mc_list_in_tit'}).text.strip()
        show_time = selected_show_element.find('span', {'class': 'mc_list_in_time'}).text.strip()

        # Now, get the content of the selected show
        show_response = requests.get(selected_show_link)
        show_soup = BeautifulSoup(show_response.text, 'html.parser')

        # Example: Extract the matches (You can loop over all matches)
        match_info = []
        image_urls = []
        matches = show_soup.find_all('p')  # Assuming each match is inside a <p> tag

        for match in matches:
            if '◆' in match.text:  # Simple filter to get match details
                match_info.append(match.text.strip())

        # Extract images (assuming the images are in <img> tags with specific classes)
        images = show_soup.find_all('img')

        for img in images:
            image_url = img.get('src')
            if image_url:  # Simple check to ensure there's a valid URL
                image_urls.append(image_url)

        return show_name, show_time, match_info, image_urls

    @commands.command()
    async def stardom(self, ctx, event_index: int = 0):
        """Post the next Stardom show match card with images, optionally specify which upcoming event to show."""
        show_name, show_time, match_info, image_urls = self.scrape_stardom_schedule(event_index)

        if match_info:
            embed = discord.Embed(
                title=f"Stardom Show: {show_name}",
                description=f"Time: {show_time}\nMatch Card:"
            )
            
            for i, match in enumerate(match_info, start=1):
                embed.add_field(name=f"Match {i}", value=match, inline=False)
            
            await ctx.send(embed=embed)

            for image_url in image_urls:
                response = requests.get(image_url)
                image = BytesIO(response.content)
                await ctx.send(file=discord.File(image, filename="image.jpg"))
        else:
            await ctx.send("No matches found or unable to scrape the page.")

    @commands.command()
    async def stardom2(self, ctx):
        """Post the match card for the second upcoming Stardom show with images."""
        await self.stardom(ctx, event_index=1)

# Setup function to add this cog to the bot
def setup(bot):
    bot.add_cog(StardomCog(bot))
