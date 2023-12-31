"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    [1, 4, 25, 49]
    """
    return [num ** 2 for num in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number: int) -> bool:
    # Гипотеза: основная часть запросов будет по числам до 1009**2
    # Список простых чисел до 1009 используем 2 раза: проверка на вхождение, проверка на делитель
    prime_list_1000 = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
                       97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191,
                       193, 197, 199,
                       211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
                       307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
                       401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
                       503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
                       601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
                       701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
                       809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887,
                       907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, }

    # Гипотеза: проверка вхождения в список быстрее, чем перебор по циклу
    if number < 1000:
        return number in prime_list_1000

    # Проверка на делители до 1000, для чисел до 1000**2
    ret_val = True
    for j in prime_list_1000:
        if number % j == 0:
            ret_val = False

    # Первое простое число больше 1000 == 1009
    j = 1009
    while j ** 2 <= number:
        if number % j == 0:
            ret_val = False
    return ret_val

def filter_numbers(numbers_list: list, return_type: str) -> list:
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if return_type == ODD:
        return [j for j in numbers_list if j % 2 != 0]
    if return_type == EVEN:
        return [j for j in numbers_list if j % 2 == 0]
    return [j for j in numbers_list if is_prime(j)]


if __name__ == "__main__":
    print("Homework_01")
    koef=55000
    print(filter_numbers(list(range(1*koef, 1*koef+101)), ODD))
    print(filter_numbers(list(range(1*koef, 1*koef+101)), EVEN))
    print(filter_numbers(list(range(1*koef, 1*koef+101)), PRIME))
