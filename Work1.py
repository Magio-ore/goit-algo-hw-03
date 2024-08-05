import datetime

date = datetime.date(year=2023, month=7, day=3)

def get_days_from_today(date):
    date_now = datetime.date.today()
    difference = date_now.toordinal() - date.toordinal()
    return difference


print (get_days_from_today(date))