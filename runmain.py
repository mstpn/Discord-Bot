# Filename: runmain.py

# ==== Externally Built Main Imports ====
import os
import discord

# ==== Externally Built Object Imports ====
from discord.ext import commands # For Slash Commands and Other Commands
from discord_slash import SlashCommand, SlashContext # For Slash Commands
from discord_slash.utils.manage_commands import create_choice, create_option # For Slash Commands options
from discord import Member
from random import randrange
from dotenv import load_dotenv
load_dotenv()

# ==== Locally Built Object Imports ====
from games import games


# ==== Set Up Discord Bot as Client ====
bot = commands.Bot(command_prefix='!', help_command=None) # For possible future command prefix use
bot.case_insensitive=True
slash = SlashCommand(bot, sync_commands=True) # Enables slash commands provided bot has permissions


# ==== Bot Connection On ====
@bot.event
async def on_ready():
    print(f'{bot.user.name} has dropped into your Discord server!')
    await bot.change_presence(activity=discord.Game(games[randrange(len(games))]),afk=False)

bot.load_extension('cogs.messages')
bot.run(os.getenv('DISCORD_TOKEN'))



# ***********************************************************************************
# *****    THIS WON'T WORK UNLESS A NEW BOT WITH A COMMAND SCOPE IS CREATED     *****
# *****   TESTED AND IT WORKS ON A NEW BOT WITH THE PROPER SCOPE PERMISSIONS    *****
# ***********************************************************************************
# ==================================================
#          Slash Commands In Chat Tester
# ==================================================
# @slash.slash(
#     name="Hello",
#     description="Hello Slash Test",
#     guild_ids=[930174863954554880]
# )
# async def hello(ctx:SlashContext):
#     await ctx.send("World!")