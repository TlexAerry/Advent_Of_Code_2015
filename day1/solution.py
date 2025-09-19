def func(string,flag = False):
    val = 0
    for i in range(len(string)):
        if string[i] == "(":
            val+=1
        elif string[i] == ")":
            val-=1
        else:
            val += 0
        
        if flag == True:
            if val == -1: 
                return i+1 
                flag = False
    return val 

#~~~~~~~~~~~~~~~~~~~TESTS PART ONE~~~~~~~~~~~~~~~~~~~~
import csv

with open("testsPartOne.csv") as fileObject:
    file = csv.reader(fileObject)
    for key in file:
        print(func(key[0]) == int(key[1]))


#~~~~~~~~~~~~~~~~~~~SOLUTION PART ONE~~~~~~~~~~~~~~~~~~~
import inputValue
answer = func(inputValue.input)
print(f"The solution is {answer}")

#~~~~~~~~~~~~~~~~~~~TESTS PART TWO~~~~~~~~~~~~~~~~~~~

with open("testsPartTwo.csv") as fileObject:
    file = csv.reader(fileObject)
    for key in file:
        print(func(key[0],True) == int(key[1]))

#~~~~~~~~~~~~~~~~~~~SOLUTION PART TWO~~~~~~~~~~~~~~~~~~~

print(func(inputValue.input, True))