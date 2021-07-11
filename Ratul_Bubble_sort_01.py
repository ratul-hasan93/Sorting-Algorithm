# Bubble sort implementation

def bubble_sort(item_list):
    n = len(item_list)

    for i in range(0, n):
        print('Loop 1: i-%d\n-----------' % i)
        for j in range(0, n-i-1):
            print('j-', j)
            if item_list[j] > item_list[j+1]:
                # swap
                tmp = item_list[j]
                item_list[j] = item_list[j+1]
                item_list[j+1] = tmp

if __name__ == "__main__" :

    item_list = [29,34,67,89,67,12,8]
    bubble_sort(item_list)
    print("Bubble sort list is:", item_list)



    
# n = 5
# for i in range(0, n):
#     print('Loop 1: i-%d\n-----------' % i)
#     for j in range(0, n-i-1):
#         print('j-', j)
