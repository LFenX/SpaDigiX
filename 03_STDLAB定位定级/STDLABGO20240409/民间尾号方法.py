import pandas as pd

# Load the Excel files
#file_path_main = '香港2010-2024完整数据生肖版.xlsx'

file_path_main = '澳门2020-2024年原始数据.xlsx'
file_path_zodiac_corrected = '生肖分配表.xlsx'

# Load all sheets from the main file
xls_main = pd.ExcelFile(file_path_main)
sheets_main = {sheet_name: xls_main.parse(sheet_name) for sheet_name in xls_main.sheet_names}

# Load the corrected zodiac allocation table
xls_zodiac_corrected = pd.ExcelFile(file_path_zodiac_corrected)
zodiac_allocation_corrected = xls_zodiac_corrected.parse(xls_zodiac_corrected.sheet_names[0])

# Extract the zodiac allocation for the corrected table
zodiac_corrected = {col: zodiac_allocation_corrected[col].dropna().astype(int).tolist() for col in
                    zodiac_allocation_corrected.columns}


# Function to apply circular logic
def circular_number(number):
    if number <= 0:
        return 49 + number
    elif number > 49:
        return number - 49
    return number


# Define the function to process the first formula with circular logic and corrected selection for one sheet
def process_first_formula_corrected(sheet):
    # Define the columns to be used
    columns = ['一', '二', '三', '四', '五', '六']

    # Function to process each row
    def process_row(row):
        # Extract and sort the values
        values = sorted([row[col] for col in columns])
        # Select the third smallest value (from the end, it is the third from the smallest)
        third_from_smallest = values[2]
        # Generate new numbers based on the corrected rule and apply circular logic
        new_numbers = [
            circular_number(third_from_smallest),
            circular_number(third_from_smallest + 1),
            circular_number(third_from_smallest - 3),
            circular_number(third_from_smallest + 6),
            circular_number(third_from_smallest + 1 + 6),
            circular_number(third_from_smallest - 3 + 6)
        ]
        # Concatenate numbers in specified format
        result = '-'.join(map(str, new_numbers))
        return result

    # Apply the function to each row
    sheet['第一公式数字'] = sheet.apply(process_row, axis=1)
    return sheet


# Define the function to process the second formula with circular logic for one sheet
def process_second_formula_circular(sheet):
    # Function to extract the last digit
    def last_digit(number):
        return number % 10

    # Function to process each row
    def process_row(row):
        # Extract the last digits from columns '一' and '六'
        last_digit_one = last_digit(row['一'])
        last_digit_six = last_digit(row['六'])
        # Sum the last digits
        sum_last_digits = last_digit_one + last_digit_six
        # Generate five consecutive numbers centered around the sum and apply circular logic
        new_numbers = [circular_number(sum_last_digits + i) for i in range(-2, 3)]
        # Concatenate numbers in specified format
        result = '-'.join(map(str, new_numbers))
        return result

    # Apply the function to each row
    sheet['第二公式数字'] = sheet.apply(process_row, axis=1)
    return sheet


# Function to validate and clean the generated columns
def clean_and_validate_generated_columns(sheet):
    # Remove rows with empty '第一公式数字' or '第二公式数字'
    sheet = sheet.dropna(subset=['第一公式数字', '第二公式数字'])

    # Ensure no empty strings in the columns
    sheet = sheet[sheet['第一公式数字'].str.strip() != '']
    sheet = sheet[sheet['第二公式数字'].str.strip() != '']

    # Ensure all segments in '第一公式数字' and '第二公式数字' are valid integers
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

    # Keep only valid rows
    valid_rows = list(set(valid_rows_first).intersection(valid_rows_second))
    sheet = sheet.loc[valid_rows]

    return sheet


# Function to map numbers to zodiac signs based on the given year
def map_to_zodiac(number, zodiac_table):
    for zodiac, numbers in zodiac_table.items():
        if number in numbers:
            return zodiac
    return "None"


# Function to process the zodiac conversion for all sheets with corrected table
def process_zodiac_conversion_all_sheets_corrected(sheets, zodiac_table):
    # Function to convert numbers to zodiac for a row
    def convert_row_to_zodiac(row, column, zodiac_table):
        numbers = list(map(int, row[column].split('-')))
        zodiacs = [map_to_zodiac(num, zodiac_table) for num in numbers]
        return '-'.join(zodiacs)

    # Apply the conversion to each row
    for sheet_name, sheet in sheets.items():
        sheet['第一公式生肖'] = sheet.apply(lambda row: convert_row_to_zodiac(row, '第一公式数字', zodiac_table),
                                            axis=1)
        sheet['第二公式生肖'] = sheet.apply(lambda row: convert_row_to_zodiac(row, '第二公式数字', zodiac_table),
                                            axis=1)
    return sheets


# Process all sheets with the corrected first formula with circular logic
processed_sheets_first_corrected = {sheet_name: process_first_formula_corrected(sheet) for sheet_name, sheet in
                                    sheets_main.items()}

# Process all sheets with the second formula with circular logic
processed_sheets_both_corrected = {sheet_name: process_second_formula_circular(sheet) for sheet_name, sheet in
                                   processed_sheets_first_corrected.items()}

# Clean and validate the generated columns for all sheets
cleaned_validated_sheets_both_corrected = {sheet_name: clean_and_validate_generated_columns(sheet) for sheet_name, sheet
                                           in processed_sheets_both_corrected.items()}

# Process all sheets for zodiac conversion with corrected table
processed_sheets_final_corrected = process_zodiac_conversion_all_sheets_corrected(
    cleaned_validated_sheets_both_corrected, zodiac_corrected)

# Save the processed sheets back to a new Excel file with corrected first formula, circular logic, and corrected zodiac allocation
output_file_path_final_corrected = '澳门2020-2024民间尾号方法数据汇总.xlsx'

with pd.ExcelWriter(output_file_path_final_corrected) as writer:
    for sheet_name, sheet_data in processed_sheets_final_corrected.items():
        sheet_data.to_excel(writer, sheet_name=sheet_name, index=False)

output_file_path_final_corrected

