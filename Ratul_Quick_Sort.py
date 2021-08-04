# Quick sort implementaion using python

def partition(L, low, high):
    pivot = L[high]
    i = low-1
    for j in range (low, high):
        if L[j] <= pivot:
            i+=1
            L[i], L[j] = L[j], L[i]

    L[i+1], L[high] = L[high], L[i+1]
    return i+1

def Quick_sort(L, low, high):
    if low >= high:
        return
    pivot_index = partition(L, low, high)
    Quick_sort(L,low, pivot_index-1) #left sub-list
    Quick_sort(L,pivot_index+1, high) #right sub-list

if __name__=="__main__" :
    Array_list = [5,3,6,8,9,1,4,7,2]
    print("Unsorted List:", Array_list)
    Quick_sort(Array_list, 0, len(Array_list)-1)
    print("Sorted List is:", Array_list)