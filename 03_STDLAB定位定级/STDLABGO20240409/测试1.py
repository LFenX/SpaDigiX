
''' from functionSpaDigiXAPPONE import  getthebasicmessageofnineGrids
a=int(input("yyyy"))
b=int(input("mmmm"))
c=int(input("dddd"))
e=int(input("hhhh"))
d=getthebasicmessageofnineGrids(a,b,c,e)[1]
ff=d[3]
yd=d[0]
qiju=d[9]
gg=f"{ff}-{yd}-{qiju}"
dingweigong=getthebasicmessageofnineGrids(a,b,c,e)[0]
print(gg)
print(dingweigong)    '''
import pandas as pd
from functionSpaDigiXAPPONE import getthebasicmessageofnineGrids
# Load the Excel file
file_path = '1080局实数.xlsx'
df = pd.read_excel(file_path)

# Function to extract the first date and hour from the given string
def extract_first_date_time(cell):
    first_entry = cell.split(',')[0]
    date, time = first_entry.rsplit('-', 1)
    return date, time

# Apply the function to extract date and time, creating two new columns
df['日期'], df['时辰'] = zip(*df['日期和时辰'].map(extract_first_date_time))


# Apply the function to the new columns and create the '阴阳九局' column
df['阴阳九局'] = df.apply(lambda row: getthebasicmessageofnineGrids(*row['日期'].split('-'), row['时辰'])[3], axis=1)

# Save the updated dataframe to a new Excel file
output_file_path = '1080局实数_更新.xlsx'
df.to_excel(output_file_path, index=False)

# Display the updated dataframe
df.head()
