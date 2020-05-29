from utils import (
    get_grayscaled_image,
    save_image
)

from skimage import img_as_int

import numpy

from scipy import ndimage


def _detect_edges_with_operator(image, operator):
    prewitt_vertical = numpy.array(
        operator,
        dtype='float64'
    )
    return ndimage.convolve(
        img_as_int(image), prewitt_vertical)


def detect_edges_with_vertical_operator(image):
    vertical_operator = [
            [-1, 0, 1],
            [-1, 0, 1],
            [-1, 0, 1]
        ]
    return _detect_edges_with_operator(image, vertical_operator)


def detect_edges_with_horizontal_operator(image):
    horizontal_operator = [
        [-1, -1, 1],
        [0, 0, 0],
        [1, 1, 1]
    ]
    return _detect_edges_with_operator(image, horizontal_operator)


if __name__ == '__main__':
    image = get_grayscaled_image('images/kitten.jpg')
    horizontally_transformed_image = detect_edges_with_horizontal_operator(image)
    vertically_transformed_image = detect_edges_with_vertical_operator(image)
    save_image(horizontally_transformed_image, 'images/horizontally_transformed_kitten.jpg')
    save_image(vertically_transformed_image, 'images/vertically_transformed_image.jpg')
