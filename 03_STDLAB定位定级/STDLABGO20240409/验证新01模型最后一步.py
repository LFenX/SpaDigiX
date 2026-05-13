import pandas as pd

# Load the Excel file
file_path = '输入01数据-加入生肖-输入实数数据-加入程序数-加入时辰和生肖组澳门20-24年原始数据.xlsx'
xls = pd.ExcelFile(file_path)


# Define the function to process each sheet
def process_sheet(sheet_df):
    # Split the '生肖组' into two groups
    sheet_df[['生肖组前', '生肖组后']] = sheet_df['生肖组'].str.split('-', expand=True)

    # Create the '预测生肖段' column based on '对比01数据'
    sheet_df['预测生肖段'] = sheet_df.apply(
        lambda row: row['生肖组前'] if row['预测01数据'] == 1 else row['生肖组后'],
        axis=1
    )

    # Rename '对比01数据' to '预测01数据'
    #sheet_df.rename(columns={'对比01数据': '预测01数据'}, inplace=True)

    # Move the '地支' column to be before '预测生肖段'
    cols = list(sheet_df.columns)
    #cols.insert(cols.index('预测生肖段'), cols.pop(cols.index('地支')))
    sheet_df = sheet_df[cols]
    sheet_df.drop(columns=['生肖组前', '生肖组后'], inplace=True)

    return sheet_df


# Process each sheet and store the results
processed_sheets = {}
for sheet_name in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet_name)
    processed_df = process_sheet(df)
    processed_sheets[sheet_name] = processed_df

# Save the processed data to a new Excel file
output_file_path = '澳门01模型20-24年数据.xlsx'
with pd.ExcelWriter(output_file_path) as writer:
    for sheet_name, processed_df in processed_sheets.items():
        processed_df.to_excel(writer, sheet_name=sheet_name, index=False)
