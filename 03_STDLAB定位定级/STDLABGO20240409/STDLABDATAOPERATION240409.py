import pandas as pd
from collections import defaultdict
import re

# Load the Excel file
file_path = '双干香港修正原始表格.xlsx'  # Replace with your actual file path
df = pd.read_excel(file_path)

# Function to extract items and their associated numbers from a given column data
def extract_items_properly(data):
    # Adjusting the pattern to capture the items and the numbers properly
    pattern = re.compile(r'([^\d\W]+)([+-]?\d)?')
    item_entries = pattern.findall(str(data))
    items = [entry[0] for entry in item_entries]  # Extract items
    numbers = [int(entry[1]) if entry[1] else 0 for entry in item_entries]  # Extract numbers, default to 0 if not present
    return items, numbers

# Function to process and format the counts for given columns
def process_columns_properly(df, column_names):
    dfs = {}

    for column_name in column_names:
        final_counts = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

        for _, row in df.iterrows():
            month_gan = row['月干']
            items, numbers = extract_items_properly(row[column_name])
            for item, number in zip(items, numbers):
                final_counts[month_gan][item][number] += 1

        # Create the formatted results DataFrame
        all_items = sorted(set(item for month_data in final_counts.values() for item in month_data))
        rows = []
        for month_gan, items in final_counts.items():
            row = {'月干': month_gan}
            for item in all_items:
                numbers_count = ['0({})'.format(count) if num == 0 else '{}({})'.format(num, count) for num, count in items[item].items()]
                row[item] = ' '.join(numbers_count) if numbers_count else ''
            rows.append(row)
        formatted_results = pd.DataFrame(rows, columns=['月干'] + all_items)
        formatted_results.fillna('', inplace=True)
        dfs[column_name] = formatted_results

    return dfs

# Specify the columns to process
column_names_proper = ['天干', '九星', '八门', '八神', '日在月']

# Process the columns with the corrected classification
dfs_proper = process_columns_properly(df, column_names_proper)

# Save each DataFrame to a separate sheet in the same Excel file
proper_output_file_path = '双干P0修正数据结果完整.xlsx'  # Adjust the file path as needed
with pd.ExcelWriter(proper_output_file_path) as writer:
    for sheet_name, data_df in dfs_proper.items():
        data_df.to_excel(writer, sheet_name=sheet_name, index=False)

