def same_values(lst1, lst2):
    values_index = []
    index = 0
    for compare in lst1:
        if compare == lst2[index]:
            values_index.append(index)
            index += 1
        else:
            index += 1

    return values_index

# def same_values(lst1, lst2):
#     values_index = []
#     index = 0
#     for compare in lst1:
#         if compare == lst2[index]:
#             values_index.append(index)
#             index += 1
#         else:
#             index += 1
#
#     return values_index

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))