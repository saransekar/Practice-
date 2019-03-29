from Product import Product

# List to store all the contacts
products = []

def createProduct():
    productName = input("Enter Productname: ")
    Price = input("Enter product price: ")
    newProduct = Product(productName, Price)
    products.append(newProduct)  
    print('Added new contact - ' + newProduct.getProductName())
   

def listProducts():
    print('All Contacts')
    for product in products:
        print(product.getProductName() + ' - ' + product.getPrice())

def printMenu():
    print("Menu")
    print("1. Create\n2. List\n3. Update\n4. Exit")


def startApp():
    items = []    
    while True:
        printMenu()
        userChoice = int(input("Enter Your choice: "))
        if userChoice == 1:
            createProduct()
        elif userChoice == 2:
            listProducts()
        elif userChoice == 3:
            Choice = input("Enter the number:")
            choiceInput = Choice.split(',')
            for i in choiceInput:
                name = i.split('-')[0]
                product = products[int(name)-1]
                print(product.getProductName())
                Quanity = i.split('-')[1]
                #import pdb; pdb.set_trace()
                quanity = int(Quanity)
                productPrice = int(product.getPrice())
                print("Product quanity {}{}".format('-', (quanity *  productPrice)))
                items.append(quanity * productPrice)
            print("Total cost price:",sum(items))    

        elif userChoice == 5:
            exit()            
        else:
            print('Invalid choice')

def main():
    print("---Products---")
    startApp()

if __name__ == "__main__":
    main()