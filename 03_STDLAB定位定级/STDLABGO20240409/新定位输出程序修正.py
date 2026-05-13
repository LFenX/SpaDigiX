import pandas as pd
from functionSpaDigiXONEANDSEVEN_P3_240430  import  getSpaDigiXdingweideshu
zodiac_to_number = {
    '子': 1, '丑': 2, '寅': 3, '卯': 4,
    '辰': 5, '巳': 6, '午': 7, '未': 8,
    '申': 9, '酉': 10, '戌': 11, '亥': 12
}
def process_workbook(file_path, combined_data):
    excel_data = pd.ExcelFile(file_path)
    all_sheets_data = {}

    for sheet_name in excel_data.sheet_names:
        df = pd.read_excel(excel_data, sheet_name=sheet_name)
        df['日期'] = pd.to_datetime(df['日期'])
        shichengduiyinlist={0:"子",1:"丑",2:"寅",3:"卯",4:"辰",5:"巳",6:"午",7:"未",8:"申",9:"酉",10:"戌",11:"亥"}
        for hour in range(12):  # 0代表子时，11代表亥时
            df[f'{shichengduiyinlist[hour]}时程序'] = df.apply(
                lambda row: getSpaDigiXdingweideshu(row['日期'].year, row['日期'].month, row['日期'].day, 2*hour)[0],
                axis=1)
            hour_str = f'{shichengduiyinlist[hour]}时'

        for index, row in df.iterrows():
            real_number_column = f'{hour_str}实数'
            digit_match = row[real_number_column]  # 强制转换为字符串
            shengxiao_match = shichengduiyinlist[hour]
            digit_part = digit_match
            shengxiao = shengxiao_match

            for hour in range(12):  # 对每个时辰进行计算
                combined_value = digit_part + row[f'{shichengduiyinlist[hour]}时程序']
                if combined_value > 1:
                    new_number = round(combined_value - 1)
                elif -1 < combined_value <= 1:
                    new_number = -1 if -1 < combined_value < 0 else 0
                else:
                    new_number = round(combined_value)
                SSSX = zodiac_to_number.get(shengxiao, 0)
                new_number += SSSX
                if new_number > 12:
                    BIAOQIAN = new_number % 12 if new_number % 12 != 0 else 12
                elif new_number == 0:
                    BIAOQIAN = 12
                elif new_number < 0:
                    BIAOQIAN = 12 - ((-new_number) % 12)
                else:
                    BIAOQIAN = new_number
                label_zodiac = {v: k for k, v in zodiac_to_number.items()}.get(BIAOQIAN, '')
                df.at[index, f'{shichengduiyinlist[hour]}时'] = label_zodiac

        # 删除程序列
        for hour in range(12):
            df.drop(f'{shichengduiyinlist[hour]}时程序', axis=1, inplace=True)
            df.drop(f'{shichengduiyinlist[hour]}时实数', axis=1, inplace=True)
        all_sheets_data[sheet_name] = df

    output_path = f'香港2023-2024-新定位数据一阶段.xlsx'
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