# Filename: mildredbot.py
# import into another file by using "from mildredbot import Bot"

# ==== Externally Built Main Imports ====
from cgitb import text
from datetime import date, datetime
from random import randrange
import discord
import os
import asyncio

from dotenv import load_dotenv
from discord.ext import commands

# ==== Locally Built Object Imports ====
from games import games
from cogs.messages import Messages
from cogs.eventcommands import EventCommands
from newsfeed import NewsFeed

#========================================
#                Bot Class              =
#========================================


class Bot():

    #===================================================
    #                     Variables                    =
    #===================================================

    __botClient = None
    __botCommands = None
    __botEvents = None
    __userList = None
    __eventList = None
    __newsFeed = None
    __textChannels = {}
    __newsChannel = None


    __commandsListener = None

    #==========================================================
    #                     Public Functions                    =
    #==========================================================

    def __init__(self):
        self.__botCommands = commands.Bot(command_prefix='!')
        self.__botClient = self.__botCommands
        self.__botCommands.case_insensitive=True
        self.__chatMessageCommands = Messages(self.__botCommands)
        self.__botEventCommands = EventCommands(self.__botCommands)
        self.__newsFeed = NewsFeed()
# ------------------------------------------------------------
    def init(self):
        self.__updateTextChannels()
        self.__newsChannel = self.__textChannels.get('newsfeed')
        self.updateNewsFeed()
# ------------------------------------------------------------
    def updateNewsFeed(self):
        stories = self.__newsFeed.postNews()
        for story in stories:
            # print(story) #console print
            self.sendMsg(self.__newsChannel, story)
# ------------------------------------------------------------
    def parseCommand(self, command):
        pass
# ------------------------------------------------------------
    def createUsername(self, object):
        pass
# ------------------------------------------------------------
    def displayCommands(self):
        pass
# ------------------------------------------------------------
    def getClient(self):
        return self.__botClient
# ------------------------------------------------------------
    def getCommands(self):
        return self.__botCommands
# ------------------------------------------------------------
    def getMessageCommands(self):
        return self.__chatMessageCommands
# ------------------------------------------------------------
    def getEventCommands(self):
        return self.__botEventCommands
# ------------------------------------------------------------
    def sendMsg(self, channel, msg):
        client = self.__botClient
        try:
            # https://stackoverflow.com/questions/64199358/discord-py-send-message-from-non-async-function
            client.loop.create_task(channel.send(msg))
        except:
            print("write error")
            return False
        else:
            return True
# ------------------------------------------------------------
    def getTextChannels(self):
        return self.__textChannels
# ------------------------------------------------------------
    def getNewsChannel(self):
        return self.__newsChannel
# ------------------------------------------------------------
    #==========================================================
    #                     Private Functions                   =
    #==========================================================

    def __updateTextChannels(self):
        client = self.__botClient
        text_channel_list = {}
        for server in client.guilds:
            for channel in server.channels:
                if str(channel.type) == 'text':
                    text_channel_list[channel.name] = channel
        self.__textChannels = text_channel_list
# ------------------------------------------------------------

#==============================================================================
#=                                 End Class Bot()                            =
#==============================================================================


#==========================================================
#                           Main                          =
#==========================================================

load_dotenv()
bot = Bot()
botCommands = bot.getCommands()

@botCommands.event
async def on_ready():
    print(f'{botCommands.user.name} commands has connected to Discord!')
    bot.init()
    await botCommands.change_presence(activity=discord.Game(games[randrange(len(games))]),afk=False)

    while(True):
        bot.updateNewsFeed()
        print("\nfeed updated\n")
        await asyncio.sleep(60) #this prevents blocking

botCommands.load_extension('cogs.messages')
botCommands.load_extension('cogs.eventcommands')
botCommands.run(os.getenv('DISCORD_TOKEN'))