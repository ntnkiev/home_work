import re
def normalize_phone(num):
    number = ''.join(re.findall(r"[\+\d]+", num)) #виділення чисел
    if number[0] == '+':
        return number
    elif len(number) == 10:
        return '+38' + number #якщо не вистачає коду держави, додаємо '+38'
    elif len(number) == 12:
        return '+' + number #якщо не вистачає лише '+', додаємо '+'
    else:
        return None #якщо номер не підпадає під умови 

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
for num in raw_numbers:
    print(normalize_phone(num))