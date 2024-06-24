#abstract class : the class those have abstract methods
#abstract methods those who no have function no have content in the function, only decliration

''' python not allow this to directly'''

from abc import ABC,abstractmethod
class vehicle(ABC):
    def start(self):
        print("srating")
    def brek(self):
        print("breaking") 
    @abstractmethod    
    def gear(self):
        pass

class car(vehicle):
    def ope(self):
        print("open sunroof")
    def gear(self):
        print("AUTOMATIC")
class trck(vehicle):
    def loadi(self):
        print("loding")
    
    def gear(self):
        print("MANNUAL")

C=car()
C.gear()
























