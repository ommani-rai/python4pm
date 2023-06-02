"""
range(2) => 0, 1
range(2, 6) => 2, 3,4,5
range(2, 10, 2) => 2, 4,6,8
range(5, 2, -1) => 5, 4, 3

"""
list = ['orange', 'apple', 'banana']
# print(range(4))
# for i in range(5): # 0 - 4
#     print(i)

# for item in list:
#     print(item)
# num = int(input("enter the number"))
# for i in range(1, 11):
#     print(f" {num} x {i} = {num * i}")

# for i in range(5):
#     for j in range(i):
#         print(j)
#     print(i)

rows = 5
# outer loop
for i in range(1, rows + 1):
    # inner loop
    for j in range(1, i + 1):
        print("*", end=" ")
    print('')


