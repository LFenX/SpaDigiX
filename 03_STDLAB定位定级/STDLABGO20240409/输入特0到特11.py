import pandas as pd

# Load the uploaded Excel file
file_path = '输入十二时辰01数据-输入十二时辰生肖_输入实数数据-加入十二时基础数据-含地支-香港01数据2010-2024.xlsx'
xls = pd.ExcelFile(file_path)

# List all sheet names to understand the structure
sheet_names = xls.sheet_names


# Define the function to add and fill new columns with the corrected logic
def process_sheet_with_circular_mapping(sheet_name):
    df = xls.parse(sheet_name)

    # 创建特0到特11列
    for i in range(12):
        df[f'特{i}'] = None

    # 十二时辰列表
    shichen = ['子时', '丑时', '寅时', '卯时', '辰时', '巳时', '午时', '未时', '申时', '酉时', '戌时', '亥时']

    # 地支列到时辰列的映射
    dizhi_to_shichen = {d: f"{d}时" for d in ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']}

    # 处理每一行
    for i in range(len(df) - 1):
        dizhi = df.loc[i, '地支']
        if dizhi not in dizhi_to_shichen:
            print(f"Unexpected 地支 value '{dizhi}' at row {i}")
            continue
        start_col = dizhi_to_shichen[dizhi]
        start_index = shichen.index(start_col)

        for j in range(12):
            target_col = f'特{j}'
            source_col = shichen[(start_index + j) % 12]
            df.loc[i + 1, target_col] = df.loc[i + 1, source_col]

    return df


# Process all sheets and save to a new Excel file with corrected circular mapping
output_file_path_circular = '输入特0-11-输入十二时辰01数据-输入十二时辰生肖_输入实数数据-加入十二时基础数据-含地支-香港01数据2010-2024.xlsx'
with pd.ExcelWriter(output_file_path_circular) as writer:
    for sheet in sheet_names:
        processed_df = process_sheet_with_circular_mapping(sheet)
        processed_df.to_excel(writer, sheet_name=sheet, index=False)

output_file_path_circular
