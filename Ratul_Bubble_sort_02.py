# bubble sort implementation

def bubble_sort(data_list):
    length = len(data_list)

    for K in range(length):
        for L in range(length-K-1):
            if data_list[L] > data_list[L+1]:
                # swap
                temp = data_list[L]
                data_list[L] = data_list[L+1]
                data_list[L+1] = temp


if __name__ == '__main__' :

    data_list = [43,45,876,23,456,32,3,56,2]
    bubble_sort(data_list)
    print("Bubble sort list =", data_list)
