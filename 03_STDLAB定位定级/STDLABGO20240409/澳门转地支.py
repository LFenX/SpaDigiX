import pandas as pd
from backup_file import  getshuangganshicheng
from functionSpaDigiXAPPONE import  getthebasicmessageofnineGrids
from functionSpaDigiXONEANDSEVEN_P3MC_240515 import getSpaDigiXdingweideshu1
from functionSpaDigiXONEANDSEVENF1MC import  gettheSpaDigiX_value
from functionSpaDigiXONEANDSEVEN import  getSpaDigiXdingweideshu
# Define the mapping from 生肖 to 地支
zodiac_to_earthly_branch = {
    '鼠': '子', '牛': '丑', '虎': '寅', '兔': '卯', '龙': '辰', '蛇': '巳',
    '马': '午', '羊': '未', '猴': '申', '鸡': '酉', '狗': '戌', '猪': '亥'
}


# Function to extract 地支 from 生肖特
def calculate_earthly_branch(zodiac_special):
    zodiac = zodiac_special.split('/')[0]
    return zodiac_to_earthly_branch.get(zodiac, '')

def process_workbook(file_path, combined_data):
    excel_data = pd.ExcelFile(file_path)
    all_sheets_data = {}

    for sheet_name in excel_data.sheet_names:
        df = pd.read_excel(excel_data, sheet_name=sheet_name)
        #df['亥时时辰'] = 22
        if '生肖特' in df.columns and '地支' in df.columns:
            df['地支'] = df['生肖特'].apply(calculate_earthly_branch)
        #df['双干时辰'] = df['日期'].apply(lambda x: getshuangganshicheng(x.year, x.month, x.day))
        #f['阴阳局-九宫'] = df.apply(
            #lambda row: getSpaDigiXdingweideshu(row['日期'].year, row['日期'].month, row['日期'].day)[
               # 1],
           # axis=1)
        ''' df['年干'] = df.apply(lambda row:
                                getthebasicmessageofnineGrids(row['日期'].year, row['日期'].month, row['日期'].day,
                                                              0)[1][1][0], axis=1)
        df['月干'] = df.apply(lambda row:
                              getthebasicmessageofnineGrids(row['日期'].year, row['日期'].month, row['日期'].day,
                                                            0)[1][2][0], axis=1)
        df['日干'] = df.apply(lambda row:
                              getthebasicmessageofnineGrids(row['日期'].year, row['日期'].month, row['日期'].day,
                                                            0)[1][3][0], axis=1) 
        df['阴阳遁'] = df.apply(lambda row:
                              getthebasicmessageofnineGrids(row['日期'].year, row['日期'].month, row['日期'].day,
                                                            0)[1][0], axis=1)
        df['双干宫'] = df.apply(
             lambda row: getSpaDigiXdingweideshu1(row['日期'].year, row['日期'].month, row['日期'].day)[
             1],
             axis=1)
        df['年月日干支时间'] = df.apply(lambda row:
                                getthebasicmessageofnineGrids(row['日期'].year, row['日期'].month, row['日期'].day,
                                                              0)[2], axis=1)'''

        #df['程序数'] = df.apply(lambda row:
                                      # getSpaDigiXdingweideshu(row['日期'].year, row['日期'].month,
                                                                #      row['日期'].day,
                                                                 #   row["时辰数字"]), axis=1)
        #df['干支月'] = df.apply(lambda row: getthebasicmessageofnineGrids(row['日期'].year, row['日期'].month, row['日期'].day, row["双干时辰"])[1][2],axis=1)
        #df['节气'] = df.apply(lambda row: getthebasicmessageofnineGrids(row['日期'].year, row['日期'].month, row['日期'].day, row["双干时辰"])[1][5],axis=1)
        #df['阴阳局-九宫'] = df.apply(lambda row: getthebasicmessageofnineGrids(row['日期'].year, row['日期'].month, row['日期'].day,row["双干时辰"])[1][9], axis=1)
        all_sheets_data[sheet_name] = df
    output_path = f'加入地支-{file_path}'
    with pd.ExcelWriter(output_path) as writer:
        for sheet_name, data in all_sheets_data.items():
            data.to_excel(writer, sheet_name=sheet_name, index=False)
    return output_path
# 替换以下文件路径
file_paths = [
    '澳门2020-2024年01模型初始数据.xlsx',
    ]
combined_data = pd.DataFrame()

processed_files = [process_workbook(fp, combined_data) for fp in file_paths]