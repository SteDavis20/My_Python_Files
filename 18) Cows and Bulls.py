import random

def main():
    number = random.randint(1000, 9999)     # generate random 4 digit number
    guess = ""
    guess_count = 0
    while guess != number:
        guess = int(input("Guess the 4-digit number: "))    # ask user to guess
        guess_count+=1
        if guess == number:
            print(f"Well done, {guess} was the number!")
        else:
            number_of_cows = cows(number, guess)
            number_of_bulls = bulls(number, guess)
            print(f"{number_of_cows} cows, {number_of_bulls} bulls. Guess again!")
    print(f"You took {guess_count} guesses.")

# for every correct digit in the correct place, user has a "cow"
def cows(number, guess):
    number = str(number)
    guess = str(guess)
    guess_index = 0
    count = 0
    for i in number:
        if i == guess[guess_index]:
            count+=1
        guess_index+=1
    return count

# for every correct digit in the wrong place, user has a "bull"
def bulls(number, guess):
    number = str(number)
    guess = str(guess)
    guess_index = 0
    count = 0
    for i in number:
        if i in guess and i !=guess[guess_index]:
            count+=1
        guess_index+=1
    return count

if __name__=="__main__":    main()
