import pandas as pd

# 甲子列表
gan_zhi_mapping = [
    "甲子", "乙丑", "丙寅", "丁卯", "戊辰", "己巳", "庚午", "辛未", "壬申", "癸酉",
    "甲戌", "乙亥", "丙子", "丁丑", "戊寅", "己卯", "庚辰", "辛巳", "壬午", "癸未",
    "甲申", "乙酉", "丙戌", "丁亥", "戊子", "己丑", "庚寅", "辛卯", "壬辰", "癸巳",
    "甲辰", "乙巳", "丙午", "丁未", "戊申", "己酉", "庚戌", "辛亥", "壬子", "癸丑",
    "甲寅", "乙卯", "丙辰", "丁巳", "戊午", "己未", "庚申", "辛酉", "壬戌", "癸亥"
]

# 加载原始Excel文件
file_path = '2010-2024年澳门汇总定级结果表G3MC-含准确率分析和错误标注240120.xlsx'
sheet_names = pd.ExcelFile(file_path).sheet_names

# 创建新的Excel写入对象
output_file_path = '2010-2024年澳门60甲子月干支汇总定级结果表G3MC-含准确率分析和错误标注240120.xlsx'
writer = pd.ExcelWriter(output_file_path, engine='xlsxwriter')

accuracy_data_list = []

# 遍历每个工作表
for sheet_name in sheet_names[:-1]:  # 排除准确率统计表
    data = pd.read_excel(file_path, sheet_name=sheet_name)
    data[['年干支', '月干支', '日干支']] = data['年月日干支'].str.split('，', expand=True)

    # 按甲子列表中的月干支分类数据
    for ganzhi in gan_zhi_mapping:
        month_data = data[data['月干支'] == ganzhi]
        if not month_data.empty:
            month_data.to_excel(writer, sheet_name=ganzhi, index=False)

            # 计算并收集每个月干支的准确率数据
            accuracy = month_data['准确'].mean()
            sample_count = month_data['准确'].count()
            accuracy_data_list.append({'月干支': ganzhi, '准确率': accuracy, '样本数量': sample_count})

# 创建准确率统计DataFrame
accuracy_data = pd.DataFrame(accuracy_data_list)

# 将准确率统计数据写入第61个工作表
accuracy_data.to_excel(writer, sheet_name='准确率统计', index=False)

# 保存并关闭Excel文件
writer.close()

