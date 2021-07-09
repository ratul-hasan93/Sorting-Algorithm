# selection sort implementation

def SELECTION_SORT(list_data):
    LENGTH = len(list_data)

    for s in range(LENGTH - 1):
        min_indx = s
        for p in range(s+1, LENGTH):
            if list_data[p] < list_data[min_indx]:
                min_indx = p
                
        if min_indx != s:
            temp = list_data[s]
            list_data[s] = list_data[min_indx]
            list_data[min_indx] = temp


if __name__ == '__main__':

    list_data = [200, 500, 100, 300, 400]
    SELECTION_SORT(list_data)
    print("SHORTED LIST =", list_data)