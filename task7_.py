print('Задача 1.1')
def is_in_range(num):
    if (num >= 1 and num <= 100) or (num >= 200 and num <= 300):
        return True
    else:
        return False

num = 654
if is_in_range(num):
    result = 'Число находится в нужном диапазоне'
else:
    result = 'Число не находится в нужном диапазоне'

print(result+'\n')



print('Задача 1.2')
def time_to_boil(start_temp):
    boiling_temp = 100
    temp = start_temp
    time = 0

    while temp < boiling_temp:
        temp += 1
        time += 2

    return time

start_temp = 98
time = time_to_boil(start_temp)
print(f"Время до закипания воды: {time} минут\n")



print('Задача 1.3')
def print_zeros(num):
    for i in range(1, num+1):
        print(f"{i}. 000")

num = 4
print_zeros(num)


print('\nЗадача 1.4')
def print_triangle(height):
    for i in range(1, height+1):
        print("*" * i)

height = 4
print_triangle(height)

print('\nЗадача 2.1')
def check_fit(a, b, c, m, k):
    if (a <= m and b <= k) or (a <= k and b <= m) or (a <= m and c <= k) or (a <= k and c <= m) or (b <= m and c <= k) or (b <= k and c <= m):
        return True
    else:
        return False

a = 3
b = 4
c = 5
m = 8
k = 9

if check_fit(a, b, c, m, k):
    print("Коробка может пройти через дверь")
else:
    print("Коробка не может пройти через дверь")


print('\nЗадача 2.2')
def print_triangle(height):
    for i in range(1, height+1):
        print(' '*(height-i) + '*'*(2*i-1))

height = 5

print_triangle(height)


print('\nЗадача 2.3')
def print_squares_less_than_n():
    n = 50
    i = 1
    while i*i < n:
        print(i*i)
        i += 1
    print("Квадраты чисел, меньших", n, "выведены.")

print_squares_less_than_n() # вызываем функцию


def squares_less_than_n(n):
    if not isinstance(n, int):
        raise TypeError("The argument must be an integer")
    if n < 0:
        raise ValueError("The argument must be non-negative")
    squares = []
    i = 1
    while i*i < n:
        squares.append(i*i)
        i += 1
    return squares



print('\nЗадача 3.1')
def can_buy_exactly_k_ice_cream_balls(k):
    """
    Функция проверяет, можно ли купить ровно k шариков мороженного,
    если продается мороженое по 3 и 5 шариков.

    :param k: количество шариков мороженного, которое нужно купить
    :return: True, если можно купить ровно k шариков, иначе False
    """
    for i in range(k//3 + 1):
        for j in range(k//5 + 1):
            if i*3 + j*5 == k:
                return True
    return False

k = 30
if can_buy_exactly_k_ice_cream_balls(k):
    print("Можно купить ровно", k, "шариков мороженного")
else:
    print("Нельзя купить ровно", k, "шариков мороженного")


print('\nЗадача 3.2')

def years_to_reach_goal(x, y, z):
    years = 0
    while x < z:
        x *= (1 + y/100)
        years += 1
    return years
X = 1000 # в тысячах гривен
Y = 10 # 10%
Z = 2000 # в тысячах гривен
years = years_to_reach_goal(X, Y, Z)
print(f"Сумма вклада достигнет {Z} тысяч гривен через {years} лет")


print('\nЗадача 3.3')
def sum_of_digits(n):
    try:
        n = int(abs(n))
    except TypeError:
        raise TypeError("Input must be an integer")
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


n = 254
result = sum_of_digits(n)
print(result)


############################################################################################


#Тест_ Задача 1.1
import unittest

class TestNumberInRange(unittest.TestCase):
    def test_is_in_range(self):
        test_cases = [(1, True), (50, True), (100, True), (101, False), (150, False), (199, False), (200, True), (250, True), (300, True), (301, False), (-5, False), (0, False), (500, False)]
        for number, expected in test_cases:
            with self.subTest(number=number):
                self.assertEqual(is_in_range(number), expected)

if __name__ == '__main__':
    unittest.main()



#Тест_ Задача 1.2
import math
import unittest

class TestTimeToBoil(unittest.TestCase):
    def test_time_to_boil(self):
        test_cases = [(0, 200), (50, 100), (98, 4), (100, 0), (101, 0)]
        for start_temp, expected_time in test_cases:
            with self.subTest(start_temp=start_temp):
                self.assertEqual(time_to_boil(start_temp), expected_time)

if __name__ == '__main__':
    unittest.main()


#Тест_ Задача 2.1
import unittest

class TestFitsThroughDoor(unittest.TestCase):
    def test_check_fit(self):
        self.assertIn(True, [check_fit(1, 2, 3, 2, 3),
                             check_fit(1, 2, 3, 3, 3),
                             check_fit(2, 2, 2, 2, 2),
                             check_fit(3, 3, 3, 3, 3)])
        self.assertIn(False, [check_fit(1, 2, 3, 2, 2),
                              check_fit(1, 2, 3, 1, 3),
                              check_fit(1, 2, 3, 1, 2),
                              check_fit(1, 2, 3, 3, 2),
                              check_fit(1, 2, 3, 1, 1),
                              check_fit(1, 2, 3, 3, 1),
                              check_fit(1, 2, 3, 2, 1)])

if __name__ == '__main__':
    unittest.main()


#Тест_ Задача 2.3
import unittest

class TestSquaresLessThanN(unittest.TestCase):
    def test_squares_less_than_n(self):
        test_cases = [
            (1, []),
            (2, [1]),
            (3, [1]),
            (4, [1]),
            (5, [1, 4]),
            (6, [1, 4]),
            (10, [1, 4, 9]),
            (16, [1, 4, 9]),
            (17, [1, 4, 9, 16])
        ]
        for n, expected in test_cases:
            with self.subTest(n=n, expected=expected):
                self.assertListEqual(squares_less_than_n(n), expected)

    def test_squares_less_than_n(self):
        self.assertRaises(TypeError, squares_less_than_n, "hello")
        self.assertRaises(ValueError, squares_less_than_n, -5)
        self.assertEqual(squares_less_than_n(0), [])

if __name__ == '__main__':
    unittest.main()


#Тест_ Задача 3.1
import unittest


class TestSomeConditions(unittest.TestCase):
    def test_can_buy_exactly_k_ice_cream_balls(self):
        self.assertEqual(can_buy_exactly_k_ice_cream_balls(5), True)
        self.assertEqual(can_buy_exactly_k_ice_cream_balls(3), True)
        self.assertEqual(can_buy_exactly_k_ice_cream_balls(8), True)
        self.assertEqual(can_buy_exactly_k_ice_cream_balls(9), True)
        self.assertEqual(can_buy_exactly_k_ice_cream_balls(10), True)
        self.assertEqual(can_buy_exactly_k_ice_cream_balls(11), True)
        self.assertEqual(can_buy_exactly_k_ice_cream_balls(12), True)
        self.assertEqual(can_buy_exactly_k_ice_cream_balls(13), True)
        self.assertEqual(can_buy_exactly_k_ice_cream_balls(14), True)
        self.assertEqual(can_buy_exactly_k_ice_cream_balls(15), True)
        self.assertEqual(can_buy_exactly_k_ice_cream_balls(16), True)
        self.assertEqual(can_buy_exactly_k_ice_cream_balls(17), True)
        self.assertEqual(can_buy_exactly_k_ice_cream_balls(18), True)
        self.assertEqual(can_buy_exactly_k_ice_cream_balls(19), True)
        self.assertEqual(can_buy_exactly_k_ice_cream_balls(20), True)
        self.assertEqual(can_buy_exactly_k_ice_cream_balls(21), True)
        self.assertEqual(can_buy_exactly_k_ice_cream_balls(22), True)
        self.assertEqual(can_buy_exactly_k_ice_cream_balls(0), True)

        self.assertEqual(can_buy_exactly_k_ice_cream_balls(1), False)
        self.assertEqual(can_buy_exactly_k_ice_cream_balls(2), False)
        self.assertEqual(can_buy_exactly_k_ice_cream_balls(4), False)
        self.assertEqual(can_buy_exactly_k_ice_cream_balls(7), False)
        self.assertEqual(can_buy_exactly_k_ice_cream_balls(-1), False)


if __name__ == '__main__':
    unittest.main()


#Тест_ Задача 3.2
import unittest

class TestCalculateDeposit(unittest.TestCase):

    def test_deposit_exceeds_target_amount(self):
        self.assertEqual(years_to_reach_goal(1000, 10, 2000), 8)
        self.assertEqual(years_to_reach_goal(5000, 5, 10000), 15)

    def test_deposit_exceeds_target_amount_with_zero_interest_rate(self):
        self.assertNotEqual(years_to_reach_goal(1000, 10, 2000), 5)
        self.assertNotEqual(years_to_reach_goal(5000, 5, 10000), 10)
        self.assertNotEqual(years_to_reach_goal(10000, 7, 15000), 14)

    def test_deposit_exceeds_target_amount_input_validation(self):
        self.assertRaises(TypeError, years_to_reach_goal, "abc", 10, 2000)
        self.assertRaises(TypeError, years_to_reach_goal, 1000, "abc", 2000)
        self.assertRaises(TypeError, years_to_reach_goal, 1000, 10, "abc")


if __name__ == '__main__':
    unittest.main()



#Тест_ Задача 3.3
import unittest

class TestSumOfDigits(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(sum_of_digits(123), 6)
        self.assertEqual(sum_of_digits(456), 15)
        self.assertEqual(sum_of_digits(789), 24)
        self.assertEqual(sum_of_digits(101010), 3)
        self.assertEqual(sum_of_digits(5555), 20)

    def test_negative_numbers(self):
        self.assertEqual(sum_of_digits(-123), 6)
        self.assertEqual(sum_of_digits(-456), 15)
        self.assertEqual(sum_of_digits(-789), 24)
        self.assertEqual(sum_of_digits(-101010), 3)
        self.assertEqual(sum_of_digits(-5555), 20)

    def test_zero(self):
        self.assertEqual(sum_of_digits(0), 0)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            sum_of_digits("abc")
        with self.assertRaises(TypeError):
            sum_of_digits([1, 2, 3])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

