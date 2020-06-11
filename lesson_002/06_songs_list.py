#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точносттю до долей минут

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ минут
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)

total_songs_time = 0
for song in enumerate(violator_songs_list):
    song1 = 'Halo'
    song2 = 'Enjoy the Silence'
    song3 = 'Clean'
    if song[1][0] == song1 or song[1][0] == song2 or song[1][0] == song3:
        print(song[1][0])
        total_songs_time += song[1][1]
print(f'Общий время звучание песен: {total_songs_time:.2f} минут')
print()
# Есть словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат ХХХ минут

total_songs_time2 = 0
for song in enumerate(violator_songs_dict):
    song1 = 'Sweetest Perfection'
    song2 = 'Policy of Truth'
    song3 = 'Blue Dress'
    if song[1] == song1 or song[1] == song2 or song[1] == song3:
        print(song[1])
        total_songs_time2 += violator_songs_dict[song[1]]
print(f'Общий время звучание песен: {total_songs_time2:.2f} минут')
print()

total_songs_time2 = 0
for song in enumerate(violator_songs_dict):
    song1 = 'Sweetest Perfection'
    song2 = 'Policy of Truth'
    song3 = 'Blue Dress'
    if song[1] != song1 and song[1] != song2 and song[1] != song3:
        print(song[1])
        total_songs_time2 += violator_songs_dict[song[1]]
print(f'Время звучание песен: {total_songs_time2:.2f} минут')
