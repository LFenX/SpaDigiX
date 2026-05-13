from functionSpaDigiXONEANDSEVENF1MC   import gettheSpaDigiX_value
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
            if time_period=="双支":
                for i in range(0,12):
                    ridizhi=getthebasicmessageofnineGrids(year,month,day,2*i)[1][3][1]
                    shichengdizhi=getthebasicmessageofnineGrids(year,month,day,2*i)[1][4][1]
                    if ridizhi==shichengdizhi:
                        hourr=2*i
                        break
                value=gettheSpaDigiX_value(year, month, day, hourr,"值使")
                df.at[index, time_period] = value

            elif time_period=="双干":
                for i in range(0,12):
                    riganzhi=getthebasicmessageofnineGrids(year,month,day,2*i)[1][3]
                    shichengganzhi = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][4]
                    if riganzhi=="甲子" and shichengganzhi=="甲子":
                        for j in range(0,12):
                            panduanwugan=getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                            if panduanwugan=="戊":
                                hourr=2*j
                                break
                    elif riganzhi == "甲戌" and shichengganzhi == "甲戌":
                        for j in range(0,12):
                            panduanwugan=getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                            if panduanwugan=="己":
                                hourr=2*j
                                break
                    elif riganzhi == "甲申" and shichengganzhi == "甲申":
                        for j in range(0,12):
                            panduanwugan=getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                            if panduanwugan=="庚":
                                hourr=2*j
                                break
                    elif riganzhi == "甲寅" and shichengganzhi == "甲子":
                        for j in range(0,12):
                            panduanwugan=getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                            if panduanwugan=="癸":
                                hourr=2*j
                                break
                    elif riganzhi == "甲午" and shichengganzhi == "甲午":
                        for j in range(0,12):
                            panduanwugan=getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                            if panduanwugan=="辛":
                                hourr=2*j
                                break
                    elif riganzhi == "甲辰" and shichengganzhi == "甲辰":
                        for j in range(0,12):
                            panduanwugan=getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                            if panduanwugan=="壬":
                                hourr=2*j
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
                        if riganzhi[0]==shichengganzhi[0]:
                            hourr=2*i
                            break

                value = gettheSpaDigiX_value(year, month, day, hourr,"值使")
                df.at[index, time_period] = value

            else:
                value = gettheSpaDigiX_value(year, month, day, hour,"值使")
                df.at[index, time_period] = value
    return df
# Time periods dictionary
#time_dict = {"双支":0,"双干":0,"子时":0,"丑时":2,"寅时":4,"卯时":6,"辰时":8,"巳时":10,"午时":12,"未时":14,"申时":16,"酉时":18,"戌时":20,"亥时":22}

time_dict = {"子时":0,"午时":12,"酉时":18}
# Load the Excel file
file_path_source = '定位、定级验证灵数误差表初始2MCF1.xlsx'
sheet_names = ['2020年',"2021年","2022年","2023年","2024年"]
# Reading data from the sheets, including the error sheets
data_1_source = pd.read_excel(file_path_source, sheet_name=sheet_names[0], parse_dates=['日期'], date_parser=pd.to_datetime)
data_2_source = pd.read_excel(file_path_source, sheet_name=sheet_names[1], parse_dates=['日期'], date_parser=pd.to_datetime)
data_3_source = pd.read_excel(file_path_source, sheet_name=sheet_names[2], parse_dates=['日期'], date_parser=pd.to_datetime)
data_4_source = pd.read_excel(file_path_source, sheet_name=sheet_names[3], parse_dates=['日期'], date_parser=pd.to_datetime)
data_5_source = pd.read_excel(file_path_source, sheet_name=sheet_names[4], parse_dates=['日期'], date_parser=pd.to_datetime)
# Perform calculations on the source sheets
data_1_calculated_source = perform_new_calculations_corrected(data_1_source.copy(), time_dict)
data_2_calculated_source = perform_new_calculations_corrected(data_2_source.copy(), time_dict)
data_3_calculated_source = perform_new_calculations_corrected(data_3_source.copy(), time_dict)
data_4_calculated_source = perform_new_calculations_corrected(data_4_source.copy(), time_dict)
data_5_calculated_source = perform_new_calculations_corrected(data_5_source.copy(), time_dict)
# Calculate errors and update the error sheets for both '澳门定位误差' and '香港定位误差'
# Formatting the date column in the calculated dataframes
data_1_calculated_source['日期'] = data_1_calculated_source['日期'].dt.strftime('%Y-%m-%d')
data_2_calculated_source['日期'] = data_2_calculated_source['日期'].dt.strftime('%Y-%m-%d')
data_3_calculated_source['日期'] = data_3_calculated_source['日期'].dt.strftime('%Y-%m-%d')
data_4_calculated_source['日期'] = data_4_calculated_source['日期'].dt.strftime('%Y-%m-%d')
data_5_calculated_source['日期'] = data_5_calculated_source['日期'].dt.strftime('%Y-%m-%d')
output_file_path_updated_source = 'F1MC澳门2020-2024按年分编码四_子_午_酉_时结果240122.xlsx'
with pd.ExcelWriter(output_file_path_updated_source, engine='openpyxl') as writer:
    data_1_calculated_source.to_excel(writer, sheet_name=sheet_names[0], index=False)
    data_2_calculated_source.to_excel(writer, sheet_name=sheet_names[1], index=False)
    data_3_calculated_source.to_excel(writer, sheet_name=sheet_names[2], index=False)
    data_4_calculated_source.to_excel(writer, sheet_name=sheet_names[3], index=False)
    data_5_calculated_source.to_excel(writer, sheet_name=sheet_names[4], index=False)
    # Apply center alignment to all cells in all worksheets
    workbook = writer.book
    for worksheet_name in workbook.sheetnames:
        worksheet = workbook[worksheet_name]
        apply_center_alignment_to_all_cells(worksheet)