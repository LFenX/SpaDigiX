import pandas as pd
from collections import defaultdict
from functionSpaDigiXAPPONE import getthebasicmessageofnineGrids

# 定义日期范围
start_date = '2010-01-01'
end_date = '2025-01-01'
date_range = pd.date_range(start=start_date, end=end_date)

# 定义时辰对应的数字
time_dict = {
    '子时': 0, '丑时': 2, '寅时': 4, '卯时': 6, '辰时': 8, '巳时': 10,
    '午时': 12, '未时': 14, '申时': 16, '酉时': 18, '戌时': 20, '亥时': 22
}

# 初始化存储标签与数据的字典
label_data_dict = defaultdict(list)
date_time_dict = defaultdict(list)

# 遍历每一天和每个时辰，处理每个单元格的数据
for date in date_range:
    year, month, day = date.year, date.month, date.day
    for time_label, hour in time_dict.items():
        labels = getthebasicmessageofnineGrids(year, month, day, hour)[0]
        label = ''
        for i in range(0, 9):
            item = labels[i]
            if i == 4:
                label += item['地盘'] + item['九星'] + '-'
            else:
                label += item['地盘'] + item['八神'] + item['天盘'] + item['九星'] + item['八门'] + '-'
        label = label.rstrip('-')
        label_data_dict[label].append(1)  # 仅生成标签数据
        date_time_dict[label].append(f"{year}-{month}-{day}-{hour}")

# 处理相同标签的数据
final_data = []
for label, values in label_data_dict.items():
    combined_date_times = ','.join(date_time_dict[label])
    final_data.append([label, combined_date_times])

# 创建一个新的DataFrame保存最终结果
final_df = pd.DataFrame(final_data, columns=['标签', '日期和时辰'])

# 保存到新的Excel文件
output_file_path = '1080局.xlsx'
final_df.to_excel(output_file_path, index=False)