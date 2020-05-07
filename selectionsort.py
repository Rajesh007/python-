
def selectionsort(l):
    # start slice from (0, len[l]), (1, len[l])
    for start in range(len(l)):
        
        # find minimum value in slice
        minpos = start
        for i in range(start, len(l)):
            if l[i] < l[minpos]:
                minpos = i
        
        # move it to start of slice
        (l[start], l[minpos]) = (l[minpos], l[start])