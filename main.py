import numpy as np
import cv2
import os
import random
import skimage
import matplotlib.pyplot as plt
#批量修改图片
path=r'C:\Users\86183\Desktop\2brain\picture2'
path_1 = r'C:\Users\86183\Desktop\pic2'
for filename in os.listdir(path):
    # if filename.endswith('.bmp'):  #代表结尾是bmp格式的
    img_path = path + '/' + filename
    img = cv2.imread(img_path)
    p2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    out_name = filename.split('.')[0]
    save_name = path_1 + '/' + out_name + '.jpg'
    cv2.imwrite(save_name,p2)

'''

p2=cv2.blur(p1,(9,9))
#p2=cv2.cvtColor(p1,cv2.COLOR_BGR2GRAY)
#cv2.imshow("1",p1)
#cv2.imshow("2",p2)
#cv2.waitKey(0)

'''
#p1=cv2.imread(r"C:\Users\86183\Desktop\pictures\10.jpg")
#cv2.imwrite("C:\Users\86183\Desktop\2brain\picture2\110.jpg",p2)