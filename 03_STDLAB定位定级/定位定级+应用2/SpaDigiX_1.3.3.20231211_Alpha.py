from functionSpadigiXAPPTHREEANDTHREE import getdingjideshu
import pandas as pd


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

    return row


# 读取上传的文件
file_path = '定级初始表香港2011.xlsx'
df = pd.read_excel(file_path)

# 将“日期”列转换为日期格式
df['日期'] = pd.to_datetime(df['日期'])

# 应用计算规则到每一行
df = df.apply(calculate_score, axis=1)
df['日期'] = df['日期'].dt.strftime('%Y-%m-%d')

# 保存处理后的数据到一个新的 Excel 文件
# 保存处理后的数据到一个新的 Excel 文件，并设置工作表名称为“澳门定级结果”
output_file_path = '2011定级结果表香港23_12_25原始.xlsx'
with pd.ExcelWriter(output_file_path, engine='xlsxwriter') as writer:
    df.to_excel(writer, index=False, sheet_name='香港定级结果')
