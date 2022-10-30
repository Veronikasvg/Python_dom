array = []
for i in range(5):
    array.append(int(input('Введите число ')))
print(array)

max = array[0]

for i in range(len(array)):
    if max <= array[i]:
        max = array[i]
print(max)
