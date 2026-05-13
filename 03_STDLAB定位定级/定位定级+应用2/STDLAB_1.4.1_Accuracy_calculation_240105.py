
import pandas as pd

# 载入Excel文件
file_path = '统一地支-NewModel-澳门2021-2023庄家模型数据汇总230105.xlsx'
xls = pd.ExcelFile(file_path)

# 读取'Sheet1'和'统计'工作表
sheet1_df = pd.read_excel(xls, 'Sheet1', dtype={'庄家数串8': str, '庄家数串9': str})
stats_df = pd.read_excel(xls, '统计', dtype={'类别': str})

# 创建处理数据的函数
def process_data(df, column_name):
    final_data = []

    # 遍历'Sheet1'中的每一行
    for index, row in df.iterrows():
        # 获取当前行的庄家数串
        current_str = row[column_name]

        # 在'统计'表中检索匹配的类别
        matching_stat = stats_df[stats_df['类别'] == current_str]

        # 如果找到匹配的类别，获取1的百分比和0的百分比
        if not matching_stat.empty:
            one_percent = matching_stat.iloc[0]['1的百分比']
            zero_percent = matching_stat.iloc[0]['0的百分比']

            # 比较1的百分比和0的百分比
            selected_value = 1 if one_percent > zero_percent else 0

            # 在'Sheet1'中比较选择的数值与庄家数，确定“准确”值
            accurate = 1 if row['庄家数'] == selected_value else 0
        else:
            one_percent = None
            zero_percent = None
            accurate = None  # 标记为None表示没有匹配项

        # 将结果添加到final_data中
        final_data.append({
            '日期': row['日期'],
            '特': row['特'],
            '地支': row['地支'],
            '庄家数': row['庄家数'],
            column_name: current_str if current_str else '',
            '准确': accurate,
            '类别': current_str if current_str else '',
            '1的百分比': one_percent if one_percent is not None else '',
            '0的百分比': zero_percent if zero_percent is not None else ''
        })

    return pd.DataFrame(final_data)

# 处理庄家数串8和庄家数串9
processed_data_8 = process_data(sheet1_df, '庄家数串8')
processed_data_9 = process_data(sheet1_df, '庄家数串9')

# 输出到新的Excel文件的不同工作表中
output_file_path = '统一地支-子丑寅卯辰巳-澳门2021-2023庄家模型准确率统计.xlsx'
with pd.ExcelWriter(output_file_path) as writer:
    processed_data_8.to_excel(writer, sheet_name='庄家数串8', index=False)
    processed_data_9.to_excel(writer, sheet_name='庄家数串9', index=False)

print(f"文件已保存到 {output_file_path}")

