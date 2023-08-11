from skimage.filters import (
    threshold_isodata, threshold_li, threshold_mean,
    threshold_minimum, threshold_otsu, threshold_triangle, threshold_yen
)
from skimage.color import rgb2gray
from skimage.transform import resize
from skimage.morphology import binary_dilation, binary_erosion
import matplotlib.pyplot as plt
import numpy as np

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

    # Resize the image (optional, you can set the desired size)
    resized_image = resize(image, (512, 512))

    # Apply the selected thresholding method
    if method == 'otsu':
        thresh_value = threshold_otsu(resized_image)
    elif method == 'li':
        thresh_value = threshold_li(resized_image)
    else:
        raise ValueError("Invalid method")

    # Threshold the image
    binary_image = resized_image > thresh_value

    # Apply morphological operations
    dilated_image = binary_dilation(binary_image)
    segmented_image = binary_erosion(dilated_image)

    return segmented_image
