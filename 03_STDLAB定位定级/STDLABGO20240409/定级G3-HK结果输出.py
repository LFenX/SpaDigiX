import pandas as pd
from functionSpadigiXAPPTHREEANDTHREEG_3_1_HK  import  getdingjideshu
def process_workbook(file_path, combined_data):
    excel_data = pd.ExcelFile(file_path)
    all_sheets_data = {}

    for sheet_name in excel_data.sheet_names:
        df = pd.read_excel(excel_data, sheet_name=sheet_name)
        df['日期'] = pd.to_datetime(df['日期'])
        shichengduiyinlist={0:"子",1:"丑",2:"寅",3:"卯",4:"辰",5:"巳",6:"午",7:"未",8:"申",9:"酉",10:"戌",11:"亥"}
        for hour in range(12):  # 0代表子时，11代表亥时
            df[f'{shichengduiyinlist[hour]}时定级程序'] = df.apply(
                lambda row: getdingjideshu(row['日期'].year, row['日期'].month, row['日期'].day, 2*hour)[0],
                axis=1)

        all_sheets_data[sheet_name] = df

    output_path = f'香港2023-2024-新定级数据一阶段.xlsx'
    with pd.ExcelWriter(output_path) as writer:
        for sheet_name, data in all_sheets_data.items():
            data.to_excel(writer, sheet_name=sheet_name, index=False)
    return output_path

# 替换以下文件路径
file_paths = [
    '香港平码实数表.xlsx',
  ]
combined_data = pd.DataFrame()

processed_files = [process_workbook(fp, combined_data) for fp in file_paths]