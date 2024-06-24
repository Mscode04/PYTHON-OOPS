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

        # CLASS METHOD
    @classmethod    
    def companyname(cls):
        print(cls.com)    

        # STATIC METHOD
    @staticmethod    
    def about():
        print("good company")



car.companyname()
car.about()