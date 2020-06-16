#!/usr/bin/env python
""" Zadanie pierwsze """

import sys

import time

import insertion

import merge

import quick

import random

import dual_pivot

import hybrid


def get_data(argv_list):

    data = []
    length = len(argv_list)
    if length < 5:
        print("Not enough arguments, --type and --comp are required!")
        data = [-1]
    elif length > 8:
        print("Too many arguments!")
        data = [-1]
    else:
        if argv_list[1] == ("--type"):
            if (argv_list[2] == "insert" or argv_list[2] == "merge" or
               argv_list[2] == "quick" or argv_list[2] == "dual_pivot" or
               argv_list[2] == "hybrid"):
               data.append(argv_list[2])
            else:
                print("There is no such algoritm! Use insert, merge, dual_pivot,hybrid or quick")
                data = [-1]
        else:
            print("Invalid argument, --type required!")
            data = [-1]

        if argv_list[3] == ("--comp"):
            if argv_list[4] == ">=":
                data.append("DESC")
            elif argv_list[4] == "<=":
                data.append("ASC")
            else:
                print("Not correct order! Use '>=' or '<=' ")
                data = [-1]
        else:
            print("Invalid argument, --comp required!")

        if length > 5 and argv_list[5] == ("--stat"):
            try:
                data.append(argv_list[6])
                data.append(argv_list[7])
            except IndexError:
                print("Not enough arguments, --stat 'file' 'repeat' !")
                data = [-1]

    return data

def sorted_info(basic_list, sorted_list):
    elements = 0
    for i in range(len(sorted_list)):
        if basic_list[i] != sorted_list[i]:
            elements += 1
    print("Sorted elements: ",elements)


def check_order(sorted_list, order):

    for i in range(len(sorted_list) - 1):
        if order == "ASC":
            if sorted_list[i] > sorted_list[i+1]:
                return False
        elif order == "DESC":
            if sorted_list[i] < sorted_list[i+1]:
                return False
    return True



def excec_program(list, args, file):
    list_dup = list.copy()
    swaps = 0
    compares = 0
    my_time = 0

    if args[0] == "insert":
        if file:
            t1_start = time.process_time()
            insertion.insertion_sort_stat(list, args[1])
            t1_stop = time.process_time()
        else:
            t1_start = time.process_time()
            insertion.insertion_sort(list, args[1])
            t1_stop = time.process_time()
        swaps = insertion.swaps
        compares = insertion.compares
        my_time = round(t1_stop - t1_start, 8)


    elif args[0] == "merge":
        merge.reset_counters()
        if file:
            t1_start = time.process_time()
            merge.merge_sort_stat(list, args[1])
            t1_stop = time.process_time()
        else:
            t1_start = time.process_time()
            merge.merge_sort(list, args[1])
            t1_stop = time.process_time()
        swaps = merge.swaps
        compares = merge.compares
        my_time = round(t1_stop - t1_start, 8)


    elif args[0] == "quick":
        quick.reset_counters()
        if file:
            t1_start = time.process_time()
            quick.quick_sort_stat(list, 0, len(list) - 1, args[1])
            t1_stop = time.process_time()
        else:
            t1_start = time.process_time()
            quick.quick_sort(list, 0, len(list) - 1, args[1])
            t1_stop = time.process_time()
        swaps = quick.swaps
        compares = quick.compares
        my_time = round(t1_stop - t1_start, 8)

    elif args[0] == "dual_pivot":
        dual_pivot.reset_counters()
        if file:
            t1_start = time.process_time()
            dual_pivot.dual_sort_stat(list, 0, len(list) - 1, args[1])
            t1_stop = time.process_time()
            # print(list)
        else:
            t1_start = time.process_time()
            dual_pivot.dual_sort(list, 0, len(list) - 1, args[1])
            t1_stop = time.process_time()
        swaps = dual_pivot.swaps
        compares = dual_pivot.compares
        my_time = round(t1_stop - t1_start, 8)

    elif args[0] == "hybrid":
        hybrid.reset_counters()
        if file:
            t1_start = time.process_time()
            hybrid.hybrid_sort(list, args[1])
            t1_stop = time.process_time()
        else:
            t1_start = time.process_time()
            hybrid.hybrid_sort(list, args[1])
            t1_stop = time.process_time()
        swaps = hybrid.swaps
        compares = hybrid.compares
        my_time = round(t1_stop - t1_start, 8)

    if file:
        info = str(len(list)) + ';'
        info += str(swaps) + ';'
        info += str(compares) + ';'
        info += str(my_time) + ';'
        info += ('\n')
        try:
            file_name = args[2]
            with open(file_name,'a+') as f:
                f.write(info)
        except FileNotFoundError:
            print("Creating new file ...")
            with open(file_name,'a+') as f:
                f.write(info)
    else:
        print("-----------------")
        print("Time: %.10f" % (t1_stop - t1_start))
        print("Swaps: ", swaps)
        print("Compares: ", compares)
        sorted_info(list_dup, list)
        if check_order:
            print(list)
        else:
            print("Something went wrong :( )")

def get_random_list(size):
    return random.sample(range(0, size*10), size)


def main():
    file = False
    args = get_data(sys.argv)
    print("-------------------")
    if args[0] != -1:
        if len(args) > 2:
            file = True
            repeats = 0
            try:
                repeats = int(args[3])
            except ValueError:
                print("Parameter k is not an integer!")
                return
            for i in range(100, 10000, 100):
                for j in range(int(args[3])):
                    list = get_random_list(i)
                    list_dup = list.copy()
                    excec_program(list_dup, args, file)


        else:
            list = []
            type = input("List type (int, string, float): ").strip()
            print("Elements of list: ")
            list = input().split()
            try:
                if type == "int":
                    for i in range(0, len(list)):
                        list[i] = int(list[i])
                elif type == "float":
                    for i in range(0, len(list)):
                        list[i] = float(list[i])
                elif type == "string":
                    pass
                else:
                    print("Invalid type!")
                    return
            except ValueError:
                print("That's not correct value!")
                return
            
            excec_program(list, args, file)


if __name__ == "__main__":
    main()
