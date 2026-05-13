import pandas as pd
def calculate_zodiac(year):
    zodiac_animals = ['鼠', '牛', '虎', '兔', '龙', '蛇', '马', '羊', '猴', '鸡', '狗', '猪']
    return zodiac_animals[(year - 1900) % 12]


def process_excel_file_to_single_excel(excel_path, date_column_name='日期', number_column_name='特'):
    xl = pd.ExcelFile(excel_path)
    base_zodiac_dict = {
        '蛇': [1, 13, 25, 37, 49],
        '马': [2, 14, 26, 38],
        '羊': [3, 15, 27, 39],
        '猴': [4, 16, 28, 40],
        '鸡': [5, 17, 29, 41],
        '狗': [6, 18, 30, 42],
        '猪': [7, 19, 31, 43],
        '鼠': [8, 20, 32, 44],
        '牛': [9, 21, 33, 45],
        '虎': [10, 22, 34, 46],
        '兔': [11, 23, 35, 47],
        '龙': [12, 24, 36, 48]
    }

    output_file_path = f"澳门历史数据2010-2024含生肖.xlsx"  # 定义输出文件的路径
    with pd.ExcelWriter(output_file_path) as writer:
        for sheet_name in xl.sheet_names:
            df = xl.parse(sheet_name=sheet_name)

            if date_column_name not in df.columns or number_column_name not in df.columns:
                print(f"列 '{date_column_name}' 或 '{number_column_name}' 在工作表 '{sheet_name}' 中不存在。")
                continue

            try:
                df[date_column_name] = pd.to_datetime(df[date_column_name], errors='coerce')
                df['年'] = df[date_column_name].dt.year.dropna().astype(int)
                df['地支'] = df['年'].apply(lambda x: calculate_zodiac(x) if pd.notnull(x) else '')
                df.drop(columns=['年'], inplace=True)
            except Exception as e:
                print(f"在工作表 '{sheet_name}' 中处理日期时出错: {e}")
                continue

            for i, row in df.iterrows():
                number = row[number_column_name]
                if pd.notnull(number):
                    number = int(number)
                    for zodiac, numbers in base_zodiac_dict.items():
                        if number in numbers:
                            df.at[i, '地支'] = zodiac
                            break

            df.to_excel(writer, sheet_name=sheet_name, index=False)

    print(f"所有工作表已处理完毕，结果已保存至一个单独的Excel文件中")
    return output_file_path
a=process_excel_file_to_single_excel("澳门历史数据2010-2024.xlsx","日期","特")
