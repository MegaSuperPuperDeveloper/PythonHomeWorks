# Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью рекурсии.
# Функция не должна ничего выводить, только возвращать значение.

def f(a, b, a1):
    if b == 1:
        return a
    print(a)
    return f(a * a1, b-1, a1)

print(f(3, 5, 3))