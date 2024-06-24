class car:
    com="oudi"
    def __init__(self,model,price,mark:list):
        # object variables
        self.mod=model
        self.pri=price
        self.mar=mark
    def details(self):
        print(f"company:{self.com}\n",self.mod,self.pri,self.mar)        
    def percent(self):
        total=0
        for i in self.mar:
            total=total+1

        value=(total/400)+100
        print(value)
x1=car(2005,25896321,[100,250])
x1.details()
x1.percent()