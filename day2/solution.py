import csv

def func1(h,l,w):
    h=int(h)
    l=int(l)
    w=int(w) 
    
    a = h*l
    b = l*w
    c = w*h
    additional = min(a,b,c) 
    total = 2*(a+b+c) + additional
    return total

def func2(h,l,w):
    h = int(h)
    l = int(l)
    w = int(w) 

    per1 = 2*(h+l)
    per2 = 2*(l+w)
    per3 = 2*(w+h)
    
    v = h*l*w

    return min(per1,per2,per3) + v

#~~~~~~~~~~~~~~~~~~~TESTS PART ONE~~~~~~~~~~~~~~~~~~~~

# with open("testsPartOne.csv") as fileObject:
#     file = csv.reader(fileObject)
#     for key in file:
#         print(func1(key[0],key[1],key[2]) == int(key[3]))

#~~~~~~~~~~~~~~~~~~~SOLUTION PART ONE~~~~~~~~~~~~~~~~~~~
answer = 0
with open("inputValue.csv") as fileObject:
    file = csv.reader(fileObject)
    for key in file:
        answer += func1(key[0],key[1],key[2])

print(f"The solution to part 1 is {answer}")

#~~~~~~~~~~~~~~~~~~~TESTS PART TWO~~~~~~~~~~~~~~~~~~~

# with open("testsPartTwo.csv") as fileObject:
#     file = csv.reader(fileObject)
#     for key in file:
#         print(func2(key[0],key[1],key[2]) == int(key[3]))

#~~~~~~~~~~~~~~~~~~~SOLUTION PART TWO~~~~~~~~~~~~~~~~~~~
answer = 0
with open("inputValue.csv") as fileObject:
    file = csv.reader(fileObject)
    for key in file:
        answer += func2(key[0],key[1],key[2])

print(f"The solution to part 2 is {answer}")
#print(func(input_value.input, True))