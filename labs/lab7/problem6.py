#   Sa se scrie un script care afiseaza in ce zi a saptamanii este anul nou,
#   pentru ultimii x ani (x este dat ca argument).
import datetime


weekdays = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}


def day_of_week(x):
    if x > 2018:
        print("Invalid number of years")
        return

    today = datetime.date.today()
    days_per_year = 365

    new_year_date = today + datetime.timedelta(days=20)

    while x > 0:
        x_years_ago_date = new_year_date - datetime.timedelta(days=(x * days_per_year))
        weekday = x_years_ago_date.weekday()
        print(str(x) + " years ago: " + str(x_years_ago_date) + " " + str(weekdays.get(weekday)))
        x -= 1


day_of_week(5)
