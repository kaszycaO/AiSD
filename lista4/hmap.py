from math import floor

import rbt

import tools as t

class HMAP_tree(object):
    def __init__(self, m):
        self.store = [rbt.RBT() for _ in range(m)]
        self.m = m

    def hash(self, element):
        helper = 0
        for el in element:
            helper += ord(el)
        return floor(self.m*((helper*0.75)%1))

    def insert(self, element):
        index = self.hash(element)
        self.store[index].insert(element)

    def load(self, file):
        t.load += 1
        try:
            with open(file, "r") as f:
                self.store = [rbt.RBT() for _ in range(400)]
                self.m = 400
                for line in f:
                    for word in line.split():
                        word = t.make_cut(word)
                        self.insert(word)
            return 1

        except FileNotFoundError:
            sys.stderr.write("File not found\n")
            return 0

    def delete(self, element):
        index = self.hash(element)
        result = self.store[index].delete(element)
        if result != 0:
            return 1

        return 0

    def find(self, element):
        index = self.hash(element)
        result, element = self.store[index].find(element)

        if result != 0:
            return 1
        else:
            return 0
