def isPalindrome(aString):
   rev = ""
   for i in range(0,len(str)):
    rev = rev + str[(len(str)-1)-i]
   
   if rev == str:
       return True
   else:
       return False
   return rev