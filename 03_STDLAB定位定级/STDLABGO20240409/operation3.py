import pandas as pd
from collections import defaultdict
import re

# Function to extract items and their associated numbers from a given column data
def extract_items_properly(data):
    pattern = re.compile(r'([^\d\W]+)([+-]?\d)?')
    item_entries = pattern.findall(str(data))
    items = [entry[0] for entry in item_entries]  # Extract items
    numbers = [int(entry[1]) if entry[1] else 0 for entry in item_entries]  # Extract numbers, default to 0 if not present
    return items, numbers

# Function to process all sheets and accumulate results for each category in separate dataframes
def process_all_sheets(excel_path, sheet_names):
    accumulated_results = {
        "天干定数": defaultdict(lambda: defaultdict(lambda: defaultdict(int))),
        "日在月定数": defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    }

    for sheet_name in sheet_names:
        df = pd.read_excel(excel_path, sheet_name=sheet_name)
        for column_name in accumulated_results.keys():
            for _, row in df.iterrows():
                month_gan = row['月干']
                items, numbers = extract_items_properly(row[column_name])
                for item, number in zip(items, numbers):
                    accumulated_results[column_name][month_gan][item][number] += 1

    dfs = {}
    for category, data in accumulated_results.items():
        all_items = sorted(set(item for month_data in data.values() for item in month_data))
        rows = []
        for month_gan, items in data.items():
            row = {'月干': month_gan}
            for item in all_items:
                numbers_count = ['0({})'.format(count) if num == 0 else '{}({})'.format(num, count) for num, count in items[item].items()]
                row[item] = ' '.join(numbers_count) if numbers_count else ''
            rows.append(row)
        formatted_results = pd.DataFrame(rows, columns=['月干'] + all_items)
        formatted_results.fillna('', inplace=True)
        dfs[category] = formatted_results

    return dfs

# Specify the Excel file path and the sheet names to process
excel_file_path = '天干+日在月确定最终调整原始数据.xlsx'  # Replace with your actual file path
sheet_names = ['子月', '丑月', '寅月', '卯月', '辰月', '巳月', '午月', '未月', '申月', '酉月', '戌月', '亥月']

# Process all sheets and accumulate results
dfs_accumulated = process_all_sheets(excel_file_path, sheet_names)

# Save the accumulated results into a single Excel file with separate sheets for each category
output_accumulated_file_path = '天干+日在月最终调整出现次数汇总.xlsx'
with pd.ExcelWriter(output_accumulated_file_path) as writer:
    for sheet_name, data_df in dfs_accumulated.items():
        data_df.to_excel(writer, sheet_name=sheet_name, index=False)