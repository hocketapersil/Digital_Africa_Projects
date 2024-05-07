def remove_duplicates(num):
    emptyList = []
    for i in num:
        if i not in emptyList:
            emptyList.append(i)
    return emptyList

print(remove_duplicates([1, 2, 3, 4, 4, 5, 6, 6, 7, 8, 9, 9]))