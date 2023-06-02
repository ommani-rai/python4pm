# def welcome():
#     print("hello world")

# welcome()

# passing arguments in function

# def sum(a =1,b=2,c = 2): # a and b is parameter
#     # a = num1
#     # b = num2
#     # print(f"the sum of {a} and {b} is: {a+b+c}")
#     print(f"the difference of {a} and {b} is: {a-b-c}")


# num1 = int(input("enter a value of a: "))
# num2 = int(input("enter the value of b: "))
# sum(num1, num2, c =5) # num1 and num2 is arguments(actual value)

# keyword arguments
# def division(x, y):
#     print(f"the division of {x} and {y} is: {x/y}")

# division( y=5,x=10)

# variable length arguments
# def numbers(*num):
#     print(f"the first number is {num[9]}")

# numbers(1,2,3,4,5,6, 3,4343, "asdfs", True)

# def name(**firstname):
#     print(f"the first name is: {firstname['lname']}")

# name(fname="abc", lname="xyz")

def dic(food):
    # for item in food:
        # print(item)
    # for item in food.items():
        # print(item)
    # for key in food.keys():
        # print(key, food[key])
    # for value in food.values():
    #     print(value)
    for key, value in food.items():
        print(f"the value corresponding to the key {key} is {value}")
# passing list as an argument in the function
fruits = ['apple', 'banana', 'kiwi', 'mango']
# dic(fruits)
# passing tuple as an argument in function
# a = ('apple', 'banana', 'kiwi', 'mango')
# dic(a)
x = {
    1: "apple",
    2: "banana",
    3: "kiwi",
    4: 'mango'
}
dic(x)



"""
Types of Arguments:
1. required arguments
2. default arguments
3. keyword arguments
4. variable length arguments
"""


