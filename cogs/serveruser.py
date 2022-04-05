# Filename: serveruser.py
# import into another file by using "from serveruser import User"


#=============================================
#=              ServerUser Class             =
#=============================================
import discord
from discord import ClientUser
from discord.ext import commands



class User(commands.Cog):

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

    # def __init__(self, discordID, firstName, faculty, programYear, username):
    #     self.__discordID = discordID
    #     self.__firstName = firstName
    #     self.__faculty = faculty
    #     self.__programYear = programYear
    #     self.__username = username

    def getDiscordID(self): # Get User Discord ID
        return 


    def firstName(self, name:str): # Get User Name

        return 

    def getFirstName(self): # Set User Name
        return self.__firstName


    def setFaculty(self): # Get User Faculty
        pass 

    def getFaculty(self): # Get User Faculty
        return self.__faculty


    def programYear(self): # Get User Program Year
        return self.__programYear

    def getProgramYear(self): # Get User Program Year
        return 

    def getUsername(self): # Get User Discord Name
        return self.__username


    # ==== Primary Methods From Deliverables ====

    def getMyEvents(self): # Get ServerUser Events
        return self.__myEvents

    def setMyEvents(self, event): # Set ServerUser Events
        if self.__myEvents(len()) < 2:
            if self.__myEvents[0] == None:
                self.__myEvents[0] == event
            else:
                self.__myEvents[1] == event
            return
        else:
            # No spot available code here
            return
        


    def createEvent(self): # Create ServerUser Event
        pass

    def deleteEvent(self): # Delete ServerUser Event
        pass
    
    # @commands.command(name="delete_event")
    # async def delete_event(self, ctx: discord.Message, channel):
    #     mbed:discord.Embed = discord.Embed(
    #         title = 'Success!',
    #         description = f'Channel: {channel} has been deleted'
    #     )
    #     delete_channel = 
    #     await ctx.channel.send(embed=mbed)
    #     await self.delete_event(ctx=ctx, channel=channel)


def setup(bot):
    bot.add_cog(User(bot))