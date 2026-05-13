import pandas as pd

# 读取Excel文件
excel文件路径 = '加四天 澳门2021-2023庄家模型数据-独立年份0104.xlsx'
xls = pd.ExcelFile(excel文件路径)

# 用于存储每个工作表修改后的DataFrame的字典
修改后的数据字典 = {}

# 用于存储所有工作表的统计结果的字典
全部统计结果 = {}

# 用于存储双干统计结果的字典
双干统计结果 = {}

# 用于存储双干宫统计结果的字典
双干宫统计结果 = {}

# 定义一个函数来计算指定列的统计数据
def 计算列统计(df, 列名, 统计列名):
    统计结果列表 = []
    值计数 = df[列名].value_counts()
    for 类别, 出现个数 in 值计数.items():
        类别数据 = df[df[列名] == 类别][统计列名]
        一的个数 = 类别数据[类别数据 == 1].count()
        零的个数 = 类别数据[类别数据 == 0].count()
        总个数 = 一的个数 + 零的个数

        if 总个数 > 0:
            一的比重 = 一的个数 / 总个数 * 100
            零的比重 = 零的个数 / 总个数 * 100
        else:
            一的比重 = 0
            零的比重 = 0

        统计结果列表.append({
            '类别': 类别,
            '出现个数': 出现个数,
            '1的个数': 一的个数,
            '1的比重': 一的比重,
            '0的个数': 零的个数,
            '0的比重': 零的比重
        })
    return pd.DataFrame(统计结果列表)

# 遍历Excel文件中的每个工作表
for 工作表名称 in xls.sheet_names:
    # 从当前工作表读取数据
    df = pd.read_excel(xls, 工作表名称)

    # 创建新列'庄家数串3', '庄家数串5', '庄家数串7' 和对应的'后'列
    df['庄家数串3'] = df['庄家数'].astype(str).shift(2) + df['庄家数'].astype(str).shift(1) + df['庄家数'].astype(str)
    df['庄家数串3后'] = df['庄家数'].shift(-1)

    df['庄家数串5'] = df['庄家数'].astype(str).shift(4) + df['庄家数'].astype(str).shift(3) + df['庄家数'].astype(
        str).shift(2) + df['庄家数'].astype(str).shift(1) + df['庄家数'].astype(str)
    df['庄家数串5后'] = df['庄家数'].shift(-1)

    df['庄家数串7'] = df['庄家数'].astype(str).shift(6) + df['庄家数'].astype(str).shift(5) + df['庄家数'].astype(
        str).shift(4) + df['庄家数'].astype(str).shift(3) + df['庄家数'].astype(str).shift(2) + df['庄家数'].astype(
        str).shift(1) + df['庄家数'].astype(str)
    df['庄家数串7后'] = df['庄家数'].shift(-1)

    # 将NaN值替换为空字符串
    df['庄家数串3'] = df['庄家数串3'].fillna('')
    df['庄家数串5'] = df['庄家数串5'].fillna('')
    df['庄家数串7'] = df['庄家数串7'].fillna('')
    # 添加'庄家数串8'列和对应的'后'列
    df['庄家数串8'] = df['庄家数'].astype(str).shift(7) + df['庄家数'].astype(str).shift(6) + df['庄家数'].astype(
        str).shift(5) + df['庄家数'].astype(str).shift(4) + df['庄家数'].astype(str).shift(3) + df['庄家数'].astype(
        str).shift(2) + df['庄家数'].astype(str).shift(1) + df['庄家数'].astype(str)
    df['庄家数串8后'] = df['庄家数'].shift(-1)
    # 添加'庄家数串9'列和对应的'后'列
    df['庄家数串9'] = df['庄家数'].astype(str).shift(8) + df['庄家数'].astype(str).shift(7) + df['庄家数'].astype(
        str).shift(6) + df['庄家数'].astype(str).shift(5) + df['庄家数'].astype(str).shift(4) + df['庄家数'].astype(
        str).shift(3) + df['庄家数'].astype(str).shift(2) + df['庄家数'].astype(str).shift(1) + df['庄家数'].astype(str)
    df['庄家数串9后'] = df['庄家数'].shift(-1)
    # 将NaN值替换为空字符串
    df['庄家数串8'] = df['庄家数串8'].fillna('')
    df['庄家数串9'] = df['庄家数串9'].fillna('')
    # 将修改后的DataFrame保存到字典中
    修改后的数据字典[工作表名称] = df

    # 创建一个列表来存储统计结果
    统计数据列表 = []

    # 统计数据逻辑（如计算庄家数串的统计等）
    for 数串长度 in [3, 5, 7, 8, 9]:
        列名 = f'庄家数串{数串长度}'
        后列名 = f'{列名}后'
        # 计算每个唯一值的出现次数，忽略空值
        值计数 = df[列名].dropna().value_counts()
        # 过滤掉空值
        值计数 = 值计数[值计数.index != '']
        # 计算非空行数
        非空行数 = df[列名].dropna().shape[0]
        # 计算百分比
        百分比 = (值计数 / 非空行数) * 100
        # 收集具体数串后的数字，将数字转换为不保留小数点的字符串
        具体数串 = df.groupby(列名)[后列名].apply(lambda x: ''.join(x.dropna().astype(int).astype(str)))
        # 将结果添加到统计数据列表
        for 类别 in 值计数.index:
            数串 = 具体数串.get(类别, '')
            数串长度 = len(数串)
            if 数串长度 > 0:
                一的百分比 = 数串.count('1') / 数串长度 * 100
                零的百分比 = 数串.count('0') / 数串长度 * 100
            else:
                一的百分比 = 0
                零的百分比 = 0
            统计数据列表.append({
                '工作表': 工作表名称,
                '类别': 类别,
                '出现个数': 值计数[类别],
                '百分比': 百分比[类别],
                '具体数串': 数串,
                '1的百分比': 一的百分比,
                '0的百分比': 零的百分比
            })

    # 将统计数据列表转换为DataFrame并添加到全部统计结果中
    全部统计结果[工作表名称] = pd.DataFrame(统计数据列表)

    # 对当前工作表进行双干统计
    双干统计结果[工作表名称] = 计算列统计(df, '双干', '庄家数')

    # 对当前工作表进行双干宫统计
    双干宫统计结果[工作表名称] = 计算列统计(df, '双干宫', '庄家数')

# 保存统计结果到Excel
with pd.ExcelWriter('加四天NewModel-澳门2021-2023庄家模型数据-独立年份240104.xlsx') as writer:
    # 保存修改后的原始数据
    for 工作表名称, 修改后的df in 修改后的数据字典.items():
        修改后的df.to_excel(writer, sheet_name=工作表名称, index=False)

    # 保存每个工作表的最终统计结果
    for 工作表名称, 统计结果df in 全部统计结果.items():
        统计结果df.to_excel(writer, sheet_name=f'{工作表名称}_统计', index=False)

    # 保存每个工作表的双干统计结果
    for 工作表名称, 双干统计df in 双干统计结果.items():
        双干统计df.to_excel(writer, sheet_name=f'{工作表名称}_双干统计', index=False)

    # 保存每个工作表的双干宫统计结果
    for 工作表名称, 双干宫统计df in 双干宫统计结果.items():
        双干宫统计df.to_excel(writer, sheet_name=f'{工作表名称}_双干宫统计', index=False)

'''
import pandas as pd

# 读取Excel文件
excel文件路径 = '澳门2021-2023庄家模型数据-独立年份0104.xlsx'
xls = pd.ExcelFile(excel文件路径)

# 用于存储每个工作表修改后的DataFrame的字典
修改后的数据字典 = {}

# 用于存储所有工作表的统计结果的列表
全部统计结果 = {}
# 定义一个函数来计算指定列的统计数据
def 计算列统计(df, 列名, 统计列名):
    统计结果列表 = []
    值计数 = df[列名].value_counts()
    for 类别, 出现个数 in 值计数.items():
        类别数据 = df[df[列名] == 类别][统计列名]
        一的个数 = 类别数据[类别数据 == 1].count()
        零的个数 = 类别数据[类别数据 == 0].count()
        总个数 = 一的个数 + 零的个数

        if 总个数 > 0:
            一的比重 = 一的个数 / 总个数 * 100
            零的比重 = 零的个数 / 总个数 * 100
        else:
            一的比重 = 0
            零的比重 = 0

        统计结果列表.append({
            '类别': 类别,
            '出现个数': 出现个数,
            '1的个数': 一的个数,
            '1的比重': 一的比重,
            '0的个数': 零的个数,
            '0的比重': 零的比重
        })
    return pd.DataFrame(统计结果列表)
# 遍历Excel文件中的每个工作表
for 工作表名称 in xls.sheet_names:
    # 从当前工作表读取数据
    df = pd.read_excel(xls, 工作表名称)

    # 创建新列'庄家数串3', '庄家数串5', '庄家数串7' 和对应的'后'列
    df['庄家数串3'] = df['庄家数'].astype(str).shift(2) + df['庄家数'].astype(str).shift(1) + df['庄家数'].astype(str)
    df['庄家数串3后'] = df['庄家数'].shift(-1)

    df['庄家数串5'] = df['庄家数'].astype(str).shift(4) + df['庄家数'].astype(str).shift(3) + df['庄家数'].astype(str).shift(2) + df['庄家数'].astype(str).shift(1) + df['庄家数'].astype(str)
    df['庄家数串5后'] = df['庄家数'].shift(-1)

    df['庄家数串7'] = df['庄家数'].astype(str).shift(6) + df['庄家数'].astype(str).shift(5) + df['庄家数'].astype(str).shift(4) + df['庄家数'].astype(str).shift(3) + df['庄家数'].astype(str).shift(2) + df['庄家数'].astype(str).shift(1) + df['庄家数'].astype(str)
    df['庄家数串7后'] = df['庄家数'].shift(-1)

    # 将NaN值替换为空字符串
    df['庄家数串3'] = df['庄家数串3'].fillna('')
    df['庄家数串5'] = df['庄家数串5'].fillna('')
    df['庄家数串7'] = df['庄家数串7'].fillna('')
    # 添加'庄家数串8'列和对应的'后'列
    df['庄家数串8'] = df['庄家数'].astype(str).shift(7) + df['庄家数'].astype(str).shift(6) + df['庄家数'].astype(
        str).shift(5) + df['庄家数'].astype(str).shift(4) + df['庄家数'].astype(str).shift(3) + df['庄家数'].astype(
        str).shift(2) + df['庄家数'].astype(str).shift(1) + df['庄家数'].astype(str)
    df['庄家数串8后'] = df['庄家数'].shift(-1)
    # 添加'庄家数串9'列和对应的'后'列
    df['庄家数串9'] = df['庄家数'].astype(str).shift(8) + df['庄家数'].astype(str).shift(7) + df['庄家数'].astype(
        str).shift(6) + df['庄家数'].astype(str).shift(5) + df['庄家数'].astype(str).shift(4) + df['庄家数'].astype(
        str).shift(3) + df['庄家数'].astype(str).shift(2) + df['庄家数'].astype(str).shift(1) + df['庄家数'].astype(str)
    df['庄家数串9后'] = df['庄家数'].shift(-1)
    # 将NaN值替换为空字符串
    df['庄家数串8'] = df['庄家数串8'].fillna('')
    df['庄家数串9'] = df['庄家数串9'].fillna('')

    # 将修改后的DataFrame保存到字典中
    修改后的数据字典[工作表名称] = df

    # 创建一个列表来存储统计结果
    统计数据列表 = []

    # 遍历每一列
    # 遍历每一列
    for 数串长度 in [3, 5, 7, 8, 9]:
        列名 = f'庄家数串{数串长度}'
        后列名 = f'{列名}后'

        # 计算每个唯一值的出现次数，忽略空值
        值计数 = df[列名].dropna().value_counts()

        # 过滤掉空值
        值计数 = 值计数[值计数.index != '']

        # 计算非空行数
        非空行数 = df[列名].dropna().shape[0]

        # 计算百分比
        百分比 = (值计数 / 非空行数) * 100

        # 收集具体数串后的数字，将数字转换为不保留小数点的字符串
        具体数串 = df.groupby(列名)[后列名].apply(lambda x: ''.join(x.dropna().astype(int).astype(str)))

        # 将结果添加到统计数据列表
        for 类别 in 值计数.index:
            数串 = 具体数串.get(类别, '')
            数串长度 = len(数串)  # 直接计算字符串长度
            if 数串长度 > 0:
                一的百分比 = 数串.count('1') / 数串长度 * 100
                零的百分比 = 数串.count('0') / 数串长度 * 100
            else:
                一的百分比 = 0
                零的百分比 = 0

            统计数据列表.append({
                '工作表': 工作表名称,
                '类别': 类别,
                '出现个数': 值计数[类别],
                '百分比': 百分比[类别],
                '具体数串': 数串,
                '1的百分比': 一的百分比,
                '0的百分比': 零的百分比
            })

    # 将统计数据列表转换为DataFrame并添加到全部统计结果中
    全部统计结果[工作表名称] = pd.DataFrame(统计数据列表)

# 将全部统计结果合并为一个DataFrame
最终统计结果 = pd.concat(全部统计结果, ignore_index=True)

# 对每个工作表进行双干和双干宫的统计
双干统计结果 = []
双干宫统计结果 = []

for 工作表名称, df in 修改后的数据字典.items():
    双干统计df = 计算列统计(df, '双干', '庄家数')
    双干统计df['工作表'] = 工作表名称
    双干统计结果.append(双干统计df)

    双干宫统计df = 计算列统计(df, '双干宫', '庄家数')
    双干宫统计df['工作表'] = 工作表名称
    双干宫统计结果.append(双干宫统计df)

# 将统计结果合并为一个DataFrame
双干统计结果df = pd.concat(双干统计结果, ignore_index=True)
双干宫统计结果df = pd.concat(双干宫统计结果, ignore_index=True)

with pd.ExcelWriter('NewModel-澳门2021-2023庄家模型数据-独立年份240104.xlsx') as writer:
    # 保存修改后的原始数据
    for 工作表名称, 修改后的df in 修改后的数据字典.items():
        修改后的df.to_excel(writer, sheet_name=工作表名称, index=False)

    # 保存每个工作表的最终统计结果
    for 工作表名称, 统计结果df in 全部统计结果.items():
        统计结果df.to_excel(writer, sheet_name=f'{工作表名称}_统计', index=False)

    # 保存双干和双干宫的统计结果
    for 工作表名称, df in 修改后的数据字典.items():
        双干统计结果df = 双干统计结果df[双干统计结果df['工作表'] == 工作表名称]
        双干宫统计结果df = 双干宫统计结果df[双干宫统计结果df['工作表'] == 工作表名称]
        双干统计结果df.to_excel(writer, sheet_name=f'{工作表名称}_双干统计', index=False)
        双干宫统计结果df.to_excel(writer, sheet_name=f'{工作表名称}_双干宫统计', index=False)
        我想对这个excel表进行一些操作，在sheet1工作表中找到日期列，从第九个日期开始，找到庄家数串8这一列，这里有一个数串，请注意这个树串是字符串格式，你需要在读取时默认他为字符串，找到这个字符串以后进入 “统计”工作表，在类别中检索与庄家数串8完全相同的字符串（注意要完全相同，类别这一列在读取时也要默认其为字符串），检索到对应类别后，找到 对应 统计工作表的“1的百分比”和“0的百分比”这两列，提取这两列的数字，比较大小，如果1的百分比大，则选1，否则选0，最后一部比较选择的数与sheet1工作表中“庄家数”这一列对应行的数，如果相同，则在新列“准确”中标示1，否则为0，最后将日期列，“特列”，“地支”列。庄家数列，以及所有前面用到的列放入一个excel表输出
'''


