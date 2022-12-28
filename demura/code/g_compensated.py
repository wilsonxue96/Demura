import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from code.dichotomy import dichotomize
from code.gg_fitting import func_gg


# 理想灰阶-亮度对应曲线
def srgb(N):
    return 0.763 * pow(N / 255, 2.2)


# 原像素灰阶-亮度对应曲线
def func(x, a, b, c, d, e):
    return pow(a + b * x + c * pow(x, 2) + d * pow(x, 3) + e * pow(x, 4), 2.2)


# 原灰阶-亮度对应
lo_16 = np.loadtxt("E:/code/demura/data/ori_data/1/16.csv", delimiter=",")
lo_32 = np.loadtxt("E:/code/demura/data/ori_data/1/32.csv", delimiter=",")
lo_64 = np.loadtxt("E:/code/demura/data/ori_data/1/64.csv", delimiter=",")
lo_128 = np.loadtxt("E:/code/demura/data/ori_data/1/128.csv", delimiter=",")
lo_192 = np.loadtxt("E:/code/demura/data/ori_data/1/192.csv", delimiter=",")

# 求出所有像素五个灰阶下原来灰阶与新的灰阶，并拟合函数，保存至coff_gg

# 原始的五个灰阶
go = np.array((16, 32, 64, 128, 192))
# 修正后五个灰阶下的亮度
an = np.array((srgb(16), srgb(32), srgb(64), srgb(128), srgb(192)))
# 存放每个像素的gg拟合系数
coff_gg = np.empty((200 * 200, 5), dtype=object)
for i in range(40000):
    gn = np.array((dichotomize(0, 1, 0.001, 16, i) * 255, dichotomize(0, 1, 0.001, 32, i) * 255,
                   dichotomize(0, 1, 0.001, 64, i) * 255, dichotomize(0, 1, 0.001, 128, i) * 255,
                   dichotomize(0, 1, 0.001, 192, i) * 255))
    popt, pcov = curve_fit(func_gg, go, gn)
    coff_gg[i, 0] = popt[0]
    coff_gg[i, 1] = popt[1]
    coff_gg[i, 2] = popt[2]
    coff_gg[i, 3] = popt[3]
    coff_gg[i, 4] = popt[4]
    print(i)

# 将coff_gg保存为csv
np.savetxt("E:/code/demura/data/coff_gg.csv", coff_gg, delimiter=",")