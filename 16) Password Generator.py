
import random

lowercase_alphabet = ("abcdefghijklmnopqrstuvwxyz")
uppercase_alphabet = lowercase_alphabet.upper()
list_of_symbols = (",./?@#[]{}()+-=£$%^&*")

def main():
    lower_letters = lowercase_letters()
    upper_letters = uppercase_letters()
    password_numbers = numbers()
    password_symbols = symbols()
    password = join_all_together(password_numbers, password_symbols, lower_letters, upper_letters)
    print(f"Your password is: {password}\n")

def lowercase_letters():
    lowercase_letters = random.sample(lowercase_alphabet, random.randint(0,15))
    return lowercase_letters

def uppercase_letters():
    uppercase_letters = random.sample(uppercase_alphabet, random.randint(0,15))
    return uppercase_letters

def numbers():
    numbers = random.sample(range(10), 5)
    return numbers

def symbols():
    symbols_sample = random.sample(list_of_symbols, 3)
    return symbols_sample

def join_all_together(password_numbers, password_symbols, lower_letters, upper_letters):
    password_list = list(password_numbers + password_symbols + lower_letters + upper_letters)
    print(f"Before shuffling: {password_list}")
    random.shuffle(password_list)
    print(f"After shuffling: {password_list}")
    password_string = ""
    for i in password_list:
        i = str(i)      # numbers generated must be converted from ints to strings.
        password_string+=i
    return password_string

if __name__=="__main__": main()