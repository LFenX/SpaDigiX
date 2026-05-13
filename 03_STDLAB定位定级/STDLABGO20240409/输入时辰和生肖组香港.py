import pandas as pd

# 读取Excel文件
file_path = '加入双干宫阴阳遁-香港2010-2024年原始数据.xlsx'
xls = pd.ExcelFile(file_path)

# 规则映射
rules = {
    "坎一": {"阳遁": ("辰时", "丑卯辰巳午戌-未寅申亥酉子"), "阴遁": ("午时", "子丑寅辰巳未-卯申酉戌亥午")},
    "巽四": {"阳遁": ("亥时", "子卯辰巳午酉-申戌亥未寅丑"), "阴遁": ("寅时", "子丑卯辰午亥-申寅未戌巳酉")},
    "坤二": {"阳遁": ("卯时", "丑寅辰未申酉-亥子戌午卯巳"), "阴遁": ("申时", "丑巳午未申亥-子辰戌寅酉卯")},
    "兑七": {"阳遁": ("卯时", "子丑辰午申亥-未酉寅戌卯巳"), "阴遁": ("酉时", "丑卯辰巳午戌-申子亥酉未寅")},
    "艮八": {"阳遁": ("酉时", "丑寅巳午未申-亥子辰酉戌卯"), "阴遁": ("酉时", "丑巳午申戌亥-子辰酉未卯寅")},
    "离九": {"阳遁": ("子时", "巳午申酉戌亥-卯丑子未辰寅"), "阴遁": ("卯时", "辰巳午申戌亥-未子丑酉寅卯")},
    "乾六": {"阳遁": ("亥时", "丑寅卯巳申酉-戌子亥未辰午"), "阴遁": ("戌时", "丑辰申酉戌亥-子午未卯寅巳")},
    "震三": {"阳遁": ("卯时", "寅辰巳午未戌-亥丑子酉卯申"), "阴遁": ("寅时", "丑寅卯午申亥-未酉戌子巳辰")}
}
# 时辰对应数字
time_to_number = {
    "子时": 0, "丑时": 2, "寅时": 4, "卯时": 6,
    "辰时": 8, "巳时": 10, "午时": 12, "未时": 14,
    "申时": 16, "酉时": 18, "戌时": 20, "亥时": 22
}

# 处理每个工作表
output_data = {}
for sheet_name in xls.sheet_names:
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    df['时辰数字'] = df.apply(lambda row: time_to_number[rules[row['双干宫']][row['阴阳遁']][0]], axis=1)
    df['生肖组'] = df.apply(lambda row: rules[row['双干宫']][row['阴阳遁']][1], axis=1)
    output_data[sheet_name] = df

# 保存处理后的数据到新文件
output_file_path = '加入时辰和生肖组香港10-24年原始数据.xlsx'
with pd.ExcelWriter(output_file_path) as writer:
    for sheet_name, data in output_data.items():
        data.to_excel(writer, sheet_name=sheet_name, index=False)

output_file_path
