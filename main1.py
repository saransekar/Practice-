from Theatre import Theatre 

# List to store all the contacts 
theatres = []
def createTheatre():
    aTheatre = Theatre("A", "Viswasam", "9.30",20,"500")
    aTheatre1 = Theatre("A", "Viswasam", "1.30",20,"500")
    aTheatre2 = Theatre("A", "Viswasam", "6.30",20,"500")

    bTheatre = Theatre("B", "petta", "9.30",4,"400")   
    bTheatre1 = Theatre("B", "petta", "1.30",3,"400")
    bTheatre2 = Theatre("B", "petta", "6.30",2,"400") 

    theatres.append(aTheatre)
    theatres.append(aTheatre1)
    theatres.append(aTheatre2)

    theatres.append(bTheatre)
    theatres.append(bTheatre1)
    theatres.append(bTheatre2)
    
       
def listTheatres():
    unique_list = [] 
    for theatre in theatres: 
        if theatre.getTheatreName() not in unique_list:
            unique_list.append(theatre.getTheatreName())
    for x,y in enumerate(unique_list):
        print(x+1,'.',y,'Theatre show')  


    #for theatre_idx,theatre_val,  in enumerate(theatres):
        #print("{}{}{}{}{}".format(theatre_idx + 1, ".", theatre_val.getTheatreName(), '-', 'Theatre show'))
        
        #print(' ' + theatre_val.getMovieName() + ' ' + theatre_val.getShowTime() + ' ' + str(theatre_val.getSeat()) + ' ' + theatre_val.getPrice())
        #print(len(theatres))

    """theatre = theatres[0]
    demo = theatre.getTheatreName()
    theatre.setTheatreName(demo) 
    print(theatre.getTheatreName(),'Theatre')

    theatre = theatres[3]
    demo = theatre.getTheatreName()
    theatre.setTheatreName(demo) 
    print("Seats are available: ", theatre.getTheatreName())"""

    """for theatre1 in theatres1:
        print(theatre1.getTheatreName() + ' ' + 'Theatre ')
        print(theatre1.getMovieName() + ' ' + theatre1.getShowTime() + ' ' + str(theatre1.getSeat()) + ' ' + theatre1.getPrice())
        theatre = theatres1[0]
        demo = int(theatre1.getSeat()) - 1
        theatre.setSeat(demo) 
        print("Seats are available: ", demo)"""

    """print('All Theatres and Movies')
    for theatre in theatres:
        print(theatre.getTheatreName() + ' - ' + theatre.getMovieName())
        theatre = theatres[0]
        demo =  int(theatre.getSeat()) -1
        theatre.setSeat(demo) 
        print("Correct",theatre.getSeat())"""



def bookTickets():
    print('Tickets Booking')
    for theatre_idx,theatre_val in enumerate(theatres):
        #print("{}{}{}{}{}".format(theatre_idx + 1, ".", theatre_val.getTheatreName(), '-', 'Theatre show'))
        
        print(' ' + theatre_val.getMovieName() + ' ' + theatre_val.getShowTime() + ' ' + str(theatre_val.getSeat()) + ' ' + theatre_val.getPrice())


    choice = int(input("Enter choice: "))

    if choice <= len(theatres):    
        book = int(input("Enter Booking Tickets: "))
        theatre = theatres[choice-1]
        seat = int(theatre.getSeat()) - book
        if theatre.getSeat() != 0:           
            theatre.setSeat(seat) 
            print("total ticket prices: ",int(theatre.getPrice()) * book)
            print("Seats are available: ", theatre.getSeat())
        else:
            print("Seats are not available")        
    else:
        print("Correct input for booking")          

def listMovies():        
    print('All Movies')
    for theatre in theatres:
        print(theatre.getMovieName())

def printMenu():
    print("Menu")
    print("1. ListTheatre\n2. BookingTickets\n3. ListMovie\n4. Exit")

  
def startApp():
    createTheatre()
    while True:
        printMenu()
        userChoice = int(input("Enter Your choice: "))           
        if userChoice == 1:
            listTheatres()
        elif userChoice == 2:
            listTheatres()
            bookTickets()
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







"""for theatre in theatres:
    print(theatre.getTheatreName() + ' ' + 'Theatre ')
    print(theatre.getMovieName() + ' ' + theatre.getShowTime() + ' ' + theatre.getSeat() + ' ' + theatre.getPrice())

for theatre in theatres:
    print(theatre.getTheatreName() + ' ' + 'Theatre ')
    print(theatre.getMovieName() + ' ' + theatre.getShowTime() + ' ' + theatre.getSeat() + ' ' + theatre.getPrice())

    choice = int(input("Enter choice: "))"""



"""choice = int(input("Enter choice: "))
    if choice == 1:
        print(aTheatre.getMovieName() + ' ' + aTheatre.getShowTime() + ' ' + aTheatre.getSeat() + ' ' + aTheatre.getPrice()) 
        print(aTheatre1.getMovieName() + ' ' + aTheatre1.getShowTime() + ' ' + aTheatre1.getSeat() + ' ' + aTheatre1.getPrice()) 
        print(aTheatre2.getMovieName() + ' ' + aTheatre2.getShowTime() + ' ' + aTheatre2.getSeat() + ' ' + aTheatre2.getPrice())
        booking = int(input("Enter booking seat: ")) 
        if booking == 1:
            #aTheatre.setSeat(19)
            demo = int(aTheatre.getSeat())
            print("Seats are available: ", demo)

            aTheatre.setSeat(demo)
            print("Hello",aTheatre.getSeat())

            #Choice = int(input("Enter the number: "))
            #aTheatre = theatres[1] 
            #aTheatre.setSeat(demo) 
            #print("Correct",aTheatre.getSeat()) 

        elif booking == 2:
            print("Seats are available: ", int(aTheatre1.getSeat())-1)
        elif booking == 3:
            print("Seats are available: ", int(aTheatre2.getSeat())-1)   
        else:
            print("Hello")      
    elif choice == 2:
        print(bTheatre.getMovieName() + ' ' + bTheatre.getShowTime() + ' ' + bTheatre.getSeat() + ' ' + bTheatre.getPrice())
        print(bTheatre1.getMovieName() + ' ' + bTheatre1.getShowTime() + ' ' + bTheatre1.getSeat() + ' ' + bTheatre1.getPrice())
        print(bTheatre2.getMovieName() + ' ' + bTheatre2.getShowTime() + ' ' + bTheatre2.getSeat() + ' ' + bTheatre2.getPrice())

    else:
        print("No theatre")

"""