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
            else: # and if we haven't visited this house before
                self.visited_houses.append(newHouse) # add it to the list of houses we've now visited
                self.presents_given += 1 
                
                return
# The issue here is that the for loop in my visit house method is getting called everytime
# something is tested. So if it's 0,0 then it will always increment the number of presents
# that have been given as that's the first house. But when santa moves to 0,1 and it's te-
# sted, then it fails the first if statement, so will create a new house regardless at the
# address   

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

    for i in func_santa.visited_houses:
        print(i.address,i.presents)
    return len(func_santa.visited_houses)

#~~~~~~~~~~~~~~~~~~~TESTS PART ONE~~~~~~~~~~~~~~~~~~~~

with open("testsPartOne.csv") as fileObject:
    file = csv.reader(fileObject)
    for key in file:
        print(solFunction(key[0]))


#~~~~~~~~~~~~~~~~~~~SOLUTION PART ONE~~~~~~~~~~~~~~~~~~~
