a = [1, 1, 2, 3, 4, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 3, 2, 3]
c = []
# solution using loops
for i in a:
    if i in c:
        continue
    for j in b:
        if i == j:
#            print(f"i is: {i}, j is {j}")
            if j not in c:
                c.append(i)
#print(c)

# solution using sets
a = [1, 1, 2, 3, 4, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 3, 2, 3, 89]
a = set(a)
b = set(b)
common_set = a & b
print(common_set)
