from functionSpaDigiXONEANDSEVEN import getSpaDigiXdingweideshu
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
        year = row['日期'].year
        month = row['日期'].month
        day = row['日期'].day
        for time_period, hour in time_dict.items():
            if time_period == "双支":
                for i in range(0, 12):
                    ridizhi = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][3][1]
                    shichengdizhi = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][4][1]
                    if ridizhi == shichengdizhi:
                        hourr = 2 * i
                        break
                value = getSpaDigiXdingweideshu(year, month, day, hourr)
                df.at[index, time_period] = value

            elif time_period == "双干":
                for i in range(0, 12):
                    riganzhi = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][3]
                    shichengganzhi = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][4]
                    if riganzhi == "甲子" and shichengganzhi == "甲子":
                        for j in range(0, 12):
                            panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                            if panduanwugan == "戊":
                                hourr = 2 * j
                                break
                    elif riganzhi == "甲戌" and shichengganzhi == "甲戌":
                        for j in range(0, 12):
                            panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                            if panduanwugan == "己":
                                hourr = 2 * j
                                break
                    elif riganzhi == "甲申" and shichengganzhi == "甲申":
                        for j in range(0, 12):
                            panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                            if panduanwugan == "庚":
                                hourr = 2 * j
                                break
                    elif riganzhi == "甲寅" and shichengganzhi == "甲子":
                        for j in range(0, 12):
                            panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                            if panduanwugan == "癸":
                                hourr = 2 * j
                                break
                    elif riganzhi == "甲午" and shichengganzhi == "甲午":
                        for j in range(0, 12):
                            panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                            if panduanwugan == "辛":
                                hourr = 2 * j
                                break
                    elif riganzhi == "甲辰" and shichengganzhi == "甲辰":
                        for j in range(0, 12):
                            panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                            if panduanwugan == "壬":
                                hourr = 2 * j
                                break
                    elif riganzhi[0] == "甲" and shichengganzhi[0] == "甲":
                        if riganzhi == "甲子":
                            for j in range(0, 12):
                                panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                                if panduanwugan == "戊":
                                    shuanggan = "戊"
                                    hourr = 2 * j
                                    break
                        elif riganzhi == "甲戌":
                            for j in range(0, 12):
                                panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                                if panduanwugan == "己":
                                    shuanggan = "己"
                                    hourr = 2 * j
                                    break
                        elif riganzhi == "甲辰":
                            for j in range(0, 12):
                                panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                                if panduanwugan == "壬":
                                    shuanggan = "壬"
                                    hourr = 2 * j
                                    break
                        elif riganzhi == "甲寅":
                            for j in range(0, 12):
                                panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                                if panduanwugan == "癸":
                                    shuanggan = "癸"
                                    hourr = 2 * j
                                    break
                        elif riganzhi == "甲申":
                            for j in range(0, 12):
                                panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                                if panduanwugan == "庚":
                                    shuanggan = "庚"
                                    hourr = 2 * j
                                    break
                        elif riganzhi == "甲午":
                            for j in range(0, 12):
                                panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                                if panduanwugan == "辛":
                                    shuanggan = "辛"
                                    hourr = 2 * j
                                    break
                    else:
                        if riganzhi[0] == shichengganzhi[0]:
                            hourr = 2 * i
                            break

                value = getSpaDigiXdingweideshu(year, month, day, hourr)
                df.at[index, time_period] = value
                nianyueriganzhi = getthebasicmessageofnineGrids(year, month, day, hourr)[2]
                df.at[index,"年月日干支时间"]=nianyueriganzhi

            else:
                value = getSpaDigiXdingweideshu(year, month, day, hour)
                df.at[index, time_period] = value
    return df

# Time periods dictionary
time_dict = {"双支":0,"双干": 0}

# Load the Excel file
file_path_source =  '香港2020-2024完整数据生肖版.xlsx'
years = list(range(2020, 2025))

# 在每个元素后面添加'香港'
sheet_names = [str(year) + '年' for year in years]

# 创建 ExcelWriter 对象
output_file_path_updated_source = '240125-定位2020-2024年香港双干双支汇总数据P0.xlsx'
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