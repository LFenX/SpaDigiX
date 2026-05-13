import pandas as pd


def process_excel_files(file_paths):
    detailed_results = []

    for file_path in file_paths:
        xls = pd.ExcelFile(file_path)
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name=sheet_name)
            if '误差值' in df.columns:
                total_count = len(df)
                count_within_2 = (df['误差值'].abs() <= 2).sum()
                count_at_least_5 = (df['误差值'].abs() >= 5).sum()
                percentage_within_2 = (count_within_2 / total_count * 100) if total_count > 0 else 0
                percentage_at_least_5 = (count_at_least_5 / total_count * 100) if total_count > 0 else 0
                detailed_results.append({
                    'File': file_path.split('/')[-1],
                    'Sheet': sheet_name,
                    'Total Count': total_count,
                    'Count <= 2': count_within_2,
                    'Percentage <= 2': percentage_within_2,
                    'Count >= 5': count_at_least_5,
                    'Percentage >= 5': percentage_at_least_5
                })

    # Convert results to DataFrame
    results_df = pd.DataFrame(detailed_results)

    # Save to an Excel file
    output_path = 'output_file.xlsx'
    results_df.to_excel(output_path, index=False)
    return output_path


# 你需要提供一个包含文件路径的列表
file_paths = [
    'P3MC-Processed_Adjusted_甲辰_240119_澳门定位P0_2010-2024_日干支分类_4_processed.xlsx',
    'P3MC-Processed_Adjusted_甲申_240119_澳门定位P0_2010-2024_日干支分类_2_processed.xlsx',
    'P3MC-Processed_Adjusted_甲午_240119_澳门定位P0_2010-2024_日干支分类_3_processed.xlsx',
    'P3MC-Processed_Adjusted_甲戌_240119_澳门定位P0_2010-2024_日干支分类_1_processed.xlsx',
    'P3MC-Processed_Adjusted_甲寅_240119_澳门定位P0_2010-2024_日干支分类_5_processed.xlsx',
    'P3MC-Processed_Adjusted_甲子_240119_澳门定位P0_2010-2024_日干支分类_0_processed.xlsx'
]


# 运行函数
output_file_path = process_excel_files(file_paths)
print(f'Results saved to: {output_file_path}')
