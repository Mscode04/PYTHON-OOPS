
class car:
    com="oudi"
    def __init__(self,model,price,color):
        # object variables
        self.mod=model
        self.pri=price
        self.col=color
        # OBJECT OR INSTANCE METHOD
    def details(self):
        print(f"company:{self.com}\n",self.mod,self.pri,self.col)
x1=car(2005,25896321,"black")
print(x1.mod,x1.pri,x1.col)
x1.col="blue"       
print(x1.mod,x1.pri,x1.col)
x1.market="good"
print(x1.mod,x1.pri,x1.col,x1.market)




