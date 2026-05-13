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
    ('上五', 120),
    ('月干', 60),
    ('上四', 240),
    ('年干', 180),
    ('上三', 240),
    ('年干', 0),
    ('上五', 60),
    ('上五', 180),
    ('年干', 60),
    ('上二', 180)
]

# 读取Excel文件
file_path = '1+香港2010-2024年输入天干数据更新.xlsx'
xls = pd.ExcelFile(file_path)

# 处理每个工作表
with pd.ExcelWriter('香港2010-2024年排干特码预测数据更新.xlsx') as writer:
    # 处理每个工作表
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet_name)
        print(f"处理工作表: {sheet_name}")

        # 从第二行开始处理
        for index in range(1, len(df)):
            for i, (tian_gan_col, angle) in enumerate(relations):
                # 获取上一行的数据
                tian_gan_1 = df.at[index - 1, tian_gan_col]
                # 计算可能的天干结果
                predicted_gan = find_second_tian_gan(tian_gan_1, angle)
                # 将结果放入新列中
                df.at[index, f'特{i + 1}'] = f"{predicted_gan}"  # 假设我们只取第一个天干

        # 保存修改后的数据到新的工作表中
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print("数据处理完成！")
