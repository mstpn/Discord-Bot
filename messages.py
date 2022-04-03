# messages.py

# ==== Externally Built Main Imports ====
import discord

# ==== Externally Built Object Imports ====
from random import randrange

# ==== Locally Built Object Imports ====
from games import games
from commandsList import commandsList

# Messages Class
# Purpose: To determine what message the user has sent and call the appropriate
#          Bot Object method to handle the given input from a user.
#
# Variables: 
#               - __botClient (private): Is the primary bot client connection to 
#                                        the discord API
#
#               - __userMessage (private): The message recieved from a user within
#                                          the chat system on discord

class Messages():

    #===================================================
    #=                    Variables                    =
    #===================================================

    __botClient = None
    __userMessage = None


    #==========================================================
    #=                    Public Functions                    =
    #==========================================================

    # -----------------------------
    # ---- Default Constructor ----
    # -----------------------------
    def __init__(self):
        pass

    # --------------------------------
    # ---- Overloaded Constructor ----
    # --------------------------------
    def __init__(self, message, client):
        self.botClient = client
        self.userMessage = message

    # -----------------------------------------
    # ---- Primary Message Command Handler ----
    # -----------------------------------------
    async def messagesHandler(self, userMessage, botClient):
       
        # ==== Ensure it doesn't respond to itself ====
        if self.userMessage.author == botClient.user:
            return
        # ==== End Self Message Check ==== 


        # ==== Hello Response ====
        elif self.userMessage.content.lower().startswith(commandsList[0]):
            await self.userMessage.channel.send(f"Hello {self.userMessage.author.name}!")
            # return
        # ==== End Hello Response ====


        # ==== Status Response(s) ====
        elif self.userMessage.content.lower().startswith(commandsList[1]):
            await self.userMessage.channel.send(f"Alright {self.userMessage.author.name}, I'm back!")
            await botClient.change_presence(status=discord.Status.online)
            # return

        elif self.userMessage.content.lower().startswith(commandsList[2]):
            await self.userMessage.channel.send(f"Ok {self.userMessage.author.name}, I'm AFK!")
            await botClient.change_presence(status=discord.Status.idle)
            # return

        elif self.userMessage.content.lower().startswith(commandsList[3]):
            await self.userMessage.channel.send(f"Shhhh {self.userMessage.author.name}, I need quiet!")
            await botClient.change_presence(status=discord.Status.dnd)
            # return

        elif self.userMessage.content.lower().startswith(commandsList[4]):
            await self.userMessage.channel.send(f"Can't see me {self.userMessage.author.name}!")
            await botClient.change_presence(status=discord.Status.invisible)
            # return
        # ==== End Status Response(s) ====


        # ==== Game Response ====
        elif self.userMessage.content.lower().startswith(commandsList[5]):
            game = discord.Game(games[randrange(len(games))])
            await botClient.change_presence(activity=game)
            await self.userMessage.channel.send(f"Alright {self.userMessage.author.name}, I'll play {game}")
            # return
        # ==== End Game Response ====
                    
                                           
        # **** Temporary Message Author & Message Content print out to Terminal ****
        print(f'Message Author:  {self.userMessage.author.name}')
        print(f'Message Content: {self.userMessage.content}')
        # **************************************************************************
