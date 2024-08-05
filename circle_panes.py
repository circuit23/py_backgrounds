import random

import pyautogui
from PIL import Image, ImageDraw

from circles import random_color, create_circle

screen_resolution = pyautogui.size()

image = Image.new('RGB', (screen_resolution.width, screen_resolution.height))
draw = ImageDraw.Draw(image)


def pane_location(screen_resolution) -> (int, int, int, int):
    pane_top_x = random.randint(0, screen_resolution.width)
    pane_top_y = random.randint(0, screen_resolution.height)
    pane_bottom_x = pane_top_x + random.randint(0, screen_resolution.width // 5)
    pane_bottom_y = pane_top_y + random.randint(0, screen_resolution.height // 5)
    return pane_top_x, pane_top_y, pane_bottom_x, pane_bottom_y


def create_pane(pane_top_x, pane_top_y, pane_bottom_x, pane_bottom_y):
    # create a smaller rectangular image, random background color
    # fill the image with randomly colored circles
    # place the rectangle somewhere within the original image using pane_location()
    pass


def main(screen_resolution):
    panes_amount = random.randint(5, 20)
    # using original image, create random amount of panes filled with circles at random locations


if __name__ == '__main__':
    main(screen_resolution)
