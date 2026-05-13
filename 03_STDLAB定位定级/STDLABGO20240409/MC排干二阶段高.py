import pandas as pd

# 定义天干关系
tianganjiayi = [['甲', '乙'], ['丙', '丁'], ['戊', '己'], ['庚', '辛'], ['壬', '癸']]
tianganbingding = [['丙', '丁'], ['戊', '己'], ['庚', '辛'], ['壬', '癸'], ['甲', '乙']]
tianganwuji = [['戊', '己'], ['庚', '辛'], ['壬', '癸'], ['甲', '乙'], ['丙', '丁']]
tiangangengxin = [['庚', '辛'], ['壬', '癸'], ['甲', '乙'], ['丙', '丁'], ['戊', '己']]
tianganrengui = [['壬', '癸'], ['甲', '乙'], ['丙', '丁'], ['戊', '己'], ['庚', '辛']]

# 获取对应天干列表的函数
def get_tian_gan_list(tian_gan):
    if tian_gan in ['甲', '乙']:
        return tianganjiayi
    elif tian_gan in ['丙', '丁']:
        return tianganbingding
    elif tian_gan in ['戊', '己']:
        return tianganwuji
    elif tian_gan in ['庚', '辛']:
        return tiangangengxin
    elif tian_gan in ['壬', '癸']:
        return tianganrengui


# 计算两个天干之间的角度
def calculate_angle(tian_gan_1, tian_gan_2):
    tian_gan_list = get_tian_gan_list(tian_gan_1)
    group_count = len(tian_gan_list)

    group_1, index_1 = next((group_index, group.index(tian_gan_1)) for group_index, group in enumerate(tian_gan_list) if
                             tian_gan_1 in group)
    group_2, index_2 = next((group_index, group.index(tian_gan_2)) for group_index, group in enumerate(tian_gan_list) if
                             tian_gan_2 in group)

    if group_1 == group_2:
        return 0

    group_diff = (group_2 - group_1) % group_count
    angle = group_diff * 60

    return angle

# 反向推算第二个天干的函数
def find_second_tian_gan(tian_gan_1, angle):
    tian_gan_1=tian_gan_1.replace(" ", "")
    tian_gan_list = get_tian_gan_list(tian_gan_1)
    if not tian_gan_list:
        print(f"未找到天干: {tian_gan_1}")
        return ["未知"]

    group_count = len(tian_gan_list)

    group_1, index_1 = next(
        (group_index, group.index(tian_gan_1)) for group_index, group in enumerate(tian_gan_list) if
        tian_gan_1 in group)

    group_diff = (angle // 60) % group_count
    group_2 = (group_1 + group_diff) % group_count

    return tian_gan_list[group_2]

# 定义关系
relations = [
    [('上四', 240), ('月干', 120), ('上三', 120)],
    [('年干', 180), ('上三', 240), ('上一', 0)],
    [('日干', 60), ('上二', 60), ('上三', 180)],
    [('上三', 0), ('上一', 120), ('上一', 240)],
    [('上一', 0), ('年干', 180), ('上五', 120)],
    [('上五', 180), ('上三', 120), ('上五', 0)],
    [('上二', 0), ('上特', 120), ('上三', 120)]
]

# 读取Excel文件
file_path = '1+澳门2020-2024年输入天干数据更新.xlsx'
xls = pd.ExcelFile(file_path)

# 处理每个工作表
with pd.ExcelWriter('澳门2020-2024年排干预测数据-高.xlsx') as writer:
    # 处理每个工作表
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet_name)
        print(f"处理工作表: {sheet_name}")

        # 从第二行开始处理
        # 假设 relations 已经被定义为新的格式
        for index in range(1, len(df)):
            for i, relation_set in enumerate(relations):
                result_list = []  # 用于存储每个 relation_set 的天干计算结果
                for tian_gan_col, angle in relation_set:
                    # 获取上一行的数据
                    tian_gan_1 = df.at[index - 1, tian_gan_col]
                    # 计算可能的天干结果
                    predicted_gan = find_second_tian_gan(tian_gan_1, angle)
                    # 将计算结果添加到 result_list 中
                    result_list.append(predicted_gan)

                # 将合并后的结果作为字符串存入特列，假设你希望用逗号分隔
                df.at[index, f'{i + 1}号预测天干'] = ','.join(map(str, result_list))

        # 保存修改后的数据到新的工作表中
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print("数据处理完成！")
