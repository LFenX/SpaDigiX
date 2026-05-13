import pandas as pd
import numpy as np
from functionSpaDigiXAPPONE import getthebasicmessageofnineGrids
# Load the Excel file
file_path = '第二套澳门庄家实战表格.xlsx'

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
# Apply the function to the '日期' column
df['节气'], df['干支月'] = zip(*df['日期'].apply(calculate_solar_term_and_lunar_month))

# Function to create a string of dealer counts and calculate the ratio of 1s and 0s
def create_ratio_string_corrected(df, start_index, days):
    end_index = start_index + days - 1
    counts = df.loc[start_index:end_index, '庄家数'].astype(str).sum()
    ratio = f"{counts.count('1')}:{counts.count('0')}"
    return f"{counts} ({ratio})"

# Apply the function for 3, 5, 7, 15, and 20 days and update the columns
for days in [3, 5, 7, 15, 20]:
    col_name = f"{days}天"
    df[col_name] = np.nan  # Initialize the column with NaNs
    # Only fill for the first occurrence of each unique solar term
    for index in df['节气'].drop_duplicates(keep='first').index:
        df.loc[index, col_name] = create_ratio_string_corrected(df, index, days)

# Function for creating the ratio string for a range of dealer counts for each unique lunar month
def create_monthly_ratio_string(df, start_index, end_index):
    counts = df.loc[start_index:end_index, '庄家数'].astype(str).sum()
    ratio = f"{counts.count('1')}:{counts.count('0')}"
    return f"{counts} ({ratio})"

# Initialize the '每月01结果' column with NaNs
df['每月01结果'] = np.nan

# Identify the first occurrence of each unique '干支月' and the last index of the DataFrame
first_occurrences_lunar = df['干支月'].drop_duplicates(keep='first').index
last_index = df.index[-1]

# Iterate over the first occurrences of each lunar month
for start_index in first_occurrences_lunar:
    # Find the index of the next change in '干支月', which indicates the end of the current lunar month range
    end_index = df.index[df.index > start_index][df['干支月'][df.index > start_index] != df.at[start_index, '干支月']].min() - 1
    # If the start_index is the last occurrence, go to the end of the dataframe
    if pd.isna(end_index):
        end_index = last_index
    # Get the ratio string for the range from the current start index to the end index
    df.at[start_index, '每月01结果'] = create_monthly_ratio_string(df, start_index, end_index)

# Saving the corrected dataframe to a new Excel file
corrected_output_file_path = '第二套MC澳门庄家实战表格finally240108.xlsx'
df.to_excel(corrected_output_file_path, index=False)

# Output path for confirmation
corrected_output_file_path