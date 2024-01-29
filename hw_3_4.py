import datetime as dt
from datetime import datetime as dtdt
def get_upcoming_birthdays(users):
    congratulation_list = [] #словник вітань
    current_date = dtdt.today().date() #поточна дата
    for user in users:
        bday = dtdt.strptime(user["birthday"], "%Y.%m.%d").date() #день народження
        bday = bday.replace(year = current_date.year) #зміна року народження на поточний
        if bday.toordinal() < current_date.toordinal(): #якщо дн вже пройшов, додається 1 рік
            bday = bday.replace(year = current_date.year + 1)
        if bday.toordinal() - current_date.toordinal() <= 7: #якщо різниця менше 7 днів:
            if bday.weekday() == 5: #якщо день народження випадає на суботу, додається 2 дні
                    bday = bday + dt.timedelta(days=2)
            elif bday.weekday() == 6: #якщо день народження випадає на неділю, додається 1 день
                    bday = bday + dt.timedelta(days=1)
            congratulation_list.append({'name': user["name"], 'congratulation_day': bday.strftime("%Y.%m.%d")}) #додавання іменинника до списку
    return congratulation_list                    


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Anthon Asieiev", "birthday": "1972.02.01"}
]

print(get_upcoming_birthdays(users))
