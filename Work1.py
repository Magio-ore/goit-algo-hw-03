import datetime

date = "2023-07-03"

def get_days_from_today(date):
    try:
        date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        date_now = datetime.date.today()
        difference = date_now.toordinal() - date.toordinal()
        return difference
    except AttributeError:
        return "Неправильний формат дати. Будь ласка, введіть об'єкт типу datetime.date."


print (get_days_from_today(date))

invalid_date = datetime.date(year=1290, month=3, day=1)
print(get_days_from_today(invalid_date))
