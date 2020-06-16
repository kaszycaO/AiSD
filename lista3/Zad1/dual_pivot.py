#!/usr/bin/python

swaps = 0
compares = 0
helper = []

def reset_counters():
    global compares
    global swaps
    swaps = 0
    compares = 0


def dual_sort_stat(my_list, low, high, order):
    if high - low < 13:
        insertion_sort_new_stat(my_list, low, high, order)
        return

    if low < high:
        pivots = partition_stat(my_list, low, high, order)
        dual_sort_stat(my_list, low, pivots[0], order)
        dual_sort_stat(my_list, pivots[0] + 1, pivots[1], order)
        dual_sort_stat(my_list, pivots[1] + 1, high, order)



def insertion_sort_new_stat(my_list, low, high, order):
    global compares
    for i in range(low, high + 1):
        for j in range(i - 1, low - 1, -1):
            compares += 1
            if order == "ASC":
                if my_list[j] > my_list[j+1]:
                    swap_elements_stat(my_list, j, j+1)
                else:
                    break
            elif order == "DESC":
                if my_list[j] < my_list[j+1]:
                    swap_elements_stat(my_list, j, j+1)
                else:
                    break

def partition_stat(my_list, low, high, order):
    """This partition has more compares"""
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
                    swap_elements_stat(my_list, index_L, j)
                    index_L += 1
                    j += 1
                    diff += 1
                else:
                    compares+=1
                    if my_list[j] < r_pivot:
                        j += 1
                    else:
                        swap_elements_stat(my_list, j, index_R)
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
                        swap_elements_stat(my_list, j, index_R)
                    j += 1
    elif order == "DESC":
        while j <= index_R:
            if diff > 0:
                compares+=1
                if my_list[j] > l_pivot:
                    swap_elements_stat(my_list, index_L, j)
                    index_L += 1
                    j += 1
                    diff += 1
                else:
                    compares+=1
                    if my_list[j] > r_pivot:
                        j += 1
                    else:
                        swap_elements_stat(my_list, j, index_R)
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
                        swap_elements_stat(my_list, j, index_R)
                    j += 1
    swap_elements_stat(my_list, low, index_L - 1)
    swap_elements_stat(my_list, high, index_R + 1)

    pivots.append(index_L-1)
    pivots.append(index_R+1)
    return pivots


def swap_elements_stat(my_list, index_A, index_B):
    """Same as swap_elements but without live comments"""
    global swaps
    swaps += 1
    temp = my_list[index_A]
    my_list[index_A] = my_list[index_B]
    my_list[index_B] = temp

def dual_sort(my_list, low, high, order):
    if high - low < 13:
        insertion_sort_new(my_list, low, high, order)
        return

    if low < high:
        pivots = partition(my_list, low, high, order)
        dual_sort(my_list, low, pivots[0], order)
        dual_sort(my_list, pivots[0] + 1, pivots[1], order)
        dual_sort(my_list, pivots[1] + 1, high, order)


def insertion_sort_new(my_list, low, high, order):
    global compares
    for i in range(low, high + 1):
        for j in range(i - 1, low - 1, -1):

            compares += 1
            if order == "ASC":
                print("Compare: ", my_list[j], my_list[j+1])
                if my_list[j] > my_list[j+1]:
                    swap_elements(my_list, j, j+1)
                else:
                    break
            elif order == "DESC":
                print("Compare: ", my_list[j], my_list[j+1])
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
                print("Compare: ", my_list[j], l_pivot)
                compares+=1
                if my_list[j] < l_pivot:
                    swap_elements_stat(my_list, index_L, j)
                    index_L += 1
                    j += 1
                    diff += 1
                else:
                    print("Compare: ", my_list[j], r_pivot)
                    compares+=1
                    if my_list[j] < r_pivot:
                        j += 1
                    else:
                        swap_elements_stat(my_list, j, index_R)
                        index_R -= 1
                        diff -= 1
            else:
                print("Compare: ", my_list[index_R] , r_pivot)
                compares+=1
                while my_list[index_R] > r_pivot:
                    index_R -= 1
                    diff -= 1
                if j <= index_R:
                    print("Compare: ", my_list[index_R], l_pivot)
                    compares+=1
                    if my_list[index_R] < l_pivot:
                        print("{} swap {}".format(my_list[i], my_list[k]))
                        print("{} swap {}".format(my_list[k], my_list[j]))
                        print("{} swap {}".format(my_list[j], my_list[i]))
                        temp = my_list[index_L]
                        my_list[index_L] = my_list[index_R]
                        my_list[index_R] = my_list[j]
                        my_list[j] = temp
                        swaps += 3
                        index_L += 1
                        diff += 1
                    else:
                        swap_elements_stat(my_list, j, index_R)
                    j += 1
    elif order == "DESC":
        while j <= index_R:
            if diff > 0:
                print("Compare: ", my_list[j], l_pivot)
                compares+=1
                if my_list[j] > l_pivot:
                    swap_elements_stat(my_list, index_L, j)
                    index_L += 1
                    j += 1
                    diff += 1
                else:
                    print("Compare: ", my_list[j], r_pivot)
                    compares+=1
                    if my_list[j] > r_pivot:
                        j += 1
                    else:
                        swap_elements_stat(my_list, j, index_R)
                        k -= 1
                        diff -= 1
            else:
                print("Compare: ", my_list[index_R], r_pivot)
                compares+=1
                while my_list[index_R] < r_pivot:
                    index_R -= 1
                    diff -= 1
                if j <= index_R:
                    print("Compare: ", my_list[index_R], l_pivot)
                    compares+=1
                    if my_list[index_R] > l_pivot:
                        print("{} swap {}".format(my_list[i], my_list[k]))
                        print("{} swap {}".format(my_list[k], my_list[j]))
                        print("{} swap {}".format(my_list[j], my_list[i]))
                        temp = my_list[i]
                        my_list[i] = my_list[index_R]
                        my_list[index_R] = my_list[j]
                        my_list[j] = temp
                        swaps += 3
                        index_L += 1
                        diff += 1
                    else:
                        swap_elements_stat(my_list, j, index_R)
                    j += 1
    swap_elements_stat(my_list, low, index_L - 1)
    swap_elements_stat(my_list, high, index_R + 1)

    pivots.append(index_L-1)
    pivots.append(index_R+1)
    return pivots


def swap_elements(my_list, index_A, index_B):
    global swaps
    print("{} swap {}".format(my_list[index_A], my_list[index_B]))
    swaps += 1
    temp = my_list[index_A]
    my_list[index_A] = my_list[index_B]
    my_list[index_B] = temp
