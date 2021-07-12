# insertion sort implementatio


def InsertionSort(array_list):
    n = len(array_list)
    for s in range(1, n):
        arr = array_list[s]
        d = s-1
        while d>=0 and array_list[d] > arr:
            array_list[d+1] = array_list[d]
            d = d-1

        array_list[d+1] = arr

array_list = [78, 12, 34, 56, 78, 9]
InsertionSort(array_list)
print("Ascending insertion sort:", array_list)