from random import sample


def get_numbers_ticket(min, max, quantity):
    if  1 <= min < 1000 and 1 <= max <= 1000 and min < max and quantity < max - min:  # перевірка вхідних даних
        numbers = sample(range(min, max + 1), quantity)  # генерація випадкової послідовності
        numbers.sort()  # сортування
        return numbers
    else:
        return []
