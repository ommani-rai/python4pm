# factorial of a number using for loop
"""
num = int(input("enter a number"))

if num < 0:
    print("negative number does not have the factorial")

elif num == 0 or num == 1:
    print(f"the factorial of {num} is {num}")

else:
    fact = 1
    for i in range(2, num + 1):
        fact = fact * i

    print(f"the factorial of {num} is {fact}")

"""
# factorial of a number using recursion

num = int(input("enter a number"))

def factorial(num):
    if num == 0 or num == 1:
        return num
    else:
        return num * factorial(num - 1) #4
    # 4 * factorial(3)
    # 4 * 3 * factorial(2)
    # 4 * 3 * 2 * factorial(1)
    # 4 * 3 *2 * 1
    # 24
    
fact = factorial(num)
print(f"the factorial of the number {num} is {fact}")
    
