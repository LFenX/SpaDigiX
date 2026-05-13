import pandas as pd


def binary_result(value):
    return 1 if value > 0 else 0


def accuracy_check(row, time_column):
    return 1 if row[time_column] == row['正确数串'] else 0


def process_sheet(sheet_data):
    #sheet_data['子时零一结果'] = sheet_data['子时'].apply(binary_result)
    #sheet_data['午时零一结果'] = sheet_data['午时'].apply(binary_result)
    sheet_data['酉时零一结果'] = sheet_data['酉时'].apply(binary_result)

    #sheet_data['子时零一准确'] = sheet_data.apply(lambda row: accuracy_check(row, '子时零一结果'), axis=1)
    #sheet_data['午时零一准确'] = sheet_data.apply(lambda row: accuracy_check(row, '午时零一结果'), axis=1)
    #sheet_data['酉时零一准确'] = sheet_data.apply(lambda row: accuracy_check(row, '酉时零一结果'), axis=1)

    return sheet_data


def process_data(file_path, output_file_path):
    # 读取Excel文件中的所有工作表
    xls = pd.ExcelFile(file_path)
    sheet_names = xls.sheet_names

    # 创建一个字典来存储处理后的数据
    processed_sheets = {}

    for sheet_name in sheet_names:
        # 读取每个工作表
        data = pd.read_excel(file_path, sheet_name=sheet_name)
        # 处理每个工作表
        processed_data = process_sheet(data)
        # 将处理后的数据存储在字典中
        processed_sheets[sheet_name] = processed_data

    # 将处理后的所有工作表保存到一个新的Excel文件中
    with pd.ExcelWriter(output_file_path) as writer:
        for sheet_name, data in processed_sheets.items():
            data.to_excel(writer, sheet_name=sheet_name, index=False)


# 指定要处理的文件路径和输出文件路径
file_path = 'F1MC澳门2024编码四酉_时结果240122.xlsx'
output_file_path = 'F1MC澳门2024编码四酉_时结果240122.xlsx'

# 处理数据
process_data(file_path, output_file_path)

print(f"所有工作表的数据已处理并保存到：{output_file_path}")

