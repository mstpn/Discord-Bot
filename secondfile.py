# import bot

#something
# SOME STUFF I WROTE

def sendMsg(client, channel, msg):
    try:
        # https://stackoverflow.com/questions/64199358/discord-py-send-message-from-non-async-function
        client.loop.create_task(channel.send(msg))
    except:
        print("write error")
        return False
    else:
        print("message sent")
        return True