import pytest
from microglia_analysis import main  # Update the import path
from skimage.io import imread_collection

def test_load_images():
    # Test the load_images function
    image_path = 'tests'  # Path to the 'tests' folder with sample images
    images = main.load_images(image_path)
    assert isinstance(images, imread_collection.ImageCollection)
    assert len(images) > 0

def test_main():
    # Test the main function (integration test)
    # This test assumes that the 'tests' folder contains sample images for testing
    main.main()
    # Add assertions to check the results, such as output files, segmented images, etc.
    # The specific assertions will depend on the expected outcomes of the main function

# Add more test cases for other functions or workflows in main.py if needed
