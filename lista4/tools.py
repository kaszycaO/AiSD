rotate = 0
insert = 0
load = 0
delete = 0
successor = 0
inorder = 0
find = 0
minimum = 0
maximum = 0

compares = 0

max_elements = 0
elements = 0

def init_stats():
    global rotate
    global insert
    global load
    global delete
    global successor
    global inorder
    global find
    global minimum
    global maximum
    global max_elements
    global elements
    global compares

    rotate = 0
    insert = 0
    load = 0
    delete = 0
    successor = 0
    inorder = 0
    find = 0
    minimum = 0
    maximum = 0
    max_elements = 0
    elements = 0

def get_stats():
    global rotate
    global insert
    global load
    global delete
    global successor
    global inorder
    global find
    global minimum
    global maximum
    global max_elements
    global elements


    results = []
    results.append(rotate)
    results.append(insert)
    results.append(load)
    results.append(successor)
    results.append(inorder)
    results.append(find)
    results.append(minimum)
    results.append(maximum)
    results.append(max_elements)
    results.append(elements)

    return results

def add_element(val):
    global elements
    global max_elements

    elements += val
    if elements > max_elements:
        max_elements = elements


def make_cut(word):
    try:
        int(word)
    except:
        if ord(word[0]) < 65 or ord(word[0]) > 122:
            word = word[1:]

        if ord(word[-1]) < 65 or ord(word[-1]) > 122:
            word = word[:-1]

        return word
    return -1
