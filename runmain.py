# runmain.py
import os
import discord


from random import randrange
from dotenv import load_dotenv
load_dotenv()


from games import games
from messages import messagesHandler


# ==================================================
#           Set Up Discord Bot as Client
# ==================================================

# Mildred Bot will load up into the server as Idle
client = discord.Client(status=discord.Status.online)


# Bot Connection
@client.event 
async def on_ready():
    print(f'{client.user.name} has dropped into your Discord server!')
    await client.change_presence(activity=discord.Game(games[randrange(len(games))]),afk=True)

# ==================================================
#               Respond to messages
# ==================================================
@client.event
async def on_message(message):
   await messagesHandler(message=message, client=client)
    
client.run(os.getenv('DISCORD_TOKEN'))