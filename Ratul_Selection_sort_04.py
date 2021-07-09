# selection sort implementation

def selection_SORT(list_item):
    length = len(list_item)

    for a in range(length - 1):
        min_index = a
        for b in range(a+1, length):
            if list_item[b] < list_item[min_index]:
                min_index = b

        if min_index is not a:
            TMP = list_item[a]
            list_item[a] = list_item[min_index]
            list_item[min_index] = TMP
            

if __name__ == '__main__' :

    list_item = [21, 443, 12, 34, 654, 31]
    selection_SORT(list_item)
    print('Sorted list is =', list_item)