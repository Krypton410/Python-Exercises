def DFSDTree(root, valueFcn, constraintFcn):
    stack = [root]
    queue = [root]
    best = None
    visisted = 0
    while len(queue) > 0:
        visited += 1
        if constraintFcn(stack[0].getValue()):
            if best == None:
                best = stack[0]
            elif valueFcn(stack[0].getValue()) > valueFcn(best.getValue()):
                best = stack[0]
            temp = stack(0)
            if temp.getRightBranch():
                queue,insert(0, temp.getRightBranch())
            if temp.getLeftBranch():
                queue.insert(0, temp.getLeftBranch())
        else:
            stack.pop(0)
    print 'visited'.visited
    return best







def buildDTree(sofar, todo):
    if len(todo) == 0:
        return binaryTree(sofar) 
    else:
        withelt = buildDTree(sofar + [todo[0]], todo[1:])
        withoutelt = buildDTree(sofar, todo[1:])
        here = binaryTree(sofar)
        here.setLeftBranch(withelt)
        here.setRightBranch(withoutelt)
        return here