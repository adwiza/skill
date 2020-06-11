#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.

first_movie = my_favorite_movies[0:10]
second_movie = my_favorite_movies[12:25]
third_movie = my_favorite_movies[27:33]
fourth_movie = my_favorite_movies[35:40]
last_movie = my_favorite_movies[42:57]
print(first_movie)
print(last_movie)
print(fourth_movie)
