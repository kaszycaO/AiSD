#!/usr/bin/env python3
import time
from random import randint
import sys

import bst
import hmap
import rbt
import tools as t


def get_results(n):
    results = []
    counter = 0
    with open("data/experiment.txt", 'r') as f:
        for line in f:
            for word in line.split():
                if counter == n:
                    break
                word = t.make_cut(word)
                results.append(word)
                counter += 1
    return results[:900]


#------------------------------INFO-------------------------------------------#

# n; load; insert; delete; find; max; min; successor; inorder

def rbt_experiment(n, type='t'):
    tree = rbt.RBT()
    experiment_data = "{};".format(n)

    clk_start = time.time()
    results = get_results(n)
    for el in results:
        tree.insert(el)
    experiment_data += str(time.time()-clk_start)
    experiment_data += ';'

    clk_start = time.time()
    tree.insert("adelaida")
    experiment_data += str(time.time()-clk_start)
    experiment_data += ';'

    index = randint(0, len(results) - 1)
    clk_start = time.time()
    tree.delete(results[index])
    experiment_data += str(time.time()-clk_start)
    experiment_data += ';'

    index = randint(0, len(results) - 1)
    clk_start = time.time()
    tree.find(results[index])
    experiment_data += str(time.time()-clk_start)
    experiment_data += ';'

    clk_start = time.time()
    tree.tree_max(tree.root)
    experiment_data += str(time.time()-clk_start)
    experiment_data += ';'

    clk_start = time.time()
    tree.tree_min(tree.root)
    experiment_data += str(time.time()-clk_start)
    experiment_data += ';'

    index = randint(0, len(results) - 1)
    clk_start = time.time()
    tree.successor(results[index])
    experiment_data += str(time.time()-clk_start)
    experiment_data += ';'

    clk_start = time.time()
    tree.inorder_stat(tree.root)
    experiment_data += str(time.time()-clk_start)
    experiment_data += '\n'

    return experiment_data

def bst_experiment(n, type='t'):
    root = bst.Node()

    experiment_data = "{};".format(n)

    clk_start = time.time()
    results = get_results(n)
    for el in results:
        bst.insert(root, el)
    experiment_data += str(time.time()-clk_start)
    experiment_data += ';'

    clk_start = time.time()
    bst.insert(root, "adelaida")
    experiment_data += str(time.time()-clk_start)
    experiment_data += ';'

    index = randint(0, len(results) - 1)
    clk_start = time.time()
    _, root = bst.delete(root, results[index])
    experiment_data += str(time.time()-clk_start)
    experiment_data += ';'

    index = randint(0, len(results) - 1)
    clk_start = time.time()
    bst.find(root, results[index])
    experiment_data += str(time.time()-clk_start)
    experiment_data += ';'

    clk_start = time.time()
    bst.tree_max(root)
    experiment_data += str(time.time()-clk_start)
    experiment_data += ';'

    clk_start = time.time()
    bst.tree_min(root)
    experiment_data += str(time.time()-clk_start)
    experiment_data += ';'

    index = randint(0, len(results) - 1)
    clk_start = time.time()
    bst.successor(root, results[index])
    experiment_data += str(time.time()-clk_start)
    experiment_data += ';'


    clk_start = time.time()
    bst.inorder_stat(root)
    experiment_data += str(time.time()-clk_start)
    experiment_data += '\n'

    return experiment_data

def hmap_experiment(n, type='t'):

    tree = hmap.HMAP_tree(n//2)
    experiment_data = "{};".format(n)

    clk_start = time.time()
    results = get_results(n)
    for el in results:
        tree.insert(el)
    experiment_data += str(time.time()-clk_start)
    experiment_data += ';'

    clk_start = time.time()
    tree.insert("adelaida")
    experiment_data += str(time.time()-clk_start)
    experiment_data += ';'

    index = randint(0, len(results) - 1)
    clk_start = time.time()
    tree.delete(results[index])
    experiment_data += str(time.time()-clk_start)
    experiment_data += ';'

    index = randint(0, len(results) - 1)
    clk_start = time.time()
    tree.find(results[index])
    experiment_data += str(time.time()-clk_start)
    experiment_data += '\n'

    return experiment_data

def save_results(result, filename):
    with open(filename, 'a') as f:
        f.write(result)

def main():
    args = sys.argv
    if len(args) == 2:
        try:
            n = int(args[1].strip())
        except ValueError:
            print("That's not an integer! ")
            return


        for i in range(100, 1001, 100):
            for _ in range(n):
                rbt_results = rbt_experiment(i)
                bst_results = bst_experiment(i)
                hmap_results = hmap_experiment(i)

                save_results(rbt_results, "data/rbt.txt")
                save_results(bst_results, "data/bst.txt")
                save_results(hmap_results, "data/hmap.txt")
    else:
        print("Arguments needed!")

if __name__ == "__main__":
    main()
