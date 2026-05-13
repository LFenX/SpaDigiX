import pandas as pd

# Load the Excel file
file_path = '澳门-日在月出现次数汇总240525.xlsx'
xls = pd.ExcelFile(file_path)

# Initialize an empty dictionary to hold processed dataframes
processed_data = {}

# Function to process each cell with added debugging
def process_cell(cell):
    if pd.isna(cell):
        return cell
    # Split the cell content into individual numbers and their counts
    elements = cell.split()
    numbers_counts = []
    for element in elements:
        try:
            number, count = element.split('(')
            count = count.rstrip(')')
            numbers_counts.append((int(number), int(count)))
        except ValueError:
            continue
    if not numbers_counts:
        return cell
    # Find the number with the maximum count
    max_count = max(numbers_counts, key=lambda x: (x[1], -abs(x[0]), -x[0]))
    return max_count[0]

# Process each sheet
for sheet_name in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name)
    processed_df = df.applymap(process_cell)
    processed_data[sheet_name] = processed_df

# Save the processed data to a new Excel file
output_path = '澳门-日在月出现次数最多240525.xlsx'
with pd.ExcelWriter(output_path) as writer:
    for sheet_name, processed_df in processed_data.items():
        processed_df.to_excel(writer, sheet_name=sheet_name, index=False)

output_path
