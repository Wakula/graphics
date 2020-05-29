from utils import (
    save_image,
    get_grayscaled_image
)
from constants import MAX_BIT_VALUE


def get_negative_image(image):
    return MAX_BIT_VALUE - image


def get_clamped_image(image, start, end):
    delta = end - start
    return (start / MAX_BIT_VALUE) * image + delta


def get_darker_image(image, coefficient):
    return MAX_BIT_VALUE * (image / MAX_BIT_VALUE) ** coefficient


if __name__ == '__main__':
    image = get_grayscaled_image('images/kitten.jpg')
    negative_image = get_negative_image(image)
    clamped_image = get_clamped_image(image, 100, 200)
    brighter_image = get_darker_image(image, 3)

    save_image(negative_image, 'images/negative_kitten.jpg')
    save_image(clamped_image, 'images/clamped_kitten.jpg')
    save_image(brighter_image, 'images/darker_kitten.jpg')
