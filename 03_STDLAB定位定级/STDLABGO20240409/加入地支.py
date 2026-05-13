import pandas as pd

def add_earthly_branch_column(input_file_path, output_file_path):
    # Define the mapping of Zodiac animals to Earthly Branches
    zodiac_to_earthly_branch = {
        '鼠': '子',
        '牛': '丑',
        '虎': '寅',
        '兔': '卯',
        '龍': '辰',
        '蛇': '巳',
        '馬': '午',
        '羊': '未',
        '猴': '申',
        '雞': '酉',
        '狗': '戌',
        '豬': '亥'
    }

    # Load the Excel file
    xls = pd.ExcelFile(input_file_path)

    # Process each sheet
    processed_sheets = {}
    for sheet in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet)
        if '特號' in df.columns:
            df['地支'] = df['特號'].map(zodiac_to_earthly_branch)
            processed_sheets[sheet] = df

    # Save the processed sheets back to a new Excel file
    with pd.ExcelWriter(output_file_path) as writer:
        for sheet, df in processed_sheets.items():
            df.to_excel(writer, sheet_name=sheet, index=False)

# Example usage:
input_file_path = '澳门01-10-19数据.xlsx'
output_file_path = '加入地支-澳门01-10-19数据.xlsx'
add_earthly_branch_column(input_file_path, output_file_path)
