from functionSpaDigiXONEANDSEVEN  import getSpaDigiXdingweideshu
from functionSpaDigiXAPPONE import getthebasicmessageofnineGrids
import pandas as pd
import math
# 定义计算得分的函数
def calculate_score(row):
    year, month, day = row['日期'].year, row['日期'].month, row['日期'].day
    for i in range(0, 12):
        ridizhi = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][3][1]
        shichengdizhi = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][4][1]
        if ridizhi == shichengdizhi:
            hourr = 2 * i
            break
    value = getSpaDigiXdingweideshu(year, month, day, hourr)
    # 将得到的五个值分别分配给对应的列
    row['双支软件得数'] = value
    riganzhi = getthebasicmessageofnineGrids(year, month, day, hourr)[1][3]
    row['年月日干支'] = getthebasicmessageofnineGrids(year, month, day, hourr)[2]
    row["日干支"] = riganzhi
    return row
# 创建一个空的 DataFrame 用于存储所有结果
result_df = pd.DataFrame()
# 遍历每年的工作表
for year in range(2021, 2024):
    sheet_name = f"新澳门{year}"
    try:
        # 读取上传的文件，并指定工作表名称
        file_path = '新澳门2021-2023定位数据初始.xlsx'
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        # 将“日期”列转换为日期格式
        df['日期'] = pd.to_datetime(df['日期'])
        # 应用计算规则到每一行
        df = df.apply(calculate_score, axis=1)
        df['日期'] = df['日期'].dt.strftime('%Y-%m-%d')
        # 将当前年份的结果添加到总结果中
        df['年份'] = year
        result_df = pd.concat([result_df, df], ignore_index=True)

        print(f'处理完成 {year} 年的数据')

    except pd.errors.ImproperExcelHeader:
        print(f'在 {year} 年找不到工作表: {sheet_name}')

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
            # 将数据写入对应的工作表
            filtered_df.to_excel(writer, sheet_name=gan_zhi, index=False)
    print(f'文件 {file_name} 创建完成')