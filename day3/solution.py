import csv

class house:
    def __init__(self,x,y,number_presents = 1):
        self.address = [x,y]
        self.presents = number_presents
        self.addressFriendly = f"[{x},{y}]"

    def __eq__(self, other):
        if self.address == other.address:
            return True
        else:
            return False
        
    def receivePresent(self):
        self.presents += 1

class santa:
    def __init__(self):
        self.address = [0,0] #initiatlise yourself at origin
        self.visited_houses = [house(0,0)] #a list of all visited house objects
        self.presents_given = 1

    def visitHouse(self, newHouse):
        for i in self.visited_houses: #i is a house
            if newHouse == i: #if the new house matches one of the existing houses....
                i.receivePresent()  #give the existing house another present
                self.presents_given += 1
                return
        self.visited_houses.append(newHouse) #or.... add it to the list of houses we've now visited
        self.presents_given += 1                 
        return


    def move(self, direction): #method for moving around the grid by input      
        if direction == "<":
            self.address[0] -=1
        elif direction == ">":
            self.address[0] +=1
        elif direction =="^":
            self.address[1] +=1
        elif direction == "v":
            self.address[1] -=1
        else:
            raise Exception("Not a valid direction")    
        self.visitHouse(house(self.address[0],self.address[1]))

def solFunction1(directions):
    func_santa = santa()
    for i in directions:
        func_santa.move(i)
    return len(func_santa.visited_houses)


def solFunction2(directions):
    directions1 = ""
    directions2 = ""
    for i in range(0,len(directions)):
        if i % 2 == 1:
            directions1 = directions1 + input_string[i]
        else:  
            directions2 = directions2 + input_string[i] 

    print(f"~~~~~~~~~~\n{directions}\n{directions1}\n{directions2}\n ~~~~~~~~~~")
    # func_santa1 = santa()
    # func_santa2 = santa()
    # for i in directions1:
    #     func_santa1.move(i)
    # for i in directions2:
    #     func_santa2.move(i)
    # total_houses = func_santa1.visited_houses + func_santa2.visited_houses
    # all_addresses = []


#~~~~~~~~~~~~~~~~~~~TESTS PART ONE~~~~~~~~~~~~~~~~~~~~

# with open("testsPartOne.csv") as fileObject:
#     file = csv.reader(fileObject)
#     for key in file:
#         print(int(solFunction1(key[0])) == int(key[1]))


#~~~~~~~~~~~~~~~~~~~SOLUTION PART ONE~~~~~~~~~~~~~~~~~~~

from inputValue import *

print(f"the answer to part 1 is {solFunction1(input_string)}")

#~~~~~~~~~~~~~~~~~~~TESTS PART TWO~~~~~~~~~~~~~~~~~~~~

with open("testsPartTwo.csv") as fileObject:
    file = csv.reader(fileObject)
    for key in file:
        print(solFunction2(key[0]))


#~~~~~~~~~~~~~~~~~~~SOLUTION PART TWO~~~~~~~~~~~~~~~~~~~

#print(f"the answer to part 2 is {solFunction2(input_string)}")
