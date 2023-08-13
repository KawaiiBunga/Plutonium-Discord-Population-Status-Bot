import disnake
from disnake.ext import tasks, commands
import aiohttp
import datetime
import json
import requests

# Import data from config file
with open('config.json') as f:
    data = json.load(f)
    token = data["token"]
    Status = data["StatusText"]
    IP = data["IP"]
    Port = data["Port"]

#API Url
url = "https://list.plutools.pw/server/" + str(IP) + "/" + str(Port) + "/json"


# Global cmd registration, set .sync_commands_debug to false once in production
command_sync_flags = commands.CommandSyncFlags.default()
command_sync_flags.sync_commands_debug = False

bot = commands.Bot(
    command_prefix = disnake.ext.commands.when_mentioned,
    command_sync_flags = command_sync_flags,
)

#Updating status from BM API
@tasks.loop(seconds=20)
async def presence():
    async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    #Get data from API response
                    resp_dict = json.loads(await resp.text())
                    online = resp_dict["online"] 
                    Map = resp_dict["map"]
                    Player_Count = resp_dict["realClients"] 
                    Max_Players = resp_dict["maxplayers"]
                    #If server is online, set status
                    if online == True:
                        statusText = disnake.Game(name = f'{Status} {Map} {Player_Count}/{Max_Players}')
                        await bot.change_presence(activity=statusText)
                    #If offline or API error, change status and send message in console
                    else:
                        statusText = disnake.Game(name = f'Server Offline')
                        await bot.change_presence(activity=statusText)
                        print(f"API Error! check if your server is online!")

# On ready event
@bot.event
async def on_ready():
    await bot.wait_until_ready()
    print(f'The bot is ready! Logged in as {bot.user}')
    presence.start()
    
bot.run(token)
