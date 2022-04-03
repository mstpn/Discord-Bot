# runmain.py

# ==== Externally Built Main Imports ====
import os
import discord

# ==== Externally Built Object Imports ====
from random import randrange
from dotenv import load_dotenv
# Grabs the Bot token locally from machine
load_dotenv()

# ==== Locally Built Object Imports ====
from games import games
from messages import Messages


# ==================================================
#           Set Up Discord Bot as Client
# ==================================================

# Mildred Bot will load up into the server as Idle
botClient = discord.Client(status=discord.Status.online)


# Bot Connection
@botClient.event 
async def on_ready():
    print(f'{botClient.user.name} has dropped into your Discord server!')
    await botClient.change_presence(activity=discord.Game(games[randrange(len(games))]),afk=True)

# ==================================================
#               Respond to messages
# ==================================================
@botClient.event
async def on_message(userMessage):
    readMessage = Messages(message=userMessage, client=botClient)
    await readMessage.messagesHandler(userMessage, botClient)


botClient.run(os.getenv('DISCORD_TOKEN'))