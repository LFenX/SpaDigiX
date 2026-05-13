from functionSpadigiXAPPTHREEANDTHREEG_4_1_MC import getdingjideshu
from functionSpaDigiXAPPONE import getthebasicmessageofnineGrids
import pandas as pd
from openpyxl.styles import Alignment
# Function to apply center alignment to all cells in a worksheet
def apply_center_alignment_to_all_cells(ws):
    """Apply center alignment to all cells in an Excel worksheet."""
    for row in ws.iter_rows():
        for cell in row:
            cell.alignment = Alignment(horizontal='center')

# Corrected function to perform the new calculations
def perform_new_calculations_corrected(df, time_dict):
    """ Perform new calculations with corrected date handling. """
    for index, row in df.iterrows():
        row['日期'] = pd.to_datetime(row['日期'], errors='coerce')
        year = row['日期'].year
        month = row['日期'].month
        day = row['日期'].day
        for time_period, hour in time_dict.items():
            value = getdingjideshu(year, month, day, hour)[0]
            df.at[index, time_period] = value
            nianyueriganzhi = getthebasicmessageofnineGrids(year, month, day, hour)[2]
            df.at[index,"年月日干支时间"]=nianyueriganzhi
    return df

# Time periods dictionary
time_dict = {"子时":0,"丑时":2,"寅时":4,"卯时":6,"辰时":8,"巳时":10,"午时":12,"未时":14,"申时":16,"酉时":18,"戌时":20,"亥时":22
             }

# Load the Excel file
file_path_source =  '定级12时辰香港初始表格.xlsx'
years = list(range(2024, 2025))

# 在每个元素后面添加'香港'
sheet_names = [str(year) + '香港' for year in years]

# 创建 ExcelWriter 对象
output_file_path_updated_source = '240303-定级G4-12时辰MC澳门2024结果.xlsx'
with pd.ExcelWriter(output_file_path_updated_source, engine='openpyxl') as writer:
    # 读取每个表格并进行相同的操作
    for sheet_name in sheet_names:
        # 读取数据
        data_source = pd.read_excel(file_path_source, sheet_name=sheet_name, parse_dates=['日期'])

        # 执行新的计算
        data_calculated_source = perform_new_calculations_corrected(data_source.copy(), time_dict)

        # 格式化日期列
        data_calculated_source['日期'] = data_calculated_source['日期'].dt.strftime('%Y-%m-%d')

        # 保存结果到 Excel 文件的不同工作表
        data_calculated_source.to_excel(writer, sheet_name=sheet_name, index=False)
