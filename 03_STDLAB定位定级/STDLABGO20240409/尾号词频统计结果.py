import pandas as pd
from collections import Counter

# Load the uploaded Excel file for processing
file_path = '福建体彩31选7-2016-2024年尾号模型数据.xlsx'

# Load the Excel data
file_data = pd.ExcelFile(file_path)

# Load data from each sheet in the file for further processing
data_frames = {sheet: file_data.parse(sheet) for sheet in file_data.sheet_names}
# Define the relation mapping for the 9-column structure (for 上一关系, 上二关系, etc.)
relation_mapping = {
    0: '下一',
    1: '下二',
    2: '下三',
    3: '下四',
    4: '下五',
    5: '下六',
    6: '下七',
    7: '下特',
    8: '下公历日尾',
    9: '下农历日尾',
}

# Initialize a dictionary to store word counts for each "对下*" relation
word_counts = {relation: Counter() for relation in relation_mapping.values()}

# Process each sheet to count the occurrences of each word for every "对下*" relation
for sheet_name, df in data_frames.items():
    for column in ['上一关系', '上二关系', '上三关系', '上四关系', '上五关系', '上六关系','上七关系', '上特关系', '公历日尾关系', '农历日尾关系']:
        for row in df[column]:
            if pd.notna(row):
                words = row.split('-')
                for idx, word in enumerate(words):
                    if idx in relation_mapping:
                        word_counts[relation_mapping[idx]][f"{column}对{relation_mapping[idx]}-{word}"] += 1

# Convert the counts into DataFrames for each relation and sort them
sorted_word_counts = {relation: pd.DataFrame(counter.items(), columns=['词语', '出现次数']).sort_values(by='出现次数', ascending=False)
                      for relation, counter in word_counts.items()}

# Save results into an Excel file
output_path = '福建体彩31选7-2016-2024年新尾号词频统计结果.xlsx'

with pd.ExcelWriter(output_path) as writer:
    for relation, df in sorted_word_counts.items():
        df.to_excel(writer, sheet_name=relation, index=False)
