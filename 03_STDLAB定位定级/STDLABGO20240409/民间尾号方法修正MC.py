import pandas as pd
from datetime import datetime

# 加载Excel文件
file_path_main = '澳门2020-2024年原始数据.xlsx'
file_path_zodiac_corrected = '生肖分配表.xlsx'

# 加载主文件中的所有工作表
xls_main = pd.ExcelFile(file_path_main)
sheets_main = {sheet_name: xls_main.parse(sheet_name) for sheet_name in xls_main.sheet_names}

# 加载修正后的生肖分配表中的所有工作表
xls_zodiac_corrected = pd.ExcelFile(file_path_zodiac_corrected)
zodiac_allocation_corrected = {sheet_name: xls_zodiac_corrected.parse(sheet_name) for sheet_name in
                               xls_zodiac_corrected.sheet_names}


# 定义循环处理函数
def circular_number(number):
    if number <= 0:
        return 49 + number
    elif number > 49:
        return number - 49
    return number


# 定义处理第一个公式的函数，包含循环逻辑和修正选择
def process_first_formula_corrected(sheet):
    # 定义要使用的列
    columns = ['一', '二', '三', '四', '五', '六']

    # 处理每一行的函数
    def process_row(row):
        # 提取并排序值
        values = sorted([row[col] for col in columns])
        # 选择第三小的值
        third_from_smallest = values[2]
        # 根据修正后的规则生成新数字并应用循环逻辑
        new_numbers = [
            circular_number(third_from_smallest),
            circular_number(third_from_smallest + 1),
            circular_number(third_from_smallest - 3),
            circular_number(third_from_smallest + 6),
            circular_number(third_from_smallest + 1 + 6),
            circular_number(third_from_smallest - 3 + 6)
        ]
        # 按指定格式连接数字
        result = '-'.join(map(str, new_numbers))
        return result

    # 对每一行应用处理函数
    sheet['第一公式数字'] = sheet.apply(process_row, axis=1)
    return sheet


# 定义处理第二个公式的函数，包含循环逻辑
def process_second_formula_circular(sheet):
    # 提取最后一位数字的函数
    def last_digit(number):
        return number % 10

    # 处理每一行的函数
    def process_row(row):
        # 提取“一”和“六”列的最后一位数字
        last_digit_one = last_digit(row['一'])
        last_digit_six = last_digit(row['六'])
        # 计算最后一位数字之和
        sum_last_digits = last_digit_one + last_digit_six
        # 生成以和为中心的五个连续数字并应用循环逻辑
        new_numbers = [circular_number(sum_last_digits + i) for i in range(-2, 3)]
        # 按指定格式连接数字
        result = '-'.join(map(str, new_numbers))
        return result

    # 对每一行应用处理函数
    sheet['第二公式数字'] = sheet.apply(process_row, axis=1)
    return sheet


# 定义验证和清理生成列的函数
def clean_and_validate_generated_columns(sheet):
    # 移除'第一公式数字'或'第二公式数字'为空的行
    sheet = sheet.dropna(subset=['第一公式数字', '第二公式数字'])

    # 确保列中没有空字符串
    sheet = sheet[sheet['第一公式数字'].str.strip() != '']
    sheet = sheet[sheet['第二公式数字'].str.strip() != '']

    # 确保'第一公式数字'和'第二公式数字'中的所有段都是有效整数
    def validate_column(column):
        valid_rows = []
        for row in sheet.itertuples():
            try:
                numbers = list(map(int, getattr(row, column).split('-')))
                valid_rows.append(row.Index)
            except ValueError:
                continue
        return valid_rows

    valid_rows_first = validate_column('第一公式数字')
    valid_rows_second = validate_column('第二公式数字')

    # 仅保留有效行
    valid_rows = list(set(valid_rows_first).intersection(valid_rows_second))
    sheet = sheet.loc[valid_rows]

    return sheet


# 定义根据日期选择生肖分配表的函数
def select_zodiac_table(date):
    date = pd.to_datetime(date)
    if date <= pd.Timestamp('2010-02-14'):
        return zodiac_allocation_corrected['2009']
    elif date <= pd.Timestamp('2011-02-02'):
        return zodiac_allocation_corrected['2010']
    elif date <= pd.Timestamp('2012-01-25'):
        return zodiac_allocation_corrected['2011']
    elif date <= pd.Timestamp('2013-02-09'):
        return zodiac_allocation_corrected['2012']
    elif date <= pd.Timestamp('2014-01-30'):
        return zodiac_allocation_corrected['2013']
    elif date <= pd.Timestamp('2015-02-18'):
        return zodiac_allocation_corrected['2014']
    elif date <= pd.Timestamp('2016-02-07'):
        return zodiac_allocation_corrected['2015']
    elif date <= pd.Timestamp('2017-01-27'):
        return zodiac_allocation_corrected['2016']
    elif date <= pd.Timestamp('2018-02-15'):
        return zodiac_allocation_corrected['2017']
    elif date <= pd.Timestamp('2019-02-04'):
        return zodiac_allocation_corrected['2018']
    elif date <= pd.Timestamp('2020-03-06'):
        return zodiac_allocation_corrected['2019']
    elif date <= pd.Timestamp('2021-02-11'):
        return zodiac_allocation_corrected['2020']
    elif date <= pd.Timestamp('2022-01-30'):
        return zodiac_allocation_corrected['2021']
    elif date <= pd.Timestamp('2023-01-20'):
        return zodiac_allocation_corrected['2022']
    elif date <= pd.Timestamp('2024-02-08'):
        return zodiac_allocation_corrected['2023']
    else:
        return zodiac_allocation_corrected['2024']


# 定义根据年份映射数字到生肖的函数
def map_to_zodiac(number, zodiac_table):
    for zodiac, numbers in zodiac_table.items():
        if number in numbers:
            return zodiac
    return "None"


# 定义处理所有工作表的生肖转换函数，使用修正后的分配表
def process_zodiac_conversion_all_sheets_corrected(sheets, zodiac_allocation_corrected):
    # 将数字转换为生肖的函数
    def convert_row_to_zodiac(row, column, zodiac_table):
        numbers = list(map(int, row[column].split('-')))
        zodiacs = [map_to_zodiac(num, zodiac_table) for num in numbers]
        return '-'.join(zodiacs)

    # 对每一行应用转换函数
    for sheet_name, sheet in sheets.items():
        # 根据日期选择对应的生肖分配表
        sheet['日期'] = pd.to_datetime(sheet['日期'])
        sheet['生肖分配表'] = sheet['日期'].apply(select_zodiac_table)
        sheet['生肖分配表'] = sheet['生肖分配表'].apply(
            lambda x: {col: x[col].dropna().astype(int).tolist() for col in x.columns})

        sheet['第一公式生肖'] = sheet.apply(lambda row: convert_row_to_zodiac(row, '第一公式数字', row['生肖分配表']),
                                            axis=1)
        sheet['第二公式生肖'] = sheet.apply(lambda row: convert_row_to_zodiac(row, '第二公式数字', row['生肖分配表']),
                                            axis=1)

        # 删除临时列
        sheet = sheet.drop(columns=['生肖分配表'])

    return sheets


# 处理所有工作表的第一个公式，包含循环逻辑
processed_sheets_first_corrected = {sheet_name: process_first_formula_corrected(sheet) for sheet_name, sheet in
                                    sheets_main.items()}

# 处理所有工作表的第二个公式，包含循环逻辑
processed_sheets_both_corrected = {sheet_name: process_second_formula_circular(sheet) for sheet_name, sheet in
                                   processed_sheets_first_corrected.items()}

# 清理并验证所有工作表的生成列
cleaned_validated_sheets_both_corrected = {sheet_name: clean_and_validate_generated_columns(sheet) for sheet_name, sheet
                                           in processed_sheets_both_corrected.items()}

# 使用修正后的分配表处理所有工作表的生肖转换
processed_sheets_final_corrected = process_zodiac_conversion_all_sheets_corrected(
    cleaned_validated_sheets_both_corrected, zodiac_allocation_corrected)

# 将处理后的工作表保存回新的Excel文件中，包含修正后的第一个公式、循环逻辑和修正后的生肖分配
output_file_path_final_corrected = '澳门2020-2024民间尾号方法数据汇总.xlsx'

with pd.ExcelWriter(output_file_path_final_corrected) as writer:
    for sheet_name, sheet_data in processed_sheets_final_corrected.items():
        sheet_data.to_excel(writer, sheet_name=sheet_name, index=False)