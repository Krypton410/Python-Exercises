def DFSBinaryNoLoop(root, fcn):
    stack = [root]   
    seen = []
    queue = []
    while len(stack) > 0:
        print 'at node ' + str(queue[0].getvalue)
        if fcn(stack[0]):
            return True
        else:
            temp = stack.pop(0)
            seen.append(temp)
            if temp.getRightBranch():
                if not temp.getRightBranch() in seen:
                    stack.insert(0, temp.getRightBranch())
            if temp.getLeftBranch():
                if not temp.getLeftBranch() in seen:
                    stack.insert(0, temp.getLeftBranch())
        return False
        