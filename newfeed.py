# Filename: newfeed.py
# import into another file by using "from newfeed import NewsFeed"

from datetime import datetime
import pandas as pd
from source import Source
from dateutil.parser import *

#=============================================
#=              News Feed Class              =
#=============================================

class NewsFeed():

    #===================================================
    #=                    Variables                    =
    #===================================================

    __sourcesList = None
    __lastUpdated = None

    
    #==========================================================
    #=                    Public Functions                    =
    #==========================================================

    # Constructor
    def __init__(self):
        self.initSources()

    def initSources(self):
        self.__sourcesList = []
        sourcesDF = pd.read_csv('sources.csv')
        for index, row in sourcesDF.iterrows():
            csvSource = Source(
                row["Name"],
                row["Type"],
                row["URL"]
            )
            self.__sourcesList.append(csvSource)  

    # Updates the source list 
    def updateSources(self):
        # self.__sourcesList = []
        # sourcesDF = pd.read_csv('sources.csv')
        # for index, row in sourcesDF.iterrows():
        #     csvSource = Source(
        #         row["Name"],
        #         row["Type"],
        #         row["URL"]
        #     )
        #     self.__sourcesList.append(csvSource)
        
        # date = []
        for source in self.__sourcesList:
            # date.append(source.updateStories())
            source.updateStories()

            # testing
            # source.printStories()

        # self.__lastUpdated = max(date)

    # Returns an array of strings that the bot can iterate through to post
    def postNews(self):
        self.updateSources()
        stories = []
        date = []
        for source in self.__sourcesList:
            for story in source.getStoryList():
                if self.__lastUpdated == None or parse(story.getDate()) > self.__lastUpdated:
                    storyString = '\n'.join(story.getAll())
                    stories.append(storyString)
                    date.append(parse(story.getDate()))
        if len(date) != 0:
            self.__lastUpdated = max(date)
        return stories
                

        
        


""" --------------------LOCAL TESTING------------------------- """

feed = NewsFeed()