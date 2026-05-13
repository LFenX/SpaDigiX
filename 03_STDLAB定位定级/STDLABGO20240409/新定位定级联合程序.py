import pandas as pd

# 加载Excel文件
file_path_stage1 = '香港2023-2024-新定位数据一阶段.xlsx'
file_path_output = '香港2023-2024-新定级级数数据输出.xlsx'

data_stage1 = pd.read_excel(file_path_stage1)
data_output = pd.read_excel(file_path_output)

# 定义生肖号码对应表
zodiac_map_2023 = {
    '子': [4, 16, 28, 40],
    '丑': [3, 15, 27, 39],
    '寅': [2, 14, 26, 38],
    '卯': ['1和13', 25, 37, 49],
    '辰': [12, 24, 36, 48],
    '巳': [11, 23, 35, 47],
    '午': [10, 22, 34, 46],
    '未': [9, 21, 33, 45],
    '申': [8, 20, 32, 44],
    '酉': [7, 19, 31, 43],
    '戌': [6, 18, 30, 42],
    '亥': [5, 17, 29, 41]
}

zodiac_map_2024 = {
    '子': [4, 16, 28, 40],
    '丑': [3, 15, 27, 39],
    '寅': [2, 14, 26, 38],
    '卯': ['1和13', 25, 37, 49],
    '辰': [1, 13, 25, 37],
    '巳': [12, 24, 36, 48],
    '午': [11, 23, 35, 47],
    '未': [10, 22, 34, 46],
    '申': [9, 21, 33, 45],
    '酉': [8, 20, 32, 44],
    '戌': [7, 19, 31, 43],
    '亥': [6, 18, 30, 42]
}

# 映射等级到级数索引
grade_to_level = {'一': 0, '二': 1, '三': 2, '四': 3}

# 转换数据
transformed_data = data_stage1.copy()
for column in ['子时', '丑时', '寅时', '卯时', '辰时', '巳时', '午时', '未时', '申时', '酉时', '戌时', '亥时']:
    transformed_column = column + '定级程序'
    for index, row in transformed_data.iterrows():
        date = row['日期']
        zodiac = row[column]
        output_grade = data_output.loc[data_output['日期'] == date, transformed_column].values[0]
        level_index = grade_to_level[output_grade]

        # 根据年份选择生肖对应表
        year = date.year
        zodiac_map = zodiac_map_2023 if year == 2023 else zodiac_map_2024

        # 获取生肖号码
        zodiac_number = zodiac_map[zodiac][level_index]
        # 更新数据
        transformed_data.at[index, column] = f"{zodiac}{zodiac_number}"

# 保存转换后的数据到新的Excel文件
transformed_output_path = '香港2023-2024新定位定级联合数据初始.xlsx'
transformed_data.to_excel(transformed_output_path, index=False)
