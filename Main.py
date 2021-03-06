# Pre-requisites
# pip install -U python-dotenv
# pip install -U discord.py
# pip install -U Pillow
# pip install sqlalchemy

# Set Discord Bot Token as Environmental Variable "ETERNAL_BOT_DISCORD_TOKEN"


import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('ETERNAL_BOT_DISCORD_TOKEN')

bot = commands.Bot(command_prefix='?', description='Eternal Bot')

# Keep this for now, users might get re-enabled later.
# cogs = ['cogs.Users', 'cogs.Raids']

cogs = ['cogs.Raids', 'cogs.Greeter']

for cog in cogs:
    bot.load_extension(cog)


@bot.event
async def on_ready():
    print('Logged in as ' + bot.user.name)
    print('------')


bot.run(TOKEN, bot=True, reconnect=True)
