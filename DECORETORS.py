# to modify any in function

from Circle import area

def cirdic(func):
    def inner(r):
        if r>100:
            r=100
        return func(r)    
    return inner        

fa=cirdic(area)
print(fa(102))

