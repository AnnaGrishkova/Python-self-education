print('1) Створити простий калькулятор, який зчитує три рядки введених користувачем даних: перше число, друге число та операцію. \n Після цього калькулятор застосовує операцію до введених чисел ("перше число" "операція" "друге число") і виводить результат на екран. \n Підтримувані операції: +, -, /, *, mod, pow, div, де: \n mod - це отримання залишку від ділення, \n pow - піднесення до степеня, \n div - цілочисельне ділення.')
print('num1 = 19')
print('num2 = 3')
print('operation = +')

num1 = 19
num2 = 3
operation = '+'
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "/":
    result = num1 / num2
elif operation == "*":
    result = num1 * num2
elif operation == "mod":
    result = num1 % num2
elif operation == "pow":
    result = num1 ** num2
elif operation == "div":
    result = num1 // num2
else:
    print("Вы ввели неверную операцию!")
    result = None

if result is not None:
    print(f"Результат: {result}")


print('\n\n2) Есть 2 числа a и b. Определите, делится ли a на b нацело. Делится ли b на a? \n a = 36, \n b = 2')

a = 36
b = 2

if a % b == 0:
    print(f"{a} делится нацело на {b}")
else:
    print(f"{a} не делится нацело на {b}")

if b % a == 0:
    print(f"{b} делится нацело на {a}")
else:
    print(f"{b} не делится нацело на {a}")


print('\n\n3) Дано трехзначное число. Определите, есть ли среди его цифр одинаковые. \n number = 332')
number = 332

digit1 = number // 100
digit2 = (number // 10) % 10
digit3 = number % 10

if digit1 == digit2 or digit1 == digit3 or digit2 == digit3:
    print("Среди цифр есть одинаковые")
else:
    print("Среди цифр нет одинаковых")
