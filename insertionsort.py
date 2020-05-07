


def insertionsort(l):
   # In each iteration slice [0:SliceEnd] is already sorted
   for SliceEnd in range(len(l)):
        
        pos = SliceEnd
        # Move value to left until it is small
        while pos > 0 and l[pos] < l[pos-1]:
            (l[pos], l[pos-1])=(l[pos-1], l[pos])
            pos = pos-1
