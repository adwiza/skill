import cv2

image_cv2 = cv2.imread('python_snippets/external_data/girl.jpg')
# Загрузка происходит не в привычном нам RGB, а в BGR


# Создадим небольшую функцию для отображения изображений в окнах windows:


def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


viewImage(image_cv2, 'Телка')

# Возможности OpenCV:

# Ресайз слайсами
cropped = image_cv2[250:2000, 100:1500]
viewImage(cropped, 'Cropped version')

# Процентное изменение размера
scale_percent = 20  # % от начального размера
width = int(image_cv2.shape[1] * scale_percent / 100)
height = int(image_cv2.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(image_cv2, dim, interpolation=cv2.INTER_AREA)
viewImage(resized, 'Resized version')

# Изменение цветовой гаммы:

gray_image = cv2.cvtColor(image_cv2, cv2.COLOR_BGR2GRAY)
viewImage(gray_image, 'Gray version')
# grey_image это одноканальная версия изображения

# Рисование на изображениях

image_with_line = image_cv2.copy()
# Для отрисовки линии необходимы координаты начала и конца, цвет линии и ширина линии
cv2.line(image_with_line, (1000, 100), (1000, 2000), (0, 255, 0), 10)
viewImage(image_with_line, 'Line')

image_with_rectangle = image_cv2.copy()
cv2.rectangle(image_with_rectangle, (100, 100), (1500, 2000), (0, 255, 255), 10)
viewImage(image_with_rectangle, 'Rectangle')
# Для отрисовки прямоугольника необходимы координаты левого верхнего и правого нижнего углов,
# цвет линии и её ширина



