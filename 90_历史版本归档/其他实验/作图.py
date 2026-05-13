import pandas as pd

# 读取原始Excel文件
file_path = 'C:\\Users\\LFen\\Desktop\\SDXCode\\定位定级+应用2\\澳门2021-2024庄家模型数据汇总240125.xlsx'
df = pd.read_excel(file_path)

# 将日期列转化为datetime格式，设定错误处理方式为'coerce'
df['日期'] = pd.to_datetime(df['日期'], errors='coerce')

# 删除无法解析的日期行
df = df.dropna(subset=['日期'])

# 将日期列格式化为文本格式
df['日期'] = df['日期'].dt.strftime('%Y-%m-%d')

# 保存DataFrame到Excel文件
df.to_excel(file_path, index=False)

