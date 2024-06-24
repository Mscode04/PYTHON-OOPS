# POLY # MORPHOSIM

# BEHAVIER LIKE SPECIFIC PEOPLE
#METHOD OVER LOADING
# METHID OVERRAIDING
#OPERATOR OVERLOADING
#DUCK TYPING



#METHOD OVER LOADING
''' PYTON NOT ALLOW THIS DIRECTLY'''
'''
class A :
    def ab(self,a,b):
        print(a+b)
    def ab(self,a,b,c):
        print(a+b+c)
    def ab(self):
        print("no aguments")        

obj=A()
obj.ab()

# use the defult aguments




# part 2
#OPERATOR OVERLOADING
class product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def __add__(self,other):
        print("add opertaor called")
        print(p1.price+p2.price)
    def __sub__(self,other): # allfunction are provided
        print("sub opertaor called")
        print(p1.price-p2.price)

p1=product("samsung",150000000)
p2=product("i phone",4884848548548)'''

'''print()  is not working '''

#p1+p2
#p1-p2



# METHID OVERRAIDING
'''class A:
    def func1(self):
        print("f1 working")
    def func3(self):
        print("f2 working")  
class B(A):         
    def func3(self):
        print("f3 wor3king")
        super().func3() # also call parent class fnction
    def func4(self):
        print("f4 working")
o=B()
o.func3()'''







#DUCK TYPING

# a object act as another objec from another class





class ani:
    def per(self):
        print(" animalperforming")
class hum:
    def per(self):
        print("himan performing")
class room:
    def play(self,animal:ani):
        animal.per()
tiger=ani()
shaheen=hum()
c=room()
c.play(shaheen)                   

''' we import anmal to room but we can also use the hum bcs the both functions act like '''

































































































