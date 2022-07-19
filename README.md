# Discord-Bot
Discord Bot for Mildred Server

## Installation

Clone the repository to a local directory (or server if hosting).  

Fololow the guide at https://www.writebots.com/discord-bot-token/ to create a discord bot token and add your bot to your server.  

Start the bot by executing 

```python mildredboy.py```

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
