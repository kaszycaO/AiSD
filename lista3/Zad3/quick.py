
def quick_sort(my_list, low, high):
    """Function doing quick sort
    low -> first element
    high -> last element
    order -> ASC or DESC
    """
    if low < high:
        # divide & conquer
        part = partition(my_list, low, high)

        quick_sort(my_list, low, part - 1)
        quick_sort(my_list, part + 1, high)

def partition(my_list, low, high):

    pivot = my_list[high]
    i = low - 1

    for j in range(low, high):
        if my_list[j] < pivot:
            i += 1
            if i != j:
                swap_elements(my_list, i, j)

    swap_elements(my_list, i + 1, high)

    return i + 1


def swap_elements(my_list, index_A, index_B):
    temp = my_list[index_A]
    my_list[index_A] = my_list[index_B]
    my_list[index_B] = temp
