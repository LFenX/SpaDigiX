import pandas as pd

# 读取Excel文件
file_path = '加入双干宫阴阳遁澳门2020-2024年原始数据.xlsx'
xls = pd.ExcelFile(file_path)

# 规则映射
rules = {
    "坎一": {"阳遁": ("子时", "子卯辰午未申-酉丑巳戌寅亥"), "阴遁": ("巳时", "子丑寅卯酉戌-辰申亥未午巳")},
    "巽四": {"阳遁": ("寅时", "子寅巳午未亥-卯申丑辰酉戌"), "阴遁": ("卯时", "卯辰巳午酉戌-寅亥未申子丑")},
    "坤二": {"阳遁": ("酉时", "子寅辰巳午未-丑申戌亥酉卯"), "阴遁": ("丑时", "子卯巳未申酉-辰戌亥午寅丑")},
    "兑七": {"阳遁": ("卯时", "子丑巳申酉亥-卯戌寅未午辰"), "阴遁": ("戌时", "巳未申酉戌亥-子辰午卯丑寅")},
    "艮八": {"阳遁": ("酉时", "丑巳午未戌亥-申子卯酉辰寅"), "阴遁": ("未时", "子丑卯未酉戌-辰申亥巳午寅")},
    "离九": {"阳遁": ("巳时", "丑卯辰午未酉-申亥子寅戌巳"), "阴遁": ("卯时", "寅卯辰巳申酉-戌亥未午子丑")},
    "乾六": {"阳遁": ("亥时", "丑寅巳午未酉-戌卯亥辰子申"), "阴遁": ("酉时", "丑辰巳午未申-戌子亥酉卯寅")},
    "震三": {"阳遁": ("辰时", "丑寅巳午申亥-辰子酉卯未戌"), "阴遁": ("辰时", "丑寅巳午未亥-辰子申卯酉戌")}
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

#  保存处理后的数据到新文件
output_file_path = '加入时辰和生肖组澳门20-24年原始数据.xlsx'
with pd.ExcelWriter(output_file_path) as writer:
    for sheet_name, data in output_data.items():
        data.to_excel(writer, sheet_name=sheet_name, index=False)

output_file_path
