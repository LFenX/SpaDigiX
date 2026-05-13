import pandas as pd
from functionSpaDigiXAPPONE import getthebasicmessageofnineGrids

# 假设的干支历计算函数
def calculate_score(date):
    if pd.isna(date):
        return None  # 如果日期无效，返回 None 或其他默认值
    year, month, day = date.year, date.month, date.day

    # 确保年月日不是 NaN
    if any(pd.isna(value) for value in [year, month, day]):
        return None

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
    nianyueriganzhi = fanhuixinxi[2]
    ninegridsbasicmessage = fanhuixinxi[0]  # 九宫基本信息
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
    print("-----------------------------------------------------------------------")
    return shuanggan,values

# 处理所有工作表的函数
def process_all_sheets(file_path):
    # 读取 Excel 文件的所有工作表
    xls = pd.ExcelFile(file_path)
    sheet_names = xls.sheet_names

    # 用于存储所有处理过的工作表
    processed_sheets = {}

    for sheet_name in sheet_names:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        df['日期'] = pd.to_datetime(df['日期'], errors='coerce')
        # 对每个工作表的日期列应用 calculate_score 函数，并创建新列 '干支历'
        df['双干识别'], df["双干宫"] = zip(*df['日期'].apply(calculate_score))
        # 将处理过的工作表存储在字典中
        processed_sheets[sheet_name] = df

    return processed_sheets

# 调用函数处理所有工作表
file_path = '240125-定位2020-2024年香港双干双支汇总数据P0.xlsx'
processed_sheets = process_all_sheets(file_path)

# 将所有处理过的工作表导出到一个新的 Excel 文件
output_file_path = '240125-定位2020-2024年香港双干双支汇总数据P0.xlsx'
writer = pd.ExcelWriter(output_file_path, engine='xlsxwriter')

# 遍历字典并将每个 DataFrame 写入不同的工作表
for sheet_name, df in processed_sheets.items():
    df.to_excel(writer, sheet_name=sheet_name, index=False)

# 关闭并保存文件
writer.close()