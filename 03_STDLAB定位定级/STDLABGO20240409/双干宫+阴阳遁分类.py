import pandas as pd

# Load the Excel file
file_path = '含双干宫+阴阳遁-加入地支-澳门01-10-19数据.xlsx'
xls = pd.ExcelFile(file_path)

# Get sheet names
sheet_names = xls.sheet_names

# Define the mapping from 生肖 to 地支
zodiac_to_earthly_branch = {
    '鼠': '子', '牛': '丑', '虎': '寅', '兔': '卯', '龙': '辰', '蛇': '巳',
    '马': '午', '羊': '未', '猴': '申', '鸡': '酉', '狗': '戌', '猪': '亥'
}

# Function to extract 地支 from 生肖特
def calculate_earthly_branch(zodiac_special):
    zodiac = zodiac_special.split('/')[0]
    return zodiac_to_earthly_branch.get(zodiac, '')

# Process each sheet and calculate the 地支 column
dfs = []

for sheet in sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet)
    dfs.append(df)

    if '生肖特' in df.columns and '地支' in df.columns:
        df['地支'] = df['生肖特'].apply(calculate_earthly_branch)
        dfs.append(df)

# Combine all dataframes into one
combined_df = pd.concat(dfs, ignore_index=True)

# Sort the combined dataframe by 日期 column in ascending order (from far to near)
combined_df['日期'] = pd.to_datetime(combined_df['日期'])
combined_df = combined_df.sort_values(by='日期', ascending=True)

# Check for unique values in 双干宫 and 阴阳遁
unique_shuangangang = combined_df['双干宫'].unique()
unique_yinyangdun = combined_df['阴阳遁'].unique()

# Create a dictionary to store the categorized data
categorized_data_sorted = {}

# Generate the categories based on 双干宫 and 阴阳遁 with sorted dates
for shuangangang in unique_shuangangang:
    for yinyangdun in unique_yinyangdun:
        category_name = f"{shuangangang}-{yinyangdun}"
        categorized_data_sorted[category_name] = combined_df[(combined_df['双干宫'] == shuangangang) & (combined_df['阴阳遁'] == yinyangdun)]

# Create a new Excel writer with sorted data
output_sorted_path = '双干宫+阴阳遁分类后-含双干宫+阴阳遁-加入地支-澳门01-10-19数据.xlsx'
with pd.ExcelWriter(output_sorted_path) as writer:
    for category, data in categorized_data_sorted.items():
        data.to_excel(writer, sheet_name=category, index=False)

output_sorted_path
