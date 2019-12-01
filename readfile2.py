# encoding: UTF-8
import glob as gb
import cv2

#Returns a list of all folders with participant numbers
img_path = gb.glob("e:\PYTHON\image\*.jpg")
for path in img_path:
  img = cv2.imread(path)
  cv2.imshow('img',img)
  cv2.waitKey(2000)
  print('how to know what is the difference')
  print('add this line and see what will happen')
