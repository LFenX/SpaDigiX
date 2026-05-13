from functionSpaDigiXAPPTWO  import getthefourmaxmessage

import pandas as pd
import math







jj=getthefourmaxmessage(2023,10,1,15,15,0,"亥",2023,10,16)
print(jj)
'''
data = {
    '序号': [None, 2, 3, 4, 5],
    '日期': ['2023-10-27', '2023-10-28', None, '2023-10-30', '2023-10-31'],
    '数字1': [10, None, 15, 12, 20],
    '数字2': [5, 8, None, 6, 10]
}

df = pd.DataFrame(data)

# 指定需要检查的列
columns_to_check = ['日期', '数字1', '数字2']

# 迭代DataFrame并删除包含空值的行
for index, row in df.iterrows():
    if any(pd.isnull(row[column]) for column in columns_to_check):
        df.drop(index, inplace=True)

print(df)
'''