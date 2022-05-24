import numpy as np
import cv2
import csv
import os

path = 'saperated_image/'
img_list = sorted(os.listdir(path))

for i in range(len(img_list)):
    now_content = []
    src = cv2.imread(path+img_list[i], cv2.IMREAD_GRAYSCALE)
    dst = src.copy().T.reshape(-1)
    label = int(img_list.copy()[i].split('.')[0].split('_')[1])
    now_content.append(f'{label}')
    for j in range(len(dst)):
        now_content.append(f'{dst[j]}')
    final_content = [now_content]
    if i == 0:
        f = open('our_handmade_dataset.csv', 'w', newline='')
        wr = csv.writer(f)
        wr.writerows(final_content)
        f.close()
    else:
        f = open('our_handmade_dataset.csv', 'a', newline='')
        wr = csv.writer(f)
        wr.writerows(final_content)
f.close()


#dst = src.copy().T.reshape(-1)

# dst = dst.reshape(28, 28)
# print(dst.shape)

# print(int(label))
#cv2.imshow('src', cv2.resize(src, (224, 224)))

# dst = src.copy().T
# print(dst.shape)

# cv2.imshow('dst', cv2.resize(dst, (224, 224)))
# cv2.waitKey()