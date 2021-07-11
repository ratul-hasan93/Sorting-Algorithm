# Bubble sort assignment implementation

def bubble_sort(item_list):
    item_length = len(item_list)

    for i in range(item_length):
        print('Loop 1: i-%d\n-----------' % i)
        swap = False



        for j in range(item_length-i-1): 
            print('j-', j)
            if item_list[j] > item_list[j+1]:
                tmp = item_list[j]
                item_list[j] = item_list[j+1]
                item_list[j+1] = tmp
                swap = True

        if swap == False:
            break

if __name__ == '__main__' :

    item_list = [1,2,3,4,6,5]
    bubble_sort(item_list)
    print("Bubble sort: ", item_list)
