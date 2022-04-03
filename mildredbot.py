# mildredbot.py

# ==== Externally Built Main Imports ====
import discord


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

    def updateNewsFeed(self, object):
        pass

    def parseCommand(self):
        pass

    def createUsername(self, object):
        pass

    def displayCommands(self):
        pass
