list = [1.1, 1.2, 3.1, 5, 10.01]
list1 = []
for element in range(len(list)):
    if list[element] % 1 != 0:
        list1.append(list[element])
list2 = [round(list1[element] % 1, 2) for element in range(len(list1))]
print(f"{list2} => {max(list2) - min(list2)}")
