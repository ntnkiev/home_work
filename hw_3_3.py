import re
def normalize_phone(num):
    num = re.findall(r"\d+", num) #виділення чисел
    num = ''.join(num) #поєднання в один рядок
    if len(num) == 10:
        return '+38' + num #якщо не вистачає коду держави, додаємо '+38'
    elif len(num) == 12:
        return '+' + num #якщо не вистачає лише '+', додаємо '+'
    else:
        return None #якщо номер не підпадає під умови 
