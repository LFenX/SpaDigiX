import numpy as np
import pandas as pd
from PyEMD import EMD
import matplotlib.pyplot as plt

# 提供的数据
data = {
    "日期": ["2023-04-25", "2023-04-26", "2023-04-27", "2023-04-28", "2023-04-29",
             "2023-04-30", "2023-05-01", "2023-05-02", "2023-05-03", "2023-05-04",
             "2023-05-05", "2023-05-06", "2023-05-07", "2023-05-08", "2023-05-09"],
    "数字": [15, 49, 41, 1, 28, 44, 30, 42, 21, 35, 22, 11, 2, 31, 35]
}

# 将数据转换为DataFrame
df = pd.DataFrame(data)
df['日期'] = pd.to_datetime(df['日期'])
df.set_index('日期', inplace=True)

# 应用EMD分解
series = df['数字'].values
emd = EMD()
imfs = emd(series)

# 绘制IMFs
plt.figure(figsize=(12, 8))
for i, imf in enumerate(imfs):
    plt.subplot(len(imfs) + 1, 1, i + 1)
    plt.plot(df.index, imf)
    plt.title(f'IMF {i+1}')
plt.subplot(len(imfs) + 1, 1, len(imfs) + 1)
plt.plot(df.index, series)
plt.title('Original Series')
plt.tight_layout()
plt.show()
