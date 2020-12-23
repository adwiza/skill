from PIL import Image, ImageDraw
import time

image = Image.open('python_snippets/external_data/mm_andy.jpg')  # Загружаем изображение
pixels = image.load()  # Загружаем значение пикселов
draw = ImageDraw.Draw(image)  # Создаем кисточку
width = image.size[0]
height = image.size[1]  # Определяем высоту

# print(f'Ширина изображения {width} высота изображения {height}')


# Первому сделаем негатив

def negative(pix):
    for i in range(width//2):
        for j in range(height//2 - 75):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            draw.point((i, j), (255 - a, 255 - b, 255 - c))


# Второму сделаем оттенки сегого
def gray_shapes(pix):
    for i in range(width//2, width):
        for j in range(height//2 - 75):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            s = (a + b + c) // 3
            draw.point((i, j), (s, s, s))


# Третьему сделаем эффект sepia
def sepia(pix):
    depth = 30
    for i in range(width//2):
        for j in range(height//2 - 75, height - 75):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            s = (a + b + c) // 3
            a = s + depth * 2
            b = s + depth
            c = c
            if a > 255:
                a = 255
            if b > 255:
                b = 255
            if c > 255:
                c = 255
            draw.point((i, j), (a, b, c))


# start = time.monotonic()
# negative(pixels)
# sepia(pixels)
# gray_shapes(pixels)
# result = time.monotonic() - start
# print(f'Все 3 функции выполнились за {result} секунд')

# Удаляем кисть и сохраняем результаты
# del draw
# image.save('mm_effects.jpg', 'JPEG')

# Обрезка изображений
img_to_crop = image.crop((150, 75, width//2, height//2 - 75))
img_to_crop.save('mm_cropped.jpg', 'JPEG')

# Ресайз и поворот
img_to_resize = img_to_crop
img_to_resize.thumbnail((1024, 1024))
img_to_resize = img_to_resize.rotate(180)
img_to_resize.save('mm_resize_rotate.jpg', 'JPEG')

# Наложение одного изображения на другое
# Координатами задается положение левого верхнего угла
# Изображения, которое вставляют, на бОльшем изображении.

img_to_paste = Image.open('mm_effects.jpg')
img_to_paste.paste(img_to_resize, (width//2 - 512, height//2 - 588))
img_to_paste.save('mm_paste.jpg', 'JPEG')


