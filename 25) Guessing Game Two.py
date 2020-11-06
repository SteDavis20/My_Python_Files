import random

def main():
    my_number = int(input("Please enter a number between 0 and 100 inclusive: "))
    computer_guess = -1
    guess_count = 0
    while computer_guess != my_number:
        computer_guess = random.randint(0,100)
        guess_count+=1
        print(f"Computer's guess: {computer_guess}")
        if computer_guess < my_number:
            computer_guess = random.randint(computer_guess+1,100)
        elif computer_guess > my_number:
            computer_guess = random.randint(0, computer_guess-1)
    print(f"Computer took {guess_count} guesses to guess your number.")

if __name__ == '__main__':  main()
