import pandas as pd

# Load the Excel file
file_path = '含标识-香港2010-2024-最高吻合度分段汇总数据结果.xlsx'
excel_data = pd.ExcelFile(file_path)

# Get all sheet names
sheet_names = excel_data.sheet_names


def process_sheet_with_counts(df, sheet_name):
    try:
        # Ensure all column names are strings
        df.columns = df.columns.astype(str)

        # Find the '地支' column
        zhi_col = next((col for col in df.columns if '地支' in col), None)
        if zhi_col is None:
            print(f"Error: '地支' column not found in sheet {sheet_name}")
            return {}, {}

        # Find all '对比01数据' columns
        compare_cols = [col for col in df.columns if '对比01数据' in col]

        # Initialize dictionaries to store results for this sheet
        sheet_result = {}
        zhi_counts_result = {}

        # Process each '对比01数据' column
        for compare_col in compare_cols:
            compare_index = df.columns.get_loc(compare_col)
            next_col = df.columns[compare_index + 1]

            # Compare the two columns and get the matching 地支 values
            matching_zhi = df[zhi_col][df[compare_col] == df[next_col]]

            # Count occurrences of each 地支
            zhi_counts = matching_zhi.value_counts()
            zhi_counts_result[compare_col] = zhi_counts

            # Get the two groups of 地支 from the next column name
            zhi_groups = next_col.split('-')

            # Sort each group based on the counts
            sorted_group1 = sorted(zhi_groups[0], key=lambda x: zhi_counts.get(x, 0), reverse=True)
            sorted_group2 = sorted(zhi_groups[1], key=lambda x: zhi_counts.get(x, 0), reverse=True)

            # Combine the sorted groups into a new column name
            new_col_name = ''.join(sorted_group1) + '-' + ''.join(sorted_group2)

            # Store the result for this compare column
            sheet_result[compare_col] = {'原始规则': next_col, '修正顺序后规则': new_col_name}

        return sheet_result, zhi_counts_result
    except Exception as e:
        print(f"Error processing sheet {sheet_name}: {e}")
        return {}, {}


# Process each sheet and store the results
final_results = {}
zhi_counts_results = {}
for sheet_name in sheet_names:
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    sheet_result, zhi_counts_result = process_sheet_with_counts(df, sheet_name)
    final_results[sheet_name] = sheet_result
    zhi_counts_results[sheet_name] = zhi_counts_result

# Create a new Excel writer for the processed results
output_file_path = '香港01最优规则-根据匹配数据最高出现次数排序.xlsx'
writer = pd.ExcelWriter(output_file_path, engine='xlsxwriter')

# Write the processed results to the new Excel file
for sheet_name, sheet_results in final_results.items():
    # Create a DataFrame for the results
    result_df = pd.DataFrame(sheet_results).T.reset_index()
    result_df.columns = ['重复规则计数', '原始规则', '修正顺序后规则']
    # Write the DataFrame to the respective sheet
    result_df.to_excel(writer, sheet_name=sheet_name, index=False)

# Save the processed results Excel file
writer.close()

# Create a new Excel writer for the 地支 counts results
zhi_counts_file_path = '香港01-匹配数据中地支出现次数排序.xlsx'
writer = pd.ExcelWriter(zhi_counts_file_path, engine='xlsxwriter')

# Write the 地支 counts results to the new Excel file
for sheet_name, zhi_counts_result in zhi_counts_results.items():
    for compare_col, zhi_counts in zhi_counts_result.items():
        # Create a DataFrame for the 地支 counts
        counts_df = pd.DataFrame(zhi_counts).reset_index()
        counts_df.columns = ['地支', '出现个数']
        # Write the DataFrame to a new sheet named after the compare column
        counts_df.to_excel(writer, sheet_name=f"{sheet_name}_{compare_col}", index=False)

# Save the 地支 counts Excel file
writer.close()

zhi_counts_file_path
