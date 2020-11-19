import os

from PIL import Image, ImageDraw, ImageFont


class PostCardmaker:

    def __init__(self, name, template=None, font_path=None):
        self.name = name
        self.template = 'post_card.jpg' if template is None else template
        if font_path is None:
            self.font_path = os.path.join('fonts', 'ofont_ru_DS Eraser2.ttf')
        else:
            self.font_path = font_path

    def make(self):

        im = Image.open(self.template)

        w, h = im.size
        resized_im = im.resize((w // 2, h // 2))

        draw = ImageDraw.Draw(resized_im)
        font = ImageFont.truetype(self.font_path, size=30)
        y = resized_im.size[1] - 20 - font.size
        draw.text((10, y), 'hello', font=font, fill='red')
        resized_im.show()
        # resized_im.save('probe.jpg')
