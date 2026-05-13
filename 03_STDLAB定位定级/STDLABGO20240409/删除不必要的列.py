import pandas as pd

# 读取Excel文件
excel_path = '完整-零一12时辰数据-24到26年.xlsx'
excel_data = pd.read_excel(excel_path, sheet_name=None)  # 读取所有工作表

# 创建一个空的字典来存储处理后的工作表
processed_data = {}

for sheet_name, df in excel_data.items():
    # 保留前七列和后十二列
    columns_to_keep = list(df.columns[:7]) + list(df.columns[-24:])
    processed_df = df[columns_to_keep]
    # 将处理后的DataFrame存储在字典中
    processed_data[sheet_name] = processed_df

# 将处理后的数据写入一个新的Excel文件
processed_excel_path = '保留生肖-零一12时辰数据-24到26年.xlsx'
with pd.ExcelWriter(processed_excel_path) as writer:
    for sheet_name, processed_df in processed_data.items():
        processed_df.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"处理后的文件已保存到 {processed_excel_path}")
