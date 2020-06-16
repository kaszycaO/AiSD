#!/usr/bin/python

swaps = 0
compares = 0

def reset_counters():
    global compares
    global swaps
    swaps = 0
    compares = 0

def quick_sort_stat(my_list, low, high, order):
    """Function doing quick sort
    low -> first element
    high -> last element
    order -> ASC or DESC
    """
    if low < high:
        # divide & conquer
        part = partition_stat(my_list, low, high, order)

        quick_sort_stat(my_list, low, part - 1, order)
        quick_sort_stat(my_list, part + 1, high, order)

def partition_stat(my_list, low, high, order):
    global compares

    pivot = my_list[high]
    i = low - 1

    if order == "ASC":
        for j in range(low, high):
            compares += 1
            if my_list[j] < pivot:
                i += 1
                if i != j:
                    swap_elements_stat(my_list, i, j)
    elif order == "DESC":
        for j in range(low, high):
            compares += 1
            if my_list[j] > pivot:
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



def quick_sort(my_list, low, high, order):
    """Function doing quick sort
    low -> first element
    high -> last element
    order -> ASC or DESC
    """
    if low < high:
        # divide & conquer
        part = partition(my_list, low, high, order)

        quick_sort(my_list, low, part - 1, order)
        quick_sort(my_list, part + 1, high, order)

def partition(my_list, low, high, order):
    global compares

    pivot = my_list[high]
    i = low - 1

    if order == "ASC":
        for j in range(low, high):
            print("Compare: ", my_list[j], pivot)
            compares += 1
            if my_list[j] < pivot:
                i += 1
                if i != j:
                    swap_elements(my_list, i, j)
    elif order == "DESC":
        for j in range(low, high):
            print("Compare: ", my_list[j], pivot)
            compares += 1
            if my_list[j] > pivot:
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
    my_list[index_B] = tempz
