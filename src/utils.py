def multiply(a, b):
    """Умножение двух чисел"""
    return a * b


def divide(a, b):
    """Деление с проверкой на ноль"""
    if b == 0:
        raise ValueError("Делить на ноль нельзя!")
    return a / b
