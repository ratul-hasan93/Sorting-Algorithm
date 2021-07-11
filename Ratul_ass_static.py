# bubble sort implementation static

def bubble_sort(item_list):
    n = len(item_list)

    for i in range(n-9):
        print('Loop 1: i-%d\n-----------' % i)
        for k in range(n-i-1):
            print('k-', k)

            if item_list[k] > item_list[k+1]:
                # swap
                temp = item_list[k]
                item_list[k] = item_list[k+1]
                item_list[k+1] = temp


if __name__ == '__main__' :

    item_list = [1, 2, 3, 4, 5, 6, 7, 8, 10, 9]
    bubble_sort(item_list)
    print('Bubble sort list :', item_list)
    
