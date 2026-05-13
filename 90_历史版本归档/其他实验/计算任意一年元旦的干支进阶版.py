import calendar
def calculate_ganzhiyuandan(year):
    # 天干和地支循环周期
    tian_gan = "甲乙丙丁戊己庚辛壬癸"
    di_zhi = "子丑寅卯辰巳午未申酉戌亥"
    # 元旦日期的天干地支索引
    # 元旦基准日期的干支为甲子年
    base_year = 1900
    base_tian_gan_index = 0  # 甲
    base_di_zhi_index = 10  # 戌
    # 计算输入年份与基准年份的差值
    index=0
    if year==1900:
        index=0
    else:
        for i in range(1900, year):
            if calendar.isleap(i):
                index = index + 6
            else:
                index = index + 5
    ganzhi_tian_gan_index=(base_tian_gan_index+index)%10
    ganzhi_di_zhi_index=(base_di_zhi_index+index)%12
    tian_gan_char=tian_gan[ganzhi_tian_gan_index]

    di_zhi_char=di_zhi[ganzhi_di_zhi_index]
    return tian_gan_char, di_zhi_char, ganzhi_tian_gan_index, ganzhi_di_zhi_index
year=int(input("请输入年份："))
ydgz = calculate_ganzhiyuandan(year)
yuandan_ganzhi = ydgz[0] + ydgz[1]
print(yuandan_ganzhi)


