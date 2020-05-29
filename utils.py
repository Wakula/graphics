from numpy import uint8

from PIL import Image

from pylab import array, gray


def get_grayscaled_image(path_):
    im = array(Image.open(path_).convert('L'))
    gray()
    return im


def save_image(image, path):
    Image.fromarray(image.astype(uint8)).save(path)
