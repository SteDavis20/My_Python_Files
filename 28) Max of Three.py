def main():
    num1 = 10
    num2 = 15
    num3 = 8
    largest_number = largest_of_three(num1, num2, num3)
    if largest_number != None:
        print(f"{largest_number} is the largest of the set {num1}, {num2} and {num3}.")
    else:
        print(f"None of the 3 numbers are greater than both the other 2.")

def largest_of_three(number1, number2, number3):
    if number1 > number2 and number1 > number3:
        return number1
    elif number2 > number1 and number2 > number3:
        return number2
    elif number3 > number1 and number3 > number2:
        return number3
    else:
        return None

if __name__ == '__main__':  main()
