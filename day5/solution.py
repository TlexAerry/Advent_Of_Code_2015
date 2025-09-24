import csv
import pandas as pd

vowel_tuple = ('a','e','i','o','u')
forbidden_tuple = ('ab','cd','pq','xy')

def vowelTest(string):
    vowelCount = 0 
    
    for i in string:
        if i in vowel_tuple:
            vowelCount += 1

    if vowelCount >= 3:
        return True
    else:
        return False 
    
def dupeTest(string):
    for i in range(0,len(string)-1):
        if string[i] == string[i+1]:
            return True
    return False

def forbiddenTest(string):
    for i in range(0,len(string)-1):
        if f"{string[i]}{string[i+1]}" in forbidden_tuple:
            return False
    return True

def isNice(string):
    a = vowelTest(string)
    b = dupeTest(string)
    c = forbiddenTest(string)
    return a and b and c



#~~~~~~~~~~~~~~~~~~~TESTS PART ONE~~~~~~~~~~~~~~~~~~~~

# with open("testsPartOne.csv") as fileObject:
#     file = csv.reader(fileObject)
#     for key in file:
#         print(isNice(key[0]) == eval(key[1]))

#~~~~~~~~~~~~~~~~~~~SOLUTION PART ONE~~~~~~~~~~~~~~~~~~~

countNice = 0
data = pd.read_csv("inputValues.csv")
for i in data["strings"]:
    if isNice(i):
        countNice += 1

#strings = data[0]
#print(strings)
# with open("inputValues.csv") as fileObject:
#     file = csv.reader(fileObject)
#     for key in file:
#         if isNice(key):
#             countNice +=1

print(f"The number of nice strings is {countNice}")