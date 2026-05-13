import numpy as np
import matplotlib.pyplot as plt

# 设置参数值
C_W = 75
theta = 0.2
W_0 = 100
W_1 = 50

# 定义函数
def f(b):
    return (C_W * theta * W_0 - (np.exp(-b * C_W * theta * W_1 - 1) / b))

# 绘制图像
b = np.linspace(0, 0.005, 1000)  # 设置 b 的取值范围和分辨率
λ = f(b)  # 计算函数值

plt.figure(figsize=(8, 6))  # 设置图形大小
plt.plot(b, λ , linewidth=2)  # 绘制函数图像
plt.grid(True)  # 添加网格线
plt.xlabel('b')  # 设置 x 轴标签
plt.ylabel('λ')  # 设置 y 轴标签
plt.title('Function Plot')  # 设置图形标题
plt.show()  # 显示图形