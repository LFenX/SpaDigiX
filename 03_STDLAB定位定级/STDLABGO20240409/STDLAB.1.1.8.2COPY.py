import pandas as pd
from functionSpaDigiXONEANDSEVEN_P3_240430  import getSpaDigiXdingweideshu
from functionSpaDigiXAPPONE import getthebasicmessageofnineGrids

# 原始数据文件路径
input_file_path = '2024-2027香港.xlsx'
# 输出文件路径
output_file_path = '2024-2027香港定位12月份数据.xlsx'

# 创建一个空的DataFrame字典，用于存储每个月份的数据
sheets_data = {f"{label}月": pd.DataFrame() for label in ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']}

# 遍历2010年至2024年
for year in range(2024, 2028):
    # 读取对应年份的工作表
    df = pd.read_excel(input_file_path, sheet_name=f"{year}年")

    # 格式化'日期'列，仅包含年、月、日
    df['日期'] = pd.to_datetime(df['日期']).dt.strftime('%Y-%m-%d')

    # 定义计算和标签的组合函数
    def calculate_and_label(date):
        date = pd.to_datetime(date)  # 将字符串转换回datetime以进行计算
        year = date.year
        month = date.month
        day = date.day
        for i in range(0, 12):
            riganzhi = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][3]
            shichengganzhi = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][4]
            if riganzhi == "甲子" and shichengganzhi[0] == "甲":
                for j in range(0, 12):
                    panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                    riganzhi = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][3]
                    if panduanwugan == "戊":
                        hourr = 2 * j
                        label = "甲子"
                        break
            elif riganzhi == "甲戌" and shichengganzhi[0] == "甲":
                for j in range(0, 12):
                    panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                    riganzhi = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][3]
                    if panduanwugan == "己":
                        hourr = 2 * j
                        label = "甲戌"
                        break
            elif riganzhi == "甲申" and shichengganzhi[0] == "甲":
                for j in range(0, 12):
                    panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                    riganzhi = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][3]
                    if panduanwugan == "庚":
                        hourr = 2 * j
                        label = "甲申"
                        break
            elif riganzhi == "甲寅" and shichengganzhi[0] == "甲":
                for j in range(0, 12):
                    panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                    riganzhi = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][3]
                    if panduanwugan == "癸":
                        hourr = 2 * j
                        label = "甲寅"
                        break
            elif riganzhi == "甲午" and shichengganzhi[0] == "甲":
                for j in range(0, 12):
                    panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                    riganzhi = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][3]
                    if panduanwugan == "辛":
                        hourr = 2 * j
                        label = "甲午"
                        break
            elif riganzhi == "甲辰" and shichengganzhi[0] == "甲":
                for j in range(0, 12):
                    panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                    riganzhi = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][3]
                    if panduanwugan == "壬":
                        hourr = 2 * j
                        label = "甲辰"
                        break
            else:
                if riganzhi[0] == shichengganzhi[0]:
                    hourr = 2 * i
                    label = f"双{riganzhi[0]}"
                    break
        value = getSpaDigiXdingweideshu(year, month, day, hourr)[0]
        nianyueriganzhi = getthebasicmessageofnineGrids(year, month, day, hourr)[2]
        label = getthebasicmessageofnineGrids(year, month, day, hourr)[1][2][1]
        return value, label, nianyueriganzhi

    # 应用组合函数

    df['双干程序'], df["标签"],df["年月日干支时间"] = zip(*df['日期'].apply(calculate_and_label))
    # 追加数据到相应的月份DataFrame中
    for index, row in df.iterrows():
        sheet_name = f"{row['标签']}月"
        row_data = pd.DataFrame([row])
        sheets_data[sheet_name] = pd.concat([sheets_data[sheet_name], row_data], ignore_index=True)

# 使用XlsxWriter引擎创建Pandas Excel写入器，并将数据写入不同的工作表
with pd.ExcelWriter(output_file_path, engine='xlsxwriter') as writer:
    for sheet_name, data in sheets_data.items():
        data.to_excel(writer, sheet_name=sheet_name, index=False)