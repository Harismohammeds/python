def parent():
    def add(x,y):
        return x+y
    return add
x=parent()
print(x(7,4))