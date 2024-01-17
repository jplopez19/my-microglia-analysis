from skimage.io import imread_collection
from data_processing import try_all_thresholds, segment_image
from functions import run_vampire_workflow
from visualizations import create_coloring_book
import os

def load_images(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"The path '{path}' does not exist.")
    images = imread_collection(path + '/*.tif') # Updated to TIFF format
    if not images:
        raise ValueError(f"No images found in the directory '{path}'.")
    return images

def main():
    # Path to the directory with images inside the 'tests' folder
    image_path = 'tests' # Updated path to the 'tests' folder

    # Load images from the directory
    images = load_images(image_path)

    # Apply different thresholding methods
    for image in images:
        try_all_thresholds(image)

    # Segment images
    segmented_images = [segment_image(image) for image in images]

    # Run VAMPIRE workflow
    run_vampire_workflow(segmented_images)

    # Create a coloring book
    create_coloring_book(segmented_images)

if __name__ == "__main__":
    main()
