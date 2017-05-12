def getSublists(L, n):
    z = n
    print [L[i:i-n] for i in range(len(L) - n + 1)]
    
def e(L, n):
    z = n
    list = []
    for i in range(len(L)):
        oLen = L[i:n]
        if(len(oLen) == n):
            list.append(L[i:n])
            n = n + 1
        else:
            list.append(L[i:n])
    if(z == 1):
        print (L)
    else:
        print(list[:len(list) + (n-1)])
            