
import pandas as pd
import numpy as np
import re
import random
from backup_file import  getshuangganshicheng
from functionSpaDigiXONEANDSEVEN_P3_240430  import  getSpaDigiXdingweideshu
zodiac_to_number = {
    '子': 1, '丑': 2, '寅': 3, '卯': 4,
    '辰': 5, '巳': 6, '午': 7, '未': 8,
    '申': 9, '酉': 10, '戌': 11, '亥': 12
}
def calculate_smallest_circular_difference(x, y):
    # 计算两个数在模12意义下的最小差值
    diff1 = (x - y) % 12
    diff2 = (y - x) % 12
    if diff1 == diff2:
        # 如果正负误差绝对值相等，随机选择一个
        return random.choice([diff1, -diff2])
    else:
        # 否则，选择绝对值较小的误差
        return diff1 if diff1 < diff2 else -diff2
def process_workbook(file_path, combined_data):
    excel_data = pd.ExcelFile(file_path)
    all_sheets_data = {}

    for sheet_name in excel_data.sheet_names:
        df = pd.read_excel(excel_data, sheet_name=sheet_name)
        df['日期'] = pd.to_datetime(df['日期'])
        #df['生肖'] = df['生肖'].replace('已', '巳')
        '''
        df['双干程序'] = df.apply(
            lambda row: getSpaDigiXdingweideshu(row['日期'].year, row['日期'].month, row['日期'].day, row["双干时辰"])[0],
            axis=1)
        df['年月日干支时间']= df.apply(
            lambda row: getSpaDigiXdingweideshu(row['日期'].year, row['日期'].month, row['日期'].day, row["双干时辰"])[1],
            axis=1)
        '''
        df['双干时辰'] = df['日期'].apply(lambda x: getshuangganshicheng(x.year, x.month, x.day))
        df['双干宫'] = df.apply(
            lambda row: getSpaDigiXdingweideshu(row['日期'].year, row['日期'].month, row['日期'].day, row["双干时辰"])[
                2],
            axis=1)

        all_sheets_data[sheet_name] = df

    output_path = f'2024-2027香港定位12月份数据pro.xlsx'
    with pd.ExcelWriter(output_path) as writer:
        for sheet_name, data in all_sheets_data.items():
            data.to_excel(writer, sheet_name=sheet_name, index=False)
    return output_path

# 替换以下文件路径
file_paths = [
    '2024-2027香港定位12月份数据.xlsx',
  ]
combined_data = pd.DataFrame()

processed_files = [process_workbook(fp, combined_data) for fp in file_paths]