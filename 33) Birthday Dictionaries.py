dictionary = dict(Stephen = "27/08/1999", Andrea = "11/05/1963", Brendan = "11/04/1962")

print("We know the dates of the following people's birthdays: ")
for k in dictionary.keys():
    print(f"{k}")
requested_birthday = input("Whose birthday would you like to know: ")
for k, v, in dictionary.items():
    if requested_birthday == k:
        print(f"{k}'s birthday is {v}")

