print("Please enter your name: ")
name = input()
print("Please enter your age: ")
age = int(input())  # input() function always returns value as a String
# age = int() converts the String age, into the int age.

year100 = (100-age)+2020
line = "{}, you will turn 100 years old in {}.\n" .format(name, year100)
print(line)

print("Please enter the amount of copies of the above line you would like: ")
copies = int(input())
print(copies * line)
