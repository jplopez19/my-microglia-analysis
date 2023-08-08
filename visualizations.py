import numpy as np
import matplotlib.image as mpimg 
import matplotlib.pyplot as plt
import pandas as pd
import cv2
from PIL import Image
import os

def plot_image(image):
  plt.imshow(image)
  plt.show()

def plot_multiple_images(images):
  for image in images:
    plot_image(image)

def plot_histogram(data):
  plt.hist(data)
  plt.show()

def plot_bar_chart(data):
  plt.bar(data)
  plt.show()

def plot_pie_chart(data):
  plt.pie(data)
  plt.show()