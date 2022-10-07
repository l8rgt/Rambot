#!C:\Users\Matt\AppData\Local\Programs\Python\Python310\python.exe
import discord
from discord.ext import commands
import json
intent = discord.Intents.all()
import sys

from index import clientAuth                                               # in this directory create an index.py file with the variable "clientAuth"

pref=json.load(open('prefix.json','r'))
bot = commands.Bot(command_prefix=pref,help_command=None,intents=intent)

@bot.event
async def on_ready():
    guild=bot.get_guild(413457661988962304)#insert server
    channel = guild.get_channel(678030513906253863)#insert id here
    await channel.send("Hey @everyone our official twitch FSC_Esports is now live at https://twitch.tv/FSC_esports ! Come support us! Go Rams!")
    #await channel.send("test")
    sys.exit(0)

bot.run(clientAuth)
