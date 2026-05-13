import pandas as pd
import numpy as np

# 设定初始参数
num_periods = 5  # 这里只考虑前五个周期
initial_S = 600  # 假设每个周期内的资源总量 S 为 600

# 定义分销商需求的正态分布参数（3个分销商）
distributors = {
    'A': {'mean': 100, 'std': 20, 'beta': 0.9},
    'B': {'mean': 150, 'std': 30, 'beta': 0.85},
    'C': {'mean': 200, 'std': 40, 'beta': 0.95}
}

# 生成需求数据（这里我们用固定的种子以保证可重复性）
np.random.seed(0)
demand_data = {d: np.random.normal(distributors[d]['mean'], distributors[d]['std'], num_periods) for d in distributors}

# 初始化资源容量
S = initial_S


# 定义计算填充率和债务优先策略的函数
def calculate_fill_rate_with_debt(S, demand_data, distributors):
    total_supply = {d: np.zeros(num_periods) for d in distributors}
    total_demand = {d: demand_data[d] for d in distributors}
    allocation_order = []
    debt_record = {d: [] for d in distributors}
    allocation_results = []

    for period in range(num_periods):
        # 计算债务
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


# 记录资源分配过程
fill_rate, allocation_order, debt_record, allocation_results = calculate_fill_rate_with_debt(S, demand_data,
                                                                                             distributors)

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

# 创建债务记录表
debt_records_flattened = []
for period in range(num_periods):
    for d in distributors:
        debt_records_flattened.append({'周期': period + 1, '分销商': d, '债务': debt_record[d][period]})

debt_records_df = pd.DataFrame(debt_records_flattened)

# 创建分配顺序表
allocation_orders_flattened = []
for period, orders in enumerate(allocation_order):
    allocation_orders_flattened.append({'周期': period + 1, '分配顺序': ','.join(orders)})

allocation_orders_df = pd.DataFrame(allocation_orders_flattened)

# 创建分配结果表
allocation_results_flattened = []
for period, alloc in enumerate(allocation_results):
    for d, amount in alloc.items():
        allocation_results_flattened.append({'周期': period + 1, '分销商': d, '分配量': amount})

allocation_results_df = pd.DataFrame(allocation_results_flattened)

# 检查数据是否正确填充
print(debt_records_df.head())
print(allocation_orders_df.head())
print(allocation_results_df.head())

# 将所有表格写入一个Excel文件的不同工作表
with pd.ExcelWriter("bisection_process_detailed_v8.xlsx") as writer:
    initial_info.to_excel(writer, sheet_name='初始信息', index=False)
    demand_data_df.to_excel(writer, sheet_name='需求数据')
    debt_records_df.to_excel(writer, sheet_name='债务记录', index=False)
    allocation_orders_df.to_excel(writer, sheet_name='分配顺序', index=False)
    allocation_results_df.to_excel(writer, sheet_name='分配结果', index=False)

file_path = "bisection_process_detailed_v8.xlsx"
file_path
