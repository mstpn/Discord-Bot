# Filename: source.py
# import into another file by using "from source import Source"

import feedparser
from datetime import datetime
from dateutil.parser import *
from story import Story


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
    
    """
    Constructor
    """
    def __init__(self, name, type, url):
        self.__sourceName = name
        self.__sourceType = type
        self.__sourceURL = url

    """ 
    Generates a list of stories from the source
        If no stories exist (lastUpdated == None), then only the 
        top story is added to the list
        If stories have been updated before, then all stories since
        the last access date are added to the list
    """
    def updateStories(self):
        feed = feedparser.parse(self.__sourceURL)
        author = feed.feed.title
        if self.__lastUpdated == None:
            self.__storyList = []
            story = Story(feed.entries[0].title,author,feed.entries[0].published,feed.entries[0].link)
            self.__storyList.append(story)
        else:
            index = 0
            if parse(feed.entries[index].published) > self.__lastUpdated:
                self.__storyList = []
                for entry in feed.entries:
                    if parse(entry.published) > self.__lastUpdated:
                        story = Story(entry.title,author,entry.published,entry.link)
                        self.__storyList.append(story)  
                    else:
                        break
        if len(self.__storyList) != 0:    
            self.__lastUpdated = parse(self.__storyList[0].getDate())
        
        return self.__lastUpdated
            # self.__lastUpdated = parse(str(datetime.now()))

    def getStoryList(self):
        return self.__storyList

    # # testing DELETE LATER
    # def printself(self):
    #     print(self.__sourceName, self.__sourceType, self.__sourceURL, self.__lastUpdated)
    #     for story in self.__storyList:
    #         print(story)
    
    def printStories(self):
        for story in self.__storyList:
            print(story.getTitle())
            print(story.getAuthor())
            print(story.getDate())
            print(story.getURL())


# local testing

# test = Source('MRU Twitter RSS', 'rss', "https://rss.app/feeds/xkh29vVdru9LoqlC.xml")

# test = Source('Calgary', 'rss', "https://newsroom.calgary.ca/tagfeed/en/tags/City__News,Transportation,City__Release")
# # NewsFeed = feedparser.parse(test.getURL())
# # entry = NewsFeed.entries[0]

# # print (entry.keys())

# # title = entry.get('title')
# # url = entry.get('link')

# # print(title)
# # print(url)

# test.updateStories()
# test.printself()
# test.printStories()