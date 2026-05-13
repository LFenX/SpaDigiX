def getlinianshujuchuli(i):
    import pandas as pd
    from functionSpaDigiXONEANDSEVEN_1227_Beta1205 import getSpaDigiXdingweideshu
    from functionSpaDigiXAPPONE import getthebasicmessageofnineGrids
    # Load the Excel file
    input_file_path = '定位2010_2023香港初始数据.xlsx'  # 原始数据文件路径
    excel_data = pd.ExcelFile(input_file_path)

    # Load one of the sheets (for example, "澳门新定位结果")
    sheet_to_process = f"{i}香港"
    df = excel_data.parse(sheet_to_process)

    # 格式化'日期'列，仅包含年、月、日
    df['日期'] = pd.to_datetime(df['日期']).dt.strftime('%Y-%m-%d')

    # 定义计算和标签的组合函数
    def calculate_and_label(date):
        date = pd.to_datetime(date)  # 将字符串转换回datetime以进行计算
        year = date.year
        month = date.month
        day = date.day
        for i in range(0, 12):
            riganzhi = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][3]
            shichengganzhi = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][4]
            if riganzhi == "甲子" and shichengganzhi[0] == "甲":
                for j in range(0, 12):
                    panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                    riganzhi = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][3]
                    if panduanwugan == "戊":
                        hourr = 2 * j
                        label = "甲子"
                        break
            elif riganzhi == "甲戌" and shichengganzhi[0] == "甲":
                for j in range(0, 12):
                    panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                    riganzhi = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][3]
                    if panduanwugan == "己":
                        hourr = 2 * j
                        label = "甲戌"
                        break
            elif riganzhi == "甲申" and shichengganzhi[0] == "甲":
                for j in range(0, 12):
                    panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                    riganzhi = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][3]
                    if panduanwugan == "庚":
                        hourr = 2 * j
                        label = "甲申"
                        break
            elif riganzhi == "甲寅" and shichengganzhi[0] == "甲":
                for j in range(0, 12):
                    panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                    riganzhi = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][3]
                    if panduanwugan == "癸":
                        hourr = 2 * j
                        label = "甲寅"
                        break
            elif riganzhi == "甲午" and shichengganzhi[0] == "甲":
                for j in range(0, 12):
                    panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                    riganzhi = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][3]
                    if panduanwugan == "辛":
                        hourr = 2 * j
                        label = "甲午"
                        break
            elif riganzhi == "甲辰" and shichengganzhi[0] == "甲":
                for j in range(0, 12):
                    panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                    riganzhi = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][3]
                    if panduanwugan == "壬":
                        hourr = 2 * j
                        label = "甲辰"
                        break
            else:
                if riganzhi[0] == shichengganzhi[0]:
                    hourr = 2 * i
                    label = f"双{riganzhi[0]}"
                    break
        value = getSpaDigiXdingweideshu(year, month, day, hourr)
        nianyueriganzhi = getthebasicmessageofnineGrids(year, month, day, hourr)[2]
        return value, label,nianyueriganzhi

    # 应用组合函数
    df['双干程序'], df['标签'] ,df["年月日干支时间"]= zip(*df['日期'].apply(calculate_and_label))


    # 创建并填充每个标签的工作表
    sheets_data = {f"{label}": pd.DataFrame() for label in
                   ['双乙', '双丙', '双丁', '双戊', '双己', '双庚', '双辛', '双壬', '双癸', '甲子', '甲戌', '甲申',
                    "甲辰", "甲午", "甲寅"]}
    summary_data = []

    for index, row in df.iterrows():
        sheet_name = f"{row['标签']}"
        row_data = pd.DataFrame([row.drop('标签')])
        sheets_data[sheet_name] = pd.concat([sheets_data[sheet_name], row_data], ignore_index=True)


    # 输出文件路径
    output_file_path = f'定位香港{i}双干分类结果1205版第四次修改.xlsx'

    # 使用XlsxWriter引擎创建Pandas Excel写入器
    with pd.ExcelWriter(output_file_path, engine='xlsxwriter') as writer:
        # 将每个数据框写入不同的工作表并调整列宽
        for sheet_name, data in sheets_data.items():
            data.to_excel(writer, sheet_name=sheet_name, index=False)
            worksheet = writer.sheets[sheet_name]
for i in range(2010,2024):
    getlinianshujuchuli(i)
