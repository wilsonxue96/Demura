import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from code.dichotomy import dichotomize
from code.gg_fitting import func_gg

plt.rcParams['font.sans-serif'] = ['SimHei']

# 原同一灰阶下亮度系数
coff_gb = np.loadtxt("E:/code/demura/data/coff.csv", delimiter=",")

# 补偿后灰阶-灰阶系数
coff_gg = np.loadtxt("E:/code/demura/data/coff_gg.csv", delimiter=",")


# 灰阶-亮度曲线形式
def func(x, a, b, c, d, e):
    return pow(a + b * x + c * pow(x, 2) + d * pow(x, 3) + e * pow(x, 4), 2.2)


std_ori = np.empty((256, 1), dtype=object)  # 原来每个灰阶下的标准差
std_n = np.empty((256, 1), dtype=object)  # 补偿后每个灰阶下的标准差
li = np.empty((200 * 200, 1), dtype=object)  # 原来每个灰阶下每个像素的亮度
g_n = np.empty((200 * 200, 1), dtype=object)  # 补偿后的新灰阶
li_n = np.empty((200 * 200, 1), dtype=object)  # 补偿后每个灰阶下每个像素的亮度

for i in range(256):
    for j in range(200 * 200):
        li[j] = func(i / 255, coff_gb[j, 0], coff_gb[j, 1], coff_gb[j, 2], coff_gb[j, 3], coff_gb[j, 4])

        g_n[j] = func_gg(i, coff_gg[j, 0], coff_gg[j, 1], coff_gg[j, 2], coff_gg[j, 3], coff_gg[j, 4])
        # 使新灰阶在0-255范围内
        if g_n[j] < 0:
            g_n[j] = 0
        if g_n[j] > 255:
            g_n[j] = 255
        li_n[j] = func(g_n[j] / 255, coff_gb[j, 0], coff_gb[j, 1], coff_gb[j, 2], coff_gb[j, 3], coff_gb[j, 4])
    std_ori[i] = np.std(li)
    std_n[i] = np.std(li_n)
    print(i)

np.savetxt("E:/code/demura/data/std_ori.csv", std_ori, delimiter=",")
np.savetxt("E:/code/demura/data/std_n.csv", std_n, delimiter=",")
