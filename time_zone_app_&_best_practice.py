import pytz
import datetime

# for country in pytz.country_names:
#     print(country, pytz.country_names[country], pytz.country_timezones.get(country))

# timezone_dict = {
#     'AD': ('Andorra', 'Europe/Andorra'),
#     'AE': ('United Arab Emirates', 'Asia/Dubai'),
#     'AF': ('Afghanistan', 'Asia/Kabul'),
#     'AG': ('Antigua & Barbuda', 'America/Antigua'),
#     'AI': ('Anguilla', 'America/Anguilla'),
#     'AL': ('Albania', 'Europe/Tirane'),
#     'AM': ('Armenia', 'Asia/Yerevan')
# }
#
# for key in timezone_dict:
#     print(key, timezone_dict[key])
#
# print('Please enter a two-letters code of the country to choose the timezone (or "q" to quit).')
#
#
# while True:
#     country_code = input('Enter here: ')
#
#     if country_code == 'q':
#         break
#     elif country_code in timezone_dict.keys():
#         timezone = pytz.timezone(timezone_dict[country_code][1])
#         print('Local time is {}'.format(datetime.datetime.now(tz=timezone)))
#         print('UTC time is {}'.format(datetime.datetime.utcnow()))

iso_format_string = '%Y-%m-%dT%H:%M:%S%z'
now_utc = datetime.datetime.now(pytz.timezone('UTC'))
print(now_utc.strftime(iso_format_string))

# now_asia_tas = now_utc.astimezone(pytz.timezone('Asia/Tashkent'))
# print(now_asia_tas.strftime(iso_format_string))
#
# now_thailand_bangkok = now_utc.astimezone(pytz.timezone('Asia/Bangkok'))
# print(now_thailand_bangkok.strftime(iso_format_string))

naive_now = datetime.datetime.now()
print(naive_now)

tashkent_timezone = pytz.timezone('Asia/Tashkent')
local_datetime = tashkent_timezone.localize(naive_now)
print(local_datetime)

# all_time_zones = pytz.all_timezones
# for timezone in all_time_zones:
#     print(timezone)

