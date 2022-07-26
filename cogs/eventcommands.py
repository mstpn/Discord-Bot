# Filename: event.py
# import into another file by using "from cogs.eventcommands import EventCommands"

import discord
from discord.ext import commands
from discord import TextChannel, VoiceChannel

#===================================================
#=              Events Commands Class              =
#===================================================

class EventCommands(commands.Cog):

    #===================================================
    #=                    Variables                    =
    #===================================================
    
    __creator = None
    __duration = None
    __startTime = None
    __voice = None
    __text = None
    __textChannels = None
    __voiceChannels = None

    #==========================================================
    #=                    Public Functions                    =
    #==========================================================

    def __init__(self, bot):
        self.bot = bot
# ------------------------------------------------------------
    @commands.Cog.listener()
    async def on_ready(self):
        print("Events Command Bot is Online")
# ------------------------------------------------------------
    def __updateTextChannels(self):
        text_channel_list = {}
        for server in self.bot.guilds:
            for channel in server.channels:
                if str(channel.type) == 'text':
                    text_channel_list[channel.name] = channel
        self.__textChannels = text_channel_list
# ------------------------------------------------------------
    def __updateVoiceChannels(self):
        voice_channel_list = {}
        for server in self.bot.guilds:
            for channel in server.channels:
                if str(channel.type) == 'voice':
                    voice_channel_list[channel.name] = channel
        self.__voiceChannels = voice_channel_list
# ------------------------------------------------------------
    @commands.command(name="event_voice")
    async def event_voice(self, ctx: commands.Context, channelName):
        # self.__updateVoiceChannels()
        guild = ctx.guild()
        mbed:discord.Embed = discord.Embed(
            title = 'Success!',
            description = "{} voice channel has been successfully created.".format(channelName)
        )
        await guild.create_voice_channel(name='{}'.format(channelName))
        await ctx.send(embed=mbed)
# ------------------------------------------------------------
    @commands.command(name="event_text")
    async def event_text(self, ctx: commands.Context, channelName):
        # self.__updateTextChannels()
        guild = ctx.guild
        mbed:discord.Embed = discord.Embed(
            title = 'Success!',
            description = "{} text channel has been successfully created.".format(channelName)
        )
        await guild.create_text_channel(name='{}'.format(channelName))
        await ctx.send(embed=mbed)
# ------------------------------------------------------------
    @commands.command(name="delete_event")
    async def delete_event(self, ctx: commands.Context, channel):
        self.__updateTextChannels()
        self.__updateVoiceChannels()
        textChannel = self.__textChannels.get(channel)
        voiceChannel = self.__voiceChannels.get(channel)

        if textChannel is not None:
            await textChannel.delete()
            mbed:discord.Embed = discord.Embed(
            title = 'Success!',
            description = "{} text channel has been successfully deleted.".format(channel)
        )
        if voiceChannel is not None:
            await voiceChannel.delete()
            mbed:discord.Embed = discord.Embed(
            title = 'Success!',
            description = "{} voice channel has been successfully deleted.".format(channel)
        )
# ------------------------------------------------------------

def setup(bot):
    bot.add_cog(EventCommands(bot))
