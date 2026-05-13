
import pandas as pd

from functionSpaDigiXONEANDSEVEN_P3MC_240515 import getSpaDigiXdingweideshu

# Function to extract numeric adjustments from string columns
def extract_adjustment(value):
    if '+' in value:
        return int(value.split('+')[-1])
    elif '-' in value:
        return -int(value.split('-')[-1])
    return 0

# Load the Excel file
file_path = '澳门双干十二月份调整数据表格P1-P3初始.xlsx'
excel_data = pd.ExcelFile(file_path)

# Prepare to save results to a new Excel file
output_path = '澳门天干日在月调整初始.xlsx'
writer = pd.ExcelWriter(output_path, engine='xlsxwriter')

# Process each sheet
for sheet_name in excel_data.sheet_names:
    sheet_data = pd.read_excel(excel_data, sheet_name=sheet_name)
    for index, row in sheet_data.iterrows():
        date = pd.to_datetime(row['日期'])
        year, month, day = date.year, date.month, date.day

        # Call the dummy function
        _, nine_star_adj, eight_gates_adj, eight_gods_adj = getSpaDigiXdingweideshu(year, month, day)

        # Update the DataFrame with these adjustments
        sheet_data.at[index, '九星调整数'] = nine_star_adj
        sheet_data.at[index, '八门调整数'] = eight_gates_adj
        sheet_data.at[index, '八神调整数'] = eight_gods_adj
        sheet_data.at[index, '日在月调整数'] = extract_adjustment(row['日在月'])

        # Compute the "天干调整数"
        total_adjustment = nine_star_adj + eight_gates_adj + eight_gods_adj + sheet_data.at[index, '日在月调整数']
        sheet_data.at[index, '天干调整数'] = row['误差值'] - total_adjustment

        # Extract and update the specific heavenly stems
        sheet_data.at[index, '具体天干'] = ''.join(filter(str.isalpha, row['天干']))

    # Save the processed sheet
    sheet_data.to_excel(writer, sheet_name=sheet_name, index=False)

# Save and close the Excel writer
writer.close()
print("Processing complete. All data saved to:", output_path)
