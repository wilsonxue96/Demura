# [a,b]为区间，e是误差限，k为计算的轮次，x为得到的数值解
import math
import numpy as np
import random
import matplotlib.pyplot as plt

from scipy.optimize import curve_fit

coff = np.loadtxt("E:/code/demura/data/coff.csv", delimiter=",")


def srgb(N):
    return 0.763 * pow(N / 255, 2.2)


def dichotomize(a, b, e, g, i):
    k = 0
    while abs(a - b) / 2 >= e:
        k = k + 1
        x = (a + b) / 2
        if func(x, coff[i, 0], coff[i, 1], coff[i, 2], coff[i, 3], coff[i, 4], srgb(g)) < 0:
            a = x
        elif func(x, coff[i, 0], coff[i, 1], coff[i, 2], coff[i, 3], coff[i, 4], srgb(g)) > 0:
            b = x
        else:
            break
    return x


def func(x, a, b, c, d, e, L):
    return pow(a + b * x + c * pow(x, 2) + d * pow(x, 3) + e * pow(x, 4), 2.2) - L


a = dichotomize(0, 1, 0.001, 192, 0)
