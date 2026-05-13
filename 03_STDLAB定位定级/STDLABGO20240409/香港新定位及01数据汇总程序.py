import pandas as pd

# Load the data
file_path = '香港2023-2024-新定位数据一阶段.xlsx'
data = pd.read_excel(file_path)

# Define the mapping rules for generating new values
rules = {
    "坎一": ["酉", "戌", "亥", "子", "丑", "寅"],
    "坤二": ["巳", "午", "未", "申", "酉", "戌"],
    "震三": ["子", "丑", "寅", "卯", "辰", "巳"],
    "巽四": ["寅", "卯", "辰", "巳", "午", "未"],
    "乾六": ["申", "酉", "戌", "亥", "子", "丑"],
    "兑七": ["午", "未", "申", "酉", "戌", "亥"],
    "艮八": ["亥", "子", "丑", "寅", "卯", "辰"],
    "离九": ["卯", "辰", "巳", "午", "未", "申"]
}

# Helper function to apply the rules
def calculate_new_value(values, dizhi):
    if dizhi in rules.get(values, []):
        return 0
    else:
        return 1

# Columns to apply the rules on
time_columns = ['子时', '丑时', '寅时', '卯时', '辰时', '巳时', '午时', '未时', '申时', '酉时', '戌时', '亥时']

# Processing each time column
for column in time_columns:
    data[column] = data.apply(lambda row: f"{row[column]}{calculate_new_value(row['双干宫'], row[column])}", axis=1)

# Save the modified data to a new Excel file
output_file_path = '香港2023-2024-新定位及01数据汇总数据初始.xlsx'
data.to_excel(output_file_path, index=False)
