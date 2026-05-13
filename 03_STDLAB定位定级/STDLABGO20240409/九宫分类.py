import pandas as pd

# Load the Excel file
file_path = '2-加入阴阳九宫-日柱-十干-香港2010-2024民间尾号方法数据汇总.xlsx'
excel_data = pd.ExcelFile(file_path)

# Display sheet names to understand the structure
sheet_names = excel_data.sheet_names


# Function to split and save the sheets based on the "阴阳局-九宫" column
def split_and_save_sheets(sheet_name):
    # Read the sheet into a DataFrame
    df = excel_data.parse(sheet_name)

    # Check if the target column exists
    if '阴阳局-九宫' not in df.columns:
        return f"Column '阴阳局-九宫' not found in sheet {sheet_name}"

    # Group by the '阴阳局-九宫' column
    grouped = df.groupby('阴阳局-九宫')

    # Create a new Excel writer object
    new_file_path = f'{sheet_name}_日柱-十干-香港2010-2024民间尾号方法数据汇总.xlsx'
    writer = pd.ExcelWriter(new_file_path, engine='xlsxwriter')

    # Write each group to a separate sheet
    for group_name, group_df in grouped:
        group_df.to_excel(writer, sheet_name=str(group_name), index=False)

    # Save the new Excel file
    writer.close()
    return new_file_path


# Process each sheet
results = {}
for sheet in sheet_names:
    result = split_and_save_sheets(sheet)
    results[sheet] = result

results
