# bot.py
import os
import discord
from discord.ext import commands
import asyncio
import random
from dotenv import load_dotenv

load_dotenv()


# ==================================================
#           Set Up Discord Bot as Client
# ==================================================
client = discord.Client()


# Bot Connection
@client.event 
async def on_ready():
    await client.change_presence(status=discord.Status.idle)
    print(f'{client.user.name} has connected to Discord!')



    # testing channels (guilds)
    text_channel_list = {}
    for server in client.guilds:
        for channel in server.channels:
            if str(channel.type) == 'text':
                text_channel_list[channel.name] = channel.id

    print(text_channel_list)
    test_channel = client.get_channel(text_channel_list.get('test'))

    # Write to channel
    # try:
    #     await test_channel.send('This is not a drill')
    # except:
    #     print("write error")
    # else:
    #     print("message sent")

    # From other file function (non-async)
    # msg = "This is definitely not a drill"
    # secondfile.sendMsg(client, test_channel, msg)
    
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
    if message.content.lower().startswith('!thumb'):
        channel = message.channel
        await channel.send('Send me that 👍 reaction, mate')

        def check(reaction):
            return str(reaction.emoji == '👍')

        try:
            await client.wait_for('reaction_add', timeout=6.0, check=check)
        except asyncio.TimeoutError:
            await channel.send('👎')
        else:
            await channel.send('👍')

            
    # ==================================================
    #                 Hello response
    # ==================================================
    if message.content.lower().startswith('!hello'):
        await message.channel.send(f'Hello! {message.author.name}')

        
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

client.run(os.getenv('DISCORD_TOKEN'))
