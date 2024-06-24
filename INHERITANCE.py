# have paent class or  super class
# also have child or sub class


class vehicle:
    def __init__(self,com,modal,feul):
        self.coma=com
        self.mod=modal
        self.fe=feul
    def stengine(self):
        print("start engine")
    def chgear(self):
        print("gear change")     


class car(vehicle): # add the another clas to my new class that want to acsess the all modes in  veicle class
    def opensun(self):
        print("sunroof open")




x=car("kretta",2005,"electric")


print(x.opensun())
print(x.stengine())
print(x.chgear()) 


# the behaiver of a contrector

class vehicle:
    def __init__(self,com,modal,feul):
        self.coma=com
        self.mod=modal
        self.fe=feul
    def stengine(self):
        print("start engine")
    def chgear(self):
        print("gear change")     


class car(vehicle): # add the another clas to my new class that want to acsess the all modes in  veicle class
    def __init__(self, bodyl,com,modal,feul):
        super().__init__(com,modal,feul)
        self.bod=bodyl
        print(self.bod)
        
    def opensun(self):
        print("sunroof open")




x=car("black body","kretta","2005","e;ectric")
print(x.mod)
















































