import discord
from redbot.core import commands
import requests
from bs4 import BeautifulSoup

class StardomCog(commands.Cog):
    """Cog for scraping Stardom schedule and posting match details."""

    def __init__(self, bot):
        self.bot = bot

    def scrape_stardom_schedule(self):
        """Scrape the Stardom schedule page and extract match details along with the show name and time."""
        schedule_url = "https://wwr-stardom.com/schedule/"

        # Get the page content
        response = requests.get(schedule_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the first show link within the <ul> with id 'upcoming-events-c6674bbda7f981637828f635a37cbeaa'
        upcoming_events = soup.find('ul', {'id': 'upcoming-events-c6674bbda7f981637828f635a37cbeaa'})

        if not upcoming_events:
            return None, None, []

        first_show_element = upcoming_events.find('a', href=True)
        
        if not first_show_element:
            return None, None, []

        first_show_link = first_show_element['href']
        show_name = first_show_element.find('span', {'class': 'mc_list_in_tit'}).text.strip()
        show_time = first_show_element.find('span', {'class': 'mc_list_in_time'}).text.strip()

        # Now, get the content of the first show
        show_response = requests.get(first_show_link)
        show_soup = BeautifulSoup(show_response.text, 'html.parser')

        # Example: Extract the first match (You can loop over all matches)
        match_info = []
        matches = show_soup.find_all('p')  # Assuming each match is inside a <p> tag

        for match in matches:
            if '◆' in match.text:  # Simple filter to get match details
                match_info.append(match.text.strip())

        return show_name, show_time, match_info

    @commands.command()
    async def stardom(self, ctx, event_index: int = 0):
        """Post the next Stardom show match card, optionally specify which upcoming event to show."""
        show_name, show_time, match_info = self.scrape_stardom_schedule(event_index)

        if match_info:
            if event_index == 0:
                title = "Next Stardom Show"
            else:
                title = f"Next {event_index} Stardom Show"

            embed = discord.Embed(
                title=title,
                description=f"Time: {show_time}\nMatch Card:"
            )
            
            for i, match in enumerate(match_info, start=1):
                embed.add_field(name=f"Match {i}", value=match, inline=False)
            
            await ctx.send(embed=embed)
        else:
            await ctx.send("No matches found or unable to scrape the page.")


# Setup function to add this cog to the bot
def setup(bot):
    bot.add_cog(StardomCog(bot))
