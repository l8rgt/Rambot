import sys
import discord
from discord.ext import commands
import json
intent = discord.Intents.all()

sys.path.insert(1,"//desktop-serv/d/Program Files (x86)/Rambot")   #This code line is for me only, delete it if you aren't L8R
sys.path.insert(2,"D:\Program Files (x86)\Rambot")                 #This code line is for me only, delete it if you aren't L8R
from index import clientAuth                                               # in this directory create an index.py file with the variable "clientAuth"

pref=json.load(open('prefix.json','r'))
bot = commands.Bot(command_prefix=pref,help_command=None,intents=intent)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for stream"))

bot.load_extension("cogs.NLC")

bot.run(clientAuth)