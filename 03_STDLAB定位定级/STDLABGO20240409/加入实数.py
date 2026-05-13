import pandas as pd
import re
from datetime import datetime
from functionSpaDigiXAPPONE import getthebasicmessageofnineGrids
# Define the time dictionary
time_dict = {
    '子时': 0, '丑时': 2, '寅时': 4, '卯时': 6, '辰时': 8, '巳时': 10,
    '午时': 12, '未时': 14, '申时': 16, '酉时': 18, '戌时': 20, '亥时': 22
}


# Function to extract year, month, day, and hour from datetime and time code
def extract_date_time_info(datetime_str, time_code):
    date_time = datetime.strptime(datetime_str, '%Y-%m-%d')
    year = date_time.year
    month = date_time.month
    day = date_time.day
    hour = time_code
    return year, month, day, hour
# Load the Excel files
file1_path = '1080局实数确定版本.xlsx'
file2_path = '加入十二时基础数据-加入双干宫+阴阳遁-零一12时辰数据-24到26年.xlsx'

# Read the first Excel file (assuming it has a single sheet)
df1 = pd.read_excel(file1_path)

# Read the second Excel file (we need to get all sheet names first)
xls = pd.ExcelFile(file2_path)
sheet_names = xls.sheet_names
sheets = {sheet: pd.read_excel(xls, sheet_name=sheet) for sheet in sheet_names}

# Process each sheet in the second Excel file
results = {}
for sheet_name, df in sheets.items():
    # Extract necessary columns
    date_times = pd.to_datetime(df['日期'])
    time_codes = df['子时时辰']


    # Calculate labels and find matches
    real_numbers = []
    for date_time, time_code in zip(date_times, time_codes):
        year, month, day, hour = extract_date_time_info(date_time.strftime('%Y-%m-%d'), time_code)
        labels = getthebasicmessageofnineGrids(year, month, day, hour)[0]
        # Generate label string
        label = ''
        for i in range(9):
            if i == 4:
                item = labels[i]
                label += item['地盘'] + item['九星'] + '-'
            else:
                item = labels[i]
                label += item['地盘'] + item['八神'] + item['天盘'] + item['九星'] + item['八门'] + '-'
        label = label.rstrip('-')

        # Find matching row in df1
        match = df1[df1.iloc[:, 0].str.contains(label, na=False)]
        if not match.empty:
            real_number = round(match.iloc[0]['实数数据'], 1)
            time_word = [k for k, v in time_dict.items() if v == time_code][0].replace('时', '')
            real_number_str = time_word + str(real_number)
            real_numbers.append(real_number_str)
        else:
            real_numbers.append(None)

    # Add the new column to the dataframe
    df['子时实数'] = real_numbers
    results[sheet_name] = df
    time_codes = df['丑时时辰']

    # Calculate labels and find matches
    real_numbers = []
    for date_time, time_code in zip(date_times, time_codes):
        year, month, day, hour = extract_date_time_info(date_time.strftime('%Y-%m-%d'), time_code)
        labels = getthebasicmessageofnineGrids(year, month, day, hour)[0]
        # Generate label string
        label = ''
        for i in range(9):
            if i == 4:
                item = labels[i]
                label += item['地盘'] + item['九星'] + '-'
            else:
                item = labels[i]
                label += item['地盘'] + item['八神'] + item['天盘'] + item['九星'] + item['八门'] + '-'
        label = label.rstrip('-')

        # Find matching row in df1
        match = df1[df1.iloc[:, 0].str.contains(label, na=False)]
        if not match.empty:
            real_number = round(match.iloc[0]['实数数据'], 1)
            time_word = [k for k, v in time_dict.items() if v == time_code][0].replace('时', '')
            real_number_str = time_word + str(real_number)
            real_numbers.append(real_number_str)
        else:
            real_numbers.append(None)

    # Add the new column to the dataframe
    df['丑时实数'] = real_numbers
    results[sheet_name] = df
    time_codes = df['寅时时辰']

    # Calculate labels and find matches
    real_numbers = []
    for date_time, time_code in zip(date_times, time_codes):
        year, month, day, hour = extract_date_time_info(date_time.strftime('%Y-%m-%d'), time_code)
        labels = getthebasicmessageofnineGrids(year, month, day, hour)[0]
        # Generate label string
        label = ''
        for i in range(9):
            if i == 4:
                item = labels[i]
                label += item['地盘'] + item['九星'] + '-'
            else:
                item = labels[i]
                label += item['地盘'] + item['八神'] + item['天盘'] + item['九星'] + item['八门'] + '-'
        label = label.rstrip('-')

        # Find matching row in df1
        match = df1[df1.iloc[:, 0].str.contains(label, na=False)]
        if not match.empty:
            real_number = round(match.iloc[0]['实数数据'], 1)
            time_word = [k for k, v in time_dict.items() if v == time_code][0].replace('时', '')
            real_number_str = time_word + str(real_number)
            real_numbers.append(real_number_str)
        else:
            real_numbers.append(None)

    # Add the new column to the dataframe
    df['寅时实数'] = real_numbers
    results[sheet_name] = df
    time_codes = df['卯时时辰']

    # Calculate labels and find matches
    real_numbers = []
    for date_time, time_code in zip(date_times, time_codes):
        year, month, day, hour = extract_date_time_info(date_time.strftime('%Y-%m-%d'), time_code)
        labels = getthebasicmessageofnineGrids(year, month, day, hour)[0]
        # Generate label string
        label = ''
        for i in range(9):
            if i == 4:
                item = labels[i]
                label += item['地盘'] + item['九星'] + '-'
            else:
                item = labels[i]
                label += item['地盘'] + item['八神'] + item['天盘'] + item['九星'] + item['八门'] + '-'
        label = label.rstrip('-')

        # Find matching row in df1
        match = df1[df1.iloc[:, 0].str.contains(label, na=False)]
        if not match.empty:
            real_number = round(match.iloc[0]['实数数据'], 1)
            time_word = [k for k, v in time_dict.items() if v == time_code][0].replace('时', '')
            real_number_str = time_word + str(real_number)
            real_numbers.append(real_number_str)
        else:
            real_numbers.append(None)

    # Add the new column to the dataframe
    df['卯时实数'] = real_numbers
    results[sheet_name] = df
    time_codes = df['辰时时辰']

    # Calculate labels and find matches
    real_numbers = []
    for date_time, time_code in zip(date_times, time_codes):
        year, month, day, hour = extract_date_time_info(date_time.strftime('%Y-%m-%d'), time_code)
        labels = getthebasicmessageofnineGrids(year, month, day, hour)[0]
        # Generate label string
        label = ''
        for i in range(9):
            if i == 4:
                item = labels[i]
                label += item['地盘'] + item['九星'] + '-'
            else:
                item = labels[i]
                label += item['地盘'] + item['八神'] + item['天盘'] + item['九星'] + item['八门'] + '-'
        label = label.rstrip('-')

        # Find matching row in df1
        match = df1[df1.iloc[:, 0].str.contains(label, na=False)]
        if not match.empty:
            real_number = round(match.iloc[0]['实数数据'], 1)
            time_word = [k for k, v in time_dict.items() if v == time_code][0].replace('时', '')
            real_number_str = time_word + str(real_number)
            real_numbers.append(real_number_str)
        else:
            real_numbers.append(None)

    # Add the new column to the dataframe
    df['辰时实数'] = real_numbers
    results[sheet_name] = df
    time_codes = df['巳时时辰']

    # Calculate labels and find matches
    real_numbers = []
    for date_time, time_code in zip(date_times, time_codes):
        year, month, day, hour = extract_date_time_info(date_time.strftime('%Y-%m-%d'), time_code)
        labels = getthebasicmessageofnineGrids(year, month, day, hour)[0]
        # Generate label string
        label = ''
        for i in range(9):
            if i == 4:
                item = labels[i]
                label += item['地盘'] + item['九星'] + '-'
            else:
                item = labels[i]
                label += item['地盘'] + item['八神'] + item['天盘'] + item['九星'] + item['八门'] + '-'
        label = label.rstrip('-')

        # Find matching row in df1
        match = df1[df1.iloc[:, 0].str.contains(label, na=False)]
        if not match.empty:
            real_number = round(match.iloc[0]['实数数据'], 1)
            time_word = [k for k, v in time_dict.items() if v == time_code][0].replace('时', '')
            real_number_str = time_word + str(real_number)
            real_numbers.append(real_number_str)
        else:
            real_numbers.append(None)

    # Add the new column to the dataframe
    df['巳时实数'] = real_numbers
    results[sheet_name] = df
    time_codes = df['午时时辰']

    # Calculate labels and find matches
    real_numbers = []
    for date_time, time_code in zip(date_times, time_codes):
        year, month, day, hour = extract_date_time_info(date_time.strftime('%Y-%m-%d'), time_code)
        labels = getthebasicmessageofnineGrids(year, month, day, hour)[0]
        # Generate label string
        label = ''
        for i in range(9):
            if i == 4:
                item = labels[i]
                label += item['地盘'] + item['九星'] + '-'
            else:
                item = labels[i]
                label += item['地盘'] + item['八神'] + item['天盘'] + item['九星'] + item['八门'] + '-'
        label = label.rstrip('-')

        # Find matching row in df1
        match = df1[df1.iloc[:, 0].str.contains(label, na=False)]
        if not match.empty:
            real_number = round(match.iloc[0]['实数数据'], 1)
            time_word = [k for k, v in time_dict.items() if v == time_code][0].replace('时', '')
            real_number_str = time_word + str(real_number)
            real_numbers.append(real_number_str)
        else:
            real_numbers.append(None)

    # Add the new column to the dataframe
    df['午时实数'] = real_numbers
    results[sheet_name] = df
    time_codes = df['未时时辰']

    # Calculate labels and find matches
    real_numbers = []
    for date_time, time_code in zip(date_times, time_codes):
        year, month, day, hour = extract_date_time_info(date_time.strftime('%Y-%m-%d'), time_code)
        labels = getthebasicmessageofnineGrids(year, month, day, hour)[0]
        # Generate label string
        label = ''
        for i in range(9):
            if i == 4:
                item = labels[i]
                label += item['地盘'] + item['九星'] + '-'
            else:
                item = labels[i]
                label += item['地盘'] + item['八神'] + item['天盘'] + item['九星'] + item['八门'] + '-'
        label = label.rstrip('-')

        # Find matching row in df1
        match = df1[df1.iloc[:, 0].str.contains(label, na=False)]
        if not match.empty:
            real_number = round(match.iloc[0]['实数数据'], 1)
            time_word = [k for k, v in time_dict.items() if v == time_code][0].replace('时', '')
            real_number_str = time_word + str(real_number)
            real_numbers.append(real_number_str)
        else:
            real_numbers.append(None)

    # Add the new column to the dataframe
    df['未时实数'] = real_numbers
    results[sheet_name] = df
    time_codes = df['申时时辰']

    # Calculate labels and find matches
    real_numbers = []
    for date_time, time_code in zip(date_times, time_codes):
        year, month, day, hour = extract_date_time_info(date_time.strftime('%Y-%m-%d'), time_code)
        labels = getthebasicmessageofnineGrids(year, month, day, hour)[0]
        # Generate label string
        label = ''
        for i in range(9):
            if i == 4:
                item = labels[i]
                label += item['地盘'] + item['九星'] + '-'
            else:
                item = labels[i]
                label += item['地盘'] + item['八神'] + item['天盘'] + item['九星'] + item['八门'] + '-'
        label = label.rstrip('-')

        # Find matching row in df1
        match = df1[df1.iloc[:, 0].str.contains(label, na=False)]
        if not match.empty:
            real_number = round(match.iloc[0]['实数数据'], 1)
            time_word = [k for k, v in time_dict.items() if v == time_code][0].replace('时', '')
            real_number_str = time_word + str(real_number)
            real_numbers.append(real_number_str)
        else:
            real_numbers.append(None)

    # Add the new column to the dataframe
    df['申时实数'] = real_numbers
    results[sheet_name] = df
    time_codes = df['酉时时辰']

    # Calculate labels and find matches
    real_numbers = []
    for date_time, time_code in zip(date_times, time_codes):
        year, month, day, hour = extract_date_time_info(date_time.strftime('%Y-%m-%d'), time_code)
        labels = getthebasicmessageofnineGrids(year, month, day, hour)[0]
        # Generate label string
        label = ''
        for i in range(9):
            if i == 4:
                item = labels[i]
                label += item['地盘'] + item['九星'] + '-'
            else:
                item = labels[i]
                label += item['地盘'] + item['八神'] + item['天盘'] + item['九星'] + item['八门'] + '-'
        label = label.rstrip('-')

        # Find matching row in df1
        match = df1[df1.iloc[:, 0].str.contains(label, na=False)]
        if not match.empty:
            real_number = round(match.iloc[0]['实数数据'], 1)
            time_word = [k for k, v in time_dict.items() if v == time_code][0].replace('时', '')
            real_number_str = time_word + str(real_number)
            real_numbers.append(real_number_str)
        else:
            real_numbers.append(None)

    # Add the new column to the dataframe
    df['酉时实数'] = real_numbers
    results[sheet_name] = df
    time_codes = df['戌时时辰']

    # Calculate labels and find matches
    real_numbers = []
    for date_time, time_code in zip(date_times, time_codes):
        year, month, day, hour = extract_date_time_info(date_time.strftime('%Y-%m-%d'), time_code)
        labels = getthebasicmessageofnineGrids(year, month, day, hour)[0]
        # Generate label string
        label = ''
        for i in range(9):
            if i == 4:
                item = labels[i]
                label += item['地盘'] + item['九星'] + '-'
            else:
                item = labels[i]
                label += item['地盘'] + item['八神'] + item['天盘'] + item['九星'] + item['八门'] + '-'
        label = label.rstrip('-')

        # Find matching row in df1
        match = df1[df1.iloc[:, 0].str.contains(label, na=False)]
        if not match.empty:
            real_number = round(match.iloc[0]['实数数据'], 1)
            time_word = [k for k, v in time_dict.items() if v == time_code][0].replace('时', '')
            real_number_str = time_word + str(real_number)
            real_numbers.append(real_number_str)
        else:
            real_numbers.append(None)

    # Add the new column to the dataframe
    df['戌时实数'] = real_numbers
    results[sheet_name] = df
    time_codes = df['亥时时辰']

    # Calculate labels and find matches
    real_numbers = []
    for date_time, time_code in zip(date_times, time_codes):
        year, month, day, hour = extract_date_time_info(date_time.strftime('%Y-%m-%d'), time_code)
        labels = getthebasicmessageofnineGrids(year, month, day, hour)[0]
        # Generate label string
        label = ''
        for i in range(9):
            if i == 4:
                item = labels[i]
                label += item['地盘'] + item['九星'] + '-'
            else:
                item = labels[i]
                label += item['地盘'] + item['八神'] + item['天盘'] + item['九星'] + item['八门'] + '-'
        label = label.rstrip('-')

        # Find matching row in df1
        match = df1[df1.iloc[:, 0].str.contains(label, na=False)]
        if not match.empty:
            real_number = round(match.iloc[0]['实数数据'], 1)
            time_word = [k for k, v in time_dict.items() if v == time_code][0].replace('时', '')
            real_number_str = time_word + str(real_number)
            real_numbers.append(real_number_str)
        else:
            real_numbers.append(None)

    # Add the new column to the dataframe
    df['亥时实数'] = real_numbers
    results[sheet_name] = df

# Save the updated sheets to a new Excel file
output_path = '加入实数-加入十二时基础数据-加入双干宫+阴阳遁-零一12时辰数据-24到26年.xlsx'
with pd.ExcelWriter(output_path) as writer:
    for sheet_name, df in results.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

output_path
