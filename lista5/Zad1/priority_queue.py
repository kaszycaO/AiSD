from math import floor

class PriorityQueue:

    def __init__(self):
        self.data = []
        self.length = 0

    def parent(self, i):
        return floor(i /2)

    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2*i + 2

    def get_priority(self, i):
        return self.data[i][1]

    def get_value(self, i):
        return self.data[i][0]

    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def heapify(self, i):
        left = self.left(i)
        right = self.right(i)
        if (left < self.length and right < self.length):
            lowest = i
            if self.get_priority(left) < self.get_priority(lowest):
                lowest = left
            if self.get_priority(right) < self.get_priority(lowest):
                lowest = right
            if (lowest != i):
                self.swap(lowest, i)
                self.heapify(lowest)

    def insert(self, x, p):

        self.data.append((x, p))

        i = self.length
        while i > 0 and self.get_priority(self.parent(i)) > p:
            self.swap(i, self.parent(i))
            i = self.parent(i)

        self.length += 1

    def empty(self):
        if self.length == 0:
            return 1
        else:
            return 0

    def top(self):
        if self.length == 0:
            return ""
        else:
            return self.get_value(0)

    def pop(self):
        if self.length == 0:
            return ""
        else:
            best = self.top()
            self.data[0] = self.data[self.length - 1]
            self.data.pop(self.length - 1)
            self.length -= 1
            self.heapify(0)
            return best

    def decrease_key(self, i):
        temp = self.data[i]
        while i > 0 and self.data[self.parent(i)][1] > temp[1]:
            self.swap(i, self.parent(i))
            i = self.parent(i)
        self.data[i] = temp

    def priority(self, x, p):
        for i in range(self.length):
            if self.data[i][0] == x and self.data[i][1] > p:
                self.data[i] = (x, p)
                self.decrease_key(i)

    def my_print(self):
        print(self.data)
