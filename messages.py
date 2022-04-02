import discord


from random import randrange


from games import games

async def messagesHandler(message, client):
    # Ensure it doesn't respond to itself
    if message.author == client.user:
        return

    # ==================================================
    #                 Status response
    # ==================================================
    elif message.content.lower().startswith('!idle'):
        await message.channel.send(f"Ok {message.author.name}, I'm AFK!")
        await client.change_presence(status=discord.Status.idle)

    elif message.content.lower().startswith('!dnd'):
        await message.channel.send(f"Shhhh {message.author.name}, I need quiet!")
        await client.change_presence(status=discord.Status.dnd)

    elif message.content.lower().startswith('!invis'):
        await message.channel.send(f"Can't see me {message.author.name}!")
        await client.change_presence(status=discord.Status.invisible)

    elif message.content.lower().startswith('!online'):
        await message.channel.send(f"Alright {message.author.name}, I'm back!")
        await client.change_presence(status=discord.Status.online)

    # ==================================================
    #                 Hello response
    # ==================================================
    elif message.content.lower().startswith('!hello'):
        await message.channel.send(f"Hello {message.author.name}!")
        
    # ==================================================
    #                 Game response
    # ==================================================
    elif message.content.lower().startswith('!game'):
        game = discord.Game(games[randrange(len(games))])
        await client.change_presence(activity=game)
        await message.channel.send(f"Alright {message.author.name}, I'll play {game}")