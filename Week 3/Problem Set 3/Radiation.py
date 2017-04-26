def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)
def radiationExposure(start, stop, step):

    sumTotal = 0
    point = start
    while point >= start and point < stop:
        sumSub = step * f(point)
        sumTotal += sumSub
        point += step
        return sumTotal
print radiationExposure(0, 4, 0.25)
print radiationExposure(5, 10, 0.25)
print radiationExposure(0, 3, 0.1)
print radiationExposure(100, 400, 4)
print radiationExposure(600, 1200, 5)
print radiationExposure(0, 40, 1)
