import datetime
import pytz
import calendar

# print(time.gmtime(0))
# print(time.time())
# print(time.sleep(3))
#
# start = time.monotonic()
# huge_number = 2 ** 100000000
# elapsed = time.monotonic() - start
# print(f'Портачено секунд {elapsed}')


sarah_birthday = datetime.date(year=1965, month=10, day=28)
print(f'Сара Коннор родилась {sarah_birthday}')

first_day_of_the_rest_of_your_life = datetime.date.today()

print(sarah_birthday.year)
print(sarah_birthday.month)
print(sarah_birthday.day)
print(sarah_birthday.weekday())

lunch_time = datetime.time(hour=12, minute=15, second=30, microsecond=5005)
print(f'Время обеда: {lunch_time}')

monday_lunch_time = datetime.time(hour=12, minute=15, second=30)
tuesday_lunch_time = datetime.time(hour=12, minute=15)
wednesday_lunch_time = datetime.time(hour=12)
print(f'Время обеда: понедельник {monday_lunch_time}, вторник {tuesday_lunch_time}, среда {wednesday_lunch_time}')

# А что если нам учитывать как дату, так и время? Для этого есть класс  datetime.datetime
terminator_time_travel = datetime.datetime(year=1984, month=5, day=12, hour=1, minute=52, second=10, microsecond=1001)
print(f'Терминатор впервые появился в будущем {terminator_time_travel}')
# Как и в модуле time, здесь можно не указывать полностью данные о времени
raise_of_skynet_datetime = datetime.datetime(year=1997, month=8, day=29, hour=10, minute=14)
print(f'Скайнет начал войну {raise_of_skynet_datetime}')
# К отдельным полям можно так же обращаться
print(raise_of_skynet_datetime.year)
print(raise_of_skynet_datetime.hour)

# Для работы с текущим моментом можно использовать метод

print(datetime.datetime.now())

print(f'День, с которого всё началось {terminator_time_travel.strftime("%d.%m.%Y")} !')

print(f'И началось это все в {terminator_time_travel.strftime("%H:%M:%S")}')

# Обратное преобрование выполняется следующим образом
kyle_death = datetime.datetime.strptime('14.05.1985', '%d.%m.%Y')
print(f'Дата смерти Кайла Риза {kyle_death}')
print(f'День, когда это случилось {kyle_death.day}')
print(f'Месяц {kyle_death.month}')
print(f'Год {kyle_death.year}')

# Кроме того, класс datetime обладает интересным свойством combine()
# получая в качестве аргументов объхекты классов date и  time он может их соединить
# создав объект datetime

sarah_birthday_lunch_time = datetime.datetime.combine(sarah_birthday, lunch_time)
print(f'Дата праздничного обеда Сары Коннор {sarah_birthday_lunch_time}')

# datetime так же позволяет производить арифметические операции с датами, для этого есть класс timedelta

end_of_war = datetime.datetime(year=2029, month=7, day=11)

duration_of_the_war = end_of_war - raise_of_skynet_datetime
print(f'Война длилась {duration_of_the_war.days} дней и {duration_of_the_war.seconds}')
# Сам же результат вычислений будет принадлежать новому классу
print(type(duration_of_the_war))
print(f'Закончилась война в {raise_of_skynet_datetime + duration_of_the_war}')
print(f'А ведь могда продлиться {duration_of_the_war * 2}')

war_time = datetime.timedelta(weeks=40, days=11358, hours=13, minutes=36, seconds=600)

imcoming_date = '30-11-2021'
imcoming_date_datetime = datetime.datetime.strptime(imcoming_date, '%d-%m-%Y')

registration_end_time = datetime.datetime(year=2019, month=1, day=1)
if imcoming_date_datetime > registration_end_time:
    print('Отказ в регистрации')
else:
    print('Вы успешно зарегистрированы')

# Про время

print(f'Перечень всех доступных таймзон:, {pytz.all_timezones}')
print(f'В перечне содержится информация о {len(pytz.all_timezones)} таймзонах')

# Как ими пользоваться

print('Asia/Vladivostok' in pytz.all_timezones)  # True

vladivostok_time_zone = pytz.timezone('Asia/Vladivostok')

moscow_time = datetime.datetime.today()
print(f'Московскаое время {moscow_time}')
vladivostok_time = moscow_time.astimezone(vladivostok_time_zone)
print(f'Время во Владивостоке {vladivostok_time}')

# Пример из двух городов России Владивосток и Калининград пришгли две заявки с датой и временем в их часовом поясе
# Нужно узнать, кто из них первым совершил покупку

print('Europe/Kaliningrad' in pytz.all_timezones)
kaliningrad_time_zone = pytz.timezone('Europe/Kaliningrad')
UTC_time_zone = pytz.utc
request_from_vladivostok_str = '2019-06-15T16:22:00 +1000'
request_from_kaliningrad_str = '2019-06-15T16:22:00 +0200'
request_from_vladivostok = datetime.datetime.strptime(request_from_vladivostok_str, '%Y-%m-%dT%H:%M:%S %z')
request_from_kaliningrad = datetime.datetime.strptime(request_from_kaliningrad_str, '%Y-%m-%dT%H:%M:%S %z')
print(f'Время отправки запроса по местному Владивостокскому времени {request_from_vladivostok}')
print(f'Время отправки запроса по местному Калининградскому времени {request_from_kaliningrad}')

print(f'Сравниваем aware {request_from_vladivostok > request_from_kaliningrad}')

# Отформатированную информацию приведем к UTC для сравнения

request_from_vladivostok_UTC = request_from_vladivostok.astimezone(UTC_time_zone)
request_from_kaliningrad_UTC = request_from_kaliningrad.astimezone(UTC_time_zone)
first_request = request_from_vladivostok if request_from_kaliningrad_UTC > request_from_vladivostok_UTC else \
    request_from_kaliningrad_UTC
print(f'Время первого запроса {first_request}')
if request_from_kaliningrad_UTC < request_from_vladivostok_UTC:
    print('Первым пришел заказ из Калининграда')
else:
    print('Первым пришел заказ из Владивостока')

# Модуль календарь

# Позволяет вывести календарь в виде простого текста или в HTML формате

# Создание строчного календаря
calendar_text = calendar.TextCalendar()  # str
# Далее, для отображения нужно уточнить год и месяц
print(calendar_text.formatmonth(2021, 1))

# так же можно создать HTML версию календаря
calendar_html = calendar.HTMLCalendar()
# print(calendar_html.formatmonth(2021, 1))

# Например мы хотим посчитать, сколько рабочих дней (не учитывая праздники) будет в Январе 2025

day_iterator = calendar_text.itermonthdays2(2021, 1)
number_of_working_days = 0

for data, weekday in day_iterator:
    if data > 0 and weekday < 5:
        number_of_working_days += 1
print(f'В январе 2021 года {number_of_working_days} рабочих дней')

# Помимо итераторов, можно вытаскивать из календаря списки дней в месяце
print(f'Дни января в списках по неделям {calendar_text.monthdayscalendar(2021, 1)}')

# Кроме прочего, доступ есть к названиям месяцев или дней недели
for month in calendar.month_name:
    print(month)
print('=' * 20)
for day in calendar.day_name:
    print(day)
