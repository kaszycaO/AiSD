#!/usr/bin/python

import insertion

def reset_counters():
    global compares
    global swaps
    swaps = 0
    compares = 0

def hybrid_sort(my_list, order):
    """merge + insertion """
    if len(my_list) == 1:
        return
    if len(my_list) < 15:
        insertion_sort_stat(my_list, order)
        return
    else:
        list_mid = len(my_list)//2
        list_B = my_list[:list_mid]
        list_C = my_list[list_mid:]
        hybrid_sort(list_B, order)
        hybrid_sort(list_C, order)
        merge_lists_stat(list_B, list_C, my_list, order)


def insertion_sort_stat(my_list, order):
    global swaps
    global compares
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
