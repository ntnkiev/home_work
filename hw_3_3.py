import re
def normalize_phone(num):
    num = re.findall(r"\d+", num)
    num = ''.join(num)
    if len(num) == 10:
        return '+38' + num
        return result
    elif len(num) == 12:
        return '+' + num
    else:
        return None

