import datetime

date = datetime.date(year=2023, month=7, day=3)

def get_days_from_today(date):
    try:
        date_now = datetime.date.today()
        difference = date_now.toordinal() - date.toordinal()
        return difference
    except AttributeError:
        return "Неправильний формат дати. Будь ласка, введіть об'єкт типу datetime.date."


print (get_days_from_today(date))

invalid_date = "2023-07-03"
print(get_days_from_today(invalid_date))
