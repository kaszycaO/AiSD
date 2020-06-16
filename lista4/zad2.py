#!/usr/bin/python3

from random import randint
import bst
import hmap
import rbt

import tools as t

def stat():
    with open('data/experiment.txt', 'r') as f:
        arg = f.read()
        arg = arg.split('\n')
    with open('data/with_dupl.txt', 'r') as f:
        arg_rep = f.read()
        arg_rep = arg_rep.split('\n')
    # "\n"
    arg.pop(-1)
    arg_rep.pop(-1)

    arg = arg[:900]
    arg_rep = arg_rep[:900]

    for n in range(100, 901, 100):
        words = arg.copy()
        words_rep = arg_rep.copy()

        for i in range(900 - n):
            words.pop(randint(0, (len(words)-1)))
            words_rep.pop(randint(0, len(words_rep)-1))


        root = bst.Node()
        rbt_root = rbt.RBT()
        hmap_root = hmap.HMAP_tree(n//4)

        for i in range(len(words)):
            bst.insert(root, words[i])
            rbt_root.insert(words[i])
            hmap_root.insert(words[i])

        min_val = bst.tree_min(root).value
        max_val = bst.tree_max(root).value

        random_val = words[randint(0, len(words))]

        t.compares = 0
        bst.find(root, min_val)
        min_c = t.compares

        t.compares = 0
        bst.find(root, max_val)
        max_c = t.compares

        t.compares = 0
        bst.find(root, random_val)
        random_c = t.compares
        
        # n, minimum, maximum, random
        with open('data/bst_limits.txt', 'a') as f:
            f.write('{};{};{};{}\n'.format(n, min_c, max_c, random_c))


        t.compares = 0
        rbt_root.find(min_val)
        min_c = t.compares

        t.compares = 0
        rbt_root.find(max_val)
        max_c = t.compares

        t.compares = 0
        rbt_root.find(random_val)
        random_c = t.compares

        with open('data/rbt_limits.txt', 'a') as f:
            f.write('{};{};{};{}\n'.format(n, min_c, max_c, random_c))

        t.compares = 0
        hmap_root.find(min_val)
        min_c = t.compares

        t.compares = 0
        hmap_root.find(max_val)
        max_c = t.compares

        t.compares = 0
        hmap_root.find(random_val)
        random_c = t.compares

        with open('data/hmap_limits.txt', 'a') as f:
            f.write('{};{};{};{}\n'.format(n, min_c, max_c, random_c))

        root = bst.Node()
        rbt_root = rbt.RBT()
        hmap_root = hmap.HMAP_tree(n//4)

        for i in range(len(words_rep)):
            bst.insert(root, words_rep[i])
            rbt_root.insert(words_rep[i])
            hmap_root.insert(words_rep[i])

        min_val = bst.tree_min(root).value
        max_val = bst.tree_max(root).value

        random_val = words[randint(0, len(words))]

        t.compares = 0
        bst.find(root, min_val)
        min_c = t.compares

        t.compares = 0
        bst.find(root, max_val)
        max_c = t.compares

        t.compares = 0
        bst.find(root, random_val)
        random_c = t.compares

        with open('data/bst_limits.txt', 'a') as f:
            f.write('{};{};{};{}\n'.format(n, min_c, max_c, random_c))


        t.compares = 0
        rbt_root.find(min_val)
        min_c = t.compares

        t.compares = 0
        rbt_root.find(max_val)
        max_c = t.compares

        t.compares = 0
        rbt_root.find(random_val)
        random_c = t.compares

        with open('data/rbt_limits.txt', 'a') as f:
            f.write('{};{};{};{}\n'.format(n, min_c, max_c, random_c))

        t.compares = 0
        hmap_root.find(min_val)
        min_c = t.compares

        t.compares = 0
        hmap_root.find(max_val)
        max_c = t.compares

        t.compares = 0
        hmap_root.find(random_val)
        random_c = t.compares

        with open('data/hmap_limits.txt', 'a') as f:
            f.write('{};{};{};{}\n'.format(n, min_c, max_c, random_c))

def main():
    stat()

if __name__ == '__main__':
    main()
