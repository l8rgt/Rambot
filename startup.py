import discord
from discord.ext import commands
import json
import asyncio
intent = discord.Intents.all()

from index import clientAuth                                               # in this directory create an index.py file with the variable "clientAuth"

pref=json.load(open('prefix.json','r'))
bot = commands.Bot(command_prefix=pref,help_command=None,intents=intent)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for stream"))
async def main():
    async with bot:
        await bot.load_extension("cogs.NLC")
        await bot.start(clientAuth)
        
asyncio.run(main())