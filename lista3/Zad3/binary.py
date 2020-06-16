compares = 0

def search(my_list, element):
    global compares
    n = len(my_list)

    if n > 0:
        mid = n//2
        #porownanie klucza z element oraz z mid
        compares += 2
        if element == my_list[mid]:
            return 1
        elif element != my_list[mid] and n == 1:
            return 0
        elif element < my_list[mid]:
            return search(my_list[:mid],  element)
        elif element > my_list[mid]:
            return search(my_list[mid + 1: ],  element)
    else:
        return 0
