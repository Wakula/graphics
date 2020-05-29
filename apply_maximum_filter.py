from utils import (
    save_image,
    get_grayscaled_image
)

from scipy.ndimage.filters import maximum_filter


def get_maximum_filtered_image(image, *, size):
    return (
        maximum_filter(image, size)
    )


if __name__ == '__main__':
    image = get_grayscaled_image('images/kitten.jpg')
    maximum_filtered_image = get_maximum_filtered_image(image, size=5)
    save_image(maximum_filtered_image, 'images/maximum_filtered_kitten.jpg')
