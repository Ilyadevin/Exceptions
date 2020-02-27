user_input = input("Введите комманду и числа оперции: ")
"""Ввод пользователем поочередно: сначала функция => потом два числа"""
input_list = user_input.split(" ")
"""Разбитие ввода на части через пробел"""


class ExceptionClass:
    def __init__(self, input_list_):
        self.input_list = input_list_

    def poland_(self):
        try:
            """Проверка условий ввода и приравнивание к integers чисел"""
            mark = (self.input_list[0])
            a = int(self.input_list[1])
            b = int(self.input_list[2])
            result = None
            if mark == "+":
                result = a + b
            elif mark == "/":
                result = a / b
            elif mark == "-":
                result = a - b
            elif mark == "*":
                result = a * b
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
        finally:
            print("Этот блок будет выполнятся всегда")


except_ = ExceptionClass(input_list)
