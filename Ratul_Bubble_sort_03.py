# Bubble sort implementation

def Bubble_Sort(element_list):
    n = len(element_list)

    for a in range(0, n):
        for b in range(0, n-a-1):
            if element_list[b] > element_list[b+1]:
                # swap
                temp = element_list[b]
                element_list[b] = element_list[b+1]
                element_list[b+1] = temp


if __name__ == '__main__' :

    element_list = [331, 34, 54, 767,63, 23, 6,5]
    Bubble_Sort(element_list)
    print("BUBBLE SORT LIST:-->", element_list)