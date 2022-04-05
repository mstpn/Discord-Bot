# Filename: mildredbot.py
# import into another file by using "from mildredbot import Bot"

# ==== Externally Built Main Imports ====
from cgitb import text
import discord
import os

from dotenv import load_dotenv
from discord.ext import commands

# ==== Locally Built Object Imports ====
from games import games
from cogs.messages import Messages
from newfeed import NewsFeed

#========================================
#                Bot Class              =
#========================================


class Bot():

    #===================================================
    #                     Variables                    =
    #===================================================
    __botClient = None
    __userList = None
    __eventList = None
    __newsFeed = None
    __textChannels = {}
    __newsChannel = None

    #for testing
    __testChannel = None


    #==========================================================
    #                     Public Functions                    =
    #==========================================================

    def __init__(self):
        self.__botClient = discord.Client(status=discord.Status.online)
        # __chatMessage = Messages()
        self.__newsFeed = NewsFeed()

    def init(self):
        self.__updateTextChannels()
        self.__newsChannel = self.__textChannels.get('newsfeed')

        #for testing
        self.__testChannel = self.__textChannels.get('testing')

    def updateNewsFeed(self):
        stories = self.__newsFeed.postNews()
        for story in stories:
            # print(story)
            # await bot.getNewsChannel().send(story)
            client.loop.create_task(bot.getNewsChannel().send(story))


    def parseCommand(self, command):
        pass

    def createUsername(self, object):
        pass

    def displayCommands(self):
        pass

    def getClient(self):
        return self.__botClient

    def sendMsg(self, channel, msg):
        client = self.__botClient
        try:
            # https://stackoverflow.com/questions/64199358/discord-py-send-message-from-non-async-function
            client.loop.create_task(channel.send(msg))
        except:
            print("write error")
            return False
        else:
            print("message sent")
            return True

    def getTextChannels(self):
        return self.__textChannels

    def getNewsChannel(self):
        return self.__newsChannel

    #==========================================================
    #                     Private Functions                    =
    #==========================================================

    def __updateTextChannels(self):
        client = self.__botClient
        text_channel_list = {}
        for server in client.guilds:
            for channel in server.channels:
                if str(channel.type) == 'text':
                    # text_channel_list[channel.name] = channel.id
                    text_channel_list[channel.name] = channel
        self.__textChannels = text_channel_list


    #DELETE DELETE DELETE DELETE DELETE DELETE DELETE DELETE DELETE
    #DELETE               TESTING Functions                  DELETE
    #DELETE DELETE DELETE DELETE DELETE DELETE DELETE DELETE DELETE

    def getTestChannel(self):
        return self.__testChannel

#================================= End Class Bot() ============================


#==========================================================
#                    Main                                 =
#==========================================================

load_dotenv()

# client = commands.Bot(command_prefix='!', help_command=None) 
# client.case_insensitive=True

# @client.event
# async def on_ready():
#     print(f'{client.user.name} has dropped into your Discord server!')
#     await client.change_presence(activity=discord.Game(games[randrange(len(games))]),afk=False)

# client.load_extension('cogs.messages')
# client.run(os.getenv('DISCORD_TOKEN'))

bot = Bot()
client = bot.getClient()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    
    bot.init() # Initialize attributes that depend on Discord connection

    bot.updateNewsFeed()
    # msg = "test message from mildredbot.py"
    # await bot.getTestChannel().send(msg)
    # bot.sendMsg(bot.getTestChannel(),msg)

client.run(os.getenv('DISCORD_TOKEN'))