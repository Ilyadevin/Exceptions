user_input = input("Введите комманду и числа оперции: ")
"""Ввод пользователем поочередно: сначала функция => потом два числа"""
input_list = user_input.split(" ")
"""Разбитие ввода на части через пробел"""


def poland_():
    try:
        """Проверка условий ввода и приравнивание к integers чисел"""
        mark = (input_list[0])
        a = int(input_list[1])
        b = int(input_list[2])
        result = 0
        if mark == "+":
            result = a + b
        elif mark == "/":
            result = a / b
        elif mark == "-":
            result = a - b
        elif mark == "*":
            result = a * b
        else:
            result = 'Переменная с результатом пуста'
        print(result)
        """Проверка на ошибки ввода - /0, ввод букв вместо чисел, недостаточное количество чисел"""
    except ZeroDivisionError as Z:
        print(Z, type(Z))
        print("Делить на ноль нельзя!")
    except ValueError as V:
        print(V, type(V))
        print("Неверный ввод данных")
    except IndexError as Index:
        print(Index, type(Index))
        print("Маловато операндов")


print(poland_())
