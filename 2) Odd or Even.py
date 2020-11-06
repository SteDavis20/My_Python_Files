number = int(input("Please enter a number: "))
if (number%4) == 0:
    print("{} is a multiple of 4." .format(number))
elif (number%2) == 0:
    print("{} is even." .format(number))
else:
    print("{} is odd." .format(number))

#-------------------------------------------------------------------
num = int(input("Please enter a number: "))
check = int(input("Please enter a second number: "))
if (num % check) == 0:
    print("{} divides evenly into {}." .format(check, num))
else:
    print("{} does not divide evenly into {}." .format(check, num))

