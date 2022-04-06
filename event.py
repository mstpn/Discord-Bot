# Filename: event.py
# import into another file by using "from event import Event"

#=========================================
#=              Event Class              =
#=========================================

import discord
import asyncio

class Event():

    #===================================================
    #=                    Variables                    =
    #===================================================
    
    __creator = None
    __duration = None
    __startTime = None
    __voice = None
    __text = None


    #==========================================================
    #=                    Public Functions                    =
    #==========================================================

    def __init__(self):
        pass

    def createVoiceChannel(__startTime, __duration):
        __startTime = __startTime
        __duration = __duration
        pass

    def createTextChannel(__startTime, __duration):
        __startTime = __startTime
        __duration = __duration
        pass
    