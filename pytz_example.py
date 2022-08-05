import pytz
import datetime

from datetime import date
from datetime import datetime

# tashkent = 'Asia/Tashkent'
# tz_tashkent = pytz.timezone(tashkent)
# tashkent_time = datetime.datetime.now(tz=tz_tashkent)
# print(tashkent_time)
#
#
# thailand = 'Asia/Bangkok'
# tz_thailand = pytz.timezone(thailand)
# thailand_time = datetime.datetime.now(tz=tz_thailand)
#
# print(thailand_time)


# print(datetime.datetime.today())
# print(datetime.datetime.now(None))
# print(datetime.datetime.utcnow())

# for tz in pytz.all_timezones:
#     print(tz)
# for country in pytz.country_names:
#     print(country, pytz.country_names[country], pytz.country_timezones.get(country))


# today = date.today()
# print(today)
# print(today.day)
# print(today.month)
# print(today.year)

# date_1 = date(2022, 3, 6)
# date_2 = date(2019, 12, 21)
# diff = date_1 - date_2
# print(diff)
# print(type(date_1))
# print(type(date_2))
# print(type(diff))

# today = date.today()
# print(today)
# birthday = date(today.year, 6, 24)
# if birthday < today:
#     birthday = birthday.replace(year=today.year + 1)
# print(birthday)
#
# days_until_birthday = birthday - today
# print(f'You will celebrate your birthday in {days_until_birthday.days} days!')
#
# week_day = date(2022, 6, 24).weekday()


# if my_birthday == 0:
#     my_birthday = 'Monday'
# elif my_birthday == 1:
#     my_birthday = 'Tuesday'
# elif my_birthday == 2:
#     my_birthday = 'Wednesday'
# elif my_birthday == 3:
#     my_birthday = 'Thursday'
# elif my_birthday == 4:
#     my_birthday = 'Friday'
# elif my_birthday == 5:
#     my_birthday = 'Saturday'
# else:
#     my_birthday = 'Sunday'

# print(my_birthday)
#
# today = date.today()
# week_day = today.weekday()
# print(week_day)
# week_day = today.isoweekday()
# print(week_day)

# year = int(input('Please enter a year: '))
# month = int(input('Please enter a month: '))
# day = int(input('Please enter a day: '))
# date_to_find = date(year, month, day)
# week_day = date_to_find.weekday()
# if week_day == 0:
#     week_day = 'Monday'
# elif week_day == 1:
#     week_day = 'Tuesday'
# elif week_day == 2:
#     week_day = 'Wednesday'
# elif week_day == 3:
#     week_day = 'Thursday'
# elif week_day == 4:
#     week_day = 'Friday'
# elif week_day == 5:
#     week_day = 'Saturday'
# else:
#     week_day = 'Sunday'
#
# print(f'{date_to_find} is {week_day}')

# def sec_per_hour(hour):
#     sec = hour * 60 * 60
#     return sec
#
#
# sec_per_day = sec_per_hour(24)
# print(sec_per_day)
# sec_per_week = sec_per_day * 7
# print(sec_per_week)
# sec_per_month = sec_per_day * 30
# print(sec_per_month)


# today = datetime(2022, 3, 7)
# time_stamp = datetime.timestamp(today)
# today_now = datetime.now()
# print(today)
# print(today_now)

# time_stamp = datetime.timestamp(today)
# print(time_stamp)
# time_stamp_now = datetime.timestamp(today_now)
# print(time_stamp_now)

# today = datetime(2022, 3, 10)
# print(today)
# time_stamp = datetime.timestamp(today)
# print(time_stamp)
# today_from_timestamp = datetime.fromtimestamp(time_stamp)
# print(today_from_timestamp)
# today_format = today.strftime('%d %B %Y')
# print('Today is', today_format)
# print('Today is', today.strftime('%A'))

today = datetime.today()
print(today)
utc_today = today.utcnow()
print(utc_today)
print(today.date())
print(today.time())
print(today.isocalendar())
print(today.isoformat())

