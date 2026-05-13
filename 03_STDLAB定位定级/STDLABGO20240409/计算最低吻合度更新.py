import pandas as pd
import itertools

# 读取上传的 Excel 文件
file_path = '含有对比01数据-输入生肖_修正-输入实数数据-亥时-未输入生肖数据-澳门双干+阴阳遁分类结果-未输入对比时间01数据.xlsx'
excel_data = pd.ExcelFile(file_path)

# 获取所有工作表的名称
sheet_names = excel_data.sheet_names

# 定义地支
earthly_branches = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]

# 生成所有可能的分类方式
combinations = list(itertools.combinations(earthly_branches, 6))

# 计算分类列名
combination_names = [f"{''.join(comb)}-{''.join(set(earthly_branches) - set(comb))}" for comb in combinations]


# 定义地支分类函数
def classify_branch(branch, group1):
    return 1 if branch in group1 else 0


# 初始化结果数据框
summary_data = []
lowest_match_data = []

# 创建一个新的ExcelWriter对象用于保存包含最低吻合度列的表格
output_path_with_lowest_cols = '亥时-修正-澳门双干宫+阴阳遁分类结果+最低吻合度列数据.xlsx'
writer_lowest_cols = pd.ExcelWriter(output_path_with_lowest_cols, engine='xlsxwriter')

for sheet in sheet_names:
    df = excel_data.parse(sheet)
    if '地支' not in df.columns or '对比01数据' not in df.columns:
        continue

    match_rates = {}

    # 添加924个分类列并计算吻合率
    for comb, name in zip(combinations, combination_names):
        df[name] = df['地支'].apply(lambda x: classify_branch(x, comb))
        match_count = sum(df[name] == df['对比01数据'])
        match_rate = match_count / len(df)
        match_rates[name] = match_rate

    # 保存工作表的吻合率
    sorted_match_rates = sorted(match_rates.items(), key=lambda x: x[1])
    summary_data.append({
        '工作表名称': sheet,
        **{rate[0]: rate[1] for rate in sorted_match_rates}
    })

    # 保存吻合度最低的列及其吻合度
    lowest_match_rate = sorted_match_rates[0][1]
    lowest_match_columns = [rate[0] for rate in sorted_match_rates if rate[1] == lowest_match_rate]
    lowest_match_count = sum(df[lowest_match_columns[0]] != df['对比01数据'])
    lowest_match_data.append({
        '工作表名称': sheet,
        '吻合度最低': f"{', '.join(lowest_match_columns)}: {lowest_match_rate}",
                      '数据总数': len(df),
    '不吻合数据量': lowest_match_count
    })

    # 保留原来的列并删除924列新数据中不是最低吻合度的列
    lowest_cols = lowest_match_columns
    columns_to_keep = [col for col in df.columns if col not in combination_names or col in lowest_cols]
    df_lowest = df[columns_to_keep]

    # 将包含最低吻合度列的新表格写入Excel
    df_lowest.to_excel(writer_lowest_cols, sheet_name=sheet, index=False)

# 生成结果Excel文件
summary_df = pd.DataFrame(summary_data)
lowest_match_df = pd.DataFrame(lowest_match_data)

output_path_summary = '亥时-修正澳门-最低吻合度结果汇总.xlsx'
with pd.ExcelWriter(output_path_summary) as writer:
    summary_df.to_excel(writer, sheet_name='分类吻合率', index=False)
    lowest_match_df.to_excel(writer, sheet_name='最低吻合度', index=False)

# 保存包含最低吻合度列的表格
writer_lowest_cols.close()
