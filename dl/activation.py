# 激活函数
import numpy as np
import matplotlib.pyplot as plt


# 阶跃函数 支持numpy
def step_fun(x):
    return np.array(x > 0, dtype=int)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def relu(x):
    return np.maximum(0, x)


x = np.arange(-5.0, 5.0, 0.1)
y = step_fun(x)
z = sigmoid(x)
m = relu(x)
plt.plot(x, y, label='阶跃函数')
plt.plot(x, z, label='sigmoid函数')
plt.plot(x, m)
plt.ylim(-0.1, 1.1)
plt.show()
