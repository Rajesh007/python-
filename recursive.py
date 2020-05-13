


# calculate factorial using recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return(n * factorial(n-1))
        
        
# calculate multipication using recursion
def multipication(m,n):
    if n == 1:
        return m
    else:
        return(m + multipication(m,n-1))
        

# calculate length of list
def length(l):
    if l == []:
        return 0
    else:
        return (1 + test(l[1:]))


# calculate sum of elements in list
def sum(l):
    if l == []:
        return 0
    else:
        return(l[0] + sum(l[1:]))
        
 
 
 # 1 1 2 3 5
 
def fibbonacci(n):
    if n ==1 or n== 2:
        return 1
    else:
        return(fibbonacci(n-1)+fibbonacci(n-2))
