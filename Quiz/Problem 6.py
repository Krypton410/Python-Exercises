def flatten(aList):
    #aList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
    a = str(aList)
    print ([s.strip('[]') for s in a])
   
    
    
    
    