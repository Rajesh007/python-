

def mergesort(arr, left, right):
    if right-left <= 1:                  # Base case
        return(arr[left :right])
    
    if right-left > 1:                  # Recursive call
        mid = (left+right)//2
        L = mergesort(arr,left, mid)
        R = mergesort(arr,mid,right)
        return(merge(L,R))
   


def merge(A,B):
    (C,m,n) = ([], len(A), len(B))
    (i, j) = (0, 0)
    
    while i+j < m+n:                    # i+j keep track of number of elements merged
        
        if i == m:                      # A is empty
            C.append(B[j])
            j = j + 1
        elif j == n:                    # B is empty
            C.append(A[i])
            i = i + 1
        elif A[i] < B[j]:               # A[i] is small than B[j]
            C.append(A[i])
            i = i + 1
        elif B[j] < A[i]:               # B[j] is small than A[i]
            C.append(B[j])
            j = j + 1

    return(C)
            
