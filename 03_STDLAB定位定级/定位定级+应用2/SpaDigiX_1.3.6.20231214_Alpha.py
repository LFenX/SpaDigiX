import pandas as pd
from functionSpaDigiXAPPONE import getthebasicmessageofnineGrids
# 定义计算得分的函数
def calculate_score(row):
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
    print("----------------------------------------------------------------------")
    return values

# 读取上传的文件
file_path = '定级初始表.xlsx'
df = pd.read_excel(file_path)

# 将“日期”列转换为日期格式
df['日期'] = pd.to_datetime(df['日期'])

# 应用计算规则到每一行
df['定级得数'] = df.apply(calculate_score, axis=1)
df['日期'] = df['日期'].dt.strftime('%Y-%m-%d')
# 保存处理后的数据到一个新的 Excel 文件
output_file_path = '双干宫号表澳门.xlsx'
df.to_excel(output_file_path, index=False)
