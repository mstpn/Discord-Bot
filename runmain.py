# runmain.py
import os
import discord
from random import randrange
from dotenv import load_dotenv
load_dotenv()

from games import games


# ==================================================
#           Set Up Discord Bot as Client
# ==================================================

# Mildred Bot will load up into the server as Idle
client = discord.Client(status=discord.Status.online)


# Bot Connection
@client.event 
async def on_ready():
    num = randrange(len(games))
    print(f'{client.user.name} has dropped into your Discord server!')
    await client.change_presence(activity=discord.Game(games[num]), afk=True)

# ==================================================
#               Respond to messages
# ==================================================
@client.event
async def on_message(message):

    # Ensure it doesn't respond to itself
    if message.author == client.user:
        return

    # ==================================================
    #                 Status response
    # ==================================================
    elif message.content.lower().startswith('!idle'):
        await message.channel.send(f"Ok {message.author.name}, I'm AFK!")
        await client.change_presence(status=discord.Status.idle)

    elif message.content.lower().startswith('!dnd'):
        await message.channel.send(f"Shhhh {message.author.name}, I need quiet!")
        await client.change_presence(status=discord.Status.dnd)

    elif message.content.lower().startswith('!invis'):
        await message.channel.send(f"Can't see me {message.author.name}!")
        await client.change_presence(status=discord.Status.invisible)

    elif message.content.lower().startswith('!online'):
        await message.channel.send(f"Alright {message.author.name}, I'm back!")
        await client.change_presence(status=discord.Status.online)

    # ==================================================
    #                 Hello response
    # ==================================================
    elif message.content.lower().startswith('!hello'):
        await message.channel.send(f"Hello {message.author.name}!")
    

    
client.run(os.getenv('DISCORD_TOKEN'))