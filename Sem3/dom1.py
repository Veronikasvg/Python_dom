list = [3, 5, 6, 8, 9, 12, 4]
summ = 0
for element in range(1, len(list), 2):
    summ += list[element]
print(f"{list} -> сумма элементов,стоящих на нечётных позициях: {summ}")
