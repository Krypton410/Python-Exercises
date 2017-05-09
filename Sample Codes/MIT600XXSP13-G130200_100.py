def DFSBinary(root, fcn, ItFcn):
    stack = [root]
    while len(stack) > 0:
        if fcn(stack[0]):
            return True
        elif ItFcn(stack[0]):
            temp = stack.pop(0)
            if temp.getRightBranch():
                stack.insert(0, temp.getRightBranch())
            if temp.getLeftBranch():
                stack.insert(0, temp.getLeftBranch())
            else:
                if temp.getRightBranch():
                    stack.insert(0, temp.getRightBranch())
    return False 
    
    
def TracePath(node):
    if not node.getParent():
        return [node]
    else:
        return [node] + TracePath(node.getParent())