import tools as t

class Node:
    def __init__(self):
        self.parent = None
        self.left = None
        self.right = None
        self.value = None


def insert(root, element):
    t.insert += 1
    if root.value is None:
        root.value = element
        t.add_element(1)
    else:
        if root.value < element:
            if root.right is None:
                node = Node()
                node.value = element
                root.right = node
                node.parent = root
                t.add_element(1)
            else:
                insert(root.right, element)
        else:
            if root.left is None:
                node = Node()
                node.value = element
                root.left = node
                node.parent = root
                t.add_element(1)
            else:
                insert(root.left, element)

def load(file):
    t.load += 1
    root = Node()
    try:
        with open(file, 'r') as f:
            for line in f:
                for word in line.split():
                    word = t.make_cut(word)
                    insert(root, word)

    except FileNotFoundError:
        sys.stderr.write("File not found\n")
        return 0

    return root

def transplant(root, node_A, node_B):

    if node_A.parent == None:
        root = node_B
        root.parent = None
        return root
    elif node_A == node_A.parent.left:
        node_A.parent.left = node_B
    else:
        node_A.parent.right = node_B

    if node_B != None:
        node_B.parent = node_A.parent

def delete(root, element):
    t.delete += 1
    _, node = find(root, element)
    if node is not None:
        if node.left == None:
            result = transplant(root, node, node.right)
            if result != None:
                root = result
        elif node.right == None:
            result = transplant(root, node, node.left)
            if result != None:
                root = result
        else:
            y = tree_min(node.right)
            if y.parent != node:
                result = transplant(root, y, y.right)
                if result != None:
                    root = result
                y.right = node.right
                y.right.parent = y

            result = transplant(root, node, y)
            if result != None:
                root = result

            y.left = node.left
            y.left.parent = y

    else:
        return 0, root

    t.add_element(-1)
    return 1, root

def find(root, element):
    t.find += 1
    current = root
    while current != None:
        t.compares += 1
        if current.value == element:
            return 1, current

        t.compares += 1
        if current.value < element:
            current = current.right
        else:
            current = current.left

    return 0, None

def tree_min(root):
    t.minimum += 1
    current = root
    while current.left != None:
        current = current.left

    return current

def tree_max(root):
    t.maximum += 1
    current = root
    while current.right != None:
        current = current.right

    return current

def successor(root, element):
    t.successor += 1
    _, node = find(root, element)
    if node is None:
        return 0
    else:
        if node.right != None:
            return tree_min(node.right).value
        else:
            y = node.parent
            while y != None and node == y.right:
                node = y
                y = y.parent

            if y is not None:
                return y.value
            else:
                return 0

def inorder(root):
    t.inorder += 1
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

def inorder_stat(root):
    t.inorder += 1
    if root:
        inorder_stat(root.left)
        inorder_stat(root.right)
