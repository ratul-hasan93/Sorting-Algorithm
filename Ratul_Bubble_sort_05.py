# bubble sort implementation

def bubble_sort(items):
    n = len(items)

    for d in range(n):
        for h in range(n-d-1):
            if items[h] > items[h+1]:
                # swap
                temp = items[h]
                items[h] = items[h+1]
                items[h+1] = temp


if __name__ == '__main__':

    items = [10,4,6,8,3,5,1,9,2,0]
    bubble_sort(items)
    print('Bubble sort list is :', items)