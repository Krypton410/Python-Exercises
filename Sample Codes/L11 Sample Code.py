class intSet(object):
    
    def __init__(self):
        self.vals=[]
        
    def insert(self, e):
        if not e in self.vals:
            self.vals.append(e)
    def __str__(self):
        self.vals.sort()
        return  '{' + ','.join([str(e) for e in self.vals]) + '}'
    def remove(self, e):
        try:
            self.vals.remove()
        except:
            raise ValueError(str(e) + ' not found')
            