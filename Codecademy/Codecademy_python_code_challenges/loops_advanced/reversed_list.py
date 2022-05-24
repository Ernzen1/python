def reversed_list(lst1, lst2):
    for elements in range(len(lst1)):
        if lst1[elements] != lst2[((len(lst2)) - 1) - elements]:
            return False
    return True

print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))