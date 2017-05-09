def BFSDTreeGoodEnough(root, valueFcn, constraintFcn, stop):
    queue = [root]
    best = None
    visited = 0
    while len(queue) > 0:
        visited += 1
        if constraintFcn(queue[0].getValue()):
            if best == None:
                best = queue[0]
            elif valueFcn(queue[0].getValue()) > valueFcn(best.getValue()):
                best = queue[0]
            if stop(best.getValue()):
                return best
            temp = queue[0]
            if temp.getLeftBranch():
                queue.append(temp.getLeftBranch)
            if temp.getRightBranch():
                queue.append(temp.getRightBranch())
            else:
                queue,pop(0)
        print 'visited'.visited
        return best
