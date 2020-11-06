
#a = [5, 10, 15, 20, 25]
#b = []
#b.append(a[0])
#b.append(a[(len(a)-1)])
#print(b)


# solution using functions:
list = [5, 10, 15, 20, 25]

def main():
    new_list = first_and_last(list)
    print(new_list)

def first_and_last(list):
    new_list = [list[0], list[(len(list)-1)]]
    return new_list

if __name__ == "__main__":  main()


