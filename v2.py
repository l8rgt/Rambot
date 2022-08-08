#!C:\Users\Matt\AppData\Local\Programs\Python\Python310\python.exe
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
    guild=bot.get_guild(1006170458732900478)#insert server
    channel = guild.get_channel(1006170459735334957)#insert id here
    await channel.send("Hey @everyone our official twitch FSC_Esports is now live at https://twitch.tv/FSC_esports ! Come support us! Go Rams!")
    #await channel.send("live")
    sys.exit(0)

bot.run(clientAuth)
