def divisors(number):
    list = []
    possibleList = range(1, number)
    for i in possibleList:
        if number % i == 0:
            list.append(i)
    print("Divisors of {} are: {}".format(number, list))
    return list

number = int(input("Please enter a number: "))
listOfDivisors = divisors(number)
for i in listOfDivisors:
    if (i != 1) and (i != number):
        print(f"{number} is not a prime number.")
        break
else:
    print(f"{number} is a prime number.")
