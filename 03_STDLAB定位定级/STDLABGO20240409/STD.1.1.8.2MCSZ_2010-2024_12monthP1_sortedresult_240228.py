import pandas as pd
from functionSpaDigiXONEANDSEVEN_P2_240418 import getSpaDigiXdingweideshu
from functionSpaDigiXAPPONE import getthebasicmessageofnineGrids

# 原始数据文件路径
input_file_path = '工作簿1.xlsx'
# 输出文件路径
output_file_path = '丑月干支历.xlsx'

# 使用XlsxWriter引擎创建Pandas Excel写入器
with pd.ExcelWriter(output_file_path, engine='xlsxwriter') as writer:
    # 遍历2010年至2024年
    for year in range(2010, 2011):
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
                if riganzhi == "甲子" and shichengganzhi == "甲子":
                    for j in range(0, 12):
                        panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                        if panduanwugan == "戊":
                            shuanggan = "戊"
                            hour = 2 * j
                            break
                elif riganzhi == "甲戌" and shichengganzhi == "甲戌":
                    for j in range(0, 12):
                        panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                        if panduanwugan == "己":
                            shuanggan = "己"
                            hour = 2 * j
                            break
                elif riganzhi == "甲申" and shichengganzhi == "甲申":
                    for j in range(0, 12):
                        panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                        if panduanwugan == "庚":
                            shuanggan = "庚"
                            hour = 2 * j
                            break
                elif riganzhi == "甲寅" and shichengganzhi == "甲子":
                    for j in range(0, 12):
                        panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                        if panduanwugan == "癸":
                            shuanggan = "癸"
                            hour = 2 * j
                            break
                elif riganzhi == "甲午" and shichengganzhi == "甲午":
                    for j in range(0, 12):
                        panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                        if panduanwugan == "辛":
                            shuanggan = "辛"
                            hour = 2 * j
                            break
                elif riganzhi == "甲辰" and shichengganzhi == "甲辰":
                    for j in range(0, 12):
                        panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
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
            value = getSpaDigiXdingweideshu(year, month, day, hour)
            label = getthebasicmessageofnineGrids(year, month, day, hour)[1][2][1]
            nianyueriganzhi = getthebasicmessageofnineGrids(year, month, day, hour)[2]

            return value, label, nianyueriganzhi
            #return  nianyueriganzhi
            #return value


        # 应用组合函数
        df['双干程序'], df['标签'], df['年月日干支时间'] = zip(*df['日期'].apply(calculate_and_label))
        #df['双干程序'] = zip(*df['日期'].apply(calculate_and_label))
        #df['年月日干支时间'] = zip(*df['日期'].apply(calculate_and_label))
        # 创建并填充每个标签的工作表
        sheets_data = {f"{label}月": pd.DataFrame() for label in ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']}
        for index, row in df.iterrows():
            sheet_name = f"{row['标签']}月"
            row_data = pd.DataFrame([row.drop('标签')])
            sheets_data[sheet_name] = pd.concat([sheets_data[sheet_name], row_data], ignore_index=True)

        # 将每个数据框写入不同的工作表并调整列宽
        for sheet_name, data in sheets_data.items():
            data.to_excel(writer, sheet_name=f"{year}_{sheet_name}", index=False)