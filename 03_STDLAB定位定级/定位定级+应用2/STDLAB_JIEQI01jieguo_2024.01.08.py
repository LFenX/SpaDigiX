import pandas as pd
import numpy as np
from functionSpaDigiXAPPONE import  getthebasicmessageofnineGrids
# Load the Excel file
file_path = '第二套香港庄家实战表格.xlsx'

# Read the first sheet of the Excel file
df = pd.read_excel(file_path, sheet_name=0)

# Simple function to calculate solar term (节气) and lunar month (干支月)
def calculate_solar_term_and_lunar_month(date):
    year=date.year
    month=date.month
    day=date.day
    for i in range(0, 12):
        riganzhi = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][3]
        shichengganzhi = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][4]
        if riganzhi == "甲子" and shichengganzhi == "甲子":
            for j in range(0, 12):
                panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][4][0]
                if panduanwugan == "戊":
                    shuanggan = "戊"
                    hour = 2 * j
                    break
        elif riganzhi == "甲戌" and shichengganzhi == "甲戌":
            for j in range(0, 12):
                panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][4][0]
                if panduanwugan == "己":
                    shuanggan = "己"
                    hour = 2 * j
                    break
        elif riganzhi == "甲申" and shichengganzhi == "甲申":
            for j in range(0, 12):
                panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][4][0]
                if panduanwugan == "庚":
                    shuanggan = "庚"
                    hour = 2 * j
                    break
        elif riganzhi == "甲寅" and shichengganzhi == "甲子":
            for j in range(0, 12):
                panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][4][0]
                if panduanwugan == "癸":
                    shuanggan = "癸"
                    hour = 2 * j
                    break
        elif riganzhi == "甲午" and shichengganzhi == "甲午":
            for j in range(0, 12):
                panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][4][0]
                if panduanwugan == "辛":
                    shuanggan = "辛"
                    hour = 2 * j
                    break
        elif riganzhi == "甲辰" and shichengganzhi == "甲辰":
            for j in range(0, 12):
                panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][4][0]
                if panduanwugan == "壬":
                    shuanggan = "壬"
                    hour = 2 * j
                    break
        elif riganzhi[0] == "甲" and shichengganzhi[0] == "甲":
            if riganzhi == "甲子":
                for j in range(0, 12):
                    panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                    if panduanwugan == "戊":
                        shuanggan = "戊"
                        hour = 2 * j
                        break
            elif riganzhi == "甲戌":
                for j in range(0, 12):
                    panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                    if panduanwugan == "己":
                        shuanggan = "己"
                        hour = 2 * j
                        break
            elif riganzhi == "甲辰":
                for j in range(0, 12):
                    panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                    if panduanwugan == "壬":
                        shuanggan = "壬"
                        hour = 2 * j
                        break
            elif riganzhi == "甲寅":
                for j in range(0, 12):
                    panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                    if panduanwugan == "癸":
                        shuanggan = "癸"
                        hour = 2 * j
                        break
            elif riganzhi == "甲申":
                for j in range(0, 12):
                    panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                    if panduanwugan == "庚":
                        shuanggan = "庚"
                        hour = 2 * j
                        break
            elif riganzhi == "甲午":
                for j in range(0, 12):
                    panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                    if panduanwugan == "辛":
                        shuanggan = "辛"
                        hour = 2 * j
                        break
        else:
            if riganzhi[0] == shichengganzhi[0]:
                shuanggan = riganzhi[0]
                hour = 2 * i
                break
    fanhuixinxi = getthebasicmessageofnineGrids(year, month, day, hour)  # 通过应用0获得排盘的基本信息
    yinyangdun_ganzhi = fanhuixinxi[1]  # 阴阳遁和干支信息
    yueganzhi= yinyangdun_ganzhi[2]
    jieqi= yinyangdun_ganzhi[5]
    print("---------------------------------------------------------------------------")
    return jieqi , yueganzhi
df['日期'] = pd.to_datetime(df['日期'], errors='coerce')
df['节气'], df['干支月'] = zip(*df['日期'].apply(calculate_solar_term_and_lunar_month))

# Identify the first occurrence of each unique solar term
unique_solar_terms = df['节气'].unique()
first_occurrences_solar = df['节气'].isin(unique_solar_terms).cumsum().drop_duplicates().index
selected_rows_solar = df.loc[first_occurrences_solar]
def create_ratio_string_corrected(df, start_index, days):
    end_index = start_index + days - 1
    counts = df.loc[start_index:end_index, '庄家数'].astype(str).sum()
    ratio = f"{counts.count('1')}:{counts.count('0')}"
    return f"{counts} ({ratio})"
#for days in [3, 5, 7,15, 20, 25]:
# Apply the function for 3, 5, 7, and 15 days
for days in [3, 5, 7, 10]:
    col_name = f"{days}天"
    df[col_name] = np.nan  # Initialize the column with NaNs
    for index in selected_rows_solar.index:
        df.loc[index, col_name] = create_ratio_string_corrected(df, index, days)

# Identify the first occurrence of each unique lunar month
# 新逻辑：找到干支月每次变化的地方
changes_in_lunar_month = df['干支月'].ne(df['干支月'].shift())
first_occurrences_lunar = df.index[changes_in_lunar_month]

# 为了确保代码的正确性，我们在这里重新初始化'每月01结果'列
df['每月01结果'] = np.nan
def create_monthly_ratio_string(df, start_index, end_index):
    counts = df.loc[start_index:end_index, '庄家数'].astype(str).sum()
    ratio = f"{counts.count('1')}:{counts.count('0')}"
    return f"{counts} ({ratio})"

# 修改后的迭代逻辑
for start_index in first_occurrences_lunar:
    # 如果不是最后一个月份，找到下一个月份开始的索引
    if start_index != first_occurrences_lunar[-1]:
        next_month_start_index = first_occurrences_lunar[first_occurrences_lunar > start_index].min()
        end_index = next_month_start_index - 1
    else:
        # 如果是最后一个月份，结束索引为DataFrame的最后一个索引
        end_index = df.index[-1]

    # Get the ratio string for the range from the current start index to the end index
    # 调用已有的函数来计算比率字符串
    df.at[start_index, '每月01结果'] = create_monthly_ratio_string(df, start_index, end_index)
# Save the modified dataframe to a new Excel file
output_file_path = 'NEWProcessed_第二套香港庄家实战表格240113.xlsx'
df.to_excel(output_file_path, index=False)

print(f"Processed data saved to {output_file_path}")

