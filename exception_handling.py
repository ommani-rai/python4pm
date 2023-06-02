try:
    num1 = int(input("enter the value of number 1: "))
    num2 = int(input("enter the value of number 2: "))
    sum = num1 + num2
    print(sum)
    # division = num1/num2
    lis = ["apple", "banana", "kiwi"]
    tup = ("abc", "def", "ghi") 
    set = {1, 2, 3, 4}
    print("abc" in set )
    print(tup[num2])
    print(lis[num1])
except Exception as e:
    # print("num1 and num2 only accept the value as an int")
    print(e)

print("some important line of code")
print("end of program")