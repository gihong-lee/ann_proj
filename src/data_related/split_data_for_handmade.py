from matplotlib.pyplot import contour
import numpy as np
import cv2
import os

# def mouse_callback(event, x, y, flags, param): 
#     print("x:", x ," y:", y) # 이벤트 발생한 마우스 위치 출력

# img = np.zeros((256, 256, 3), np.uint8)  # 행렬 생성, (가로, 세로, 채널(rgb)),bit)

path = 'project_image/'



file_name_list = os.listdir(path)
# print(file_name_list)

# src = cv2.imread(path+file_name_list[0], cv2.IMREAD_GRAYSCALE)
# result = cv2.cvtColor(src.copy(), cv2.COLOR_GRAY2BGR)
# # cv2.namedWindow('src')
# # cv2.setMouseCallback('src', mouse_callback)

# print(src.shape[:2])
# src[src<100] = 0
# f, s = 0, 1
# for i in range(src.shape[0]-1):
#     a = src[f, 339]-src[s, 339]

#     if a == 255:
#         print("시작",s)
#         result[f,:] = (0, 0, 255)
#         cv2.imshow('result', cv2.resize(result, (200, 1000)))
#         cv2.imshow('result', result)
#         cv2.waitKey()
        
#     elif 0<a <5: 
#         print("끝", f)
#         result[s,:] = (0, 0, 255)
#         cv2.imshow('result', cv2.resize(result, (200, 1000)))
#         # cv2.imshow('result', result)
#         cv2.waitKey()
#         # cv2.circle(result, (s, 200), 10, (255, 0, 0), -1)
#     f +=1
#     s += 1

dst_path = 'saperated_image/'


# src = cv2.imread(path+file_name_list[2], cv2.IMREAD_GRAYSCALE)
x_grid = [[135, 349], [357, 568],[577, 791], [798, 1016], [1022, 1235], [1244, 1457], [1467, 1681], [1688, 1903], [1910, 2125], [2132, 2347]]
y_grid = [[194,498], [506, 808], [817, 1118], [1131, 1430], [1444, 1742], [1757, 2048], [2068, 2368]]

test_folder ='test/'
file_index, i = 0, 0
processing_file_index = 0

for file_index in range(len(file_name_list)):
    src = cv2.imread(path+file_name_list[file_index], cv2.IMREAD_GRAYSCALE)
    image_index, i = 0, 0
    for y_g in y_grid:
        for x_g in x_grid:
            if i > 65:
                break
            elif 35< i <40:
                pass
            else:
                now_image = ~src[y_g[0]:y_g[1], x_g[0]:x_g[1]].copy()
                now_image = cv2.resize(now_image, (28, 28), interpolation=cv2.INTER_AREA)
                cv2.imwrite((dst_path + f'{file_index}_{image_index}.png'), now_image)
                image_index +=1
            i+=1

    processing_file_index+=1

        # cv2.imshow('src', cv2.resize(now_image, (512, 512)))
        # cv2.waitKey()
        


# cv2.imshow('src', result)

# cv2.waitKey()

# for i in range(len(file_name_list)):
#     src = cv2.imread(path+file_name_list[i], cv2.IMREAD_GRAYSCALE)
#     print(src.shape[:2])
#     cv2.imshow('src', cv2.resize(src, (int(src.shape[1]//2.5), int(src.shape[0]//2.5))))
#     cv2.waitKey()