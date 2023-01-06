#!C:\Users\Matt\AppData\Local\Programs\Python\Python310\python.exe
import discord
from discord.ext import commands
import json
intent = discord.Intents.all()
import sys
import requests

from index import clientAuth                                              
from index import TwitchID
from index import TwitchSecret
from index import ChannelName
from index import DiscordChannelID
from index import DiscordServerID

# Get OAuth token from Twitch
response = requests.post('https://id.twitch.tv/oauth2/token', data={
    'client_id': TwitchID,
    'client_secret': TwitchSecret,
    'grant_type': 'client_credentials'
})

response_json = response.json()
access_token = response_json['access_token']
headers = {
    'Authorization': f'Bearer {access_token}',
    'Client-ID': TwitchID
}

#Get some channel data including channel ID
getuser = requests.get('https://api.twitch.tv/helix/users', params={
    'login': ChannelName
}, headers=headers)

getUser_json = getuser.json()
user = getUser_json['data'][0]
profilePic=user['profile_image_url']    
displayName=user['display_name']
channelID = user['id']

#Get the stream title and game
getTitle = requests.get('https://api.twitch.tv/helix/channels', params={
    'broadcaster_id': channelID
}, headers=headers)

getTitle_json = getTitle.json()
streamData = getTitle_json['data'][0]
streamTitle=streamData['title']
streamGame = streamData['game_name']


pref=json.load(open('prefix.json','r'))
bot = commands.Bot(command_prefix=pref,help_command=None,intents=intent)

@bot.event
async def on_ready():
    guild=bot.get_guild(DiscordServerID)
    channel = guild.get_channel(DiscordChannelID)
    embedVar = discord.Embed(title=streamTitle, url="https://twitch.tv/"+ChannelName, color = 0x6441A4)
    embedVar.set_author(name=displayName, icon_url=profilePic)
    embedVar.set_image(url="https://static-cdn.jtvnw.net/previews-ttv/live_user_"+ChannelName+"-320x180.jpg?r=834905")
    embedVar.add_field(name="Game:", value=streamGame)
    embedVar.set_thumbnail(url=profilePic)
    await channel.send("Hey @everyone our official twitch "+displayName+" is now live at <https://twitch.tv/"+ChannelName+">! Come support us! Go Rams!",embed=embedVar)  #For a blank message above the embed, replace the first string with ""
    sys.exit(0)

bot.run(clientAuth)