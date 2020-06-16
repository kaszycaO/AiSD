RED = "red"
BLACK = "black"

import tools as t

class Node:
    def __init__(self, value):
        self.value = value
        self.right = self
        self.left = self
        self.parent = self
        self.color = RED

class RBT:
    def __init__(self):
        self.nil = Node(None)
        self.root = self.nil
        self.nil.left = self.nil
        self.nil.right = self.nil
        self.nil.parent = self.nil
        self.nil.color = BLACK

    def left_rotate(self, node):
        t.rotate += 1
        y = node.right
        node.right = y.left
        if y.left != self.nil:
            y.left.parent = node
        y.parent = node.parent
        if node.parent == self.nil:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        y.left = node
        node.parent = y

    def right_rotate(self, node):
        t.rotate += 1
        y = node.left
        node.left = y.right
        if y.right != self.nil:
            y.right.parent = node
        y.parent = node.parent
        if node.parent == self.nil:
            self.root = y
        elif node == node.parent.right:
            node.parent.right = y
        else:
            node.parent.left = y
        y.right = node
        node.parent = y

    def insert(self, element):
        t.insert += 1
        t.add_element(1)
        node = Node(element)
        node.parent = self.nil
        node.left = self.nil
        node.right = self.nil

        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if node.value < x.value:
                x = x.left
            else:
                x = x.right
        node.parent = y

        if y == self.nil:
            self.root = node
        elif node.value < y.value:
            y.left = node
        else:
            y.right = node

        node.left = self.nil
        node.right = self.nil
        node.color = RED
        self.insert_fixup(node)

    def insert_fixup(self, node):
        while node.parent.color == RED:
            if node.parent == node.parent.parent.left:
                y = node.parent.parent.right
                if y.color == RED:
                    node.parent.color = BLACK
                    y.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.right_rotate(node.parent.parent)
            else:
                y = node.parent.parent.left
                if y.color == RED:
                    node.parent.color = BLACK
                    y.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.left_rotate(node.parent.parent)

        self.root.parent = self.nil
        self.root.color = BLACK

    def transplant(self, node_A, node_B):
        if node_A.parent == self.nil:
            self.root = node_B
        elif node_A == node_A.parent.left:
            node_A.parent.left = node_B
        else:
            node_A.parent.right = node_B
        node_B.parent = node_A.parent

    def load(self, file):
        t.load += 1
        try:
            with open(file, "r") as f:
                for line in f:
                    for word in line.split():
                        word = t.make_cut(word)
                        self.insert(word)
            return self

        except FileNotFoundError:
            sys.stderr.write("File not found\n")
            return 0

    def tree_min(self, root):
        t.minimum += 1
        if self.root != self.nil:
            current = root
            while current.left != self.nil:
                current = current.left
            return current

        return None

    def tree_max(self, root):
        t.maximum += 1
        if self.root != self.nil:
            current = root
            while current.right != self.nil:
                current = current.right
            return current

        return None

    def delete(self, element):
        t.delete += 1
        _, node = self.find(element)
        if node != self.nil:
            if node.left == self.nil or node.right == self.nil:
                n = node
            else:
                n = self.successor(element)

            if n.left != self.nil:
                m = n.left
            else:
                m = n.right

            m.parent = n.parent

            if (n.parent == self.nil):
                self.root = m
            elif (n == n.parent.left):
                n.parent.left = m
            else:
                n.parent.right = m

            if n != node:
                node.value = n.value

            if n.color == BLACK:
                self.delete_fixup(m)
            t.add_element(-1)
            return 1

        else:
            return 0

    def delete_fixup(self, node):
        while node != self.root and node.color == BLACK:
            if node == node.parent.left:
                m = node.parent.right

                if m.color == RED:
                    m.color = BLACK
                    node.parent.color = RED
                    self.left_rotate (node.parent)
                    m = node.parent.right


                if m.left.color == BLACK and m.right.color == BLACK:
                    m.color = RED
                    node = node.parent
                else:
                    if m.right.color == BLACK:
                        m.left.color = BLACK
                        m.color = RED
                        self.right_rotate(m)
                        m = node.parent.right

                    m.color = node.parent.color
                    node.parent.color = BLACK
                    m.right.color = BLACK
                    self.left_rotate (node.parent)
                    node = self.root

            else:
                m = node.parent.left

                if m.color == RED:
                    m.color = BLACK
                    node.parent.color = RED
                    self.right_rotate(node.parent)
                    m = node.parent.left


                if m.right.color == BLACK and m.left.color == BLACK:
                    m.color = RED
                    node = node.parent
                else:
                    if m.left.color == BLACK:
                        m.right.color = BLACK
                        m.color = RED
                        self.left_rotate (m)
                        m = node.parent.left


                    m.color = node.parent.color
                    node.parent.color = BLACK
                    m.left.color = BLACK
                    self.right_rotate (node.parent)
                    node = self.root

        node.color = BLACK

    def successor(self, element):
        t.successor += 1
        _, node = self.find(element)
        if node != self.nil:
            if node.right != self.nil:
                return self.tree_min(node.right)

            helper = node.parent
            while helper != self.nil and node == helper.right:
                node = helper
                helper = helper.parent

            if helper != self.nil:
                return helper
        else:
            return None

    def inorder(self, node):
        t.inorder += 1
        if node != self.nil:
            self.inorder(node.left)
            print(node.value, end=' ')
            self.inorder(node.right)

    def inorder_stat(self, node):
        t.inorder += 1
        if node != self.nil:
            self.inorder_stat(node.left)
            self.inorder_stat(node.right)

    def find(self, element):
        t.find += 1
        current = self.root
        while current != self.nil:
            t.compares += 1
            if current.value == element:
                return 1, current

            t.compares += 1
            if current.value < element:
                current = current.right
            else:
                current = current.left

        return 0, self.nil
