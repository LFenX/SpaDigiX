import pandas as pd
import pyreadstat

# 加载 .sav 文件
sav_file_path = r"C:\Users\LFen\Desktop\非参数假设检验\非参数检验（多独立样本-儿童身高）.sav"
df, meta = pyreadstat.read_sav(sav_file_path)

# 将数据保存为 Excel 文件
excel_file_path = '多独立样本-儿童身高.xlsx'
df.to_excel(excel_file_path, index=False)

print(f"文件已成功保存为 {excel_file_path}")
print(df.head())
# 如果想要查看所有数据，可以取消下面的注释
# 打印所有行
print(df)
