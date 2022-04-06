# Filename: runmain.py

# ==== Externally Built Main Imports ====
from distutils.command.clean import clean
import os
import discord

# ==== Externally Built Object Imports ====
import discord
from discord.ext import commands
from random import randrange
from dotenv import load_dotenv

# ==== Locally Built Object Imports ====
from games import games
from mildredbot import Bot

load_dotenv()
bot = Bot()
botCommands = commands.Bot(command_prefix='!')
botMessageCommands = bot.getMessageCommands()
botEventCommands = bot.getEventCommands()
client = bot.getClient()

@botCommands.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    bot.init() # Initialize attributes that depend on Discord connection
    await client.change_presence(activity=discord.Game(games[randrange(len(games))]),afk=False)

botCommands.load_extension('cogs.messages')
botCommands.load_extension('cogs.eventcommands')
botCommands.run(os.getenv('DISCORD_TOKEN'))