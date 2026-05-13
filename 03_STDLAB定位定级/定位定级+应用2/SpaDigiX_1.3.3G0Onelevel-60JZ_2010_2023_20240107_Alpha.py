from functionSpadigiXAPPTHREEANDTHREEforG0Onelevel import getdingjideshu
import pandas as pd
import math

# 定义计算得分的函数
def calculate_score(row):
    year, month, day = row['日期'].year, row['日期'].month, row['日期'].day
    values = getdingjideshu(year, month, day)
    shuanggangonghao=values[7]
    zhifugonghao=values[8]
    zhishigonghao=values[9]
    shengmengonghao=values[10]
    yinyangjiujugonghao=values[11]
    if shuanggangonghao==0:
        shuanggangong="坎一"
    elif shuanggangonghao==1:
        shuanggangong="坤二"
    elif shuanggangonghao==2:
        shuanggangong="震三"
    elif shuanggangonghao==3:
        shuanggangong="巽四"
    elif shuanggangonghao==5:
        shuanggangong="乾六"
    elif shuanggangonghao==6:
        shuanggangong="兑七"
    elif shuanggangonghao==7:
        shuanggangong="艮八"
    elif shuanggangonghao==8:
        shuanggangong="离九"

    if zhifugonghao==0:
        zhifugong="坎一"
    elif zhifugonghao==1:
        zhifugong="坤二"
    elif zhifugonghao==2:
        zhifugong="震三"
    elif zhifugonghao==3:
        zhifugong="巽四"
    elif zhifugonghao==5:
        zhifugong="乾六"
    elif zhifugonghao==6:
        zhifugong="兑七"
    elif zhifugonghao==7:
        zhifugong="艮八"
    elif zhifugonghao==8:
        zhifugong="离九"

    if zhishigonghao==0:
        zhishigong="坎一"
    elif zhishigonghao==1:
        zhishigong="坤二"
    elif zhishigonghao==2:
        zhishigong="震三"
    elif zhishigonghao==3:
        zhishigong="巽四"
    elif zhishigonghao==5:
        zhishigong="乾六"
    elif zhishigonghao==6:
        zhishigong="兑七"
    elif zhishigonghao==7:
        zhishigong="艮八"
    elif zhishigonghao==8:
        zhishigong="离九"

    if shengmengonghao==0:
        shengmengong="坎一"
    elif shengmengonghao==1:
        shengmengong="坤二"
    elif shengmengonghao==2:
        shengmengong="震三"
    elif shengmengonghao==3:
        shengmengong="巽四"
    elif shengmengonghao==5:
        shengmengong="乾六"
    elif shengmengonghao==6:
        shengmengong="兑七"
    elif shengmengonghao==7:
        shengmengong="艮八"
    elif shengmengonghao==8:
        shengmengong="离九"


    if yinyangjiujugonghao==0:
        yinyangjiujugong="坎一局"
    elif yinyangjiujugonghao==1:
        yinyangjiujugong="坤二局"
    elif yinyangjiujugonghao==2:
        yinyangjiujugong="震三局"
    elif yinyangjiujugonghao==3:
        yinyangjiujugong="巽四局"
    elif yinyangjiujugonghao==4:
        yinyangjiujugong="中五局"
    elif yinyangjiujugonghao==5:
        yinyangjiujugong="乾六局"
    elif yinyangjiujugonghao==6:
        yinyangjiujugong="兑七局"
    elif yinyangjiujugonghao==7:
        yinyangjiujugong="艮八局"
    elif yinyangjiujugonghao==8:
        yinyangjiujugong="离九局"

    # 将得到的五个值分别分配给对应的列
    row['定级得数'] = values[0]
    row["阴阳九局"] =yinyangjiujugong
    row['双干得数'] = values[1]
    row["双干宫"]=shuanggangong
    row['值使得数'] = values[2]
    row["值使宫"]=zhishigong
    row['值符得数'] = values[3]
    row['值符宫']=zhifugong
    row['生门得数'] = values[4]
    row["生门宫"]= shengmengong
    row['年月日干支'] = values[5]
    row['日干支'] = values[6]

    return row

# 创建一个空的 DataFrame 用于存储所有结果
result_df = pd.DataFrame()

# 遍历每年的工作表
for year in range(2010, 2025):
    sheet_name = f"{year}年"
    try:
        # 读取上传的文件，并指定工作表名称
        file_path = '澳门历史数据.xlsx'
        df = pd.read_excel(file_path, sheet_name=sheet_name)

        # 将“日期”列转换为日期格式
        df['日期'] = pd.to_datetime(df['日期'])

        # 应用计算规则到每一行
        df = df.apply(calculate_score, axis=1)
        df['日期'] = df['日期'].dt.strftime('%Y-%m-%d')

        # 新增处理规则
        df['实际数'] = df['特'].apply(lambda x: min(math.ceil(x / 12), 4))
        # 计算实际差值
        df["实际差值"] = df["特"] / 12
        # 对于特殊情况（特=49），设置实际差值为 4
        df.loc[df["特"] == 49, "实际差值"] = 4
        df['定级数'] = df['定级得数'].apply(lambda x: math.ceil(x))
        df['准确'] = df.apply(lambda x: 1 if str(x['实际数']) in ["1", "2", "3", "4"][x['定级数'] - 1] else 0, axis=1)

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

# 遍历映射关系，创建Excel文件
for file_number, gan_zhi_list in gan_zhi_mapping.items():
    file_name = f'澳门MCG4修正2010-2024_Onlevel_日干支分类_{file_number}20240119.xlsx'
    accuracy_stats = []  # 存储每个日干支的准确率数据

    with pd.ExcelWriter(file_name, engine='xlsxwriter') as writer:
        for gan_zhi in gan_zhi_list:
            # 筛选符合该日干支的数据
            filtered_df = result_df[result_df['日干支'] == gan_zhi]

            # 计算准确率
            accuracy = filtered_df['准确'].mean() * 100
            # 计算总个数和准确个数
            total_count = len(filtered_df)
            accurate_count = filtered_df['准确'].sum()

            # 添加到统计列表
            accuracy_stats.append({
                '日干支': gan_zhi,
                '准确率': accuracy,
                '总个数': total_count,
                '准确个数': accurate_count
            })

            # 将数据写入对应的工作表
            filtered_df.to_excel(writer, sheet_name=gan_zhi, index=False)

        # 创建一个新的工作表用于存储准确率统计
        accuracy_df = pd.DataFrame(accuracy_stats)
        accuracy_df.to_excel(writer, sheet_name='准确率统计', index=False)

    print(f'文件 {file_name} 创建完成')