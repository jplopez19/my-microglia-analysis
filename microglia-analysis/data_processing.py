from skimage.filters import (
    threshold_isodata, threshold_li, threshold_mean,
    threshold_minimum, threshold_otsu, threshold_triangle, threshold_yen
)
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

def try_all_thresholds(image):
    # Convert to grayscale if the image is in color
    if len(image.shape) == 3:
        image = rgb2gray(image)

    fig, ax = plt.subplots(nrows=3, ncols=4, figsize=(10, 10))
    methods = [
        "Original", "Isodata", "Li", "Mean",
        "Minimum", "Otsu", "Triangle", "Yen"
    ]
    images = [
        image, threshold_isodata(image), threshold_li(image),
        threshold_mean(image), threshold_minimum(image),
        threshold_otsu(image), threshold_triangle(image),
        threshold_yen(image)
    ]
    for i, img in enumerate(images):
        ax[i // 4, i % 4].imshow(img, cmap='gray')
        ax[i // 4, i % 4].set_title(methods[i])
        ax[i // 4, i % 4].axis('off')
    plt.show()

def segment_image(image, method='otsu'):
    # Convert to grayscale if the image is in color
    if len(image.shape) == 3:
        image = rgb2gray(image)

    if method == 'otsu':
        return threshold_otsu(image)
    elif method == 'li':
        return threshold_li(image)
    else:
        raise ValueError("Invalid method")
