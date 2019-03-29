class Product:

    def __init__(self, productname, price):
        self.__productname = productname
        self.__price = price

    def getProductName(self):
    	return self.__productname

    def setProductName(self,productName):
        self.__productName = productName

    def getPrice(self):
        return self.__price

    def setPrice(self, Price):  
        self.__Price = Price


