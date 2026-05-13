import numpy as np
import pandas as pd

# 设置随机种子以确保结果可重复
np.random.seed(42)

# 设置参数
mean_demand = 10
std_dev = 2
service_level = 0.8
num_periods = 1000

# 生成需求数据
demands = np.random.normal(mean_demand, std_dev, (num_periods, 3))

# 计算每个供应商的安全库存
z_score = 0.8416  # 对应80%服务水平的标准正态分布z值
safety_stock = z_score * std_dev

# 计算每个供应商的总库存需求
total_demand = demands + safety_stock

# 初始化结果数据框
results = pd.DataFrame({
    'Period': np.arange(1, num_periods + 1),
    'Supplier_A_Demand': demands[:, 0],
    'Supplier_B_Demand': demands[:, 1],
    'Supplier_C_Demand': demands[:, 2],
    'Supplier_A_Total_Demand': total_demand[:, 0],
    'Supplier_B_Total_Demand': total_demand[:, 1],
    'Supplier_C_Total_Demand': total_demand[:, 2]
})

# 二分法求最优S的计算过程
def find_optimal_S(demands, service_level, num_periods):
    low, high = np.sum(np.min(demands, axis=1)), np.sum(np.max(demands, axis=1))
    binary_search_steps = []
    while high - low > 0.01:
        mid = (low + high) / 2
        fulfilled = np.sum(np.sum(demands <= mid, axis=1) / 3) / num_periods
        binary_search_steps.append([low, high, mid, fulfilled])
        if fulfilled >= service_level:
            high = mid
        else:
            low = mid
    return mid, binary_search_steps

optimal_S, binary_search_steps = find_optimal_S(total_demand, service_level, num_periods)

# 将二分法的每一步添加到数据框
binary_search_df = pd.DataFrame(binary_search_steps, columns=['Low', 'High', 'Mid', 'Fulfilled'])

# 添加最优S结果到数据框
results['Optimal_S'] = optimal_S

# 保存为Excel文件
file_path = 'Numerical_Analysis_Results_Updated.xlsx'
with pd.ExcelWriter(file_path) as writer:
    results.to_excel(writer, sheet_name='Demands and Total Demand', index=False)
    binary_search_df.to_excel(writer, sheet_name='Binary Search Steps', index=False)

print(f"File saved as {file_path}")


