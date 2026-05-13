import pandas as pd
from functionSpaDigiXONEANDSEVEN_P3MC_240515  import getSpaDigiXdingweideshu
def process_workbook(file_path, combined_data):
    excel_data = pd.ExcelFile(file_path)
    all_sheets_data = {}

    for sheet_name in excel_data.sheet_names:
        df = pd.read_excel(excel_data, sheet_name=sheet_name)
        df['日期'] = pd.to_datetime(df['日期'])
        df['天干调整数'] = df.apply(
            lambda row: getSpaDigiXdingweideshu(row['日期'].year, row['日期'].month, row['日期'].day)[3],
            axis=1)
        df['九星调整数'] = df.apply(
            lambda row: getSpaDigiXdingweideshu(row['日期'].year, row['日期'].month, row['日期'].day)[4],
            axis=1)
        df['八神调整数'] = df.apply(
            lambda row: getSpaDigiXdingweideshu(row['日期'].year, row['日期'].month, row['日期'].day)[5],
            axis=1)
        df['八门调整数'] = df.apply(
            lambda row: getSpaDigiXdingweideshu(row['日期'].year, row['日期'].month, row['日期'].day)[6],
            axis=1)
        all_sheets_data[sheet_name] = df
    output_path = f'240523-进一步处理-{file_path}'
    with pd.ExcelWriter(output_path) as writer:
        for sheet_name, data in all_sheets_data.items():
            data.to_excel(writer, sheet_name=sheet_name, index=False)
    return output_path

file_paths = [
    '澳门日在月调整更新初始.xlsx',
]
'''
# 替换以下文件路径
file_paths = [
    '澳门双干十二月份调整表格2010-2027.xlsx',

]'''
combined_data = pd.DataFrame()
processed_files = [process_workbook(fp, combined_data) for fp in file_paths]
