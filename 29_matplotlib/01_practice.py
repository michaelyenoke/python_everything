import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(1)
print(np.random.rand(4,3))

N = 100

# 第一位同学， 成绩平平大约在85分左右， 比较稳定
rand1 = np.random.normal(0, 1, N)
print(rand1)
avg1 = 85
std1 = np.rint(avg1 + rand1) #整個過程就是湊一個隨機數
print(std1)
plt.plot(std1)
plt.ylim(50, 100) # 設定y座標
plt.show()

