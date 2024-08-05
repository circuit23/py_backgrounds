import random
import sys

from PIL import Image, ImageDraw

orig_dimension = 1500


def create_circle(draw, xy, radius=10, fill=None, outline=None, width=1):
    draw.circle(xy, radius, fill=fill, outline=outline, width=width)


def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def main(img_size_x, img_size_y):
    orig_dimension_x, orig_dimension_y = img_size_x, img_size_y
    amount = random.randint(50, 200)
    image = Image.new('RGB', (orig_dimension_x, orig_dimension_y), color=random_color())
    draw = ImageDraw.Draw(image)
    for i in range(0, amount):
        center_xy = (random.randint(0, orig_dimension), random.randint(0, orig_dimension))
        radius = random.randint(20, 150)
        create_circle(draw, center_xy, radius, fill=random_color())
    return image


if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2])).save(
        "Circles/Circles-" + str(sys.argv[1] + "x" + str(sys.argv[1]) + ".jpg"))
