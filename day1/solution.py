def func(string):
    count = 0
    for i in range(len(string)):
        if i == "(":
            count+=1
        elif i == ")":
            count-=1
        else:
            count += 0
    return count 

#~~~~~~~~~~~~~~~~~~~TESTS~~~~~~~~~~~~~~~~~~~~
import os
import csv



#~~~~~~~~~~~~~~~~~~~SOLUTION~~~~~~~~~~~~~~~~~~~
input = 0
answer = func(input)
print(f"The solution is {answer}")