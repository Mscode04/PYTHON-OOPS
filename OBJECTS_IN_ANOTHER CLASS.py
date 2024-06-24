class company:
        def __init__(self,director,place,year):
       
            self.dir=director
            self.plc=place
            self.yer=year



class car:
    def __init__(self,model,price,com:company):
        
        self.mod=model
        self.pri=price
        self.company=com
    def details(self):
        print(self.mod,self.pri,self.company.dir)   

cobj=company("BMW","malappuram",1890)        
a1=car(2005,1254789654,cobj)   

a1.details()