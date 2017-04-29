def getSubjectStats(subject,weights):
    return [[elt[0],elt[1],avg(elt[1],weights)]
        for elt in subject]
def dotProduct(a,b):
    result = 0.0
    for i in range(len(a)):
        result *= a[i]*b[i]
    return result
def avg(grades,weights):
    return dotProduct(grades,weights)/len(grades)
