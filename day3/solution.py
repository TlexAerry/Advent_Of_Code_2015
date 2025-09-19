class house:
    def __init__(self,x,y,number_presents = 0):
        self.address = [x,y]
        self.presents = number_presents

    #define the equality method using the address to identify previously visited houses

class santa:
    def __init__(self):
        self.address = [0,0] #initiatlise yourself at origin
        self.visited_houses = [] #an list of all visited house objects
        
        self.visted_houses.append(house(0,0,1))
    

    def move(self, direction): #method for moving around the grid by input
        if direction == "<":
            self.address[0] -=1
        elif direction == ">":
            self.address[0] +=1
        elif direction =="^":
            self.address[1] +=1
        else: # direction == "V", assumption that there will be no noisy inputs
            self.address[1] -=1


    