import pandas as pd
import ast
# 基础天干序列
base_sequence = ['己', '戊', '丁', '丙', '乙', '甲', '癸', '壬', '辛', '庚']


# 生成特定年份的天干序列
def generate_tian_gan_for_year(base_sequence, start_year, target_year):
    shift = (target_year - start_year) % 10
    shifted_sequence = base_sequence[-shift:] + base_sequence[:-shift]

    tian_gan_list = []
    for i in range(49):
        tian_gan_list.append(shifted_sequence[i % 10])

    tian_gan_to_numbers = {gan: [] for gan in shifted_sequence}
    for i in range(49):
        tian_gan_to_numbers[tian_gan_list[i]].append(i + 1)

    return tian_gan_to_numbers


# 转换天干字符串为数字序列
def convert_tian_gan_to_first_two_numbers(tian_gan_string, tian_gan_to_numbers):
    list_of_lists = ast.literal_eval(tian_gan_string)

    # 2. 展开列表并连接成单一字符串
    tian_gan_list = ''.join(item for sublist in list_of_lists for item in sublist)
    result = {}

    for gan in tian_gan_list[:6]:
        if gan in tian_gan_to_numbers:
            result[gan] = tian_gan_to_numbers[gan]

    output = ""
    for gan, numbers in result.items():
        output += f"{numbers}\r\n"  # 使用 \r\n 替代 \n

    print(output)
    return output.strip()


file_path = '香港2010-2024年排干特码预测数据更新.xlsx'
xls = pd.ExcelFile(file_path)

with pd.ExcelWriter('香港2010-2024年排干特码预测号码数据更新.xlsx') as writer:
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet_name)
        print(f"处理工作表: {sheet_name}")

        # 获取年份
        year = df.at[1, '日期'].year  # 假设日期在第二行，并且格式是日期类型
        tian_gan_to_numbers = generate_tian_gan_for_year(base_sequence, 2009, year)
        # 转换天干为数字并创建新列
        for i in range(1, 11):  # 特1到特10
            tian_gan_col = f'特{i}'
            df[f'特{i}号预测号码'] = df[tian_gan_col].apply(
                lambda x: (
                    print(f"Processing cell: {x}") or  # 打印单元格内容
                    convert_tian_gan_to_first_two_numbers(x, tian_gan_to_numbers)  # 不再使用 eval
                    if pd.notna(x) and x else None
                )
            )
            # # 调整列顺序，将"一", "二", "三", "四", "五", "六", "特" 移动到预测号码前一列
            # cols_order = df.columns.tolist()
            #
            # for i, col in enumerate(['一', '二', '三', '四', '五', '六', '特'], start=1):
            #     prediction_col = f'{i}号预测号码'
            #     if col in cols_order and prediction_col in cols_order:
            #         # 先移除这些列，然后插入到预测号码列的前面
            #         cols_order.remove(col)
            #         insert_index = cols_order.index(prediction_col)
            #         cols_order.insert(insert_index, col)
            #
            # # 重新排序列
            # df = df[cols_order]
        # 保存修改后的数据到新的工作表中
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print("数字转换完成！")