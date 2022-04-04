# Filename: source.py
# import into another file by using "from source import Source"

from dotenv import load_dotenv
# import tweepy
import os
import feedparser


#==========================================
#=              Source Class              =
#==========================================

class Source():

    #===================================================
    #=                    Variables                    =
    #===================================================

    __sourceName = None
    __sourceType = None
    __sourceURL = None
    __storyList = None
    __lastUpdated = None


    #==========================================================
    #=                    Public Functions                    =
    #==========================================================
    
    def __init__(self, name, type, url):
        self.__sourceName = name
        self.__sourceType = type
        self.__sourceURL = url
        self.__getStories()
        
        pass

    def __getStories(self):
        # gets all the stories @init
        pass

    def updateStories(self):
        pass

    def getURL(self):
        return self.__sourceURL

    # testing
    def printself(self):
        print(self.__sourceName, self.__sourceType, self.__sourceURL, self.__lastUpdated)
        for story in self.__storyList:
            print(story)


# local testing

test = Source('MRU Twitter RSS', 'rss', "https://rss.app/feeds/xkh29vVdru9LoqlC.xml")
NewsFeed = feedparser.parse(test.getURL())
entry = NewsFeed.entries[0]

print (entry.keys())

title = entry.get('title')
url = entry.get('link')

print(title)
print(url)

# Authenticate to Twitter
# load_dotenv()

# auth = tweepy.OAuthHandler(
#     os.getenv('TWITTER_KEY'), 
#     os.getenv('TWITTER_KEY_SECRET'))

# auth.set_access_token(
#     os.getenv('TWITTER_ACCESS'), 
#     os.getenv('TWITTER_ACCESS_SECRET'))

# auth = tweepy.OAuth1UserHandler(
#     os.getenv('TWITTER_KEY'), 
#     os.getenv('TWITTER_KEY_SECRET'),
#     os.getenv('TWITTER_ACCESS'),
#     os.getenv('TWITTER_ACCESS_SECRET'))
        
# api = tweepy.API(auth, wait_on_rate_limit=True)

# try:
#     api.verify_credentials()
#     print("Authentication OK")
# except:
#     print("Error during authentication")