import pandas as pd

# 加载Excel文件
file_path = '加入日柱-香港2010-2024民间尾号方法数据汇总.xlsx'
xls = pd.ExcelFile(file_path)

# 获取所有工作表的名称
sheet_names = xls.sheet_names

# 创建一个字典来存储按'日柱'第一个字符分类的数据
classified_data = {}

# 遍历每一个工作表
for sheet_name in sheet_names:
    # 读取工作表数据
    df = pd.read_excel(xls, sheet_name=sheet_name)

    # 遍历数据行
    for index, row in df.iterrows():
        first_char = row['日柱'][0]  # 获取'日柱'的第一个字符
        if first_char not in classified_data:
            classified_data[first_char] = []
        classified_data[first_char].append(row)

# 将列表转换为数据框，并按日期排序
for key in classified_data:
    df = pd.DataFrame(classified_data[key])
    df = df.sort_values(by='日期', ascending=True)  # 假设'日期'列存在且格式正确
    classified_data[key] = df

# 将分类好的数据保存到新的Excel文件中，每个类别一个工作表
output_path = '日柱-十干-香港2010-2024民间尾号方法数据汇总.xlsx'
with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
    for key, df in classified_data.items():
        df.to_excel(writer, sheet_name=key, index=False)
