def gcdIter(a,b):
    gcd = min(a,b)
    while (gcd > 1):
        if ((a%gcd == 0) and (b%gcd == 0)):
            return gcd
        else:
            gcd -= 1
            return 1
print gcdIter(6, 12)