#a = [1, 4, 8, 3, 2, 19, 34, 88]
#for i in a:
#    if i < 5:
#        print("{} is less than 5." .format(i))

#--------------------------------------------------------
#a = [1, 4, 8, 19, 3, 2, 34, 88]
#newList = []
#for i in a:
#    if i < 5:
#        newList.append(i)
#print("The new list is: {}" .format(newList))

#--------------------------------------------------------
a = [1, 4, 8, 19, 3, 2, 34, 88]
number = int(input("Please enter a number: "))
newList = []
for i in a:
    if i < number:
        newList.append(i)
print("New list with numbers < {}: {}" .format(number, newList))
