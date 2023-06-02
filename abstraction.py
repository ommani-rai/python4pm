from abc import ABC, abstractmethod

# abstract class
class shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def demo(self):
        print("from abstract class, no abstract method")

class circle(shape):
    def area(self):
        self.demo() # a.demo()
        print("area of circle")

a = circle()
a.area()
