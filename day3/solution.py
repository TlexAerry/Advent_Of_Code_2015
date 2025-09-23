import csv

class house:
    def __init__(self,x,y,number_presents = 1):
        self.address = [x,y]
        self.presents = number_presents

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

def solFunction(directions):
    func_santa = santa()
    for i in directions:
        func_santa.move(i)
    return len(func_santa.visited_houses)

#~~~~~~~~~~~~~~~~~~~TESTS PART ONE~~~~~~~~~~~~~~~~~~~~

with open("testsPartOne.csv") as fileObject:
    file = csv.reader(fileObject)
    for key in file:
        print(solFunction(key[0]),key[1],int(solFunction(key[0])) == int(key[1]))


#~~~~~~~~~~~~~~~~~~~SOLUTION PART ONE~~~~~~~~~~~~~~~~~~~

from inputValue import *

print(f"the answer to part 1 is {solFunction(input_string)}")