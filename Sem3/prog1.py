g = ["fsvs4s45vs342f236", "235n234wqfe", "rdwqh352527asfs", "dahfw324"]
num = input("Введите искомое число: ")
flag = True
for i in g:
    for j in i:
        if num == j:
            print("Число присутствует в элементе " + i)
            flag = False
            break
        if flag:
            print("Число не найдено!")
