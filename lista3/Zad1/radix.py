swaps = 0

def reset_counters():
    global swaps
    swaps = 0

def radix_sort(my_list, order):
    divider = 1
    max_val = max(my_list)
    while max_val//divider > 0:
        counting_sort(my_list, divider, order)
        divider*=10


def counting_sort(my_list, divider, order):
    global swaps
    #badamy kazdy przypadek 10^i
    max_num = 10
    helper = [0 for i in range(max_num)]
    result = [0 for i in range(len(my_list))]

    if order == "ASC":
        for j in range(0, len(my_list)):
            index = (my_list[j]//divider)%10
            helper[index] = helper[index] + 1

        for i in range(1, max_num):
            helper[i] = helper[i] + helper[i-1]

        for j in range(len(my_list)-1, -1, -1):
            index = (my_list[j]//divider)%10
            result[helper[index] -1] = my_list[j]
            swaps+=1
            helper[index] = helper[index] - 1


    elif order == "DESC":
        for j in range(0, len(my_list)):
            index = my_list[j]//divider%10
            helper[index] = helper[index] + 1

        for i in range(max_num - 2, -1, -1):
            helper[i] = helper[i] + helper[i+1]


        for j in range(len(my_list)-1, -1, -1):
            index = (my_list[j]//divider)%10
            result[helper[index] -1] = my_list[j]
            swaps+=1
            helper[index] = helper[index] - 1


    for i in range(len(result)):
        my_list[i] = result[i]


def max_modulo(my_list, divider):
    result = -1
    for i in range(len(my_list)):
        index = my_list[i]//divider
        if result < index%10:
            result = index%10
    return result
