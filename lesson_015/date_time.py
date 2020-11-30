import datetime
import time

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