# selection sort implementation

def selection_sort(data_list):
    length = len(data_list)

    for i in range(length - 1):
        min = i
        for j in range(i+1, length):
            if data_list[j] < data_list[min]:
                min = j

        if min != i:
            temp = data_list[i]
            data_list[i] = data_list[min]
            data_list[min] = temp

if __name__ == '__main__' :

    data_list = [15, 50, 12, 6, 34, 23]
    selection_sort(data_list)
    print('Sorted list: ', data_list)