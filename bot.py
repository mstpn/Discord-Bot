# bot.py
import os
import asyncio

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


# ==================================================
#           Set Up Discord Bot as Client
# ==================================================
client = discord.Client()

# Bot Connection
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    
# ==================================================
#               Respond to messages
# ==================================================
@client.event
async def on_message(message):

    # Ensure it doesn't respond to itself
    if message.author == client.user:
        return

    
    # ==================================================
    #               Thumbs up response
    # ==================================================
    if message.content.startswith('!thumb'):
        channel = message.channel
        await channel.send('Send me that 👍 reaction, mate')

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '👍'

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await channel.send('👎')
        else:
            await channel.send('👍')

            
    # ==================================================
    #                 Hello response
    # ==================================================
    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

        
    # ==================================================
    #                 Joke response
    # ==================================================
    # # Knock Knock
    # @client.event
    # async def on_message(message):
    #     if message.author == client.user:
    #         return

    #     if message.content.startswith('$joke'):
    #         await message.channel.send('Knock knock!')   

    #     def who(message, user):
    #         return user == message.author and message.content.startswith('who')      

    #     # try:
    #     #     message, user = await client.wait_for('')   

client.run(TOKEN)
