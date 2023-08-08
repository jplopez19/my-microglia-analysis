import numpy as np
import matplotlib.image as mpimg 
import matplotlib.pyplot as plt
import pandas as pd
import cv2
from PIL import Image
import os


def c(x):
  col = plt.cm.twilight(x)
  fig, ax = plt.subplots(figsize=(1,1))
  fig.set_facecolor(col)
  ax.axis("off")
  plt.show()

def color_image(im_file_path, csv_file_path, label_save_file_path):

  #Reading in the image and its labels
  img = mpimg.imread(im_file_path)
  csv_df = pd.read_csv(csv_file_path)

  #Getting the file path from the file name
  im_file_name_split = im_file_path.split('/')
  length = len(im_file_name_split)
  file_name = im_file_name_split[length-1]

  mask = np.zeros(np.asarray(img.shape)+2, dtype=np.uint8)

  csv_df = csv_df[csv_df.Filename == file_name]
  csv_df = csv_df.reset_index(drop=True)

  for shapes in range(len(csv_df)):
    shape_mode = (csv_df['Shape mode'][shapes]).astype(int)
    start_pt = (csv_df['X'][shapes], csv_df['Y'][shapes])
    area =csv_df['Area'][shapes]

    if img[csv_df['Y'][shapes]][csv_df['X'][shapes]]== 1:
      if shape_mode==1: #0.5
        cv2.floodFill(img, mask, start_pt, 0, flags=0)
        mask[mask == 1] = 128

      elif shape_mode==2: #0.047
        cv2.floodFill(img, mask, start_pt, 0, flags=0)
        mask[mask == 1] = 12
      elif shape_mode==3: #0.7
        cv2.floodFill(img, mask, start_pt, 0, flags=0)
        mask[mask == 1] = 179

      elif shape_mode==4: #0.33
        cv2.floodFill(img, mask, start_pt, 0, flags=0)
        mask[mask == 1] = 85

      elif shape_mode==5: #0.9
        cv2.floodFill(img, mask, start_pt, 0, flags=0)
        mask[mask == 1] = 230

      if shapes == len(csv_df)-1:
        mask = mask[1:-1, 1:-1]
        mask[0][0] = 255

        mask = mask.astype('float')
        mask[mask==0] = np.nan

        plt.imshow(mask,cmap='twilight')
        plt.tick_params(
          axis='x',
          which='both',
          bottom=False,
          top=False,
          labelbottom=False)
        plt.yticks([])
        plt.savefig(str(label_save_file_path + str(shape_mode) + file_name), bbox_inches = 'tight',
        pad_inches = 0)

        #img_to_save = Image.fromarray(mask)
        #img_to_save.save(str(label_save_file_path + str(shape_mode) + file_name))
