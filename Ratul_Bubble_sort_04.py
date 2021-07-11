# Bubble sort implementation

def BUBBLE_SORT(ELEMENTS):
    N = len(ELEMENTS)

    for x in range(N):
        for y in range(N-x-1):
            if ELEMENTS[y] > ELEMENTS[y+1]:
                # swap
                TMP = ELEMENTS[y]
                ELEMENTS[y] = ELEMENTS[y+1]
                ELEMENTS[y+1] = TMP


if __name__ == '__main__' :

    ELEMENTS = [700, 300, 100, 400, 800, 600]
    BUBBLE_SORT(ELEMENTS)
    print("BUBBLE_SORT-->", ELEMENTS)