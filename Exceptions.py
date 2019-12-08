user_input = input("Введите комманду и числа оперции: ")
"""Ввод пользователем поочередно: сначала функция => потом два числа"""
input_list = user_input.split(" ")
"""Разбитие ввода на части через пробел"""

try:
    """Проверка условий ввода и приравнивание к integers чисел"""
    mark = (input_list[0])
    a = int(input_list[1])
    b = int(input_list[2])
    if mark == "+":
        result = a + b
    elif mark == "/":
        result = a / b
    elif mark == "-":
        result = a - b
    elif mark == "*":
        result = a * b
    print(result)
    """Проверка на шибки ввода - /0, ввод букв вместо чисел, недостаточное количество чисел"""
except ZeroDivisionError as Z:
    print(Z, type(Z))
    print("Делить на ноль нельзя!")
except ValueError as V:
    print(V, type(V))
    print("Неверный ввод данных")
except IndexError as I:
    print(I, type(I))
    print("Маловато операндов")
finally:
    print("Этот блок будет выполнятся всегда")
