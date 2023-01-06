create a new file in this directory called "index.py" with the contents below:
```
clientAuth = ''                                          #discord bot client ID
TwitchID = ''                                            #Twitch Client ID
TwitchSecret = ''                                        #Twitch Client Secret
ChannelName = ''                                         #Twitch Channel Name
DiscordChannelID =                                       #Discord Channel ID
DiscordServerID =                                        #Discord Server ID
```
Fill in the spaces as required. (inside the '' unless there are no '' present)
If needed, update prefix in "prefix.json"
To edit the output message, go to line 62 on "v2.py"

Note: the program calls "v2.py" instead of having the message in the cog in order to make it easier to call the command via a webhook if the user does not want to use the command


- Discord bot ID location: https://discord.com/developers/applications
- Twitch API IDs location: https://dev.twitch.tv/console/apps
- To get the discord channel and server IDs enable developer mode on your client