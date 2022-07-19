# Discord-Bot
A Discord Bot designed to simplify administration for large servers.

## Dependencies

If an error occurs check these installs:

You will need pip installed as well prior to installing these packages see https://realpython.com/what-is-pip/ for more information on pip.

``` 
pip install python-dotenv
pip install discord.py
pip install feedparser
pip install pandas
pip install python-dateutil 
pip install paramiko
```

The "None type / strip" error is a result of not having the .env file in your build path. This is less of an error, and more of just a missing file situation if you are not dealing with news postings.

## Installation

Clone the repository to a local directory (or server if hosting).  

Fololow the guide at https://www.writebots.com/discord-bot-token/ to create a discord bot token and add your bot to your server.  

Start the bot by executing 

```python mildredboy.py```

## Features
### Nicknames:
1. To change your nickname on the server, type “!change”
2. You will receive a direct message (DM), from the Bot with prompts asking for a Name (Character limit 12), followed by a Faculty (Character limit 12), and the Year you are in (Character limit 5). *** Press enter after typing in your answer for each question ***
3. The Bot will then prompt you asking if the name change is correct [yes / no].
4. If ‘yes’, then the Discord Bot will have created a new nickname. To see it, go to the Discord server and check out your new nickname.

### Events:
1. To create a voice channel, users type into the chat box “!event_voice <name>” (For ex. “!event_voice study”). This will create a voice channel in the user’s server immediately and can be accessed by clicking on the name.
2. To create a text channel, the server user types into the command box “!event_text <name>” (For ex. “!event_text message”) This will create a text channel in the user’s server immediately and can be accessed by clicking on the name.
3. To delete a channel, user types into the command box “!delete_event <name>” (For ex. !delete_event study), which will remove the channel from the server and the user's account.
4. To view created events, the user types into the command box “!display_events”, which shows each event name, creator, and start time in the channel the command was entered in.

### News Feeds:
1. Log into Discord and click on the server that has Mildred Bot.
2. Newsfeed content is handled by the administrators, by providing sources into the csv file currently required to run this system.
3. Click on the text channel called ‘newsfeed’ and read the news headline. If further interested, then click on the link provided to see the full news story.

