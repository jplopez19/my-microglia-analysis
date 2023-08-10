from skimage.io import imread_collection
from data_processing import try_all_thresholds, segment_image
from functions import run_vampire_workflow
from visualization import create_coloring_book

def load_images(path):
    images = imread_collection(path + '/*.tif') # Updated to TIFF format
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

    # Run VAMPIRE workflow (You'll need to complete the implementation in functions.py)
    run_vampire_workflow(segmented_images)

    # Create a coloring book (You'll need to complete the implementation in visualization.py)
    create_coloring_book(segmented_images)

if __name__ == "__main__":
    main()
