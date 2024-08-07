import numpy as np

X = np.array([1.0, 0.5])  # 输入
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])  # 第一层权重
B1 = np.array([0.1, 0.2, 0.3])  # 第一层偏置

print(X.shape)
print(W1.shape)
print(B1.shape)

A1 = np.dot(X, W1) + B1
print(A1)
