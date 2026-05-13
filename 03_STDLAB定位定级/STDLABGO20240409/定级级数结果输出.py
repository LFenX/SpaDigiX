import pandas as pd

# 加载Excel文件
file_path = '香港2023-2024-新定级数据一阶段.xlsx'
data = pd.read_excel(file_path)

# 定义一个函数来根据指定的规则转换数字为文字
def transform_rating(value):
    if 0 <= value <= 1:
        return '一'
    elif 1 < value <= 2:
        return '二'
    elif 2 < value <= 3:
        return '三'
    elif 3 < value <= 4:
        return '四'
    else:
        return value  # 或者对超出[0,4]范围的值进行其他处理

# 假设需要转换的列是从'子时定级程序'到'亥时定级程序'
columns_to_transform = [
    '子时定级程序', '丑时定级程序', '寅时定级程序', '卯时定级程序', '辰时定级程序',
    '巳时定级程序', '午时定级程序', '未时定级程序', '申时定级程序', '酉时定级程序',
    '戌时定级程序', '亥时定级程序'
]
# 对指定列应用转换函数
for column in columns_to_transform:
    data[column] = data[column].apply(transform_rating)

# 将转换后的数据保存回Excel文件
output_path = '香港2023-2024-新定级级数数据输出.xlsx'
data.to_excel(output_path, index=False)
