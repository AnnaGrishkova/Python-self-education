import sys
import math

#1.1 Читаем первую строку, которая содержит "Задача 1.1:" и не используем её
with open('input.txt', 'r') as f:
    f.readline()
    user_input = f.readline().strip()

# Переводим ввод в число
number = int(user_input)
print('Задача 1.1 \nВведенное число:',number)

# Проверяем, попадает ли число в заданный диапазон
if (1 <= number <= 100) or (200 <= number <= 300):
    result = 'Число попадает в диапазон'
else:
    result  = 'Число не попадает в диапазон'
print(result)

with open('output.txt', 'w') as f:
    f.write('Задача 1.1\n')
    f.write(result+'\n \n')



#1.2 Считываем температуру из файла
with open('input.txt', 'r') as f:
    for i in range(4):
        f.readline()
    user_input = f.readline().strip()
    temperature = int(user_input)
    print('\nЗадача 1.2 \nВведенное число:', temperature)

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


#1.3 Заменила решение задачи
# Открываем файл input.txt для чтения
with open('input.txt', 'r') as f:
    # Читаем все строки файла в список
    lines = f.readlines()
    # Получаем значение X из шестой строки
    X = int(lines[7])

# Открываем файл output.txt для добавления данных в конец файла
with open('output.txt', 'a') as f:
    # Выводим заголовок задачи
    print('\nЗадача 1.3:')
    # Записываем заголовок задачи в файл
    f.write('Задача 1.3:\n')

    # Выводим и записываем X строк с тремя нулями
    for i in range(1, X + 1):
        # Формируем строку с номером и тремя нулями
        line = f'{i}. 000'
        # Выводим строку на экран
        print(line)
        # Записываем строку в файл с переводом строки
        f.write(line + '\n')



#1.4 Заменила решение задачи
# Открываем файл для чтения и считываем высоту треугольника
with open('input.txt', 'r') as f:
    height = int(f.readlines()[10])

# Открываем файл для записи и выводим заголовок задачи
with open('output.txt', 'a') as f:
    f.write('\nЗадача1.4:\n')

    print("\nЗадача1.4:")

    # Рисуем треугольник и выводим его на экран и в файл
    for i in range(height):
        for j in range(i+1):
            print('*', end='')
            f.write('*')
        print()
        f.write('\n')




#2.1
with open('input.txt', 'r') as f:
    data = f.readlines()
    A = int(data[13].split('=')[1])
    B = int(data[14].split('=')[1])
    C = int(data[15].split('=')[1])
    M = int(data[16].split('=')[1])
    K = int(data[17].split('=')[1])
    print('\nЗадача 2.1')

    max_side = max(A, B, C)
    min_door = min(M, K)

    if max_side <= min_door:
        result = 'Коробка войдет в дверь'
    else:
        result = 'Коробка не войдет в дверь'
print(result)

with open('output.txt', 'a') as f:
    f.write('\nЗадача 2.1\n')
    f.write(result+'\n \n')

#2.2 Заменила решение задачи
# читаем значение из файла input.txt
# Open the input file and read the 16th line
with open('input.txt', 'r') as file:
    lines = file.readlines()
    height = int(lines[20].strip())

# Build the isosceles triangle using nested loops
triangle = ''
for i in range(height):
    for j in range(height-i-1):
        triangle += ' '
    for k in range(2*i+1):
        triangle += '*'
    triangle += '\n'

print("\nЗадача2.2")

# Print the triangle to the console
print(triangle)

# Append the triangle to the output file
with open('output.txt', 'a') as file:
    file.write('Задача2.2:\n')
    file.write(triangle)



#2.3 Заменила решение задачи
# Открываем файл для чтения и считываем значение N из 24-ой строки
with open('input.txt', 'r') as f:
    lines = f.readlines()
    n = int(lines[23])

# Предположим, что последовательность квадратов уже определена в программе или загружена из другого файла
squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Создаем пустой список, в который будем добавлять числа, меньшие N
result = []
for square in squares:
    if square < n:
        result.append(square)

# Выводим результат на экран
print("Задача2.3:")
print(result)

# Открываем файл для дополнительной записи и записываем результат
with open('output.txt', 'a') as f:
    f.write("\nЗадача2.3:\n")
    f.write(str(result))
    f.write("\n")



# 3.1 Заменила решение задачи
# Читаем данные из файла input.txt
with open('input.txt', 'r') as f:
    line = f.readlines()[26]  # строка с количествами шариков

# Преобразуем строку в список чисел
counts = list(map(int, line.strip().split()))

# Проверяем, можно ли купить ровное количество шариков мороженного
total = sum(counts)
if total % 2 == 0:
    answer = "да"
else:
    answer = "нет"

# Выводим ответ на экран и записываем его в файл output.txt
print(f"\nЗадача3.1: \nМожно ли купить ровное количество шариков мороженого? {answer}")
with open('output.txt', 'a') as f:
    f.write(f"\nЗадача3.1:\nМожно ли купить ровное количество шариков мороженого? {answer}\n")



import math


#3.2 читаем данные из файла input.txt
with open('input.txt', 'r') as file:
    lines = file.readlines()

# извлекаем значения из строк
x = int(lines[29].split('=')[1])
y = int(lines[30].split('=')[1])
z = int(lines[31].split('=')[1])
print('\nЗадача 3.2')
# вычисляем количество лет
result = math.ceil(math.log(z/x)/math.log(1+y/100))
print(result)

with open("output.txt", "a") as file:
    file.write('\nЗадача 3.2')
    file.write('\n')
    file.write(str(result)+ '\n\n')



# 3.3 Заменила решение задачи
# Шаг 1: Чтение входных данных из файла
with open("input.txt", "r") as f:
    W = int(f.readlines()[34])

# Шаг 2: Вычисление суммы цифр числа W
sum_digits = sum(int(digit) for digit in str(W))

print("\nЗадача3.3:")

# Шаг 3: Вывод результата на экран
print(sum_digits)

# Шаг 4: Запись результата в файл output.txt
with open("output.txt", "a") as f:
    f.write(f"Задача3.3:\n{sum_digits}\n")

# python task4.py
