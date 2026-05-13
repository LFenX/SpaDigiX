def calculate_ganzhiyuandan(year):
    # 天干和地支循环周期
    tian_gan = "甲乙丙丁戊己庚辛壬癸"
    di_zhi = "子丑寅卯辰巳午未申酉戌亥"
    # 元旦日期的天干地支索引
    # 元旦基准日期的干支为甲子年
    base_year = 1900
    base_tian_gan_index = 0  # 甲
    base_di_zhi_index = 10  # 子
    # 计算输入年份与基准年份的差值
    year_diff = year - base_year
    a=year_diff//4
    b=year_diff%4

    if a>25 and a%25!=0:
        lf=calculate_ganzhiyuandan(year-(a-25*(a//25))*4-b)
        base_tian_gan_index=lf[2]
        base_di_zhi_index=lf[3]
        year_diff=(a-25*(a//25))*4+b
        c = year-(a-25*(a//25))*4-b
        a = year_diff // 4
        b = year_diff % 4
        if c%400==0:
            if b==0:
                # 计算元旦日期的天干地支索引
                ganzhi_tian_gan_index = (base_tian_gan_index +21*a) % len(tian_gan)
                ganzhi_di_zhi_index = (base_di_zhi_index + 21*a) % len(di_zhi)
            else:
                ganzhi_tian_gan_index = (base_tian_gan_index + 21*a+b*5+1) % len(tian_gan)
                ganzhi_di_zhi_index = (base_di_zhi_index + 21*a+b*5+1) % len(di_zhi)
        else:
            if b==0:
                # 计算元旦日期的天干地支索引
                ganzhi_tian_gan_index = (base_tian_gan_index +21*a-1) % len(tian_gan)
                ganzhi_di_zhi_index = (base_di_zhi_index + 21*a-1) % len(di_zhi)
            else:
                ganzhi_tian_gan_index = (base_tian_gan_index + 21*a+b*5) % len(tian_gan)
                ganzhi_di_zhi_index = (base_di_zhi_index + 21*a+b*5) % len(di_zhi)
    elif a>25 and a%25==0:
        lf = calculate_ganzhiyuandan(year-100)
        base_tian_gan_index = lf[2]
        base_di_zhi_index = lf[3]
        year_diff =100
        c = year - 100
        a = year_diff // 4
        b = year_diff % 4
        if c % 400 == 0:
            if b == 0:
                # 计算元旦日期的天干地支索引
                ganzhi_tian_gan_index = (base_tian_gan_index + 21 * a) % len(tian_gan)
                ganzhi_di_zhi_index = (base_di_zhi_index + 21 * a) % len(di_zhi)
            else:
                ganzhi_tian_gan_index = (base_tian_gan_index + 21 * a + b * 5 + 1) % len(tian_gan)
                ganzhi_di_zhi_index = (base_di_zhi_index + 21 * a + b * 5 + 1) % len(di_zhi)
        else:
            if b == 0:
                # 计算元旦日期的天干地支索引
                ganzhi_tian_gan_index = (base_tian_gan_index + 21 * a - 1) % len(tian_gan)
                ganzhi_di_zhi_index = (base_di_zhi_index + 21 * a - 1) % len(di_zhi)
            else:
                ganzhi_tian_gan_index = (base_tian_gan_index + 21 * a + b * 5) % len(tian_gan)
                ganzhi_di_zhi_index = (base_di_zhi_index + 21 * a + b * 5) % len(di_zhi)
    else:
            if b==0:
                # 计算元旦日期的天干地支索引
                ganzhi_tian_gan_index = (base_tian_gan_index +21*a-1) % len(tian_gan)
                ganzhi_di_zhi_index = (base_di_zhi_index + 21*a-1) % len(di_zhi)
            else:
                ganzhi_tian_gan_index = (base_tian_gan_index + 21*a+b*5) % len(tian_gan)
                ganzhi_di_zhi_index = (base_di_zhi_index + 21*a+b*5) % len(di_zhi)
    # 获取对应的天干和地支字符
    tian_gan_char = tian_gan[ganzhi_tian_gan_index]
    di_zhi_char = di_zhi[ganzhi_di_zhi_index]
    return tian_gan_char,di_zhi_char,ganzhi_tian_gan_index,ganzhi_di_zhi_index

# 输入年份
year = int(input("请输入年份："))
# 计算元旦这天的干支
ganzhi = calculate_ganzhiyuandan(year)
x=ganzhi[0]+ganzhi[1]
print(f"{year}年元旦的干支（日干支）为：{x}")