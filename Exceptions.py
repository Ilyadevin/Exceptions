user_input = input("Введите число ")
input_list = user_input.split(" ")

try:
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
