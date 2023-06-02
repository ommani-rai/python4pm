"""
types of inheritance:
1. single level inheritance
2. multi level inheritance
3. multiple inheritance
"""

# single level inheritance
# class A:
#     name = 'python'
#     id = 1
#     role = "admin"

#     def info(self):
#         print("from info method of class A")

# a = A()
# print(a.name)
# print(a.id)
# print(a.role)
# print(a.info())

# class B(A):
#     def displayInfo(self):
#         print("from method display Info")

# b = B()
# print(b.id, b.name, b.role)
# b.info()


# multi level inheritance

# class fruits:
#     name = "apple"
#     category = "fruits"

#     def fun1(self):
#         print("from class fruits")

# class food(fruits):
#     id = 1
#     def fun2(self):
#         print("from class food")

# class drinks(food):
#     def fun3(self):
#         print("from drinks method")

# c = drinks()
# c.fun2()
# c.fun1()
# c.fun3()
# print(c.name, c.category)
# print(c.id)


# multiple inheritance
class fruits:
    name = "apple"
    category = "fruits"

    def fun1(self):
        print("from class fruits")

class food:
    id = 1
    def fun2(self):
        print("from class food")

class drinks(fruits, food):
    def fun3(self):
        print("from drinks method")

d = drinks()
d.fun1()
d.fun2()
d.fun3()
print(d.name, d.category, d.id)
