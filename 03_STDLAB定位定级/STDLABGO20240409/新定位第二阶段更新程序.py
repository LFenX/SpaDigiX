import pandas as pd

# 定义生肖到时间列的映射
zodiac_to_time = {
    '子': '子时', '丑': '丑时', '寅': '寅时', '卯': '卯时', '辰': '辰时', '巳': '巳时',
    '午': '午时', '未': '未时', '申': '申时', '酉': '酉时', '戌': '戌时', '亥': '亥时'
}

# 顺序排列的时间列，用于循环
time_columns = ['子时', '丑时', '寅时', '卯时', '辰时', '巳时', '午时', '未时', '申时', '酉时', '戌时', '亥时']


# 处理每个工作表的函数
def process_sheet(df):
    # 从第二行开始处理，并使用前一行的生肖来确定数据的输入
    for index in range(1, len(df)):
        # 根据前一行的生肖找到起始时间列
        start_time_col = zodiac_to_time[df.at[index - 1, '生肖']]
        start_idx = time_columns.index(start_time_col)

        # 填充特0到特11列
        for i in range(12):
            target_col = '特' + str(i)
            time_idx = (start_idx + i) % 12
            df.at[index, target_col] = df.at[index, time_columns[time_idx]]

    return df


# 加载Excel文件
file_path = '香港2023-2024-新定位及01数据汇总数据初始.xlsx'
excel_data = pd.ExcelFile(file_path)

# 为处理后的数据创建一个新的Excel文件
writer = pd.ExcelWriter('香港2023-2024-新定位及01数据汇总数据.xlsx', engine='xlsxwriter')

# 处理每个工作表并保存
for sheet_name in excel_data.sheet_names:
    df = pd.read_excel(excel_data, sheet_name=sheet_name)
    processed_df = process_sheet(df)
    processed_df.to_excel(writer, sheet_name=sheet_name, index=False)

writer.close()
