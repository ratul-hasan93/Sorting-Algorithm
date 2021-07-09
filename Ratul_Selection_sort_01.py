# selection sort implementation

def selection_sort(item_list):
    length = len(item_list)

    for j in range(length - 1):
        min_index = j
        for k in range(j+1, length):
            if item_list[k] < item_list[min_index]:
                min_index = k

        if min_index != j:
            tmp = item_list[j]
            item_list[j] = item_list[min_index]
            item_list[min_index] = tmp


if __name__ == '__main__':

    item_list = [56, 34, 67, 21, 5, 71, 2]
    selection_sort(item_list)
    print("sorted list: ", item_list)