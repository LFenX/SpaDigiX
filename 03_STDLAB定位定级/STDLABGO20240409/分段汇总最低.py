import pandas as pd
import os

# 定义需要处理的时间点和分类名称
time_points = ["子时", "丑时","寅时","卯时","辰时","巳时","午时","未时","申时","酉时","戌时","亥时","双干时辰"]
classification_names = ["震三-阳遁", "震三-阴遁", "乾六-阳遁", "乾六-阴遁", "离九-阳遁", "离九-阴遁",
                        "艮八-阳遁", "艮八-阴遁", "兑七-阳遁", "兑七-阴遁", "坤二-阳遁", "坤二-阴遁",
                        "巽四-阳遁", "巽四-阴遁", "坎一-阳遁", "坎一-阴遁"]

# 初始化一个字典来保存每个分类在所有时间点中的最低吻合度行
best_matches = {name: {"time": "", "data": None} for name in classification_names}

# 读取每个时间点的吻合度结果汇总表格，找到每个分类的最低吻合度
for time_point in time_points:
    summary_file_path = f'{time_point}-修正澳门-最低吻合度结果汇总.xlsx'
    summary_df = pd.read_excel(summary_file_path, sheet_name="最低吻合度")

    for classification_name in classification_names:
        # 找到当前时间点中当前分类的最低吻合度行
        current_row = summary_df[summary_df["工作表名称"] == classification_name]
        if not current_row.empty:
            current_match_rate = float(current_row["吻合度最低"].str.split(": ").str[-1].values[0])
            if (best_matches[classification_name]["data"] is None or
                    current_match_rate < float(
                        best_matches[classification_name]["data"]["吻合度最低"].split(": ")[-1])):
                best_matches[classification_name]["time"] = time_point
                best_matches[classification_name]["data"] = current_row.iloc[0]

# 创建一个新的DataFrame保存每个分类在所有时间点中的最低吻合度行
summary_data = []
for classification_name in classification_names:
    best_match = best_matches[classification_name]
    if best_match["data"] is not None:
        best_match_data = best_match["data"].copy()
        best_match_data["工作表名称"] = f"{best_match['time']}-{best_match_data['工作表名称']}"
        summary_data.append(best_match_data)

summary_df = pd.DataFrame(summary_data)

# 保存最低吻合度结果汇总
output_summary_path = '修正澳门-分段最低吻合度结果汇总.xlsx'
with pd.ExcelWriter(output_summary_path) as writer:
    summary_df.to_excel(writer, sheet_name='最低吻合度', index=False)

# 从对应的澳门双干宫+阴阳遁分类结果中提取相应的工作表并将其放入新的Excel表格中
output_classification_path = '修正澳门-最低吻合度分段汇总数据结果.xlsx'
with pd.ExcelWriter(output_classification_path) as writer:
    for classification_name in classification_names:
        time_point = best_matches[classification_name]["time"]
        classification_file_path = f'{time_point}-修正-澳门双干宫+阴阳遁分类结果+最低吻合度列数据.xlsx'
        classification_df = pd.ExcelFile(classification_file_path).parse(classification_name)

        # 更改工作表名称为“时间点-分类名称”
        new_sheet_name = f'{time_point}-{classification_name}'
        classification_df.to_excel(writer, sheet_name=new_sheet_name, index=False)
