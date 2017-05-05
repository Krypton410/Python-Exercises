class Queue(object):
    def __init__(self):
        self.qlist = []

    def insert(self, e):
        self.qlist.append(e)
            
    def remove(self):
        try:
            return self.qlist.pop(0)
        except:
            raise ValueError()
    def __str__(self): 
        return '{' + ','.join([str(e) for e in self.qlist]) + '}' 