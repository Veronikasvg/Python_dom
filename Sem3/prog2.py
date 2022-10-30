list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
print(list)
a = input("Введите искомый элемент: ")
count = 0
for i in range(len(list)):
    if list[i] == a:
        count += 1
        if count == 2:
            print(i)
else:
    print("нет")
