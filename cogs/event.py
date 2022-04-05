# Filename: event.py
# import into another file by using "from event import Event"

#=========================================
#=              Event Class              =
#=========================================
import discord
import asyncio


from discord.ext import commands
from discord import TextChannel, VoiceChannel

class Event(commands.Cog):

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

    def __init__(self, bot):
        self.bot = bot

    def createVoiceChannel(self, __startTime, __duration):
        __startTime = __startTime
        __duration = __duration

    def createTextChannel(self, __startTime, __duration):
        __startTime = __startTime
        __duration = __duration

    @commands.command(name="event_voice")
    async def event_voice(self, ctx: commands.Context, channelName: str):
        guild = ctx.guild

        mbed:discord.Embed = discord.Embed(
            title = 'Success!',
            description = "{} voice channel has been successfully created.".format(channelName)
        )
        await guild.create_voice_channel(name='{}'.format(channelName))
        await ctx.send(embed=mbed)
        return


    @commands.command(name="event_text")
    async def event_text(self, ctx: commands.Context, channelName: str):
        guild = ctx.guild

        mbed:discord.Embed = discord.Embed(
            title = 'Success!',
            description = "{} text channel has been successfully created.".format(channelName)
        )
        await guild.create_text_channel(name='{}'.format(channelName))
        await ctx.send(embed=mbed)
        return


    # @commands.command(name="delete_event")
    # async def delete_event(self, ctx, channel: TextChannel=None):
    #     # mbed = discord.Embed(
    #     #     title = 'Success!',
    #     #     description = "Channel: {} has been deleted".format(channel),
    #     # # )
    #     # await ctx.send(embed=mbed)
    #     await channel.delete()
    #     return

    # @commands.command(name="delete_event")
    # async def delete_event(self, ctx, channel: VoiceChannel=None):
    #     # mbed = discord.Embed(
    #     #     title = 'Success!',
    #     #     description = "Channel: {} has been deleted".format(channel),
    #     # )
    #     # await ctx.send(embed=mbed)
    #     await channel.delete()
    #     return

    @commands.command(name="delete_event")
    async def delete_event(self, ctx, text_channel: TextChannel=None, voice_channel: VoiceChannel=None):
        if text_channel:
            await text_channel.delete()
        else:
            await voice_channel.delete()
        return


def setup(bot):
    bot.add_cog(Event(bot))

