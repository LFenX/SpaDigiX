import pandas as pd

# Define the date ranges for each year mapping
date_ranges = {
    '2009': ('2010-01-01', '2010-02-14'),
    '2010': ('2010-02-15', '2011-02-02'),
    '2011': ('2011-02-03', '2012-01-25'),
    '2012': ('2012-01-26', '2013-02-13'),
    '2013': ('2013-02-14', '2014-02-03'),
    '2014': ('2014-02-04', '2015-02-21'),
    '2015': ('2015-02-22', '2016-02-10'),
    '2016': ('2016-02-11', '2017-01-27'),
    '2017': ('2017-01-28', '2018-02-19'),
    '2018': ('2018-02-20', '2019-02-05'),
    '2019': ('2019-02-06', '2020-01-31'),
    '2020': ('2020-02-01', '2021-02-11'),
    '2021': ('2021-02-12', '2022-02-04'),
    '2022': ('2022-02-05', '2023-01-25'),
    '2023': ('2023-01-26', '2024-02-13'),
    '2024': ('2024-02-14', '2024-12-31')
}

# Convert date ranges to pandas datetime format
date_ranges = {k: (pd.to_datetime(v[0]), pd.to_datetime(v[1])) for k, v in date_ranges.items()}


# Function to get the appropriate mapping year based on the date
def get_mapping_year(date):
    for year, (start_date, end_date) in date_ranges.items():
        if start_date <= date <= end_date:
            return year
    return None


# Function to process each sheet with new date-based rules
def process_sheet_with_date_rules(sheet_name, xls1, xls2):
    # Load the original data sheet
    original_data = pd.read_excel(xls1, sheet_name=sheet_name)
    original_data['日期'] = pd.to_datetime(original_data['日期'])

    # Columns to be mapped
    columns_to_map = ['一', '二', '三', '四', '五', '六', '特']

    # Initialize the new columns
    for col in columns_to_map:
        original_data[f'上{col}'] = None

    # Process each row to apply the correct mapping based on the date
    for idx, row in original_data.iterrows():
        date = row['日期']
        mapping_year = get_mapping_year(date)
        mapping_data = pd.read_excel(xls2, sheet_name=mapping_year)
        mapping_dict = dict(zip(mapping_data['数字'], mapping_data['天干']))

        for col in columns_to_map:
            original_data.at[idx, f'上{col}'] = mapping_dict.get(row[col], None)

    return original_data


# Load the Excel files
file_path_1 = '澳门2020-2024年原始数据.xlsx'
xls1 = pd.ExcelFile(file_path_1)

file_path_2 = '2009-2024年号码天干对应表.xlsx'
xls2 = pd.ExcelFile(file_path_2)

# Process all sheets and store them in a dictionary
processed_sheets_date_rules = {sheet: process_sheet_with_date_rules(sheet, xls1, xls2) for sheet in xls1.sheet_names}

# Save the processed sheets to a new Excel file
output_file_path_date_rules = '澳门2020-2024年排干数据第一步.xlsx'
with pd.ExcelWriter(output_file_path_date_rules) as writer:
    for sheet_name, data in processed_sheets_date_rules.items():
        data.to_excel(writer, sheet_name=sheet_name, index=False)

print(output_file_path_date_rules)
