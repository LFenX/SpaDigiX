import pandas as pd

# Load the Excel file
file_path = '第二步-澳门2020-2024年排干数据第一步.xlsx'
excel_data = pd.ExcelFile(file_path)

# List all sheet names to understand the structure
sheet_names = excel_data.sheet_names

# Define tian gan and their grouping for angle calculation
tianganjiayi = [['甲', '乙'], ['丙', '丁'], ['戊', '己'], ['庚', '辛'], ['壬', '癸']]
tianganbingding = [['丙', '丁'], ['戊', '己'], ['庚', '辛'], ['壬', '癸'], ['甲', '乙']]
tianganwuji = [['戊', '己'], ['庚', '辛'], ['壬', '癸'], ['甲', '乙'], ['丙', '丁']]
tiangangengxin = [['庚', '辛'], ['壬', '癸'], ['甲', '乙'], ['丙', '丁'], ['戊', '己']]
tianganrengui = [['壬', '癸'], ['甲', '乙'], ['丙', '丁'], ['戊', '己'], ['庚', '辛']]


# Function to select the correct tian gan list
def get_tian_gan_list(tian_gan):
    if tian_gan in ['甲', '乙']:
        return tianganjiayi
    elif tian_gan in ['丙', '丁']:
        return tianganbingding
    elif tian_gan in ['戊', '己']:
        return tianganwuji
    elif tian_gan in ['庚', '辛']:
        return tiangangengxin
    elif tian_gan in ['壬', '癸']:
        return tianganrengui
    return []


# Function to calculate angle between two tian gan based on the correct list
def calculate_angle(tian_gan_1, tian_gan_2):
    tian_gan_list = get_tian_gan_list(tian_gan_1)
    group_count = len(tian_gan_list)

    # Find groups and indices
    group_1, index_1 = next((group_index, group.index(tian_gan_1)) for group_index, group in enumerate(tian_gan_list) if
                            tian_gan_1 in group)
    group_2, index_2 = next((group_index, group.index(tian_gan_2)) for group_index, group in enumerate(tian_gan_list) if
                            tian_gan_2 in group)

    # Calculate angle
    if group_1 == group_2:
        return 0

    group_diff = (group_2 - group_1) % group_count
    angle = group_diff * 60

    return angle


# Read all sheets into a dictionary
data = {sheet: excel_data.parse(sheet) for sheet in sheet_names}

# Sort sheets by year
sorted_sheets = sorted(sheet_names)

# Clean the tian gan values by stripping leading and trailing spaces
for sheet in sorted_sheets:
    df = data[sheet]
    for col in ['上一', '上二', '上三', '上四', '上五', '上六', '上特', '年干', '月干', '日干']:
        df[col] = df[col].str.strip()
    data[sheet] = df

# Re-run the processing with separate columns for each relationship
result_data = {}

for i, sheet in enumerate(sorted_sheets):
    df = data[sheet].copy()  # Use a copy to avoid SettingWithCopyWarning

    # Handle the comparison with the next year's first row
    if i < len(sorted_sheets) - 1:
        next_year_df = data[sorted_sheets[i + 1]]
        current_year_last_row = df.iloc[-1]
        next_year_first_row = next_year_df.iloc[0]

        # Initialize columns for relationships
        for col in ['上一关系', '上二关系', '上三关系', '上四关系', '上五关系', '上六关系', '上特关系','年干关系','月干关系','日干关系']:
            df[col] = ''

        for j, col in enumerate(['上一', '上二', '上三', '上四', '上五', '上六', '上特','年干','月干','日干']):
            relationship = []
            for next_col in ['上一', '上二', '上三', '上四', '上五', '上六', '上特', '年干', '月干', '日干']:
                angle = calculate_angle(current_year_last_row[col], next_year_first_row[next_col])
                relationship.append(f"{angle}")

            df.at[len(df) - 1, f'{col}关系'] = '-'.join(relationship)

    relationships = []

    for row_index in range(len(df) - 1):
        row = df.iloc[row_index]
        next_row = df.iloc[row_index + 1]

        for j, col in enumerate(['上一', '上二', '上三', '上四', '上五', '上六', '上特','年干','月干','日干']):
            relationship = []
            for next_col in ['上一', '上二', '上三', '上四', '上五', '上六', '上特', '年干', '月干', '日干']:
                angle = calculate_angle(row[col], next_row[next_col])
                relationship.append(f"{angle}")

            df.at[row_index, f'{col}关系'] = '-'.join(relationship)

    result_data[sheet] = df

# Save the results to a new Excel file
output_path = '澳门2020-2024年排干数据汇总纠正.xlsx'
with pd.ExcelWriter(output_path) as writer:
    for sheet, df in result_data.items():
        df.to_excel(writer, sheet_name=sheet, index=False)

output_path
