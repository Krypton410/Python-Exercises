def oddTuples(aTup):
    rTup = ()
    index = 0
    while index < len(aTup):
        rTup += (aTup[index],)
        index += 2

    return rTup