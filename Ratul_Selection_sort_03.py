# selection sort implementation

def S_sort(element_list):
    length = len(element_list)

    for L in range(length - 1):
        min_index = L
        for M in range(L+1, length):
            if element_list[M] < element_list[min_index]:
                min_index = M

        if min_index is not L:
            tmp = element_list[L]
            element_list[L] = element_list[min_index]
            element_list[min_index] = tmp

if __name__ == "__main__" :

    element_list = [34, 56, 78, 90, 23, 12]
    S_sort(element_list)
    print("SHORTED LIST IS: ", element_list)