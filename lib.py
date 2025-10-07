# Собственный модуль lib.py
# В нём простой калькулятор
# в виде 4-й функций

def summ(a: int, b: int) -> int:
    """
    Возвращает сумму 2-х чисел
    :param a: целое число
    :param b: целое число
    :return: Сумма в виде целого
    """
    return a + b


def diff(a: int, b: int) -> int:
    """
    Возвращает разность 2-х чисел
    :param a: целое число
    :param b: целое число
    :return: разность в виде целого
    """
    return a - b


def mul(a: int, b: int) -> int:
    """
    Возвращает произведение двух чисел
    :param a: целое число
    :param b: целое число
    :return: Сумма в виде целого
    """
    return a * b


def div(a: int, b: int) -> float | None:
    """

    :param a: целое число
    :param b: целое число
    :return:
    Вернёт None в случае деления на 0
    """
    if b != 0:
        return a / b

if __name__ == '__main__':  # Если этот файл исполняемый
    print('Запускайте файл "такой-то", в котором эта библиотека вызывается')
    print(__name__)