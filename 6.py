array = input('Введите массив: ').split()
delta = int(input('Введите число DELTA: '))
min_elem = 10 ** 100
count = 0
for i in range(len(array)):
    array[i] = int(array[i])
for elem in array:
    if int(elem) < min_elem:
        min_elem = elem
for el in array:
    if el - min_elem == delta:
        count += 1
print(count, array.count(min(array) + delta))