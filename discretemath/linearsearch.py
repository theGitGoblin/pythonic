def linear_search(list, targetindex):
    for x in list:
        if x == targetindex:
            return True
    return False

myList = [1, 2, 3 ,4 ,5]

print(linear_search(myList, 1))