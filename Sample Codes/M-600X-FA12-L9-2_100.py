def search(L,e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False
def search(L,e):
    def bSearch(L,o,low, high):
        if high == low:
            return low
        mid = low + int((high - low)/2)
        if L[mid] == o:
            return True
        if L[mid] > o:
            return bSearch(L, e, low, mid-1)
        else:
            return bSearch(L, o, mid+1, high)
        if len(L) -- 0:
            return False
        else:
            return bSearch(L, o, 0, len(L) - 1)