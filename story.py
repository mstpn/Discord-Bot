# Filename: story.py
# import into another file by using "from story import Story"


#=========================================
#=              Story Class              =
#=========================================

class Story():  
    
    #===================================================
    #=                    Variables                    =
    #===================================================

    __title = None
    __author = None
    __date = None
    __url = None

    #==========================================================
    #=                    Public Functions                    =
    #==========================================================

    def __init__(self, title, author, date, url):
        self.__title = title
        self.__author = author
        self.__date = date
        self.__url = url
        
    def getTitle(self):
        return self.__title

    def getAuthor(self):
        return self.__author

    def getDate(self):
        return self.__date

    def getURL(self):
        return self.__url

    def getAll(self):
        return [self.__title, self.__author, self.__date, self.__url]