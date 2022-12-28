import numpy as np
import random
from scipy.optimize import curve_fit

# 由给定五个灰阶下的亮度值拟合每个像素的灰阶-亮度曲线

# 读取样品1的灰阶-亮度信息
a_16 = np.loadtxt("E:/code/demura/data/ori_data/1/16.csv", delimiter=",")
a_32 = np.loadtxt("E:/code/demura/data/ori_data/1/32.csv", delimiter=",")
a_64 = np.loadtxt("E:/code/demura/data/ori_data/1/64.csv", delimiter=",")
a_128 = np.loadtxt("E:/code/demura/data/ori_data/1/128.csv", delimiter=",")
a_192 = np.loadtxt("E:/code/demura/data/ori_data/1/192.csv", delimiter=",")


# 灰阶-亮度曲线形式
def func(x, a, b, c, d, e):
    return pow(a + b * x + c * pow(x, 2) + d * pow(x, 3) + e * pow(x, 4), 2.2)


# 拟合各个灰阶的灰阶-亮度曲线，把系数保存至coff.csv
coff = np.empty((200 * 200, 5), dtype=object)  # 存放每个像素的abcde
grey = np.array([16 / 255, 32 / 255, 64 / 255, 128 / 255, 192 / 255])   # 归一化灰阶
js = 0
for i in range(200):
    for j in range(200):
        x1 = a_16[i, j]
        x2 = a_32[i, j]
        x3 = a_64[i, j]
        x4 = a_128[i, j]
        x5 = a_192[i, j]

        light = np.array([x1, x2, x3, x4, x5])
        popt, pcov = curve_fit(func, grey, light)
        # 获取popt里面是拟合系数
        coff[js, 0] = popt[0]
        coff[js, 1] = popt[1]
        coff[js, 2] = popt[2]
        coff[js, 3] = popt[3]
        coff[js, 4] = popt[4]

        print('js=', js, '\n')
        js += 1

np.savetxt("E:/code/demura/data/coff.csv", coff, delimiter=",")
