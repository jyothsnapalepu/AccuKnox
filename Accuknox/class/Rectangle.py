class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def __iter__(self):
        return iter([{'length': self.length}, {'width': self.width}])
    
a=Rectangle(8,15)
for i in a:
    print(a)