import datetime


def get_days_from_today(date):
    try:
        date_from = datetime.datetime.strptime(
            date, "%Y-%m-%d"
        )  # перевод в фотрат datetime
    except ValueError:
        return None  # якщо невірний формат повертаєм None
    date_now = datetime.datetime.today()  # сьогоднішня дата
    return date_now.toordinal() - date_from.toordinal()  # повертаємо різницю днів
