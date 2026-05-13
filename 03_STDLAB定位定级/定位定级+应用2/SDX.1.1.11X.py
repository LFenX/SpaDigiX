import pandas as pd
from functionSpaDigiXONEANDNINE   import getSpaDigiXdingweideshu
from functionSpaDigiXAPPONE import getthebasicmessageofnineGrids
# Load the Excel file
input_file_path = '定位、定级验证灵数误差双支表.xlsx'  # 原始数据文件路径
excel_data = pd.ExcelFile(input_file_path)

# Load one of the sheets (for example, "澳门新定位结果")
sheet_to_process = "澳门新定位结果"
df = excel_data.parse(sheet_to_process)

# 格式化'日期'列，仅包含年、月、日
df['日期'] = pd.to_datetime(df['日期']).dt.strftime('%Y-%m-%d')

# 定义计算和标签的组合函数
def calculate_and_label(date):
    date = pd.to_datetime(date)  # 将字符串转换回datetime以进行计算
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
    return value, label

# 应用组合函数
df['双支程序'], df['标签'] = zip(*df['日期'].apply(calculate_and_label))

# 计算"误差"和"误差ABS"
df['误差'] = df['双支灵数'] - df['双支程序']
df['误差ABS'] = df['误差'].abs()

# 创建并填充每个标签的工作表
sheets_data = {f"{label}时": pd.DataFrame() for label in ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']}
summary_data = []

for index, row in df.iterrows():
    sheet_name = f"{row['标签']}时"
    row_data = pd.DataFrame([row.drop('标签')])
    sheets_data[sheet_name] = pd.concat([sheets_data[sheet_name], row_data], ignore_index=True)

# 添加"误差均值"和"准确率"到每个工作表，并收集汇总数据
for sheet_name, data in sheets_data.items():
    error_mean = data['误差ABS'].mean()
    accuracy_rate = ((data['误差'] >= -3) & (data['误差'] <= 3)).mean()
    summary_data.append({'时辰': sheet_name, '误差均值': error_mean, '准确率': accuracy_rate})

# 创建汇总数据表
summary_df = pd.DataFrame(summary_data)

# 输出文件路径
output_file_path = '双支十二时辰结果澳门1219.xlsx'

# 使用XlsxWriter引擎创建Pandas Excel写入器
with pd.ExcelWriter(output_file_path, engine='xlsxwriter') as writer:
    # 将每个数据框写入不同的工作表并调整列宽
    for sheet_name, data in sheets_data.items():
        data.to_excel(writer, sheet_name=sheet_name, index=False)
        worksheet = writer.sheets[sheet_name]

    # 将汇总数据表写入新的工作表
    summary_df.to_excel(writer, sheet_name='十二时辰误差汇总', index=False)
    worksheet = writer.sheets['十二时辰误差汇总']