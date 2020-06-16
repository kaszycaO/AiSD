#!/usr/bin/env python3

import sys

import bst
import rbt
import hmap

import tools as t
import time

def get_input():
    data = sys.stdin.read()
    data = data.split("\n")
    length = data[0]
    data.pop(0)

    for i in range(len(data)):
        data[i] = data[i].split()

    return length, data

def print_results():
    result = t.get_stats()
    sys.stderr.write("\n")
    sys.stderr.write("Rotation: {} \n".format(result[0]))
    sys.stderr.write("Insertion: {} \n".format(result[1]))
    sys.stderr.write("Load: {} \n".format(result[2]))
    sys.stderr.write("Successor: {} \n".format(result[3]))
    sys.stderr.write("Inorder: {} \n".format(result[4]))
    sys.stderr.write("Find: {} \n".format(result[5]))
    sys.stderr.write("Minimum: {} \n".format(result[6]))
    sys.stderr.write("Maximum: {} \n".format(result[7]))
    sys.stderr.write("Maximum elements during excecution: {} \n".format(result[8]))
    sys.stderr.write("Elements at the end: {} \n".format(result[9]))

def main():

    option = sys.argv

    if len(option) > 2:
        if option[1] == '--type':
            commands_count, commands = get_input()
            try:
                commands_count = int(commands_count)
            except ValueError:
                sys.stderr.write("Number of operations must be an integer!\n")
                return

            type = option[2]
            t.init_stats()
            clk_start = time.time()
            if type == 'bst':
                root = bst.Node()
                for command in commands:
                    try:
                        if len(command) != 0:
                            if command[0] == 'insert':
                                element = t.make_cut(command[1])
                                if element != -1:
                                    bst.insert(root, element)
                                else:
                                    sys.stderr.write("Invalid symbol in {} \n".format(element))
                                    continue
                            elif command[0] == 'load':
                                loaded = bst.load("data/{}".format(command[1]))
                                if loaded != 0:
                                    root = loaded
                            elif command[0] == 'delete':
                                result, new_root = bst.delete(root, command[1])
                                while result == 1:
                                    result, new_root = bst.delete(root, command[1])
                                    root = new_root
                            elif command[0] == 'find':
                                result, _ = bst.find(root, command[1])
                                print(result)
                            elif command[0] == 'min':
                                node = bst.tree_min(root)
                                if node.value != None:
                                    print(node.value)
                                else:
                                    print()
                            elif command[0] == 'max':
                                node = bst.tree_max(root)
                                if node.value != None:
                                    print(node.value)
                                else:
                                    print()
                            elif command[0] == 'successor':
                                result = bst.successor(root, command[1])
                                if result != 0:
                                    print(result)
                                else:
                                    print()
                            elif command[0] == 'inorder':
                                bst.inorder(root)
                                print()
                            else:
                                sys.stderr.write("Invalid command in ", command, ("\n"))
                                continue

                    except IndexError:
                        sys.stderr.write("Invalid command parameters in ", command, ("\n"))
                        continue

            elif type == 'rbt':
                tree = rbt.RBT()
                for command in commands:
                    if len(command) != 0:
                        if command[0] == 'insert':
                            element = t.make_cut(command[1])
                            if element != -1:
                                tree.insert(command[1])
                            else:
                                sys.stderr.write("Invalid symbol in {} \n".format(element))
                                continue
                        elif command[0] == 'load':
                            tree = rbt.RBT()
                            tree = tree.load("data/{}".format(command[1]))
                        elif command[0] == 'delete':
                            result = tree.delete(command[1])
                            while result == 1:
                                result = tree.delete(command[1])
                        elif command[0] == 'find':
                            result, _ = tree.find(command[1])
                            print(result)
                        elif command[0] == 'min':
                            minimum = tree.tree_min(tree.root)
                            if minimum != None:
                                print(minimum.value)
                            else:
                                print()
                        elif command[0] == 'max':
                            maximum = tree.tree_max(tree.root)
                            if maximum != None:
                                print(maximum.value)
                            else:
                                print()
                        elif command[0] == 'successor':
                            result = tree.successor(command[1]).value
                            if result != None:
                                print(result)
                            else:
                                print()
                        elif command[0] == 'inorder':
                            tree.inorder(tree.root)
                            print()
                        else:
                            sys.stderr.write("Invalid symbol in {} \n".format(command))
                            continue

            elif type == 'hmap':
                tree = hmap.HMAP_tree(100)
                for command in commands:
                    if len(command) != 0:
                        if command[0] == 'insert':
                            element = t.make_cut(command[1])
                            if element != -1:
                                tree.insert(command[1])
                            else:
                                sys.stderr.write("Invalid symbol in {} \n".format(element))
                                continue

                        elif command[0] == 'load':
                            result = tree.load("data/{}".format(command[1]))
                        elif command[0] == 'delete':
                            result = tree.delete(command[1])
                            while result == 1:
                                result = tree.delete(command[1])
                        elif command[0] == 'find':
                            print(tree.find(command[1]))
                        elif command[0] == 'min':
                            print()
                        elif command[0] == 'max':
                            print()
                        elif command[0] == 'successor':
                            print()
                        elif command[0] == 'inorder':
                            print()
                        else:
                            sys.stderr.write("Invalid symbol in {} \n".format(command))
                            continue


            else:
                sys.stderr.write("Invalid structure! Available: bst, rbt or hmap!\n")

            sys.stderr.write("\n")
            sys.stderr.write("Total time of excecution {}\n".format(time.time()-clk_start))
            print_results()

        else:
            sys.stderr.write("Invalid argument! Use --type !\n")
    else:
        sys.stderr.write("Not enough arguments! \n")



if __name__ == "__main__":
    main()
