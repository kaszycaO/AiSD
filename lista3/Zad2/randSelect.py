import random

compares = 0
swaps = 0

def reset_counters():
    global compares
    global swaps
    swaps = 0
    compares = 0

def randomized(my_list, low, high, element):
    global compares

    if element == 1:
        print("Calculating minimum")
        min = my_list[0]
        index = 0
        for i in range(1, len(my_list)):
            compares+=1
            if my_list[i] < min:
                min = my_list[i]
                index = i

        my_list[index] = [my_list[index]]
        return
    elif element == high + 1:
        print("Calculating maximum")
        max = my_list[0]
        index = 0
        for i in range(1, len(my_list)):
            compares+=1
            if my_list[i] > max:
                max = my_list[i]
                index = i

        my_list[index] = [my_list[index]]
        return
    else:
        rand_select(my_list, low, high, element)

def rand_select(my_list, low, high, element):
    global compares

    print("Compare: ", low, high)
    compares += 1
    if low == high:
        my_list[low] = [my_list[low]]
        return

    pivot = rand_partition(my_list, low, high)
    print("Index of chosen pivot: ", pivot)
    # rozmiar pierwszej polowy
    size = pivot - low + 1

    print("Compare: ", element, size)
    compares += 1
    if element == size:
        my_list[pivot] = [my_list[pivot]]
        return
    elif element < size:
        rand_select(my_list, low, pivot - 1, element)
    else:
        rand_select(my_list, pivot + 1, high, element - size)


def rand_partition(my_list, low, high):
    helper = random.randint(low, high)
    swap_elements(my_list, high, helper)
    return partition(my_list, low, high)


def partition(my_list, low, high):
    global compares

    pivot = my_list[high]
    print("Chosen pivot: ", pivot)
    i = low - 1
    for j in range(low, high):
        print("Compare: ", my_list[j], pivot)
        compares += 1
        if my_list[j] < pivot:
            i += 1
            if i != j:
                swap_elements(my_list, i, j)
    swap_elements(my_list, i + 1, high)

    return i + 1

def swap_elements(my_list, index_A, index_B):
    global swaps
    print("{} swap {}".format(my_list[index_A], my_list[index_B]))
    swaps += 1
    temp = my_list[index_A]
    my_list[index_A] = my_list[index_B]
    my_list[index_B] = temp
    print(my_list)



def randomized_stat(my_list, low, high, element):
    global compares

    if element == 1:
        min = my_list[0]
        index = 0
        for i in range(1, len(my_list)):
            compares+=1
            if my_list[i] < min:
                min = my_list[i]
                index = i

        my_list[index] = [my_list[index]]
        return
    elif element == high + 1:
        max = my_list[0]
        index = 0
        for i in range(1, len(my_list)):
            compares+=1
            if my_list[i] > max:
                max = my_list[i]
                index = i

        my_list[index] = [my_list[index]]
        return
    else:
        rand_select_stat(my_list, low, high, element)

def rand_select_stat(my_list, low, high, element):
    global compares

    compares += 1
    if low == high:
        my_list[low] = [my_list[low]]
        return

    pivot = rand_partition_stat(my_list, low, high)

    # rozmiar pierwszej polowy
    size = pivot - low + 1

    compares += 1
    if element == size:
        my_list[pivot] = [my_list[pivot]]
        return
    elif element < size:
        rand_select_stat(my_list, low, pivot - 1, element)
    else:
        rand_select_stat(my_list, pivot + 1, high, element - size)


def rand_partition_stat(my_list, low, high):
    helper = random.randint(low, high)
    swap_elements_stat(my_list, high, helper)
    return partition_stat(my_list, low, high)

def partition_stat(my_list, low, high):
    global compares

    pivot = my_list[high]
    i = low - 1
    for j in range(low, high):
        compares += 1
        if my_list[j] < pivot:
            i += 1
            if i != j:
                swap_elements_stat(my_list, i, j)
    swap_elements_stat(my_list, i + 1, high)

    return i + 1

def swap_elements_stat(my_list, index_A, index_B):
    global swaps
    swaps += 1
    temp = my_list[index_A]
    my_list[index_A] = my_list[index_B]
    my_list[index_B] = temp
