class Theatre:
    def __init__(self, theatrename, moviename, price):
        self.__theatre = theatrename
        self.__moviename = moviename
        self.__price = price
       

    def getTheatreName(self):
    	return self.__theatre

    #def setTheatreName(self, theatreName):
        #self.__theatre = theatreName

    def getMovieName(self):
        return self.__moviename

    #def setMovieName(self, movieName):
       # self.__moviename = movieName

    def getPrice(self):
        return self.__price
   