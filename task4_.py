import sys
import math

# Читаем первую строку, которая содержит "Задача 1.1:" и не используем её
with open('input.txt', 'r') as f:
    f.readline()
    user_input = f.readline().strip()

# Переводим ввод в число
number = int(user_input)
print('Задача 1.1 \n Введенное число:',number)

# Проверяем, попадает ли число в заданный диапазон
if (1 <= number <= 100) or (200 <= number <= 300):
    result = 'Число попадает в диапазон'
else:
    result  = 'Число не попадает в диапазон'
print(result)

with open('output.txt', 'w') as f:
    f.write('Задача 1.1\n')
    f.write(result+'\n \n')



# Считываем температуру из файла
with open('input.txt', 'r') as f:
    for i in range(4):
        f.readline()
    user_input = f.readline().strip()
    temperature = int(user_input)
    print('\n Задача 1.2 \n Введенное число:', temperature)

# Инициализируем начальную температуру и время
current_temperature = temperature
time = 0

# Пока текущая температура не достигнет 100 градусов, увеличиваем ее на 1 градус каждые 2 минуты
while current_temperature < 100:
    current_temperature += 1
    time += 2

# Выводим результат в терминал и в файл
print(f'Вода закипит через {time} минут')
with open('output.txt', 'a') as f:
    f.write('Задача 1.2\n')
    f.write(f'Вода закипит через {time} минут \n \n')




# Читаем число из файла input.txt
with open('input.txt', 'r') as f:
    for line in f:
        if line.startswith('Задача 1.3:'):
            n = int(f.readline())
            break
print('\n Задача 1.3 \n Введенное число:', n)
# Выводим X строк из трех нулей
for i in range(1, n+1):
    print(f"{i}. 000")
with open('output.txt', 'a') as f:
    f.write('Задача 1.3\n')
    f.write(f"{i}. 000"+'\n \n')

# Читаем число из файла input.txt
with open('input.txt', 'r') as f:
    for line in f:
        if line.startswith('Задача 1.4:'):
            n = int(f.readline())
            break
print('\n Задача 1.4 \n Введенное число:', n)
# Выводим прямоугольный треугольник
for i in range(n):
    print("*" * (i+1))
with open('output.txt', 'a') as f:
    f.write('Задача 1.4\n')
    f.write("*"+'\n')
    f.write("*" * (i+1)+'\n\n')





with open('input.txt', 'r') as f:
    data = f.readlines()
    A = int(data[13].split('=')[1])
    B = int(data[14].split('=')[1])
    C = int(data[15].split('=')[1])
    M = int(data[16].split('=')[1])
    K = int(data[17].split('=')[1])
    print('\n Задача 2.1')

    max_side = max(A, B, C)
    min_door = min(M, K)

    if max_side <= min_door:
        result = 'Коробка войдет в дверь'
    else:
        result = 'Коробка не войдет в дверь'
print(result)

with open('output.txt', 'a') as f:
    f.write('Задача 2.1\n')
    f.write(result+'\n \n')




# читаем значение из файла input.txt
with open('input.txt', 'r') as f:
    for line in f:
        if line.startswith('Задача 2.2:'):
            n = int(f.readline())
            break

with open('output.txt', 'a') as f:
    f.write('Задача 2.2\n')
    for i in range(n):
        for j in range(n-i):
            f.write(' ')
        for j in range(2*i+1):
            f.write('*')
        f.write('\n')



import math




# Читаем число N из файла input.txt
with open('input.txt', 'r') as f:
    for line in f:
        if line.startswith('Задача 2.3:'):
            n = int(f.readline().strip())
            break

with open('output.txt', 'a') as out_file:
    out_file.write('Задача 2.3\n')
    print('\n\n Задача 2.3')
    # Вычисляем последовательность квадратов чисел, которые меньше или равны N
    squares = []
    i = 1
    while i**2 <= n:
        squares.append(i**2)
        i += 1

    # Выводим числа, которые меньше N
    for sq in squares:
        out_file.write(str(sq) + '\n')




# Считываем число k из файла input.txt
with open("input.txt") as f:
    for line in f:
        if line.startswith('Задача 3.1:'):
            k = int(f.readline())
            break
print('\n Задача 3.1')
# Ищем все возможные комбинации из 3 и 5 шариков мороженого
found = False
for i in range(k//3 + 1):
    for j in range(k//5 + 1):
        if 3*i + 5*j == k:
            found = True
            break
    if found:
        break

# Выводим ответ в зависимости от наличия комбинации, дающей в сумме k шариков мороженого
if found:
    result = 'да'
else:
    result = 'нет'
with open('output.txt', 'a') as f:
    f.write('\nЗадача 3.1\n')
    f.write(result+'\n')



import math


# читаем данные из файла input.txt
with open('input.txt', 'r') as file:
    lines = file.readlines()

# извлекаем значения из строк
x = int(lines[29].split('=')[1])
y = int(lines[30].split('=')[1])
z = int(lines[31].split('=')[1])
print('\n Задача 3.2')
# вычисляем количество лет
result = math.ceil(math.log(z/x)/math.log(1+y/100))
print(result)

with open("output.txt", "a") as file:
    file.write('Задача 3.2')
    file.write('\n')
    file.write(str(result)+ '\n\n')



# Открытие файла с данными
with open('input.txt', 'r') as f:
    data = f.readlines()
    print('\n Задача 3.3')
    # Обработка данных и запись результата в файл
    for i in range(len(data)):
        if 'Задача 3.3' in data[i]:
            num = int(data[i+1].strip())
            sum_of_digits = sum(int(digit) for digit in str(num))
print(sum_of_digits)

with open('output.txt', 'a') as file:
    file.write('Задача 3.3\n')
    file.write(str(sum_of_digits)+ '\n \n')

