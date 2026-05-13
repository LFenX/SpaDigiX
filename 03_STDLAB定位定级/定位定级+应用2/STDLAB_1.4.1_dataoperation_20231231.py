import pandas as pd

# 读取Excel文件
excel文件路径 = '澳门2021-2023庄家模型数据汇总1231.xlsx'
xls = pd.ExcelFile(excel文件路径)

# 用于存储每个工作表修改后的DataFrame的字典
修改后的数据字典 = {}

# 用于存储所有工作表的统计结果的列表
全部统计结果 = []

# 遍历Excel文件中的每个工作表
for 工作表名称 in xls.sheet_names:
    # 从当前工作表读取数据
    df = pd.read_excel(xls, 工作表名称)

    # 创建新列'庄家数串3'
    df['庄家数串3'] = df['庄家数'].astype(str).shift(2) + df['庄家数'].astype(str).shift(1) + df['庄家数'].astype(str)

    # 创建新列'庄家数串5'
    df['庄家数串5'] = df['庄家数'].astype(str).shift(4) + df['庄家数'].astype(str).shift(3) + df['庄家数'].astype(str).shift(2) + df['庄家数'].astype(str).shift(1) + df['庄家数'].astype(str)

    # 创建新列'庄家数串7'
    df['庄家数串7'] = df['庄家数'].astype(str).shift(6) + df['庄家数'].astype(str).shift(5) + df['庄家数'].astype(str).shift(4) + df['庄家数'].astype(str).shift(3) + df['庄家数'].astype(str).shift(2) + df['庄家数'].astype(str).shift(1) + df['庄家数'].astype(str)

    # 将NaN值替换为空字符串
    df['庄家数串3'] = df['庄家数串3'].fillna('')
    df['庄家数串5'] = df['庄家数串5'].fillna('')
    df['庄家数串7'] = df['庄家数串7'].fillna('')

    # 将修改后的DataFrame保存到字典中
    修改后的数据字典[工作表名称] = df

    # 创建一个DataFrame来存储统计结果
    统计结果df = pd.DataFrame(columns=['工作表', '类别', '出现个数', '百分比'])

    # 遍历每一列
    for 列 in ['庄家数串3', '庄家数串5', '庄家数串7']:
        # 计算每个唯一值的出现次数，忽略空值
        值计数 = df[列].dropna().value_counts()

        # 过滤掉空值
        值计数 = 值计数[值计数.index != '']

        # 计算百分比
        百分比 = (值计数 / len(df)) * 100

        # 将结果添加到统计DataFrame
        统计结果df = pd.concat([统计结果df, pd.DataFrame({
            '工作表': [工作表名称] * len(值计数),
            '类别': 值计数.index,
            '出现个数': 值计数.values,
            '百分比': 百分比.values
        })], ignore_index=True)

    # 将当前工作表的统计结果添加到全部统计结果中
    全部统计结果.append(统计结果df)

# 将全部统计结果合并为一个DataFrame
最终统计结果 = pd.concat(全部统计结果, ignore_index=True)

# 将统计结果保存到Excel文件的新工作表中
with pd.ExcelWriter('统计澳门2021-2023庄家模型数据汇总1231.xlsx') as writer:
    for 工作表名称, 修改后的df in 修改后的数据字典.items():
        # 将修改后的DataFrame保存
        修改后的df.to_excel(writer, sheet_name=工作表名称, index=False)

    # 将最终统计结果DataFrame保存到新的工作表中
    最终统计结果.to_excel(writer, sheet_name='统计', index=False)



