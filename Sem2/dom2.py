
n = int(input('Введите число N: '))
f = 1


for i in range(1, n + 1):
    f *= i
    print(f, end=', ')
