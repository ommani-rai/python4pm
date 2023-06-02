# function within a function

# fibonacci series using for loop

# 0 1 1 2 3 5 8 13
# num1= 0
# num2= 1
# num3 = num2 + num1
# num4 = num3 + num2
# num(n) = num(n-1) + num(n-2)

"""

a = 0
b = 1
num = int(input("enter a number"))
if num == 0:
    print(a)
elif num == 1:
    print(a)
    print(b)

elif num > 1:
    print(a)     
    print(b)
    for i in range(2, num):
        c = a +b
        a = b
        b = c
        print(b)


"""
# Fibonacci series using Recursion
print("enter the value greate than zero")
def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return (fib(num-2) + fib(num-1))
        # 4
        # fib(2) + fib(3)
        # fib(0) + fib(1) + fib(2)
        # 0 + 1 + fib(0) + fib(1)
        # 1 + 0 + 1
        # 2

    
num = int(input("enter a number to find the fibonacci series"))
for i in range(num):
    print(fib(i), end=" ")
