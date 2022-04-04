# Filename: cogs.messages.py
# import into another file by using "from cogs.messages import Messages"

# ==== Externally Built Main Imports ====
import discord

# ==== Externally Built Object Imports ====
from discord.ext import commands
from random import randrange

# ==== Locally Built Object Imports ====
from games import games
from commandsList import commandsList

# Messages Class
# Purpose: To determine what message the user has sent and call the appropriate
#          Bot Object method to handle the given input from a user.

class Messages(commands.Cog):
 
    # --------------------------------
    # ---- Overloaded Constructor ----
    # --------------------------------
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        return

    # --------------------------------------------
    # ---- Primary Message Command Handler(s) ----
    # --------------------------------------------

    @commands.command(name="nickname")
    async def nickname(self, ctx: commands.Context, member, nick):
        await ctx.send(f"Nickname Command: ctx = {ctx}, member = {member}, nick = {nick} '")
        return

    @commands.command(name="hello")
    async def hello(self, ctx: commands.Context):
        await ctx.channel.send(f"Hello {ctx.author.name}!")
        return

    @commands.command(name="online")
    async def online(self, ctx: commands.Context):
            await ctx.channel.send(f"Alright {ctx.author.name}, I'm back!")
            await self.bot.change_presence(status=discord.Status.online)
            return

    @commands.command(name="idle")
    async def idle(self, ctx: commands.Context):
            await ctx.channel.send(f"Ok {ctx.author.name}, I'm AFK!")
            await self.bot.change_presence(status=discord.Status.idle)
            return

    @commands.command(name="dnd")
    async def dnd(self, ctx: commands.Context):
            await ctx.channel.send(f"Shhhh {ctx.author.name}, I need quiet!")
            await self.bot.change_presence(status=discord.Status.dnd)
            return

    @commands.command(name="invis")
    async def invis(self, ctx: commands.Context):
            await ctx.channel.send(f"Can't see me {ctx.author.name}!")
            await self.bot.change_presence(status=discord.Status.invisible)
            return

    @commands.command(name="game")
    async def game(self, ctx: commands.Context):
            game = discord.Game(games[randrange(len(games))])
            await self.bot.change_presence(activity=game)
            await ctx.channel.send(f"Alright {ctx.author.name}, I'll play {game}")
            return
                    
                                           
        # # **** Temporary Message Author & Message Content print out to Terminal ****
        # print(f'Message Author:  {self.__userMessage.author.name}')
        # print(f'Message Content: {self.__userMessage.content}')
        # # **************************************************************************

def setup(bot):
    bot.add_cog(Messages(bot))
