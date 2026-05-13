import pandas as pd

# Load the data
real_numbers_path = "香港10-24实数表格.xlsx"
adjustment_path = "香港2010-2023完整数据生肖版.xlsx"

real_number_data = pd.read_excel(real_numbers_path)
adjustment_xls = pd.ExcelFile(adjustment_path)

# Convert date columns to datetime for proper merging
real_number_data['日期'] = pd.to_datetime(real_number_data['日期'])

# Dictionary to store updated DataFrames
updated_sheets = {}

# Merge and update the real numbers for each sheet in the first file
for sheet_name in adjustment_xls.sheet_names:
    sheet_data = pd.read_excel(adjustment_xls, sheet_name=sheet_name)
    sheet_data['日期'] = pd.to_datetime(sheet_data['日期'])
    merged_data = sheet_data.merge(real_number_data, on='日期', how='left', suffixes=('_old', '_new'))
    merged_data.drop(columns=['实数_old'], inplace=True)
    merged_data.rename(columns={'实数_new': '实数'}, inplace=True)
    updated_sheets[sheet_name] = merged_data

# Adjust the column order to place '实数' right after '生肖'
adjusted_sheets = {}
for sheet_name, data in updated_sheets.items():
    col_order = ['日期', '特', '生肖', '实数'] + [col for col in data.columns if col not in ['日期', '特', '生肖', '实数']]
    adjusted_data = data[col_order]
    adjusted_sheets[sheet_name] = adjusted_data

# Save the final adjusted data back to a new Excel file
output_path = "香港实数更新2010-2023完整数据生肖版.xlsx"
with pd.ExcelWriter(output_path) as writer:
    for sheet_name, data in adjusted_sheets.items():
        data.to_excel(writer, sheet_name=sheet_name, index=False)
