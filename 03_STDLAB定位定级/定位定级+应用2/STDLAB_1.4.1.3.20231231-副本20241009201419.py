import pandas as pd
import numpy as np
from functionSpaDigiXAPPONE import getthebasicmessageofnineGrids
# 定义计算得分的函数
def calculate_score(row):
    row['日期'] = pd.to_datetime(row['日期'], errors='coerce')
    year, month, day = row['日期'].year, row['日期'].month, row['日期'].day
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
    ninegridsbasicmessage = fanhuixinxi[0]  # 九宫基本信息
    yinyangdun_ganzhi = fanhuixinxi[1]  # 阴阳遁和干支信息
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
    if zhishigongdingwei_index==0:
        values="坎一"
    elif zhishigongdingwei_index==1:
        values="坤二"
    elif zhishigongdingwei_index==2:
        values="震三"
    elif zhishigongdingwei_index==3:
        values="巽四"
    elif zhishigongdingwei_index==5:
        values="乾六"
    elif zhishigongdingwei_index==6:
        values="兑七"
    elif zhishigongdingwei_index==7:
        values="艮八"
    elif zhishigongdingwei_index==8:
        values="离九"

    dizhi = row['地支']
    # 根据 values 和地支的组合判断庄家数
    if (values == "坎一" and dizhi in ["酉", "戌", "亥", "子", "丑", "寅"]) or \
            (values == "坤二" and dizhi in ["巳", "午", "未", "申", "酉", "戌"]) or \
            (values == "震三" and dizhi in ["子", "丑", "寅", "卯", "辰", "巳"]) or \
            (values == "巽四" and dizhi in ["寅", "卯", "辰", "巳", "午", "未"]) or \
            (values == "乾六" and dizhi in ["申", "酉", "戌", "亥", "子", "丑"]) or \
            (values == "兑七" and dizhi in ["午", "未", "申", "酉", "戌", "亥"]) or \
            (values == "艮八" and dizhi in ["亥", "子", "丑", "寅", "卯", "辰"]) or \
            (values == "离九" and dizhi in ["卯", "辰", "巳", "午", "未", "申"]):
        zhuangjia_number = 0
    else:
        zhuangjia_number = 1
    print(f"日期：{year}-{month}-{day}-{hour},地支: {dizhi}, 双干宫: {values},庄家数：{zhuangjia_number}")
    print("----------------------------------------------------------------------")
    return pd.Series([zhuangjia_number, shuanggan, values])

# 读取 Excel 文件中的所有工作表
excel_file_path = '新澳门230103_2021-2023特码及地支数据.xlsx'
all_sheets = pd.read_excel(excel_file_path, sheet_name=None)
# 创建一个新的 DataFrame 用于存储结果
result_df = pd.DataFrame()
# 遍历每个工作表
for sheet_name in reversed(all_sheets):
    sheet_data = all_sheets[sheet_name]
    # 删除除日期列、特列、地支列以外的所有列
    columns_to_keep = ['日期', '特', '地支']
    sheet_data = sheet_data[columns_to_keep]
    # 创建新列'庄家数'
    new_columns = sheet_data.apply(calculate_score, axis=1)
    new_columns.columns = ['庄家数', '双干', '双干宫']
    # 将处理后的数据追加到结果 DataFrame
    # 将新列添加到原始数据
    sheet_data = pd.concat([sheet_data, new_columns], axis=1)
    result_df = pd.concat([result_df, sheet_data])
# 保存结果到新的 Excel 文件中，包括庄家数串列
result_df.to_excel('澳门2021-2023庄家模型数据汇总240104.xlsx', index=False)