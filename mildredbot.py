# Filename: mildredbot.py
# import into another file by using "from mildredbot import Bot"

# ==== Externally Built Main Imports ====
import discord

# ==== Locally Built Object Imports ====
from games import games
from cogs.messages import Messages

#========================================
#=               Bot Class             =
#========================================


class Bot():

    #===================================================
    #=                    Variables                    =
    #===================================================
    __botClient = None
    __userList = None
    __eventList = None
    __newsFeed = None


    #==========================================================
    #=                    Public Functions                    =
    #==========================================================

    def __init__(self):
        self.__botClient = discord.Client(status=discord.Status.online)
        __chatMessage = Messages()

    def updateNewsFeed(self, object):
        pass

    def parseCommand(self, command):
        pass

    def createUsername(self, object):
        pass

    def displayCommands(self):
        pass
