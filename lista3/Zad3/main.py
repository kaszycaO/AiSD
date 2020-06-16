#!/usr/bin/env python3

import sys

import random

import time

import quick

import binary


def random_list(max):
    return list([random.randint(0, max*2) for i in range(max)])

def main():
    args = sys.argv
    result = -1
    my_time = 0

    if len(args) < 3:
        print("Not enough input arguments! Required: [len] [v]")
    elif len(args) > 3:
        print("Too many arguments!")
    else:
        if args[1] == "--stat":
            try:
                v = int(args[2])
            except ValueError:
                print("Arguments must be integers!")
                return

            for i in range(1000, 100001, 1000):
                for j in range(5):
                    binary.compares = 0
                    my_list = random_list(i)
                    quick.quick_sort(my_list, 0, len(my_list) - 1)

                    t1_start = time.process_time()
                    result = binary.search(my_list, v)
                    t1_stop = time.process_time()
                    my_time = round(t1_stop - t1_start, 8)
                    print(result)
                    if result == 0:
                        print("{} is not an element of array".format(v))
                    else:
                        print("{} is an element of array".format(v))


                    info = str(i) + ';'
                    info += str(binary.compares) + ';'
                    info += str(my_time) + ';'
                    info += str(result) + ';'
                    info += ('\n')
                    with open("binary_stats.txt",'a+') as f:
                        f.write(info)

        else:
            try:
                n = int(args[1])
                v = int(args[2])
            except ValueError:
                print("Arguments must be integers!")
                return

            print("Elements of list: ")
            my_list = input().split()
            my_list = [int(my_list[i]) for i in range(len(my_list))]
            if len(my_list) != n:
                print("Incorrect length! ")

            else:
                if n > 0:
                    print("Array: ", my_list)
                    t1_start = time.process_time()
                    result = binary.search(my_list, v)
                    t1_stop = time.process_time()
                    my_time = round(t1_stop - t1_start, 8)
                    print(result)
                    if result == 0:
                        print("{} is not an element of array".format(v))
                    else:
                        print("{} is an element of array".format(v))
                    print("Time: ", my_time)
                    print("Compares: ", binary.compares)

                else:
                    print("Invalid size of the array!")



if __name__ == "__main__":
    main()
