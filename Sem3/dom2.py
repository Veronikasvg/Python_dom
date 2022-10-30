import math
list = [3, 5, 6, 8, 9, 12]

# if len(list)%2 == 0:
#     size = len(list) // 2
size = math.ceil(len(list)/2)
print(size)
list2 = []
for i in range(size):
    list2.append(list[i]*list[-i - 1])
print(list2)
