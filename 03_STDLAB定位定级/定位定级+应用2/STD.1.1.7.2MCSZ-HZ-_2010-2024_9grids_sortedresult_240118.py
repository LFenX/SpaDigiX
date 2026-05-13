import pandas as pd
from functionSpaDigiXONEANDSEVEN  import getSpaDigiXdingweideshu
from functionSpaDigiXAPPONE import getthebasicmessageofnineGrids
# 原始数据文件路径
input_file_path = '澳门历史数据.xlsx'
# 输出文件路径
output_file_path = '240119_2010至2024汇总定位澳门双支九宫结果P0.xlsx'

# 创建8个空的DataFrame，用于存储每个标签的数据
sheets_data = {label: pd.DataFrame() for label in ['坎宫', '坤宫', '震宫', '巽宫', '乾宫', '兑宫', '艮宫', '离宫']}

# 遍历2010年到2024年的数据
for year in range(2010, 2025):
    sheet_name = f"{year}年"
    df = pd.read_excel(input_file_path, sheet_name=sheet_name)

    # 格式化日期列
    df['日期'] = pd.to_datetime(df['日期']).dt.strftime('%Y-%m-%d')

    # 应用复合函数
    def label_and_calculate(date):
        date = pd.to_datetime(date)
        year = date.year
        month = date.month
        day = date.day
        for i in range(0, 12):
            ridizhi = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][3][1]
            shichengdizhi = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][4][1]
            dingwei = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][6]
            if ridizhi == shichengdizhi:
                hourr = 2 * i
                break
        value = getSpaDigiXdingweideshu(year, month, day, hourr)
        labels = {0: '坎宫', 1: '坤宫', 2: '震宫', 3: '巽宫', 5: '乾宫', 6: '兑宫', 7: '艮宫', 8: '离宫'}
        label = labels.get(dingwei)
        nianyueriganzhi = getthebasicmessageofnineGrids(year, month, day, hourr)[2]
        return value, label, nianyueriganzhi

    df['双支程序'], df['标签'], df['年月日干支时间'] = zip(*df['日期'].apply(label_and_calculate))

    # 将数据追加到对应标签的DataFrame中
    for index, row in df.iterrows():
        label = row['标签']
        sheets_data[label] = pd.concat([sheets_data[label], pd.DataFrame([row])], ignore_index=True)

# 使用XlsxWriter引擎创建Pandas Excel写入器，并将数据写入不同的工作表
with pd.ExcelWriter(output_file_path, engine='xlsxwriter') as writer:
    for label, data in sheets_data.items():
        data.to_excel(writer, sheet_name=label, index=False)
        # 如果需要调整列宽，可以在这里添加代码