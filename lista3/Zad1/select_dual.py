#!/usr/bin/python

swaps = 0
compares = 0
helper = []

def reset_counters():
    global compares
    global swaps
    swaps = 0
    compares = 0

def dual_sort(my_list, low, high, order):
    if high - low < 13:
        insertion_sort_new(my_list, low, high, order)
        return

    if low < high:
        # podobne do mediany median ale dzielone przez 3
        # szukamy 2 pivotow
        median_a = do_select(my_list, low, high, 1)
        median_b = do_select(my_list, low, high, 2)

        pivots = prepare_pivots(my_list, low, high, median_a, median_b, order)

        dual_sort(my_list, low, pivots[0], order)
        dual_sort(my_list, pivots[0] + 1, pivots[1], order)
        dual_sort(my_list, pivots[1] + 1, high, order)

def insertion_sort_new(my_list, low, high, order):
    global compares
    for i in range(low, high + 1):
        for j in range(i - 1, low - 1, -1):
            compares += 1
            if order == "ASC":
                if my_list[j] > my_list[j+1]:
                    swap_elements(my_list, j, j+1)
                else:
                    break
            elif order == "DESC":
                if my_list[j] < my_list[j+1]:
                    swap_elements(my_list, j, j+1)
                else:
                    break

def partition(my_list, low, high, order):
    global swaps, compares
    pivots = []
    l_pivot = my_list[low]
    r_pivot = my_list[high]
    diff = 0 # difference between small and large elemet
    index_L = low + 1
    index_R  = high - 1
    j = index_L
    if order == "ASC":
        while j <= index_R :
            if diff > 0:
                compares+=1
                if my_list[j] < l_pivot:
                    swap_elements(my_list, index_L, j)
                    index_L += 1
                    j += 1
                    diff += 1
                else:
                    compares+=1
                    if my_list[j] < r_pivot:
                        j += 1
                    else:
                        swap_elements(my_list, j, index_R)
                        index_R -= 1
                        diff -= 1
            else:
                compares+=1
                while my_list[index_R] > r_pivot:
                    index_R -= 1
                    diff -= 1
                if j <= index_R:
                    compares+=1
                    if my_list[index_R] < l_pivot:
                        temp = my_list[index_L]
                        my_list[index_L] = my_list[index_R]
                        my_list[index_R] = my_list[j]
                        my_list[j] = temp
                        swaps += 3
                        index_L += 1
                        diff += 1
                    else:
                        swap_elements(my_list, j, index_R)
                    j += 1
    elif order == "DESC":
        while j <= index_R:
            if diff > 0:
                compares+=1
                if my_list[j] > l_pivot:
                    swap_elements(my_list, index_L, j)
                    index_L += 1
                    j += 1
                    diff += 1
                else:
                    compares+=1
                    if my_list[j] > r_pivot:
                        j += 1
                    else:
                        swap_elements(my_list, j, index_R)
                        index_R -= 1
                        diff -= 1
            else:
                compares+=1
                while my_list[index_R] < r_pivot:
                    index_R -= 1
                    diff -= 1
                if j <= index_R:
                    compares+=1
                    if my_list[index_R] > l_pivot:
                        temp = my_list[index_L]
                        my_list[index_L] = my_list[index_R]
                        my_list[index_R] = my_list[j]
                        my_list[j] = temp
                        swaps += 3
                        index_L += 1
                        diff += 1
                    else:
                        swap_elements(my_list, j, index_R)
                    j += 1
    swap_elements(my_list, low, index_L - 1)
    swap_elements(my_list, high, index_R + 1)

    pivots.append(index_L-1)
    pivots.append(index_R+1)
    return pivots

def prepare_pivots(my_list, low, high, pivot_a, pivot_b, order):
    index_a = my_list.index(pivot_a)
    index_b = my_list.index(pivot_b)
    # zamiana nowo wybranych pivotow z najnizszym i najwyzszym indeksem
    swap_elements(my_list, low, index_a)
    swap_elements(my_list, high, index_b)
    return partition(my_list, low, high, order)

def do_select(my_list, low, high, type):
    """ Mediana median """
    groups = divide(my_list, low, high)
    if type == 1:
        medians = list([get_median_1(group) for group in groups])
        if len(medians) <= 5:
            return get_median_1(medians)
        else:
            return do_select(medians, 0, len(medians), type)

    elif type == 2:
        medians = list([get_median_2(group) for group in groups])
        if len(medians) <= 5:
            return get_median_2(medians)
        else:
            return do_select(medians, 0, len(medians), type)

def divide(my_list, low, high):
    helper = []
    result = []
    for i in range(low, high):
        helper.append(my_list[i])
        if len(helper) == 5:
            result.append(helper)
            helper = []

    if len(helper) > 0:
        result.append(helper)

    return result

def get_median_1(group):
    """ Element w 1/3 """
    insertion_sort_new(group, 0, len(group) - 1, "ASC")
    index = len(group)//3

    return group[index]

def get_median_2(group):
    """ Element w 2/3 """
    insertion_sort_new(group, 0, len(group) - 1, "ASC")
    index = 2*(len(group)//3)

    return group[index]

def swap_elements(my_list, index_A, index_B):
    global swaps
    swaps += 1
    temp = my_list[index_A]
    my_list[index_A] = my_list[index_B]
    my_list[index_B] = temp
