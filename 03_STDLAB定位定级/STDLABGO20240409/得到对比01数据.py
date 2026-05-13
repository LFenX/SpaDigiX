import pandas as pd

# Load the new Excel file
file_path = '加入生肖-输入实数数据-加入程序数-加入时辰和生肖组香港10-24年原始数据.xlsx'

# Read the Excel file (we need to get all sheet names first)
xls = pd.ExcelFile(file_path)
sheet_names = xls.sheet_names
sheets = {sheet: pd.read_excel(xls, sheet_name=sheet) for sheet in sheet_names}

# Define the palace and corresponding animal groups
palace_animal_groups = {
    '坎一': (['酉', '戌', '亥', '子', '丑', '寅'], ['卯', '辰', '巳', '午', '未', '申']),
    '坤二': (['巳', '午', '未', '申', '酉', '戌'], ['亥', '子', '丑', '寅', '卯', '辰']),
    '震三': (['子', '丑', '寅', '卯', '辰', '巳'], ['午', '未', '申', '酉', '戌', '亥']),
    '巽四': (['寅', '卯', '辰', '巳', '午', '未'], ['申', '酉', '戌', '亥', '子', '丑']),
    '乾六': (['申', '酉', '戌', '亥', '子', '丑'], ['寅', '卯', '辰', '巳', '午', '未']),
    '兑七': (['午', '未', '申', '酉', '戌', '亥'], ['子', '丑', '寅', '卯', '辰', '巳']),
    '艮八': (['亥', '子', '丑', '寅', '卯', '辰'], ['巳', '午', '未', '申', '酉', '戌']),
    '离九': (['卯', '辰', '巳', '午', '未', '申'], ['酉', '戌', '亥', '子', '丑', '寅'])
}

# Process each sheet in the Excel file
results = {}
for sheet_name, df in sheets.items():
    compare_01_data = []
    for index, row in df.iterrows():
        palace = row['双干宫']
        animal = row['预测生肖']
        group0, group1 = palace_animal_groups.get(palace, ([], []))
        if animal in group0:
            compare_01_data.append(0)
        elif animal in group1:
            compare_01_data.append(1)
        else:
            compare_01_data.append(None)

    # Add the new column to the dataframe
    df['预测01数据'] = compare_01_data
    results[sheet_name] = df

# Save the updated sheets to a new Excel file
output_path = '输入01数据-加入生肖-输入实数数据-加入程序数-加入时辰和生肖组香港10-24年原始数据.xlsx'
with pd.ExcelWriter(output_path) as writer:
    for sheet_name, df in results.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

output_path
