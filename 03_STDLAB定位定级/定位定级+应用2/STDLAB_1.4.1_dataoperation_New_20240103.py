import pandas as pd

# 读取Excel文件
excel文件路径 = '240106早更新-香港2010-2023庄家模型数据汇总.xlsx'
xls = pd.ExcelFile(excel文件路径)

# 用于存储每个工作表修改后的DataFrame的字典
修改后的数据字典 = {}

# 用于存储所有工作表的统计结果的列表
全部统计结果 = []
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
    '''
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
    '''
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
    df['庄家数串10'] = (
            df['庄家数'].astype(str).shift(9) + df['庄家数'].astype(str).shift(8) +
            df['庄家数'].astype(str).shift(7) + df['庄家数'].astype(str).shift(6) +
            df['庄家数'].astype(str).shift(5) + df['庄家数'].astype(str).shift(4) +
            df['庄家数'].astype(str).shift(3) + df['庄家数'].astype(str).shift(2) +
            df['庄家数'].astype(str).shift(1) + df['庄家数'].astype(str)
    )
    df['庄家数串10后'] = df['庄家数'].shift(-1)
    df['庄家数串11'] = (
            df['庄家数'].astype(str).shift(10) + df['庄家数'].astype(str).shift(9) +
            df['庄家数'].astype(str).shift(8) + df['庄家数'].astype(str).shift(7) +
            df['庄家数'].astype(str).shift(6) + df['庄家数'].astype(str).shift(5) +
            df['庄家数'].astype(str).shift(4) + df['庄家数'].astype(str).shift(3) +
            df['庄家数'].astype(str).shift(2) + df['庄家数'].astype(str).shift(1) +
            df['庄家数'].astype(str)
    )
    df['庄家数串11后'] = df['庄家数'].shift(-1)
    # 将NaN值替换为空字符串
    df['庄家数串8'] = df['庄家数串8'].fillna('')
    df['庄家数串9'] = df['庄家数串9'].fillna('')
    df['庄家数串10'] = df['庄家数串10'].fillna('')
    df['庄家数串11'] = df['庄家数串11'].fillna('')
    # 将修改后的DataFrame保存到字典中
    修改后的数据字典[工作表名称] = df

    # 创建一个列表来存储统计结果
    统计数据列表 = []

    # 遍历每一列
    # 遍历每一列
    for 数串长度 in [ 8, 9,10,11]:
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
    全部统计结果.append(pd.DataFrame(统计数据列表))

# 将全部统计结果合并为一个DataFrame
最终统计结果 = pd.concat(全部统计结果, ignore_index=True)



# 将统计结果保存到Excel文件的新工作表中
with pd.ExcelWriter('NewModel-240119更新-澳门2010-2024庄家模型数据汇总.xlsx') as writer:
    for 工作表名称, 修改后的df in 修改后的数据字典.items():
        # 将修改后的DataFrame保存
        修改后的df.to_excel(writer, sheet_name=工作表名称, index=False)

    # 将最终统计结果DataFrame保存到新的工作表中
    最终统计结果.to_excel(writer, sheet_name='统计', index=False)

