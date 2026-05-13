import pandas as pd

# Load the uploaded Excel file
file_path_data = '澳门2020-2024历史数据未处理.xlsx'
data_excel = pd.ExcelFile(file_path_data)


# Function to reformat data by grouping every 17 rows and placing them side by side with correct column names
def reformat_data_in_groups_with_correct_columns(df, group_size=17):
    # Split the data into chunks of 17 rows
    chunks = [df.iloc[i:i + group_size].reset_index(drop=True) for i in range(0, len(df), group_size)]

    # Concatenate these chunks side by side and rename columns
    reformatted_df = pd.concat(chunks, axis=1)
    reformatted_df.columns = range(1, len(chunks) + 1)

    return reformatted_df


# Process all sheets in the Excel file
all_sheets_reformatted_correct = {}
for sheet_name in data_excel.sheet_names:
    df = data_excel.parse(sheet_name, dtype=str)  # Read data as string to preserve format
    reformatted_df = reformat_data_in_groups_with_correct_columns(df)
    all_sheets_reformatted_correct[sheet_name] = reformatted_df

# Save all reformatted sheets to a new Excel file with correct column names
output_path_all_sheets_correct = 'reformatted_data_all_sheets_correct.xlsx'
with pd.ExcelWriter(output_path_all_sheets_correct) as writer:
    for sheet_name, reformatted_df in all_sheets_reformatted_correct.items():
        reformatted_df.to_excel(writer, index=False, sheet_name=sheet_name)

# Display the output path
output_path_all_sheets_correct
