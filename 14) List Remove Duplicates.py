a = [1, 2, 1, 3, 1, 4, 1, 4, 2, 3]

def main():
    #solution = remove_duplicates_sets(a)
    solution = remove_duplicates_loop(a)
    print(solution)

def remove_duplicates_loop(list):
    b = list
    c = []
    for i in list:
        if i not in c:
            for k in b:
                if k not in c:
                    if i == k:
                        c.append(i)
    return c

def remove_duplicates_sets(list):
    new_list = set(list)
    return new_list

if __name__ == "__main__":  main()


