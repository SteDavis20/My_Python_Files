def main():
    string = get_string()
    reverse_of_string = get_reverse_of_string(string)
    print(reverse_of_string)
    is_palindromic = test_if_palindromic(string, reverse_of_string)
    if is_palindromic == True:
        print(f"{string} is palindromic.")
    else:
        print(f"{string} is not palindromic.")

def get_string():
    string = input("Please enter a string (one word): ")
    return string

def get_reverse_of_string(string):
    reverse_of_string = []
    next_index = len(string)-1
    for i in string:
        reverse_of_string.append(string[next_index])
        next_index -= 1
    reverse_of_string = "".join(reverse_of_string)
    return reverse_of_string

def test_if_palindromic(string, reverse_of_string):
    if string == reverse_of_string:
        return True
    else:
        return False

if __name__=="__main__":    main()