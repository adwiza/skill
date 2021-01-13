# -*- coding: utf-8 -*-

# Задача: взять изображения коллег с сайта, пририсовать усы и сохранить в базу
import bs4
import requests
import cv2
import peewee

# Шаг - 1 Выкачиваем все картинки https://skillbox.ru/course/profession-python/

html = requests.get('https://skillbox.ru/course/profession-python/').text

soup = bs4.BeautifulSoup(html, 'html.parser')

all_images = soup.find_all('img')

# print('\n'.join(str(t.get('data-src', t.get('src'))) for t in all_images))

downloaded_files = set()

for tag in all_images:
    url = tag.get('data-src', tag.get('src'))
    if url:
        filename = url.split('/')[-1]
        filename_full = f'pics/{filename}'
        if filename_full in downloaded_files:
            filename_full = f'pics/1{filename}'
        downloaded_files.add(filename_full)
        with open(f'{filename_full}', 'wb') as f:
            f.write(requests.get(url).content)


def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def draw_mustache(image, x, y, w, h):
    m_w = w * 2 // 4
    m_h = h // 10
    m_x = x + w // 2 - m_w // 2
    m_y = y + h * 2 // 3
    hair_w = max(m_w // 30, 1)
    for dx in range(m_w // hair_w):
        # cv2.rectangle(image, (m_x, m_y), (m_x + m_w, m_y + m_h), (255, 255, 0), 2)
        cv2.line(image, (m_x + hair_w * dx, m_y), (m_x + hair_w * (dx + 1), m_y + m_h), (0, 0, 0), 1)
        cv2.line(image, (m_x + hair_w * dx, m_y + m_h), (m_x + hair_w * (dx + 1), m_y), (0, 0, 0), 1)


database = peewee.SqliteDatabase('Mustached.db')


# Чтобы создать таблицу в нашей БД, нам нужно создать класс
class Mustached(peewee.Model):
    name = peewee.CharField()  # От типа столбца зависит тип данный, которые мы можем в него записать

    class Meta:
        database = database


Mustached.create_table()

# Шаг - 2  Распознаём лица

for image_path in downloaded_files:
    image = cv2.imread(image_path)
    face_cascade = cv2.CascadeClassifier('python_snippets/external_data/haarcascade_frontalface_default.xml')
    try:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    except cv2.error:
        continue
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(10, 10),
    )
    if len(faces):
        # print(image_path)

        # Шаг 3 - рисование усов
        for (x, y, w, h) in faces:
            draw_mustache(image, x, y, w, h)

# Шаг 4 - пишем в базу
        mustached_image_path = image_path.replace('pics', 'photos_result')
        cv2.imwrite(mustached_image_path, image)
        Mustached.create(name=mustached_image_path)

print(list(Mustached.select()))

