# Filename: newfeed.py
# import into another file by using "from newfeed import NewsFeed"

from datetime import datetime
import pandas as pd
from source import Source

#=============================================
#=              News Feed Class              =
#=============================================

NAME_INDEX = 0
TYPE_INDEX = 1
LINK_INDEX = 2

class NewsFeed():

    #===================================================
    #=                    Variables                    =
    #===================================================

    __sourcesList = []
    __lastUpdated = None

    
    #==========================================================
    #=                    Public Functions                    =
    #==========================================================

    # Constructor
    def __init__(self):
        self.getSources()
        # testing
        for source in self.__sourcesList:
            source.printself()
        print("Last updated: ", self.__lastUpdated)

    # Builds the initial source list upon initialization
    def getSources(self):
        sourcesDF = pd.read_csv('sources.csv')
        for index, row in sourcesDF.iterrows():
            source = Source(
                row["Name"],
                row["Type"],
                row["URL"]
            )
            self.__sourcesList.append(source)
            # source.printself() #testing

        self.__lastUpdated = datetime.now()        

    # Updates the already initialized source list 
    def updateSources(self):

        self.__lastUpdated = datetime.now()

    def postNews(self):
        pass
        


""" --------------------LOCAL TESTING------------------------- """

feed = NewsFeed()
feed.getSources()

