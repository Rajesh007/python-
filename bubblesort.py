
#[8, 10, 6, 2, 12]
#[8, 6, 2, 10, 12]
#[6, 2, 8, 10, 12]
#[2, 6, 8, 10, 12]

def bubblesort(l):
    for i in range(1,len(l)):
        for j in range(0, len(l)-i):
            if l[j] > l[j+1]:
                (l[j], l[j+1])=(l[j+1], l[j])
        print(l)
