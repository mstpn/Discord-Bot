# Filename: serveruser.py
# import into another file by using "from cogs.user import User"

from discord.ext import commands

class User():

    #===================================================
    #=                    Variables                    =
    #===================================================

    __discordID:str = None
    __firstName:str = None
    __faculty:str = None
    __programYear:int = None
    __username:str = None
    __myEvents = [None]*2
    
    #==========================================================
    #=                    Public Functions                    =
    #==========================================================

    def __init__(self, bot): # Default Constructor for User
        self.bot = bot
        pass
# ------------------------------------------------------------
    def getDiscordID(self): # Get User Discord ID
        return 
# ------------------------------------------------------------
    def firstName(self, name:str): # Get User Name
        return 
# ------------------------------------------------------------
    def getFirstName(self): # Set User Name
        return self.__firstName
# ------------------------------------------------------------
    def setFaculty(self): # Get User Faculty
        pass 
# ------------------------------------------------------------
    def getFaculty(self): # Get User Faculty
        return self.__faculty
# ------------------------------------------------------------
    def programYear(self): # Get User Program Year
        return self.__programYear
# ------------------------------------------------------------
    def getProgramYear(self): # Get User Program Year
        return 
# ------------------------------------------------------------
    def getUsername(self): # Get User Discord Name
        return self.__username
# ------------------------------------------------------------
    def getMyEvents(self): # Get User Events
        return self.__myEvents
# ------------------------------------------------------------
    def setMyEvents(self, event): # Set User Events
        if self.__myEvents(len()) < 2:
            if self.__myEvents[0] == None:
                self.__myEvents[0] == event
            else:
                self.__myEvents[1] == event
            return
        else:
            # "No Free Event Space Available" code here
            return
# ------------------------------------------------------------       
    def createEvent(self): # Create User Event
        pass
# ------------------------------------------------------------
    def deleteEvent(self): # Delete User Event
        pass
# ------------------------------------------------------------