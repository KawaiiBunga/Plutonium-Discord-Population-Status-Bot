# Plutonium-Discord-Population-Status-Bot
Sets the map and player count of a Plutonium server as a bot's status for Discord.

Uses API from PluTools (https://plutools.pw/)
Works with IW5/T4/T4ZM/T5/T5ZM/T6/T6ZM/IW4x/IW6/S1 Plutonium or Alterware servers

## Requirements
- Python 3.11 or higher
- A Plutonium Call of Duty Server (https://plutonium.pw/)
  - Will also work with AlterWare servers (https://github.com/mxve/alterware-launcher)

## Setup

1. Edit the ```config.json``` file and set your bot token, server IP/Port, and what you want the status to say
  - Default status is ```on {Map} {Players}/{MaxPlayers}```, changing the status in the config will change what is before the map and playercount
2. Install the requirements by running ```pip install -r requirements.txt``` in the root of the project
3. Run the bot with ```py bot.py``` or ```python3 bot.py``` in the cmd or Terminal


