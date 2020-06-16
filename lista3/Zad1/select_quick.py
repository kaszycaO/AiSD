compares = 0
swaps = 0

def reset_counters():
    global compares
    global swaps
    swaps = 0
    compares = 0

def quick_sort(my_list, low, high, order):
    """Function doing quick sort
    low -> first element
    high -> last element
    order -> ASC or DESC
    """
    if low < high:
        # divide & conquer
        pivot = do_select(my_list, low, high)
        part = partition(my_list, low, high, pivot, order)

        quick_sort(my_list, low, part - 1, order)
        quick_sort(my_list, part + 1, high, order)

def do_select(my_list, low, high):
    groups = divide(my_list, low, high)
    medians = list([get_median(group) for group in groups])

    if len(medians) <= 5:
        pivot =  get_median(medians)
    else:
        pivot =  do_select(medians, 0, len(medians))

    return pivot

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

def get_median(group):
    insertion_sort(group)
    index = len(group)//2
    if len(group) % 2 == 0:
        return min(group[index], group[index - 1])
    else:
        return group[index]

def partition(my_list, low, high, pivot, order):
    global compares
    if low == high:
        return 0

    my_index = my_list.index(pivot)
    swap_elements(my_list, low, my_index)
    i = low
    j = high + 1
    counter = 0
    if order == "ASC":
        while True:
            j -= 1
            compares += 1
            while my_list[j]>pivot:
                j -= 1
            i += 1
            while i <= high and my_list[i] < pivot:
                i += 1
            if i < j:
                swap_elements(my_list, i, j)
            else:
                swap_elements(my_list, i - 1, low)
                return j
    elif order == "DESC":
        while True:
            j -= 1
            compares += 1
            while j >= low and my_list[j]<pivot:
                j -= 1
            i += 1
            while i <= high and my_list[i] > pivot:
                i += 1
            if i < j:
                swap_elements(my_list, i, j)
            else:
                swap_elements(my_list, i - 1, low)
                return j

def insertion_sort(my_list):
    global swaps
    global compares

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

def swap_elements(my_list, index_A, index_B):
    global swaps
    swaps += 1
    temp = my_list[index_A]
    my_list[index_A] = my_list[index_B]
    my_list[index_B] = temp
