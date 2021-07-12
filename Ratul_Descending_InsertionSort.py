# insertion sort descending

def InsertionSort(item_list):
    n = len(item_list)
    for i in range(1, n):
        item = item_list[i]
        k = i-1
        while k>=0 and item_list[k] < item:
            item_list[k+1] = item_list[k]
            k = k-1

        item_list[k+1] = item

item_list = [50, 80, 15, 90, 11, 35, 20]
InsertionSort(item_list)
print("Descending Insertion Sort:", item_list)
