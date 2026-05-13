from backup_file import  getshuangganshicheng
import pandas as pd
def process_workbook(file_path):
    # 读取原始Excel文件，包含所有工作表
    xls = pd.ExcelFile(file_path)
    output_path = f'香港2010-2024十二月份定位数据仅含有双干程序_pro.xlsx'

    # 使用with语句创建ExcelWriter，自动处理文件关闭
    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        # 遍历所有工作表
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name=sheet_name)

            # 假设 '日期' 列是datetime类型，我们从这里提取年月日
            df['双干时辰'] = df['日期'].apply(lambda x: getshuangganshicheng(x.year, x.month, x.day))

            # 将处理后的DataFrame保存到新的Excel文件，保留原来的工作表名
            df.to_excel(writer, sheet_name=sheet_name, index=False)

    return output_path


# 文件路径列表
file_paths = [
    "香港2010-2024十二月份定位数据仅含有双干程序.xlsx",
]

# 处理每个文件并收集新文件的路径
processed_files = [process_workbook(fp) for fp in file_paths]

# 输出处理后的文件路径，以便检查
print("处理完成的文件:")
for f in processed_files:
    print(f)
