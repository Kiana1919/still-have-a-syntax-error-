"""
Program Goals:
1. Get the input from the user!
2. Convert that input to an INT
3. Add that input to a list
4. Pull values from specific index positions
"""

#create funtions that will perform those actions above
import random
myList = []
unique_list = []

def mainProgram():
    #build your while loop
    while True:
            print("Hello,there! Let's work with lists!")
            print("Choose one of the following options.  Type a number ONLY!")
            choice = input("""1. Add to list,
2. Add a bunch of numbers
3. Get an item at an index
4. Sort list
5. Random Choice
6. Linear Search
7. Recursive Binary Search
8. Iterative Binary Search
9.Print List
10. Quit """)
            if choice == "1":
                addToList()
            elif choice == "2":
                addABunch()
            elif choice == "3":
                indexValues
            elif choice == "4":
                sortList(myList)
            elif choice == "5":
                randomSearch()
            elif choice == "6":
                linearSearch()
            elif choice == "7":
                binSearch = input("What number are you looking for? ")
                recursiveBinarySearch(unique_list, 0, len(unique_list-1, int(binSearch))
            elif choice == "8":
                binSearch = input("What number are you looking for?")
                result = interactiveBinarySearch(unique_list, int(inSearch))
                if result != -1:
                    print("Your number is at index position {}".format(result))
                else:
                    print("Your number isn't here!")
            elif choice == "9":
                printLists()
            else:
                break
        except:
            print("An error occured")
            #we need to add an exit program AAAAAND error catching!

def addToList():
    print("Adding to list! Great choice!")
    newItem = input("Please type an integer! ")
    myList.append(int(newItem))

def addABunch():
    print("We're gonna add bunch of numbers to your list!")
    numToAdd = input("How many new integers do you want to add? ")
    numRange = input("And how high would you like these numbers to go? ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("Your list is now complete!")

def sortList(myList):
    #note that this is the first function we've built here that takes ARGUEMENTS
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input("Would you like to see the unique values in your list? Y/N ")
    if showMe.lower() == "y":
        print(unique_list)

def indexValues():
    print("At what index posion do you want to search?")
    indexPos = input("Type an index position here: ")
    print(myList[int(indexPos)])

def randomSearch():
    print("oH iM sO rAnDom!!!")
    print(myList[random.randint(0, len(myList)-1)])
    if len(unique_list) > 0:
        print(unique_list[random.randint(0, len(unique_list)-1)])


def linearSearch():
    print("We're going to go through this list one itm at a time!")
    searchItem = input("What are you looking for? ")
    for x in range(len(myList)):
        if myList[x] == int(searchValue):
            print("Your item is at index position {}".format(x))

def printLists():
    if len(unique_list) == 0:
        print(myList)
    else:
        whichOne = input("Which list do you wanna see, Sorted or un sorted? ")
        if whichOne.lower() == "sorted":
            print(unique_list)
        else:
                print(myList)

def recursiveBinarySearch(unique_list, low, high, x):
    if high >= low;
        mid = (high+low) //2

        if unique_list[mid] == :
            print("Your number is at index position {}".format(mid))
            return mid
        
        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, high, mid - 1, x)
        else:
            return recursiveBinarySearch(unique_list, mid + 1, high, x)
    else:
        print("Your number isn't here!")

def interactiveBinarySearch(unique_list, x):
    low = 0
    high = len(unique_list)-1
    mid = 0

    while low <=high:
        mid = (high + low) // 2

    if unique_list[mid] < x:
        low= mid +1

    elif unique_list[mid] > x:
        high = mid -1
    else:
        return mid
    return-1

             
if __name__  == "__main__":
        mainProgram()
