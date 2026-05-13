import pandas as pd
import re

# 读取Excel文件
excel_file = "澳门历史数据2010-2024含生肖.xlsx"
df = pd.read_excel(excel_file, sheet_name=None)

# 定义地支对应表
zodiac_mapping = {
    "鼠": "子",
    "牛": "丑",
    "虎": "寅",
    "兔": "卯",
    "龙": "辰",
    "蛇": "巳",
    "马": "午",
    "羊": "未",
    "猴": "申",
    "鸡": "酉",
    "狗": "戌",
    "猪": "亥",
}

# 遍历每个工作表
for sheet_name, sheet_data in df.items():
    '''
    # 提取生肖
    sheet_data["生肖"] = sheet_data["特码"].apply(
        lambda x: re.search(r"([鼠牛虎兔龙蛇马羊猴鸡狗猪])", str(x)).group(1) if re.search(
            r"([鼠牛虎兔龙蛇马羊猴鸡狗猪])", str(x)) else None)
    '''
    # 添加新列"地支"
    sheet_data["地支"] = sheet_data["地支"].map(zodiac_mapping)

# 保存修改后的Excel文件
with pd.ExcelWriter("澳门历史数据2010-2024含生肖地支.xlsx") as writer:
    for sheet_name, sheet_data in df.items():
        sheet_data.to_excel(writer, sheet_name=sheet_name, index=False)
