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
                fanhuixinxi = getthebasicmessageofnineGrids(year, month, day, hourr)
                ninegridsbasicmessage = fanhuixinxi[0]
                for i in range(0, 9):
                    if i == 4:
                        pass
                    else:
                        tianpanganshuju = ninegridsbasicmessage[i]["天盘"]
                        if len(tianpanganshuju) == 1 or len(tianpanganshuju) == 3:
                            if shuanggan == tianpanganshuju[-1]:
                                zhishigongdingwei_index = i
                        else:
                            tianpanganshuju_list = tianpanganshuju.split("\n")
                            if shuanggan == tianpanganshuju_list[0][-1] or shuanggan == tianpanganshuju_list[1][-1]:
                                zhishigongdingwei_index = i
                if zhishigongdingwei_index == 0:
                    values = "坎一"
                elif zhishigongdingwei_index == 1:
                    values = "坤二"
                elif zhishigongdingwei_index == 2:
                    values = "震三"
                elif zhishigongdingwei_index == 3:
                    values = "巽四"
                elif zhishigongdingwei_index == 5:
                    values = "乾六"
                elif zhishigongdingwei_index == 6:
                    values = "兑七"
                elif zhishigongdingwei_index == 7:
                    values = "艮八"
                elif zhishigongdingwei_index == 8:
                    values = "离九"

                nianyueriganzhi = getthebasicmessageofnineGrids(year, month, day, hourr)[2]
                df.at[index, time_period] = value
                df.at[index,"年月日干支时间"]=nianyueriganzhi
                df.at[index,"双干"]=shuanggan
                df.at[index,"双干宫"]=values
            else:
                value = getSpaDigiXdingweideshu(year, month, day, hour)
                df.at[index, time_period] = value

    return df

# Time periods dictionary
time_dict = {"双支":0,"双干": 0,"子时":0,"丑时":2,"寅时":4,"卯时":6,"辰时":8,"巳时":10,"午时":12,"未时":14,"申时":16,"酉时":18,"戌时":20,"亥时":22
             }

# Load the Excel file
file_path_source =  '澳门历史数据.xlsx'
years = list(range(2010, 2025))

# 在每个元素后面添加'香港'
sheet_names = [str(year) + '年' for year in years]

# 创建 ExcelWriter 对象
output_file_path_updated_source = '240119-定位2010-2024年澳门汇总数据P0.xlsx'
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