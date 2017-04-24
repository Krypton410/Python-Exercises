s = 'azcbobobegghaklbobobob'


s = s.replace("b","bb")

# Bob counter
nBobs = s.count('bob',0,len(s))

# Print the result.    
print ('Number of times bob occurs is: ' + str(nBobs))