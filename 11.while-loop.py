# i = 1
#
# while i < 6:
#     if i % 2 == 0:
#         print(f'is even = {i}')
#     else:
#         print(f'is odd = {i}')
#     i += 1

#checking even or odd thru input
# x = int(input("enter the num: "))
# i = 0
# while i <= x:
#     if i % 2 == 0:
#         print(f'{i} is even')
#     else:
#         print(f'{i} is odd')
#     i += 1


# removing something from a list which is repeating
num = [1, 29, 33, 29, 4, 29, 44, 56, 76, 21, 29]

while 29 in num:
    num.remove(29)
print(num)
