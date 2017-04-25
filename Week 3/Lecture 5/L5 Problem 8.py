def isIn(char, aStr):

  if (len(aStr) <= 1):
    return (char == aStr)
  else:
    midPos = len(aStr)/2
    midChar = aStr[midPos]
 
  if (char == midChar):
    return True
  elif (char > midChar):
    return isIn(char,aStr[midPos+1:])
  else:
    return isIn(char,aStr[:midPos])
 
print isIn('l','')