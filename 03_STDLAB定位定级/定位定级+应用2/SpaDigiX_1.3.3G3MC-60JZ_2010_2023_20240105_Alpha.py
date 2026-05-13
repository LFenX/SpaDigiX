from functionSpadigiXAPPTHREEANDTHREEG3MC import getdingjideshu
import pandas as pd
import math

# 定义计算得分的函数
def calculate_score(row):
    year, month, day = row['日期'].year, row['日期'].month, row['日期'].day
    values = getdingjideshu(year, month, day)

    # 将得到的五个值分别分配给对应的列
    row['定级得数'] = values[0]
    row['双干得数'] = values[1]
    row['值使得数'] = values[2]
    row['值符得数'] = values[3]
    row['生门得数'] = values[4]
    row['年月日干支'] = values[5]
    row['日干支'] = values[6]

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

        # 新增处理规则
        df['实际数'] = df['特'].apply(lambda x: min(math.ceil(x / 12), 4))
        df['定级数'] = df['定级得数'].apply(lambda x: math.ceil(x))
        df['准确'] = df.apply(lambda x: 1 if str(x['实际数']) in ["412", "123", "234", "341"][x['定级数'] - 1] else 0, axis=1)

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
    file_name = f'澳门G3MC日干支分类_{file_number}.xlsx'
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