number = int(input("Please enter a number: "))
list = []
possibleList = range(1, number)
for i in possibleList:
    if number % i == 0:
        list.append(i)
print("Divisors of {} are: {}" .format(number, list))

