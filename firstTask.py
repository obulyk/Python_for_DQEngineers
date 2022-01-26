# import bibliothek random
import random
# create empty List
randomList1000 = []
# cycle for that creates 0 to 1000 cells
for i in range (0,1000):
    # n assign random number in diapason from0 to 1000
    n = random.randint(0,1000)
    # append function adds created random number to our list
    randomList1000.append(n)
# print whole list in console
print(randomList1000)
# create empty List
sortedListMinToMax = []
# cycle while
while randomList1000:
# first number is lowest
    minimum = randomList1000[0]
# cycle for. x=1 to randomList1000
    for x in randomList1000:
# if x=1 is lower than the first number of random number
        if x < minimum:
#minimum is set to X
            minimum = x
#add that lower number as first number to new List
    sortedListMinToMax.append(minimum)
# remove that number from list
    randomList1000.remove(minimum)
# print whole list in console
print(sortedListMinToMax)
# Even numbers from randomList1000
# empty list for even Numbers
evenNumbers = []
# empty list for odd Numbers
oddNumbers = []
# Cycle for
for e in sortedListMinToMax:
# if a number is divided on 2 without any decimal numbers
    if (e % 2) == 0:
# Add to empty list with that even Numbers
        evenNumbers.append(e)
# another case: not even
    else:
# add that number to odd list
        oddNumbers.append(e)
# case when we have 0, which is not even and not add
    if 0 in evenNumbers:
# remove 0 from two lists
        evenNumbers.remove(0)
# print whole list in console
print(evenNumbers)
# print whole list in console
print(oddNumbers)