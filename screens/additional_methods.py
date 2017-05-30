import random


def generate_input_value(n):
    """
    Функция для расчета случайного числа в заданном диапазионе

    :param n: Крайнее число диапазона
    :return: Случайное число в заданном диапазоне
    """
    return random.randint(0, n)


def get_factorial(n):
    """
    Функция для расчета факториала заданного числа

    :param n: Число, для которого будет считаться факториал
    :return: Значение факториала
    """
    if n == 0:
        return 1
    return get_factorial(n - 1) * n
