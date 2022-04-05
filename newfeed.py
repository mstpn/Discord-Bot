# Filename: newfeed.py
# import into another file by using "from newfeed import NewsFeed"

from datetime import datetime
import pandas as pd
from source import Source

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
        self.updateSources()


    # Updates the source list 
    def updateSources(self):
        self.__sourcesList = []
        sourcesDF = pd.read_csv('sources.csv')
        for index, row in sourcesDF.iterrows():
            csvSource = Source(
                row["Name"],
                row["Type"],
                row["URL"]
            )
            self.__sourcesList.append(csvSource)
        
        for source in self.__sourcesList:
            source.updateStories()

            # testing
            # source.printStories()

        self.__lastUpdated = datetime.now()     

    # Returns an array of strings that the bot can iterate through to post
    def postNews(self):
        self.updateSources()
        stories = []
        for source in self.__sourcesList:
            for story in source.getStoryList():
                storyString = '\n'.join(story.getAll())
                stories.append(storyString)
        return stories
                

        
        


""" --------------------LOCAL TESTING------------------------- """

feed = NewsFeed()