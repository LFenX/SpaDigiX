from functionSpadigiXAPPTHREEANDTHREEG4MC import getdingjideshu
import pandas as pd
import os
import math

# 定义计算得分的函数
def calculate_score(row):
    year, month, day = row['日期'].year, row['日期'].month, row['日期'].day
    values = getdingjideshu(year, month, day)

    # 将得到的五个值分别分配给对应的列
    row['定级得数'] = values[0]
    row['双干得数'] = values[1]
    row['值使得数'] = values[2]
    row['值符得数'] = values[3]
    row['生门得数'] = values[4]
    row['年月日干支']=values[5]
    row['日干支']=values[6]

    return row

# 创建一个空的 DataFrame 用于存储所有结果
result_df = pd.DataFrame()

# 遍历每年的工作表
for year in range(2010, 2025):
    sheet_name = f"{year}年"

    try:
        # 读取上传的文件，并指定工作表名称
        file_path = '澳门历史数据.xlsx'
        df = pd.read_excel(file_path, sheet_name=sheet_name)

        # 将“日期”列转换为日期格式
        df['日期'] = pd.to_datetime(df['日期'])

        # 应用计算规则到每一行
        df = df.apply(calculate_score, axis=1)
        df['日期'] = df['日期'].dt.strftime('%Y-%m-%d')

        # 新增处理规则
        df['实际数'] = df['特'].apply(lambda x: min(math.ceil(x / 12), 4))  # 更新实际数规则
        df['定级数'] = df['定级得数'].apply(lambda x: math.ceil(x))
        df['准确'] = df.apply(lambda x: 1 if str(x['实际数']) in ["412", "123", "234", "341"][x['定级数'] - 1] else 0, axis=1)

        # 将当前年份的结果添加到总结果中
        df['年份'] = year
        result_df = pd.concat([result_df, df], ignore_index=True)

        print(f'处理完成 {year} 年的数据')

    except pd.errors.ImproperExcelHeader:
        print(f'在 {year} 年找不到工作表: {sheet_name}')

# 打印一些调试信息，确保 '准确' 列存在于 result_df 中
print("调试信息:")
print(result_df.info())

# 保存所有结果到一个 Excel 文件中
output_file_path = '2010-2024年澳门汇总定级结果表G4MC-含准确率分析240119.xlsx'
with pd.ExcelWriter(output_file_path, engine='xlsxwriter') as writer:
    yearly_stats = []
    for year in range(2010, 2025):
        year_df = result_df[result_df['年份'] == year]

        # 新增处理规则
        year_df.loc[:, '准确率'] = year_df['准确'].mean()  # 计算准确率的平均值
        year_df['准确率'] = year_df['准确率'] * 100  # 将准确率转换为百分比形式
        year_df.loc[:, '准确个数'] = year_df['准确'].sum()  # 统计准确这一列中含数字1的个数
        year_df.loc[:, '总数'] = len(year_df)  # 统计准确这一列中数据的总个数

        # 存储每年的准确率、准确个数和总数
        yearly_stats.append(year_df.iloc[0][['准确个数', '准确率', '总数']])

        # 删除准确率、准确个数和总数这三列
        year_df.drop(['准确率', '准确个数', '总数'], axis=1, inplace=True)

        # 保存每年的数据到 Excel 文件
        year_df.to_excel(writer, index=False, sheet_name=str(year) + '年')

        # 新建一个工作表，获取每一年数据的第一行的三个数据：准确个数、准确率、总数
    overall_stats_df = pd.DataFrame(yearly_stats).reset_index()

    # 新增处理规则
    overall_stats_df['总年份准确率'] = (overall_stats_df['准确个数'].sum() / overall_stats_df[
        '总数'].sum()) * 100  # 计算总年份准确率
    overall_stats_df['总年份准确率'] = overall_stats_df['总年份准确率'].apply(lambda x: f"{x:.2f}%")  # 将总年份准确率转换为百分比形式
    overall_stats_df['准确率'] = overall_stats_df['准确率'].apply(lambda x: f'{x:.2f}%')  # 将准确率转换为百分比形式
    # 将数据写入Excel文件
    overall_stats_df.to_excel(writer, index=False, sheet_name='准确率统计')

print('全部处理完成')