import cv2
import numpy as np
import os

ambient = cv2.VideoCapture('Video00005_ambient.avi')
intensity = cv2.VideoCapture('Video00005_intensity.avi')
range = cv2.VideoCapture('Video00005_range.avi')
success1,image1 = ambient.read()
success2,image2 = intensity.read()
success3,image3 = range.read()
count = 0
while success1:
  image1 = image1[:, :, 0]
  image2 = image2[:, :, 0]
  image3 = image3[:, :, 0]

  image = np.stack((image1, image2, image3), axis=-1)

  if count ==0:
    cv2.imwrite("image1_" + "5" + str(count).zfill(5) +".PNG", image1)
    cv2.imwrite("image2_" + "5"+ str(count).zfill(5) +".PNG", image2)
    cv2.imwrite("image3_" + "5"+ str(count).zfill(5) +".PNG", image3)
    cv2.imwrite("image_" + "5"+ str(count).zfill(5) +".PNG", image)
  cv2.imwrite("../test/images/frame_" + "5" + str(count).zfill(5) +".PNG", image)     # save frame as JPEG file
  success1,image1 = ambient.read()
  success2,image2 = intensity.read()
  success3,image3 = range.read()
  print('Read a new frame: ', success1)
  count += 1
