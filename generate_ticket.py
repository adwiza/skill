from io import BytesIO

import requests
from PIL import Image, ImageDraw, ImageFont
from urllib3 import response

TEMPLATE_PATH = 'lesson_016/ticket/ticket-base.png'
FONT_PATH = 'lesson_016/fonts/Roboto-Regular.ttf'
FONT_SIZE = 20
BLACK = (0, 0, 0, 255)
NAME_OFFSET = (390, 300)
EMAIL_OFFSET = (390, 345)
AVATAR_OFFSET = (200, 300)
AVATAR_SIZE = 100



def generate_ticket(name, email):
    base = Image.open(TEMPLATE_PATH).convert('RGBA')
    fnt = ImageFont.truetype(FONT_PATH, FONT_SIZE)

    draw = ImageDraw.Draw(base)
    # draw text, half opacity
    draw.text(NAME_OFFSET, name, font=fnt, fill=BLACK)
    # draw text, full opacity
    draw.text(EMAIL_OFFSET, email, font=fnt, fill=BLACK)
    avatar = Image.open('lesson_016/ticket/avatar.png')
    # response = requests.get(url=f'https://api.adorable.io/avatar/{AVATAR_SIZE}/{email}')
    # avatar_like_file = BytesIO(response.content)
    base.paste(avatar, AVATAR_OFFSET)

    temp_file = BytesIO()
    # with open('lesson_016/ticket/ticket-example.png', 'wb') as f:
    #     base.save(f, 'png')
    base.save(temp_file, 'png')
    temp_file.seek(0)

    # base.show()
    return temp_file
