def factl(n):
    res = 1
    while n>1:
        res = res*n
        n -=1
    return res
    
def factR(n):
    if n== 1:
        print n
        return n
    return n*factR(n-1)