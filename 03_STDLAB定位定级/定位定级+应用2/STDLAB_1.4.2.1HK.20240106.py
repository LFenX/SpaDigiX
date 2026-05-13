import pandas as pd
from datetime import datetime
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
    return nianyueriganzhi

# 主函数
def process_excel(file_path, sheet_name, start_date, end_date, n, h):
    # 读取Excel文件
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    df['日期'] = pd.to_datetime(df['日期'], errors='coerce')

    # 应用筛选条件
    mask = (df['日期'] >= start_date) & (df['日期'] <= end_date)
    df_filtered = df.loc[mask].copy()

    # 初始化平均数列和预测庄家数列
    df_filtered['平均数'] = 0.0
    df_filtered['预测庄家数'] = None

    # 计算平均数并进行预测
    for i in range(len(df_filtered)):
        if i >= n:
            mean_value = df_filtered['庄家数'].iloc[i-n:i].mean()
            df_filtered.at[df_filtered.index[i], '预测庄家数'] = 1 if mean_value > h else 0
            df_filtered.at[df_filtered.index[i], '平均数'] = mean_value
    # 计算准确率
    valid_predictions = df_filtered['预测庄家数'].dropna().tolist()
    valid_actuals = df_filtered['庄家数'].iloc[n:].tolist()
    correct_predictions = 0
    total_predictions = len(valid_actuals)
    for i in range(len(valid_predictions)):
        if valid_predictions[i] == valid_actuals[i]:
            correct_predictions += 1

    accuracy = correct_predictions / total_predictions
    # 统计日期数量
    total_dates = len(df_filtered)
    valid_dates = len(valid_predictions)

    # 打印结果
    print(f"准确率: {accuracy}")
    print(f"有预测值的日期个数: {valid_dates}")
    print(f"正确数：{correct_predictions}")
    print(f"在范围内的总日期个数: {total_dates}")
    # 计算干支历
    df_filtered['年月日干支历'] = df_filtered['日期'].apply(calculate_score)

    # 返回处理后的数据框
    return df_filtered
# 调用函数并打印结果
file_path = 'HK2010-2023_dataforAPP1.4.2prediction.xlsx'  # 替换为您的文件路径
qishiriqi=input("请输入起始日期（输入格式：2024-1-6）：")
zhongzhiriqi=input("请输入终止日期：")
n=int(input("请输入参数n(步长）："))
h=float(input("请输入参数h（0<h<1)："))
start_date = pd.to_datetime(qishiriqi)
end_date = pd.to_datetime(zhongzhiriqi)
# 根据之前定义的 process_excel 函数处理数据并打印所有结果
processed_df_full = process_excel(file_path, 'Sheet1', start_date, end_date, n, h)
# 打印所有数据，确保列标题与数据对齐
with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', 1000):
    print(processed_df_full)

print("请确认是否需要将本次数据输出为excel表格：")
print("0. 不输出")
print("1. 输出")
choices = input("请选择操作 (0/1): ")
if choices=='0':
    pass
else:
    output_file_path = f'HK{qishiriqi}到{zhongzhiriqi}参数为n=={n}且h=={h}.xlsx'
    processed_df_full.to_excel(output_file_path, index=False)
while True:
    print("请选择操作:")
    print("1. 输入所有参数重新计算")
    print("2. 固定起始日期和终止日期，重新输入 n 和 h 进行计算")
    print("3. 固定起始日期、终止日期和 n，调整 h 进行计算")
    print("4. 固定起始日期、终止日期和 h，调整 n 进行计算")
    print("0. 退出")
    choice = input("请选择操作 (0/1/2/3/4): ")

    if choice == '0':
        break
    elif choice == '1':
        qishiriqi = input("请输入起始日期（输入格式：2024-1-6）：")
        zhongzhiriqi = input("请输入终止日期：")
        n = int(input("请输入参数 n："))
        h = float(input("请输入参数 h："))
        start_date = pd.to_datetime(qishiriqi)
        end_date = pd.to_datetime(zhongzhiriqi)
    elif choice == '2':
        n = int(input("请输入参数 n："))
        h = float(input("请输入参数 h："))
    elif choice == '3':
        h = float(input("请输入参数 h："))
    elif choice== "4":
        n=int(input("请输入参数 n："))
    # 调用函数并打印结果
    processed_df_full = process_excel(file_path, 'Sheet1', start_date, end_date, n, h)
    # 打印所有数据，确保列标题与数据对齐
    with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', 1000):
        print(processed_df_full)
    print("请确认是否需要将本次数据输出为excel表格：")
    print("0. 不输出")
    print("1. 输出")
    choices = input("请选择操作 (0/1): ")
    if choices == '0':
        pass
    else:
        output_file_path =f'HK{qishiriqi}到{zhongzhiriqi}参数为n=={n}且h=={h}.xlsx'
        processed_df_full.to_excel(output_file_path, index=False)