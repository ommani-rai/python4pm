class Profile:
    __role = "user"
    role = "admin"

    def __info(self):
        print("from __info method")

    def info(self):
        self.__info()
        print(self.__role)
        print("name: ", self.name)
        print("age: ", self.age)
        print("gender: ", self.gender)
obj = Profile()
obj.name = "ram"
obj.age = 23
obj.gender = "Male"
print(obj.role)
# print(obj.__role)
# obj.__info()

obj.info()
