import pandas as pd
from zhdate import ZhDate
import datetime


# Function to extract the last digit
def extract_last_digit(series):
    return series.apply(lambda x: int(str(x)[-1]) if pd.notnull(x) else None)


# Function to convert date to lunar date and extract the last digit of the day
def convert_to_lunar(date_series):
    lunar_days = []
    for date in date_series:
        if pd.notnull(date):
            date_obj = pd.to_datetime(date)
            lunar_date = ZhDate.from_datetime(date_obj)
            lunar_days.append(int(str(lunar_date.lunar_day)[-1]))
        else:
            lunar_days.append(None)
    return lunar_days


# Define the five-element attributes
attribute_map = {
    1: '水', 6: '水',
    2: '火', 7: '火',
    3: '木', 8: '木',
    4: '金', 9: '金',
    5: '土', 0: '土'
}

# Define the relationship rules
generation_map = {
    '水': '木', '木': '火', '火': '土', '土': '金', '金': '水'
}
overcoming_map = {
    '水': '火', '木': '土', '火': '金', '土': '水', '金': '木'
}


# Function to determine the relationship
def determine_relationship(attr1, attr2):
    if attr1 == attr2:
        return '本我'
    elif generation_map[attr1] == attr2:
        return '生'
    elif overcoming_map[attr1] == attr2:
        return '克'
    elif generation_map[attr2] == attr1:
        return '被生'
    elif overcoming_map[attr2] == attr1:
        return '被克'
    else:
        return '无关'


# Load the Excel file
file_path = '福建体彩31选7-2016-2024年数据汇总.xlsx'
excel_data = pd.read_excel(file_path, sheet_name=None)

# Ensure sheet names are sorted by year
sheet_names = sorted(excel_data.keys())

# First pass: add last digit and attribute columns
for sheet_name in sheet_names:
    df = excel_data[sheet_name]

    # Extract last digits for specified columns
    df['上一'] = extract_last_digit(df['一'])
    df['上二'] = extract_last_digit(df['二'])
    df['上三'] = extract_last_digit(df['三'])
    df['上四'] = extract_last_digit(df['四'])
    df['上五'] = extract_last_digit(df['五'])
    df['上六'] = extract_last_digit(df['六'])
    df['上七'] = extract_last_digit(df['七'])
    df['上特'] = extract_last_digit(df['特'])
    df['公历日尾'] = extract_last_digit(df['日期'].dt.day)
    df['农历日尾'] = convert_to_lunar(df['日期'])

    # Add attributes columns
    for col in ['上一', '上二', '上三', '上四', '上五', '上六','上七', '上特', '公历日尾', '农历日尾']:
        df[f'{col}属性'] = df[col].map(attribute_map)

    # Save back to dictionary
    excel_data[sheet_name] = df

# Second pass: add relationship columns
for i in range(len(sheet_names)):
    sheet_name = sheet_names[i]
    df = excel_data[sheet_name]

    # Prepare next sheet for comparison if exists
    if i < len(sheet_names) - 1:
        next_df = excel_data[sheet_names[i + 1]]
        next_row = next_df.iloc[0]
    else:
        next_row = None

    # Add relationship columns
    for idx in range(len(df)):
        base_row = df.iloc[idx]
        if idx < len(df) - 1:
            compare_row = df.iloc[idx + 1]
        else:
            if next_row is not None:
                compare_row = next_row
            else:
                continue  # Skip the last row of the last sheet

        for base_col in ['上一', '上二', '上三', '上四', '上五', '上六','上七', '上特', '公历日尾', '农历日尾']:
            base_attr = base_row[f'{base_col}属性']
            relationships = []
            for compare_col in ['上一', '上二', '上三', '上四', '上五', '上六','上七', '上特', '公历日尾', '农历日尾']:
                compare_attr = compare_row[f'{compare_col}属性']
                rel = determine_relationship(base_attr, compare_attr)
                relationships.append(rel)
            df.at[idx, f'{base_col}关系'] = '-'.join(relationships)

    # Save back to dictionary
    excel_data[sheet_name] = df

# Save the processed data with relationships to a new Excel file
relationship_processed_file_path = '福建体彩31选7-2016-2024年尾号模型数据.xlsx'
with pd.ExcelWriter(relationship_processed_file_path) as writer:
    for sheet_name, df in excel_data.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)
