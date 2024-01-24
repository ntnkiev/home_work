import datetime as dt
from datetime import datetime as dtdt
def get_upcoming_birthdays(users):
    congratulation_dict = {} #словник вітань
    current_date = dtdt.today().date() #поточна дата
    for user in users:
        bday = dtdt.strptime(user["birthday"], "%Y.%m.%d").date() #день народження
        bday = bday.replace(year = current_date.year) #зміна року народження на поточний
        if bday < current_date: #якщо дн вже пройшов, додаємо 1 рік
            bday = bday.replace(year = current_date.year + 1)
            if bday.toordinal() - current_date.toordinal() < 7: #якщо різниця менше 7 днів:
                if bday.weekday()

        print(bday)

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

get_upcoming_birthdays(users)
