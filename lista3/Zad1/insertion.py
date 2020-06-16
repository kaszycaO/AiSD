
swaps = 0
compares = 0

def insertion_sort_stat(my_list, order):
    global swaps
    global compares
    compares = 0
    swaps = 0
    if order == "ASC":
        for j in range(1, len(my_list)):
            key = my_list[j]
            i = j - 1
            while i >= 0 and my_list[i] > key:
                my_list[i+1] = my_list[i]
                compares += 1
                swaps += 1
                i -= 1
                my_list[i+1] = key

            compares += 1

    elif order == "DESC":
        for j in range(1, len(my_list)):
            key = my_list[j]
            i = j - 1
            while i >= 0 and my_list[i] < key:
                my_list[i+1] = my_list[i]
                compares += 1
                swaps += 1
                i -= 1
                my_list[i+1] = key

            compares += 1

def insertion_sort(my_list, order):
    global swaps
    global compares
    compares = 0
    swaps = 0
    if order == "ASC":
        for j in range(1, len(my_list)):
            key = my_list[j]
            i = j - 1
            while i >= 0 and my_list[i] > key:
                my_list[i+1] = my_list[i]
                print("Compare: ", key, my_list[i])
                compares += 1
                print("{} swap {}".format(my_list[i], key))
                swaps += 1
                i -= 1
                my_list[i+1] = key

            print("Compare: ", key, my_list[i])
            compares += 1

    elif order == "DESC":
        for j in range(1, len(my_list)):
            key = my_list[j]
            i = j - 1
            while i >= 0 and my_list[i] < key:
                my_list[i+1] = my_list[i]
                print("Compare: ", key, my_list[i])
                compares += 1
                print("{} swap {}".format(my_list[i], key))
                swaps += 1
                i -= 1
                my_list[i+1] = key

            print("Compare: ", key, my_list[i])
            compares += 1
