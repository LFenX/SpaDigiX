import pandas as pd
from functionSpaDigiXONEANDSEVEN import getSpaDigiXdingweideshu
from functionSpaDigiXAPPONE import getthebasicmessageofnineGrids

# 原始数据文件路径
input_file_path = '澳门历史数据.xlsx'
# 输出文件路径
output_file_path = '240119_2010-2024-汇总-定位双支十二时辰分类结果澳门P0.xlsx'

# 创建12个空的DataFrame，用于存储每个时辰的数据
sheets_data = {f"{label}时": pd.DataFrame() for label in ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']}

# 遍历2010年到2024年的数据
for year in range(2010, 2025):
    # 读取对应年份的工作表
    df = pd.read_excel(input_file_path, sheet_name=f"{year}年")

    # 格式化'日期'列，仅包含年、月、日
    df['日期'] = pd.to_datetime(df['日期']).dt.strftime('%Y-%m-%d')

    # 定义计算和标签的组合函数
    def calculate_and_label(date):
        date = pd.to_datetime(date)
        year = date.year
        month = date.month
        day = date.day
        for i in range(0, 12):
            ridizhi = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][3][1]
            shichengdizhi = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][4][1]
            if ridizhi == shichengdizhi:
                hourr = 2 * i
                label = ridizhi
                break
        value = getSpaDigiXdingweideshu(year, month, day, hourr)
        nianyueriganzhi = getthebasicmessageofnineGrids(year, month, day, hourr)[2]

        return value, label, nianyueriganzhi

    # 应用组合函数
    df['双支程序'], df['标签'], df['年月日干支时间'] = zip(*df['日期'].apply(calculate_and_label))

    # 追加数据到相应时辰的DataFrame中
    for index, row in df.iterrows():
        sheet_name = f"{row['标签']}时"
        row_data = pd.DataFrame([row])
        sheets_data[sheet_name] = pd.concat([sheets_data[sheet_name], row_data], ignore_index=True)

# 使用XlsxWriter引擎创建Pandas Excel写入器，并将数据写入不同的工作表
with pd.ExcelWriter(output_file_path, engine='xlsxwriter') as writer:
    for sheet_name, data in sheets_data.items():
        data.to_excel(writer, sheet_name=sheet_name, index=False)

