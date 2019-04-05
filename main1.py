from Theatre import Theatre

# List to store all the contacts 
theatres = []

def create():
    try:

        theatreName = input("Enter Theatrename: ")
        movieName = input("Enter Moviename: ")
        #show = input("Enter movie show: ")
        print("1. seatA - Rs.500\n2. seatB - Rs.300\n3. seatC - Rs.200")

        Choice = int(input("Enter Your choice: "))

        if Choice == 1:
            price = input("Enter your ticket price: ")
            if price == '500':
                print(price)
            else:
                print("Incorrect")  

        elif Choice == 2:
            price = input("Enter your ticket price: ")
            if price == '300':
                print(price)
            else:
                print("Incorrect") 

        elif Choice == 3:
            price = input("Enter your ticket price: ")
            if price == '200':
                print(price)
            else:
                print("Incorrect")  
        else:
            print("Correct input")                        

        newTheatre = Theatre(theatreName, movieName, price)
        theatres.append(newTheatre)    
        print('Added theatre - ' + newTheatre.getTheatreName())
        print('Movie name  - ' + newTheatre.getMovieName())
        print('Ticket price  - ' + newTheatre.getPrice())
    except IOError as e:    
        print("File not found in directory.")
   
def listTheatres():
    print('All Theatres and Movies')
    for theatre in theatres:
        print(theatre.getTheatreName() + ' - ' + theatre.getMovieName())

def listMovies():        
    print('All Movies')
    for theatre in theatres:
        print(theatre.getMovieName())

def printMenu():
    print("Menu")
    print("1. Create\n2. ListTheatre\n3. ListMovie\n4. Ticket\n5. Exit")

  
def startApp():
    while True:
        printMenu()
        userChoice = int(input("Enter Your choice: "))
        if userChoice == 1:
            create()
        elif userChoice == 2:
            listTheatres()
        elif userChoice == 3:
            listMovies()
        elif userChoice == 4:
            exit()            
        else:
            print('Invalid choice')

def main():
    print("---Theatres---")
    startApp()

if __name__ == "__main__":
    main()






"""seatA = 20
seatB = 15
seatC = 10
#tickets
sectionA=300
sectionB=500
sectionC=200"""    