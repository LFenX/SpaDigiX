import pandas as pd
import numpy as np
import re
import random
from backup_file import  getshuangganshicheng
from functionSpaDigiXONEANDSEVEN_P3MC_240515  import  getSpaDigiXdingweideshu
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
        df['生肖'] = df['生肖'].replace('已', '巳')
        #df['双干时辰'] = df['日期'].apply(lambda x: getshuangganshicheng(x.year, x.month, x.day))
        df['双干程序'] = df.apply(
            lambda row: getSpaDigiXdingweideshu(row['日期'].year, row['日期'].month, row['日期'].day)[0],
            axis=1)
        #df['年月日干支时间']= df.apply(
            #lambda row: getSpaDigiXdingweideshu(row['日期'].year, row['日期'].month, row['日期'].day, row["双干时辰"])[1],
           # axis=1)
        #df['双干宫'] = df.apply(
            #lambda row: getSpaDigiXdingweideshu(row['日期'].year, row['日期'].month, row['日期'].day, row["双干时辰"])[
               # 2],
            #axis=1)
        #df['预测生肖'] = df['预测生肖'].astype(str)  # 确保标签列是字符串类型

        for index, row in df.iterrows():
            if pd.notnull(row['生肖']):  # 检查生肖列是否有数据
                real_number = str(row['实数'])  # 强制转换为字符串
                digit_match = re.search(r'\d+\.?\d*', real_number)
                shengxiao_match = re.search(r'[^\d]+', real_number)

                if digit_match and shengxiao_match:
                    digit_part = float(digit_match.group())
                    shengxiao = shengxiao_match.group().strip()
                    combined_value = digit_part + row['双干程序']

                    if combined_value > 1:
                        new_number = round(combined_value - 1)
                    elif -1 < combined_value <= 1:
                        new_number = -1 if -1 < combined_value < 0 else 0
                    else:
                        new_number = round(combined_value)

                    SSSX = zodiac_to_number.get(shengxiao, 0)
                    new_number = new_number + SSSX

                    # 新的BIAOQIAN计算方法
                    if new_number > 12:
                        BIAOQIAN = new_number % 12 if new_number % 12 != 0 else 12
                    elif new_number == 0:
                        BIAOQIAN = 12
                    elif new_number < 0:
                        BIAOQIAN = 12 - ((-new_number) % 12)
                    else:
                        BIAOQIAN = new_number

                    label_zodiac = {v: k for k, v in zodiac_to_number.items()}.get(BIAOQIAN, '')
                    df.at[index, '预测生肖'] = label_zodiac

                    SX = zodiac_to_number.get(row['生肖'], 0)
                    WUCHA = calculate_smallest_circular_difference(SX, BIAOQIAN)
                    df.at[index, '误差值'] = WUCHA
        all_sheets_data[sheet_name] = df

    output_path = f'240606澳门定位P3-10-27逐年数据.xlsx'
    with pd.ExcelWriter(output_path) as writer:
        for sheet_name, data in all_sheets_data.items():
            data.to_excel(writer, sheet_name=sheet_name, index=False)
    return output_path

# 替换以下文件路径
file_paths = [
    '澳门定位P3-10-27逐年-240525最新数据_澳门历史数据_含有实数.xlsx',
  ]
combined_data = pd.DataFrame()

processed_files = [process_workbook(fp, combined_data) for fp in file_paths]