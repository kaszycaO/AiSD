compares = 0
swaps = 0

def reset_counters():
    global compares
    global swaps
    swaps = 0
    compares = 0


def my_select(my_list, element):
    copy = my_list.copy()
    result = do_select(my_list, element)
    index = my_list.index(result)
    my_list[index] = [my_list[index]]


def do_select(my_list, element):
    global compares

    groups = divide(my_list)
    medians = list([get_median(group) for group in groups])

    if len(medians) <= 5:
        pivot =  get_median(medians)
    else:
        pivot =  do_select(medians, len(medians)//2)

    print("Chosen pivot: ", pivot)
    pivot_index = partition(my_list, 0, len(my_list)-1, pivot)
    print("Index of chosen pivot: ", pivot)

    print("Compare: ", element, pivot_index+1)
    # +1 wynika z roznicy w indeksowaniu
    if element < pivot_index+1:
        return do_select(my_list[:pivot_index], element)
    elif element > pivot_index+1:
        return do_select(my_list[pivot_index+1:], element-pivot_index-1)
    else:
        return pivot

def divide(my_list):
    helper = []
    result = []
    for i in range(0, len(my_list)):
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


def partition(my_list, low, high, pivot):
    global compares
    if low == high:
        return 0

    my_index = my_list.index(pivot)
    swap_elements(my_list, low, my_index)
    i = low
    j = high + 1
    counter = 0
    while True:
        j -= 1
        print("Compare: ", my_list[j], pivot)
        compares += 1
        while my_list[j]>pivot:

            j -= 1
        i += 1
        while my_list[i]<pivot:
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
            print("Compare: ", key, my_list[i])
            compares += 1
            print("{} swap {}".format(my_list[i], key))
            swaps += 1
            i -= 1
            my_list[i+1] = key

        print("Compare: ", key, my_list[i])
        compares += 1


def swap_elements(my_list, index_A, index_B):
    global swaps
    print("{} swap {}".format(my_list[index_A], my_list[index_B]))
    swaps += 1
    temp = my_list[index_A]
    my_list[index_A] = my_list[index_B]
    my_list[index_B] = temp
    print(my_list)
