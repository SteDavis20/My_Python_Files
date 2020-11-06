def main():
    user_string = ask_for_long_string()
    substrings = split_long_string(user_string)
    reversed_list = reverse_order(substrings)
    reversed_string = join_reversed_list(reversed_list)
    print(reversed_string)

def ask_for_long_string():
    long_string = input("Please enter a long string containing multiple words: ")
    return long_string

def split_long_string(long_string):
    list_of_substrings = long_string.split()
    return list_of_substrings

def reverse_order(substrings):
    reverse_list = []
    next_index = len(substrings)-1
    for i in substrings:
        reverse_list.append(substrings[next_index])
        next_index -= 1
    return reverse_list

def join_reversed_list(list):
    joint_list = " ".join(list)
    return joint_list


if __name__=="__main__":  main()
