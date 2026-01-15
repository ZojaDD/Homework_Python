from math import ceil


def square(a):
    return ceil(a * a)


num_a = float(input("Введите сторону квадрата: "))
print(f"Площадь квадрата: {square(num_a)}")
