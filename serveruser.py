#=============================================
#=              ServerUser Class             =
#=============================================

from discord import User
import event

class ServerUser(object): # param(object) means object is made ancestor of all classes

    #===================================================
    #=                    Variables                    =
    #===================================================

    __discordID = None
    __firstName = None
    __faculty = None
    __programYear = None
    __username = None
    __myEvents = event.Event()


    #==========================================================
    #=                    Public Functions                    =
    #==========================================================

    def __init__(self): # Default Constructor for ServerUser
        pass

    def discordID(): # Acquire ServerUser Discord ID
        pass
    
    def firstName(): # Acquire ServerUser
        pass

    def faculty(): # Acquire ServerUser
        pass

    def programYear(): # Acquire ServerUser
        pass

    def userName(): # Acquire ServerUser
        pass

    def myEvents(): # Acquire ServerUser
        pass

    def createEvent(): # Create ServerUser Event
        pass

    def deleteEvent(): # Delete ServerUser Event
        pass
    


