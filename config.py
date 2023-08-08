import os

# The path to the directory of images to be processed
IMAGE_DIR = os.path.join(os.path.dirname(__file__), 'images')

# The path to the directory where the labeled images will be saved
LABEL_DIR = os.path.join(os.path.dirname(__file__), 'labeled_images')

# The shape modes to use for coloring the images
SHAPE_MODES = [1, 2, 3, 4, 5]

# The colormap to use for the colored images
COLORMAP = 'twilight'