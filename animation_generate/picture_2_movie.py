import numpy as np
import cv2

#讀取一張圖片
size = (1009,348)
print(size)

#完成寫入物件的建立，第一個引數是合成之後的影片的名稱，第二個引數是可以使用的編碼器，第三個引數是幀率即每秒鐘展示多少張圖片，第四個引數是圖片大小資訊
videowrite = cv2.VideoWriter(r'D:\Users\xkllkx\Desktop\all_program\picture_2_movie\f_w\test.mp4',-1,20,size)#20是幀數，size是圖片尺寸
img_array=[]
for filename in [r'D:\Users\xkllkx\Desktop\all_program\picture_2_movie\f_w\{0}.png'.format(i) for i in range(81)]:
    img = cv2.imread(filename)
    if img is None:
        print(filename + " is error!")
        continue
    img_array.append(img)
for i in range(81):
    videowrite.write(img_array[i])
print('end!')