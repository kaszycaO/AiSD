
swaps = 0
compares = 0

def reset_counters():
    global compares
    global swaps
    swaps = 0
    compares = 0

def merge_sort_stat(my_list, order):
    if len(my_list) == 1:
        return
    else:
        list_mid = len(my_list)//2
        list_B = my_list[:list_mid]
        list_C = my_list[list_mid:]
        merge_sort_stat(list_B, order)
        merge_sort_stat(list_C, order)
        merge_lists_stat(list_B, list_C, my_list, order)

def merge_lists_stat(list_A, list_B, new_list ,order):
    global compares
    global swaps
    i = 0
    j = 0
    k = 0
    if order == "ASC":
        while i < len(list_A) and j < len(list_B):
            compares += 1
            if list_A[i] < list_B[j]:
                swaps += 1
                new_list[k] = list_A[i]
                i += 1
            else:
                swaps += 1
                new_list[k] = list_B[j]
                j += 1
            k += 1

    elif order == "DESC":
        while i < len(list_A) and j < len(list_B):
            compares += 1
            if list_A[i] > list_B[j]:
                swaps += 1
                new_list[k] = list_A[i]
                i += 1
            else:
                new_list[k] = list_B[j]
                swaps += 1
                j += 1
            k += 1

    while i < len(list_A):
        swaps += 1
        new_list[k] = list_A[i]
        i += 1
        k += 1

    while j < len(list_B):
        swaps += 1
        new_list[k] = list_B[j]
        j += 1
        k += 1


def merge_sort(my_list, order):
    if len(my_list) == 1:
        return
    else:
        list_mid = len(my_list)//2
        list_B = my_list[:list_mid]
        list_C = my_list[list_mid:]
        merge_sort(list_B, order)
        merge_sort(list_C, order)
        merge_lists(list_B, list_C, my_list, order)

def merge_lists(list_A, list_B, new_list ,order):
    global compares
    global swaps
    i = 0
    j = 0
    k = 0
    if order == "ASC":
        while i < len(list_A) and j < len(list_B):
            print("Compare: ", list_A[i] , list_B[j])
            compares += 1
            if list_A[i] < list_B[j]:
                print("{} swap {}".format(new_list[k], list_A[i]))
                swaps += 1
                new_list[k] = list_A[i]
                i += 1
            else:
                print("{} swap {}".format(new_list[k], list_B[j]))
                swaps += 1
                new_list[k] = list_B[j]
                j += 1
            k += 1

    elif order == "DESC":
        while i < len(list_A) and j < len(list_B):
            print("Compare: ", list_A[i] , list_B[j])
            compares += 1
            if list_A[i] > list_B[j]:
                print("{} swap {}".format(new_list[k], list_A[i]))
                swaps += 1
                new_list[k] = list_A[i]
                i += 1
            else:
                new_list[k] = list_B[j]
                print("{} swap {}".format(new_list[k], list_B[j]))
                swaps += 1
                j += 1
            k += 1

    while i < len(list_A):
        print("{} swap {}".format(new_list[k], list_A[i]))
        swaps += 1
        new_list[k] = list_A[i]
        i += 1
        k += 1

    while j < len(list_B):
        print("{} swap {}".format(new_list[k], list_B[j]))
        swaps += 1
        new_list[k] = list_B[j]
        j += 1
        k += 1
