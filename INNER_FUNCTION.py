def area(l,b,r):
    def circle(r):
        return 3.14*r*r
    def rec(L,b):
        return l*b
    return circle(r)+rec(l,b)
print(area(10,10,10))