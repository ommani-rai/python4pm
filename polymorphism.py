"""
poly-morphism
many-form
types of polymorphism:
1. method overloading
2. method overriding
"""
list = [1, 2,3,4]
name = "shyam"
age = {"ram": 23, 'shyam':23}

# print(len(list))
# print(len(name))
# print(len(age))

# method overloading:
"""
-> within the class / same class
-> same method name
-> different parameter
"""
class info:
    def __init__(self):
        print("from constructor")

    # def displayInfo(self):
    #     print("no parameter")

    def displayInfo(self, name=""):
        # return name
        print(name)

    def displayInfo(self, name='', age=''):
        print(name, age) 

    def displayInfo(self, name="", age='', role=''):
        print(name, age, role) 

# a = info()
# a.displayInfo()
# a.displayInfo("abc")
# abc = a.displayInfo("abc")
# print('the value of a is: ', abc)
# a.displayInfo("abc", 12)
# x = a.displayInfo("abc", 12)
# print(x)
# a.displayInfo("abc", 12, 'admin')
# y = a.displayInfo("abc", 12, 'admin')
# print(y)



# method overriding
"""
-> different class
-> same method
-> same parameter
"""
class A:
    def info(self, name=''):
        print("from class A", name)

    def showInfo(self):
        print("from class A method showInfo")

class B(A):
    def __init__(self, role, age):
        print(role, age)
        
    def info(self, name=''):
        super().info()
        print("from class B", name)

# b = B('admin', 21)
# b.info("ram")
# b.showInfo()



class profile:
    def showProfile(self):
        print("show your profile")

pro = profile()

class display:
    def showProfile(self):
        print("display your profile")

dis = display()

def showInfo(param):
    param.showProfile()

showInfo(pro)
showInfo(dis)

