x = int(input("Введите число:  "))
y = []
y.insert(-1, 1)
y.insert(-2, -1)

for n in range(x-2, 1):
    n = -3
    y[n] = y[n+2] - y[n+1]
    y.insert(n, y[n])
    n = n - 1
print(y)
