#every thing is object
#class design or blueprint of object
#object created by class
#class is a user defind data type
#class : plan to create the object
#class has no real exsistence
#object have real exsistence
#class have one and object have more than one
#class : objct = 1.properties [vaiables]  2.behaivior[function, function in class is called methods]
#variables have two= 1.class variables   2.object variables
#object varibles =instance varibl, class varibles=static varibles
#costractor : a method who create or generate the objects use: alocating the memory for object variables
# constrctoe __init__ special methods




#example 01
'''
class car:
    com="oudi"
    mod=2005
    pri=15000000
    col="black"
    def details(self):
        print("self.com")

#object
a=car()
print(a.com,a.mod,a.pri,a.col)
print(car.com,car.mod,car.pri,car.col)
a.details() '''


'''
# example 02
class car:
    com="oudi"
    def __init__(self,model,price,color):
        # object variables
        self.mod=model
        self.pri=price
        self.col=color
    def details(self):
        print(self.com,self.mod,self.pri,self.col)
a=car(2005,150000,"black")
b=car(2008,250000,"blue")
c=car(2005,5550000,"black")

a.details()
b.details()
c.details()

'''

class car:
    com="oudi"
    def __init__(self,model,price,color):
        # object variables
        self.mod=model
        self.pri=price
        self.col=color
    def details(self):
        print(f"company:{self.com}\n",self.mod,self.pri,self.col)

    def mark(self,phy,che,cs):
        self.physics=phy
        self.chemistry=che
        self.computer=cs
    def avg(self):
        return (self.physics+self.chemistry+self.computer)/4
    


a=car(2005,150000,"black")
b=car(2008,250000,"blue")
c=car(2005,5550000,"black")

a.details()
b.details()
c.details()

a.mark(90,85,99)
print("avg",a.avg())



