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

    def make(self, resize=False, out_path=None):
        im = Image.open(self.template)
        if resize:
            w, h = im.size
            im = im.resize((w // 2, h // 2))
        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype(self.font_path, size=26)
        y = im.size[1] - 10 - (10 + font.size) * 2
        message = f'Привет {self.name}!'
        draw.text((10, y), message, font=font, fill='red')
        y = im.size[1] - 20 - font.size
        message = f'С праздником тебя!'
        draw.text((10, y), message, font=font, fill='red')
        # im.show()
        out_path = out_path if out_path else 'postcard.jpg'
        im.save(out_path)
        print(f'Postcard saved as {out_path}')


if __name__ == '__main__':
    maker = PostCardmaker(name='Вася')
    maker.make(resize=True)
