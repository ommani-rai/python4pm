"""
oop => object oriented programming
main pillars of oop
1. class
2. object
3. encapsulation
4. abstraction
5. polymorphism
6. inheritance

1. class , object , method
-> class is not a real world entity
-> class does not occupy a memory
-> class is a combination of attribute and behaviour

Animal => dog, cat => eat(), run() => color, age, weight

2. object
-> object is the real world entity
-> object occupy memory

naming convention:
myName - camel case
MyName - pascal case
my_name - snake case
my-name - kebab case

"""
class Animal:
    color = "red"
    age = 5
    weight = 15

    def run(self, size, year, weight):
        print(f"the color is : {size}")
        print(f"the age is : {year}")
        # print(color, age, weight)
        # print(self.color)

dog = Animal()
cat = Animal()
print(cat.color)
cat.color = "blue"
cat.age = 2
cat.weight = 5
print(cat.color)
print(cat.age)
print(cat.weight)


# print(dog.color)
# print(dog.age)
# print(dog.weight)
# x = dog.run(1, 3, 33)
# print(x)
# print(dog.run("yellow", 1, 2))