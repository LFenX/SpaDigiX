from zhdate import ZhDate

# 创建一个农历日期对象，参数分别是年、月、日
lunar_date = ZhDate(2023, 8, 7)

# 调用to_datetime()方法将农历日期转换为公历日期
solar_date = lunar_date.to_datetime()
solar_year = solar_date.year
solar_month = solar_date.month
solar_day = solar_date.day

# 打印导出的阳历年份、月份和日
print("阳历日期：")
print("年份:", solar_year)
print("月份:", solar_month)
print("日:", solar_day)
# 打印转换后的公历日期
print(solar_date)
current_datetime = datetime.now()
lunar_date = ZhDate.from_datetime(current_datetime)
lunar_year = lunar_date.lunar_year
lunar_month = lunar_date.lunar_month
lunar_day = lunar_date.lunar_day
solar_hour = current_datetime.hour
solar_minute = current_datetime.minute
lunar_to_numeric = {
    "初一": 1, "初二": 2, "初三": 3, "初四": 4, "初五": 5,
    "初六": 6, "初七": 7, "初八": 8, "初九": 9, "初十": 10,
    "十一": 11, "十二": 12, "十三": 13, "十四": 14, "十五": 15,
    "十六": 16, "十七": 17, "十八": 18, "十九": 19, "二十": 20,
    "廿一": 21, "廿二": 22, "廿三": 23, "廿四": 24, "廿五": 25,
    "廿六": 26, "廿七": 27, "廿八": 28, "廿九": 29, "三十": 30
}
month_dict = {
    "一": 1,
    "二": 2,
    "三": 3,
    "四": 4,
    "五": 5,
    "六": 6,
    "七": 7,
    "八": 8,
    "九": 9,
    "十": 10,
    "十一": 11,
    "十二": 12
}

for key in lunar_to_numeric:
    if lunar_to_numeric[key] == lunar_day:
        lunar_day = key
        break
    else:
        continue
for key in month_dict:
    if month_dict[key] == lunar_month:
        lunar_month = key
        break
    else:
        continue
self.NIANSHUCHUKUANGNONGLI_shuru.input_text.setText(lunar_year)
self.YUESHUCHUKUANGNONGLI_shuru.input_text.setText(lunar_month)
self.RISHUCHUKUANGNONGLI_shuru.input_text.setText(lunar_day)
self.SHISHUCHUKUANGNONGLI_shuru.input_text.setText(solar_hour)
self.JIEQIYDSHUCHUNONGLI_shuru.input_text.setText(solar_minute)