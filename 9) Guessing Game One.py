import random

number = random.randint(1,9)
count = 0
guess = -1
while guess != number:
    count += 1
    guess = int(input("Guess the number: "))
    if guess < number:
        print(f"{guess} is too low.")
    elif guess > number:
        print(f"{guess} is too high.")
    elif guess == number:
        print(f"Bingo! {guess} was the number!")
    elif guess == "exit":
        break
print(f"Thank you for playing! It took you {count} guesses to guess the number.")


