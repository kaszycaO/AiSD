#!/usr/bin/env python3

import sys

import time

import randSelect

import myselect

import random

import numpy as np

import math

def random_values(max):
    return random.sample(range(0, max*10), max)

def random_permutation(length):
    return list(np.random.permutation(length)+1)

def deviation(my_list):
    avg = np.average(my_list)
    result = 0
    helper = 0
    for el in my_list:
        helper += (el - avg)**2

    res = []
    res.append(math.sqrt(helper/len(my_list)))
    res.append(avg)
    return res

def main():
    stats = False
    copy_1 = []
    copy_2 = []
    time_1 = 0
    time_2 = 0
    args = sys.argv
    if len(args) == 3:
        if args[2] == "--stat":
            stats = True
    if len(args) < 2:
        print("Arguments are required! Use '-r' or '-p' ")
        return
    elif len(args) > 3:
        print("Too many arguments!")
    else:
        data = args[1]
        first = input("Podaj n: ").strip()
        second = input("Podaj k: ").strip()
        print("---------------------------------------------------------------")
        try:
            n = int(first)
            k = int(second)
        except ValueError:
            print("That's not correct parameter!")
            return

        if k < 1 or k > n:
            print("k not in: < 1, n >")
        else:
            if stats:
                #to select
                compares = []
                swaps = []
                #to random
                compare = []
                swap = []
                for i in range(10):
                    if data == '-r':
                        randSelect.reset_counters()
                        myselect.reset_counters()
                        arguments = random_values(n)
                        copy_1 = arguments.copy()
                        copy_2 = arguments.copy()
                        randSelect.randomized_stat(copy_1, 0, len(copy_1) - 1, k)
                        myselect.my_select_stat(copy_2, k)


                    elif data == '-p':
                        randSelect.reset_counters()
                        myselect.reset_counters()
                        arguments = random_permutation(n)
                        copy_1 = arguments.copy()
                        copy_2 = arguments.copy()

                        randSelect.randomized_stat(copy_1, 0, len(copy_1) - 1, k)
                        myselect.my_select_stat(copy_2, k)



                    swaps.append(myselect.swaps)
                    compares.append(myselect.compares)

                    swap.append(randSelect.swaps)
                    compare.append(randSelect.compares)


                    info = str(n) + ';'
                    info += str(randSelect.compares) + ';'
                    info += str(randSelect.swaps) + ';'
                    info += ('\n')
                    with open("random.txt",'a+') as f:
                        f.write(info)
                    info = ""
                    info = str(n) + ';'
                    info += str(myselect.compares) + ';'
                    info += str(myselect.swaps) + ';'
                    info += ('\n')
                    with open("select.txt",'a+') as f:
                        f.write(info)


                s_odch = deviation(swaps)
                c_odch = deviation(compares)


                info = "Odchylenie swap: " + str(s_odch[0]) + " Srednia swap: " + str(s_odch[1])
                info += '\n'
                info += "Odchylenie comp: " + str(c_odch[0]) + " Srednia comp: " + str(c_odch[1])
                info += ('\n')
                info += "Max comp: " + str(max(compares)) + " Min comp: " + str(min(compares))
                info += ('\n')
                with open("select.txt",'a+') as f:
                    f.write(info)

                s_odch_2 = deviation(swap)
                c_odch_2 = deviation(compare)
                info = "Odchylenie swap: " + str(s_odch_2[0]) + " Srednia swap: " + str(s_odch_2[1])
                info += '\n'
                info += "Odchylenie comp: " + str(c_odch_2[0]) + " Srednia comp: " + str(c_odch_2[1])
                info += ('\n')
                info += "Max comp: " + str(max(compare)) + " Min comp: " + str(min(compare))
                info += ('\n')
                with open("random.txt",'a+') as f:
                    f.write(info)

            else:

                if data == '-r':
                    randSelect.reset_counters()
                    myselect.reset_counters()
                    arguments = random_values(n)
                    copy_1 = arguments.copy()
                    copy_2 = arguments.copy()
                    print("-RANDOMIZED SELECT-")
                    print("")
                    print("Starting list: ", arguments)
                    randSelect.randomized(copy_1, 0, len(copy_1) - 1, k)
                    print("")
                    print("-SELECT-")
                    print("Starting list: ", copy_2)
                    myselect.my_select(copy_2, k)


                elif data == '-p':
                    randSelect.reset_counters()
                    myselect.reset_counters()
                    arguments = random_permutation(n)
                    copy_1 = arguments.copy()
                    copy_2 = arguments.copy()
                    print("-RANDOMIZED SELECT-")
                    print("")
                    print("Starting list: ", arguments)
                    randSelect.randomized(copy_1, 0, len(copy_1) - 1, k)

                    print("")
                    print("-SELECT-")
                    print("Starting list: ", copy_2)
                    myselect.my_select(copy_2, k)


                print("")
                print("-------------------------RESULTS-------------------------------")
                print("-RANDOMIZED SELECT-")
                print(copy_1)
                print("Total compares: ", randSelect.compares)
                print("Total swaps: ", randSelect.swaps)
                print("---------------------------------------------------------------")
                print("-SELECT-")
                print(copy_2)
                print("Total compares: ", myselect.compares)
                print("Total swaps: ", myselect.swaps)


if __name__ == "__main__":
    main()
