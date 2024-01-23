import random


def get_numbers_ticket(min, max, quantity):
    if (
        1 <= min < 1000 and 1 <= max <= 1000 and min < max and quantity < max - min
    ):  # перевірка вхідних даних
        numbers = random.sample(
            range(min, max + 1), quantity
        )  # генерація випадкової послідовності
        numbers.sort()  # сортування
        return numbers
    else:
        return []


print(get_numbers_ticket(1, 36, 5))
print(get_numbers_ticket(1, 49, 6))
print(get_numbers_ticket(1, 1, 1))
