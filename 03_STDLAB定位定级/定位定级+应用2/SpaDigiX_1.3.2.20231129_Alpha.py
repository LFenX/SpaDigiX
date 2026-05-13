from functionSpadigiXAPPTHREEANDTWO import getdingjideshu
import pandas as pd

# 定义计算得分的函数
def calculate_score(row):
    year, month, day = row['日期'].year, row['日期'].month, row['日期'].day
    value=getdingjideshu(year,month,day)
    return value

# 读取上传的文件
file_path = '定级初始表香港.xlsx'
df = pd.read_excel(file_path)

# 将“日期”列转换为日期格式
df['日期'] = pd.to_datetime(df['日期'])

# 应用计算规则到每一行
df['定级得数'] = df.apply(calculate_score, axis=1)
df['日期'] = df['日期'].dt.strftime('%Y-%m-%d')
# 保存处理后的数据到一个新的 Excel 文件
output_file_path = '定级结果表香港.xlsx'
df.to_excel(output_file_path, index=False)
