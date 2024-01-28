till_num = int(input("enter the num:"))
my_list = []
for i in range(1, till_num + 1):
    result = ""
    if i % 3 == 0 and i % 5 == 0:
        result = result + 'fizzbuzz'
        my_list.append(result)
    elif i % 3 == 0:
        result = result + "fizz"
        my_list.append(result)
    elif i % 5 == 0:
        result = (result + "buzz")
        my_list.append(result)
    else:
        my_list.append(i)
print(my_list)
