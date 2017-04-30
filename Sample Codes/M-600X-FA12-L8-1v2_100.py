def linearSearch(L,x):
    for e in L:
        if e == x:
            return True
        return False
        
        
def fact(n):
    answer = 1
    while n > 1:
        answer *= n
        n -= 1
    return answer
    
def sqrtExhaust(x, eps):
    steps = eps**2
    ans = 0.0
    while abs(ans**2-x) >= eps and ans <= max(x,1):
        ans += steps
    return ans
def sqrtBi(x, eps):
    low = 0.0
    high = max(1,x)
    ans = (high + low)/2.0
    while abs(ans**2 - x):
        if ans**2<x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
    return ans
        
    