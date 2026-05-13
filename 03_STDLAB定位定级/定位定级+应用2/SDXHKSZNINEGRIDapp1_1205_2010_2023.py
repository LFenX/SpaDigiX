def getdingweishuangzhijiugongshuju(i):
    import pandas as pd
    from functionSpaDigiXONEANDSEVEN_1227_Beta1205 import getSpaDigiXdingweideshu
    from functionSpaDigiXAPPONE import getthebasicmessageofnineGrids
    # Load the Excel file
    input_file_path = '定位2010_2023香港初始数据.xlsx'  # Original data file path
    excel_data = pd.ExcelFile(input_file_path)

    # Load one of the sheets (for example, "澳门新定位结果")
    sheet_to_process = f"{i}香港"
    df = excel_data.parse(sheet_to_process)

    # Format the '日期' column to only include year, month, and day
    df['日期'] = pd.to_datetime(df['日期']).dt.strftime('%Y-%m-%d')

    # Define a combined function for labeling and calculation
    def label_and_calculate(date):
        date = pd.to_datetime(date)
        year = date.year
        month = date.month
        day = date.day
        for i in range(0, 12):
            ridizhi = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][3][1]
            shichengdizhi = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][4][1]
            dingwei = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][6]
            if ridizhi == shichengdizhi:
                hourr = 2 * i
                break
        value = getSpaDigiXdingweideshu(year, month, day, hourr)
        labels = {0: '坎宫', 1: '坤宫', 2: '震宫', 3: '巽宫', 5: '乾宫', 6: '兑宫', 7: '艮宫', 8: '离宫'}
        label = labels.get(dingwei)
        nianyueriganzhi = getthebasicmessageofnineGrids(year, month, day, hourr)[2]
        return label, value, nianyueriganzhi

    # Apply the combined function
    df['标签'], df['双支程序'], df["年月日干支时间"] = zip(*df['日期'].apply(label_and_calculate))

    # Create and populate the sheets for each new category
    sheets_data = {label: pd.DataFrame() for label in ['坎宫', '坤宫', '震宫', '巽宫', '乾宫', '兑宫', '艮宫', '离宫']}

    for index, row in df.iterrows():
        sheet_name = row['标签']
        row_data = pd.DataFrame([row.drop('标签')])
        sheets_data[sheet_name] = pd.concat([sheets_data[sheet_name], row_data], ignore_index=True)

    # Output file path
    output_file_path = f'定位香港{i}双支九宫分类结果1205版第四次修改.xlsx'

    # Create a Pandas Excel writer using XlsxWriter as the engine
    with pd.ExcelWriter(output_file_path, engine='xlsxwriter') as writer:
        # Write each dataframe to a different worksheet and adjust column widths
        for sheet_name, data in sheets_data.items():
            data.to_excel(writer, sheet_name=sheet_name, index=False)
            worksheet = writer.sheets[sheet_name]

for i in range(2010,2024):
    getdingweishuangzhijiugongshuju(i)