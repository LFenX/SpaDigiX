import pandas as pd
from functiontogetP2sdjustedvalue import getmodified_value
# 加载Excel文件
file_path = '240228_2010至2024汇总定位香港双干十二月份结果P1.xlsx'
excel_data = pd.ExcelFile(file_path)

# 准备写入器以保存更新后的工作表
output_path = '240418香港定位P1调整后对比数据.xlsx'
with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
    # 遍历每个工作表，计算五个调整值，并添加到新的列中
    for sheet_name in excel_data.sheet_names:
        data = pd.read_excel(excel_data, sheet_name)
        # 从日期列提取年、月、日
        data['Year'] = pd.to_datetime(data['日期']).dt.year
        data['Month'] = pd.to_datetime(data['日期']).dt.month
        data['Day'] = pd.to_datetime(data['日期']).dt.day

        # 应用函数到每一行，将返回的元组展开到多个新列中
        adjustments = data.apply(lambda x: getmodified_value(x['Year'], x['Month'], x['Day']), axis=1)
        data[['九星最终调整数', '八神最终调整数', '八门最终调整数', '天干最终调整数', '日在月最终调整数']] = pd.DataFrame(adjustments.tolist(), index=data.index)

        # 汇总五个调整数得到最终调整数
        data['最终调整数'] = data[['九星最终调整数', '八神最终调整数', '八门最终调整数', '天干最终调整数', '日在月最终调整数']].sum(axis=1)

        # 计算调整数差值
        data['调整数差值'] = data['最终调整数'] - data['调整']

        # 计算准确列
        data['准确'] = data['调整数差值'].apply(lambda x: 1 if -2 <= x <= 2 else 0)

        # 删除不需要的年月日列
        data.drop(['Year', 'Month', 'Day'], axis=1, inplace=True)

        # 保存更新后的工作表到新的Excel文件中
        data.to_excel(writer, sheet_name=sheet_name, index=False)

print("处理完毕，所有工作表已更新并保存到：" + output_path)
