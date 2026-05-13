import pandas as pd
import numpy as np

# 设定初始参数
num_periods = 10000
initial_S_upper = 2000
initial_S_lower = 800

# 定义分销商需求的正态分布参数（8个分销商）
distributors = {
    'A': {'mean': 200, 'std': 20, 'beta': 0.9},
    'B': {'mean': 150, 'std': 30, 'beta': 0.85},
    'C': {'mean': 200, 'std': 40, 'beta': 0.95},
    'D': {'mean': 120, 'std': 25, 'beta': 0.88},
    'E': {'mean': 180, 'std': 35, 'beta': 0.92},
    'F': {'mean': 130, 'std': 28, 'beta': 0.87},
    'G': {'mean': 170, 'std': 32, 'beta': 0.93},
    'H': {'mean': 140, 'std': 30, 'beta': 0.89}
}

# 生成需求数据
np.random.seed(0)
demand_data = {d: np.random.normal(distributors[d]['mean'], distributors[d]['std'], num_periods) for d in distributors}

# 初始化资源容量范围
S_lower = initial_S_lower
S_upper = initial_S_upper
S_mid = (S_lower + S_upper) / 2


# 定义计算填充率的函数
def calculate_fill_rate_with_debt(S, demand_data, distributors):
    total_supply = {d: np.zeros(num_periods) for d in distributors}
    total_demand = {d: demand_data[d] for d in distributors}
    allocation_order = []
    debt_record = {d: [] for d in distributors}
    allocation_results = []

    for period in range(num_periods):
        # 按债务优先策略分配资源
        debt = {d: max(0, distributors[d]['beta'] * distributors[d]['mean'] * (period + 1) - np.sum(
            total_supply[d][:period + 1])) for d in distributors}
        sorted_distributors = sorted(debt.keys(), key=lambda x: debt[x], reverse=True)
        allocation_order.append(sorted_distributors)

        available_S = S
        period_allocation = {}
        for d in sorted_distributors:
            if available_S >= demand_data[d][period]:
                total_supply[d][period] = demand_data[d][period]
                period_allocation[d] = demand_data[d][period]
                available_S -= demand_data[d][period]
            else:
                total_supply[d][period] = available_S
                period_allocation[d] = available_S
                available_S = 0
        allocation_results.append(period_allocation)

        # 记录每个分销商的债务
        for d in distributors:
            debt_record[d].append(debt[d])

    fill_rate = {d: np.sum(total_supply[d]) / np.sum(total_demand[d]) for d in distributors}
    return fill_rate, allocation_order, debt_record, allocation_results


# 记录二分过程和每次分配的顺序、债务、分配结果
bisection_steps = []
allocation_orders = []
all_debt_records = []
allocation_results_all = []

# 进行二分搜索
while S_upper - S_lower > 1:
    S_mid = (S_lower + S_upper) / 2
    fill_rate, allocation_order, debt_record, allocation_results = calculate_fill_rate_with_debt(S_mid, demand_data,
                                                                                                 distributors)

    # 记录当前状态
    bisection_steps.append({
        'S_lower': S_lower,
        'S_upper': S_upper,
        'S_mid': S_mid,
        **{f'Fill_Rate_{d}': fill_rate[d] for d in distributors}
    })
    allocation_orders.append(allocation_order)
    all_debt_records.append(debt_record)
    allocation_results_all.append(allocation_results)

    if all(fill_rate[d] >= distributors[d]['beta'] for d in distributors):
        S_upper = S_mid
    else:
        S_lower = S_mid

# 记录最终的最小总资源量
optimal_S = S_mid

# 创建初始信息表
initial_info = pd.DataFrame({
    '分销商': distributors.keys(),
    '平均需求': [distributors[d]['mean'] for d in distributors],
    '需求标准差': [distributors[d]['std'] for d in distributors],
    '填充率要求': [distributors[d]['beta'] for d in distributors]
})

# 创建需求数据表
demand_data_df = pd.DataFrame(demand_data)
demand_data_df.index.name = '周期'

# 创建约束条件表
constraints = pd.DataFrame({
    '分销商': distributors.keys(),
    '填充率要求': [distributors[d]['beta'] for d in distributors]
})

# 创建二分过程表
df_bisection = pd.DataFrame(bisection_steps)

# 创建分配顺序和债务记录表
allocation_orders_flattened = []
for period, orders in enumerate(allocation_orders):
    for order in orders:
        allocation_orders_flattened.append({'周期': period, '分配顺序': ','.join(order)})

debt_records_flattened = []
for period in range(num_periods):
    for d in distributors:
        for i, debt_record in enumerate(all_debt_records):
            debt_records_flattened.append({'周期': period, '分销商': d, '债务': debt_record[d][period]})

allocation_results_flattened = []
for i, alloc_result in enumerate(allocation_results_all):
    for period, alloc in enumerate(alloc_result):
        for d, amount in alloc.items():
            allocation_results_flattened.append({'周期': period, '分销商': d, '分配量': amount, '总资源量': optimal_S})

allocation_orders_df = pd.DataFrame(allocation_orders_flattened)
debt_records_df = pd.DataFrame(debt_records_flattened)
allocation_results_df = pd.DataFrame(allocation_results_flattened)

# 检查数据是否正确填充
print(df_bisection.head())
print(allocation_orders_df.head())
print(debt_records_df.head())
print(allocation_results_df.head())

# 将所有表格写入一个Excel文件的不同工作表
with pd.ExcelWriter("bisection_process_detailed_v6.xlsx") as writer:
    initial_info.to_excel(writer, sheet_name='初始信息', index=False)
    demand_data_df.to_excel(writer, sheet_name='需求数据')
    constraints.to_excel(writer, sheet_name='约束条件', index=False)
    df_bisection.to_excel(writer, sheet_name='二分过程', index=False)
    allocation_orders_df.to_excel(writer, sheet_name='分配顺序', index=False)
    debt_records_df.to_excel(writer, sheet_name='债务记录', index=False)
    allocation_results_df.to_excel(writer, sheet_name='分配结果', index=False)

print("文件已生成并保存为 bisection_process_detailed_v6.xlsx")
