from functionSpaDigiXONEANDSEVEN_P3_240430  import getSpaDigiXdingweideshu
from functionSpaDigiXAPPONE import getthebasicmessageofnineGrids
import pandas as pd
import math
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
    for i in range(0, 9):
        if i == 4:
            pass
        else:
            tianpanganshuju = ninegridsbasicmessage[i]["天盘"]
            if len(tianpanganshuju) == 1 or len(tianpanganshuju) == 3:
                if shuanggan == tianpanganshuju[-1]:
                    shuanggandingwei_index = i
            else:
                tianpanganshuju_list = tianpanganshuju.split("\n")
                if shuanggan == tianpanganshuju_list[0][-1] or shuanggan == tianpanganshuju_list[1][-1]:
                    shuanggandingwei_index = i
    shuangganlist={0:"坎",1:"坤", 2:"震",3:"巽",5:"乾",6:"兑",7:"艮",8:"离"}
    for i in shuangganlist:
        if i==shuanggandingwei_index:
            shuanggangong=shuangganlist[i]
    value = getSpaDigiXdingweideshu(year, month, day, hour)
    yinyangdun_ganzhi = fanhuixinxi[1]  # 阴阳遁和干支信息
    zhishigongdingwei_index=yinyangdun_ganzhi[6]
    for i in shuangganlist:
        if i == zhishigongdingwei_index:
            zhishigong = shuangganlist[i]
    for i in range(0, 9):
        if i == 4:
            pass
        else:
            bashenpanbie = ninegridsbasicmessage[i]["八神"]
            if "值符" == bashenpanbie:
                zhifugongdingwei_index = i
    for i in shuangganlist:
        if i == zhifugongdingwei_index:
            zhifugong = shuangganlist[i]
    q=f"{zhishigong}-日时{shuanggangong}-值符{zhifugong}"
    row["值使宫-日宫-值符宫"]=q
    yinyangdun_ganzhi = fanhuixinxi[1]  # 阴阳遁和干支信息
    yinyangdun=yinyangdun_ganzhi[0][1]
    qiju=yinyangdun_ganzhi[9]
    w=f"{shuanggangong}-{yinyangdun}-{qiju}局"
    row["双干宫-阴阳-九局"] = w
    # 将得到的五个值分别分配给对应的列
    #row['双干程序'] = value
    riganzhi = getthebasicmessageofnineGrids(year, month, day, hour)[1][3]
    #row['年月日干支时间'] = getthebasicmessageofnineGrids(year, month, day, hourr)[2]
    row["日干支"] = riganzhi

    return row
# 创建一个空的 DataFrame 用于存储所有结果
result_df = pd.DataFrame()
# 遍历每年的工作表
for sheet_name in ["子月","丑月","寅月","卯月","辰月","巳月","午月","未月","申月","酉月","戌月","亥月"]:
    sheet_name = sheet_name
    try:
        # 读取上传的文件，并指定工作表名称
        file_path = '香港2010-2027-60甲子数据初始.xlsx'
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        # 将“日期”列转换为日期格式
        df['日期'] = pd.to_datetime(df['日期'])
        # 应用计算规则到每一行
        df = df.apply(calculate_score, axis=1)
        df['日期'] = df['日期'].dt.strftime('%Y-%m-%d')
        # 将当前年份的结果添加到总结果中
        result_df = pd.concat([result_df, df], ignore_index=True)

        print(f'处理完成 {sheet_name} 年的数据')

    except pd.errors.ImproperExcelHeader:
        print(f'在 {sheet_name} 找不到工作表: {sheet_name}')

# 定义日干支映射
gan_zhi_mapping = {
    0: ["甲子", "乙丑", "丙寅", "丁卯", "戊辰", "己巳", "庚午", "辛未", "壬申", "癸酉"],
    1: ["甲戌", "乙亥", "丙子", "丁丑", "戊寅", "己卯", "庚辰", "辛巳", "壬午", "癸未"],
    2: ["甲申", "乙酉", "丙戌", "丁亥", "戊子", "己丑", "庚寅", "辛卯", "壬辰", "癸巳"],
    3: ["甲午", "乙未", "丙申", "丁酉", "戊戌", "己亥", "庚子", "辛丑", "壬寅", "癸卯"],
    4: ["甲辰", "乙巳", "丙午", "丁未", "戊申", "己酉", "庚戌", "辛亥", "壬子", "癸丑"],
    5: ["甲寅", "乙卯", "丙辰", "丁巳", "戊午", "己未", "庚申", "辛酉", "壬戌", "癸亥"]
}

xuntouyinshe={0:"甲子",1:'甲戌',2:"甲申",3:"甲午",4:"甲辰",5:"甲寅"}
# 遍历映射关系，创建Excel文件
for file_number, gan_zhi_list in gan_zhi_mapping.items():
    file_name = f'240507_香港定位P3日干支分类_{xuntouyinshe[file_number]}.xlsx'
    with pd.ExcelWriter(file_name, engine='xlsxwriter') as writer:
        for gan_zhi in gan_zhi_list:
            filtered_df = result_df[result_df['日干支'] == gan_zhi]
            # 对filtered_df按日期列排序
            filtered_df = filtered_df.sort_values('日期')
            # 将数据写入对应的工作表
            filtered_df.to_excel(writer, sheet_name=gan_zhi, index=False)
    print(f'文件 {file_name} 创建完成')