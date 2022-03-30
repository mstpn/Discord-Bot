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
            # return str(reaction.emoji) == '👍'

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

    if message.content.lower().startswith('!joke'):
        await message.channel.send('Knock knock!')

        def check1(msg):
            matches = ["whose", "who", "who\'s"]
            return message.author == msg.author and any(word in msg.content.lower() for word in matches)      

        def check2(msg):
            matches = ["who", "who?"]
            return message.author == msg.author and any(word in msg.content.lower() for word in matches)  

        response1 = await client.wait_for('message', check=check1)
        await message.channel.send('Etch')

        response2 = await client.wait_for('message', check=check2)
        await message.channel.send('Bless you')

        # Getting the content the messages that the user sent in
        response1_content = response1.content
        response2_content = response2.content
        # print(response1_content)
        # print(response2_content) 
        await message.channel.send('\nYour joke replies were:\n' + response1_content + '\n' + response2_content)

client.run(TOKEN)
