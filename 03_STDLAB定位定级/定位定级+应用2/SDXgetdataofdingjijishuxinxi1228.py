import pandas as pd
import os
import math

# 计算不同范围内的数量和百分比的函数
# 定义实际值的范围
actual_value_ranges = [
    (0, 1), (1, 2), (2, 3), (3, 4)
]

# 定义实际值四舍五入到最近整数的范围
actual_value_rounded_ranges = [
    (0, 1), (1, 2), (2, 3), (3, 4),
    (0, 0.5), (0.5, 1), (1, 1.5), (1.5, 2),
    (2, 2.5), (2.5, 3), (3, 3.5), (3.5, 4)
]
def calculate_ranges_stats(df, column_name, ranges):
    stats = {}

    # 初始化统计字典
    for r in ranges:
        stats[f"{column_name}在{r[0]}到{r[1]}的个数"] = 0
        stats[f"{column_name}在{r[0]}到{r[1]}的百分比"] = 0.0
        # 遍历数据框，统计每个范围内的出现次数
    for index, row in df.iterrows():
        value = row[column_name]
        for r in ranges:
            if r[0] < value <= r[1]:
                stats[f"{column_name}在{r[0]}到{r[1]}的个数"] += 1
                if row['准确'] == 1:
                    stats[f"{column_name}在{r[0]}到{r[1]}的百分比"] += 1
    # 计算百分比
    total_count = len(df)
    for r in ranges:
        stats[f"{column_name}在{r[0]}到{r[1]}的百分比"] = (stats[f"{column_name}在{r[0]}到{r[1]}的个数"] / total_count) * 100

    return stats
# 计算准确列中数字1的百分比的函数
def calculate_accuracy_percentage(df, column_name, ranges):
    percentages = {}

    # 遍历数据框，计算每个范围内的准确列中数字1的百分比
    for r in ranges:
        subset_df = df[(df[column_name] > r[0]) & (df[column_name] <= r[1])]
        total_count = len(subset_df)
        if total_count > 0:
            accuracy_count = subset_df['准确'].sum()
            percentages[f"准确列在{r[0]}到{r[1]}的准确列中数字1的百分比"] = (accuracy_count / total_count) * 100
        else:
            percentages[f"准确列在{r[0]}到{r[1]}的准确列中数字1的百分比"] = 0.0

    return percentages

# 计算各个区间的平均值的函数
def calculate_ranges_mean(df, column_name,ranges):
    means = {}

    # 遍历数据框，计算每个范围内的平均值
    for r in ranges:
        subset_df = df[(df[column_name] > r[0]) & (df[column_name] <= r[1])]
        means[f"{column_name}在{r[0]}到{r[1]}的平均值"] = subset_df[column_name].mean()




    return means

# 处理每一年的数据的函数
def process_yearly_data(df):
    # 计算 '定级得数' 列的统计信息
    actual_value_stats = calculate_ranges_stats(df, '定级得数', actual_value_ranges)

    # 计算 '定级得数' 列四舍五入到最近整数的统计信息
    actual_value_rounded_stats = calculate_ranges_stats(df, '定级得数', actual_value_rounded_ranges)

    # 计算 '定级得数' 列的平均值
    actual_value_means = calculate_ranges_mean(df, '定级得数', actual_value_ranges)
    # 计算 '准确' 列的统计信息
    accuracy_means = calculate_accuracy_percentage(df, '定级得数', actual_value_ranges)

    # 新增处理规则
    for val in [0.5, 1.5, 2.5, 3.5]:
        count_key = f"定级得数等于{val}的个数"
        percent_key = f"定级得数等于{val}的百分比"
        actual_value_stats[count_key] = len(df[df['定级得数'] == val])
        actual_value_stats[percent_key] = (actual_value_stats[count_key] / len(df)) * 100
    # 计算 '特' 列的统计信息
    special_ranges = [
        (1, 6), (7, 12), (13, 18), (19, 24), (25, 30), (31, 36), (37, 42), (43, 49)
    ]
    special_stats = calculate_ranges_stats(df, '特', special_ranges)

    # 添加 '特' 列统计信息到结果字典中
    actual_value_stats.update(special_stats)
    return actual_value_stats, actual_value_rounded_stats, actual_value_means, accuracy_means

# 创建存储每年统计信息的列表
yearly_stats_list = []

# 遍历每一年
for year in range(2010, 2024):
    sheet_name = f"{year}年"

    try:
        # 读取当前年份的数据
        file_path = '2010-2023年香港汇总定级结果表-含准确率分析和错误数据标注.xlsx'
        df = pd.read_excel(file_path, sheet_name=sheet_name)

        # 处理每年的数据
        actual_value_stats, actual_value_rounded_stats, actual_value_means, accuracy_means = process_yearly_data(df)

        # 将统计信息添加到列表中
        yearly_stats_list.append({
            '年份': year,
            **actual_value_stats,
            **actual_value_rounded_stats,
            **actual_value_means,
            **accuracy_means
        })

        print(f'处理完成 {year} 年的数据')

    except pd.errors.ImproperExcelHeader:
        print(f'在 {year} 年找不到工作表: {sheet_name}')

# 从年度统计列表创建数据框
yearly_stats_df = pd.DataFrame(yearly_stats_list)

# 将年度统计保存到新的 Excel 文件中
output_stats_file_path = '2010-2023年香港汇总定级结果表G1-1229.xlsx'
yearly_stats_df.to_excel(output_stats_file_path, index=False)

print('全部处理完成')
