from ephem import *
def getthebasicmessageofnineGrids(NIAN,YUE,RI,SHICHENG):
    from zhdate import ZhDate
    import math
    import calendar
    import datetime
    yea = NIAN
    mon = YUE
    da = RI
    ho = SHICHENG
    Tiangan = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
    Dizhi = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
    shengxiao = ['鼠', '牛', '虎', '兔', '龙', '蛇', '马', '羊', '猴', '鸡', '狗', '猪']
    tian = []
    modified_date = datetime.datetime(int(yea), int(mon), int(da), int(ho))
    year = modified_date.year
    month = modified_date.month
    day = modified_date.day
    hour = modified_date.hour
    Solar_date = datetime.datetime(year, month, day)
    lunar_date = ZhDate.from_datetime(Solar_date)
    shijiannian = lunar_date.lunar_year
    shijianyue = lunar_date.lunar_month
    shijianri = lunar_date.lunar_day
    year_jian = (int(shijiannian) - 1900) % 12
    shengxiaonian = shengxiao[year_jian]
    # year=Solar_date.year
    # month=Solar_date.month
    # day=Solar_date.day
    # 以下为计算对应时间点的节气
    jieqi = ["春分", "清明", "谷雨", "立夏", "小满", "芒种", \
             "夏至", "小暑", "大暑", "立秋", "处暑", "白露", \
             "秋分", "寒露", "霜降", "立冬", "小雪", "大雪", \
             "冬至", "小寒", "大寒", "立春", "雨水", "惊蛰"]

    # 计算黄经
    def ecliptic_lon(jd_utc):
        s = Sun(jd_utc)  # 构造太阳
        equ = Equatorial(s.ra, s.dec, epoch=jd_utc)  # 求太阳的视赤经视赤纬（epoch设为所求时间就是视赤经视赤纬）
        e = Ecliptic(equ)  # 赤经赤纬转到黄经黄纬
        return e.lon  # 返回黄纬

    # 根据时间求太阳黄经，计算到了第几个节气，春分序号为0
    def sta(jd):
        e = ecliptic_lon(jd)
        n = int(e * 180.0 / math.pi / 15)
        return n

    # 根据当前时间，求下个节气的发生时间
    def iteration(jd, sta):  # jd：要求的开始时间，sta：不同的状态函数
        s1 = sta(jd)  # 初始状态(太阳处于什么位置)
        s0 = s1
        dt = datetime.timedelta(days=1.0)
        while True:
            jd += dt
            s = sta(jd)
            if s0 != s:
                s0 = s
                dt = -dt / 2  # 使时间改变量折半减小
            if abs(dt.total_seconds()) < 0.0000001 and s != s1:
                break
        return jd

    def jq(year):  # 从当前时间开始连续输出未来n个节气的时间
        jd = datetime.datetime(year - 1, 12, 15, 0, 0,
                               0)  # 获取当前时间的一个儒略日和1899/12/31 12:00:00儒略日的差值
        e = ecliptic_lon(jd)
        n = int(e * 180.0 / math.pi / 15) + 1
        a = []
        for i in range(26):
            if n >= 24:
                n -= 24
            jd = iteration(jd, sta)
            d = Date(jd + datetime.timedelta(days=1 / 3)).tuple()
            jieqishijian = datetime.datetime(d[0], d[1], d[2], d[3], 0, 0)
            a.append(jieqishijian)
            # print(
            # "{0}-{1:02d}-{2:02d} {3}：{4:02d}:{5:02d}:{6:03.1f}".format(d[0], d[1], d[2], jieqi[n], d[3],
            #  d[4], d[5]))
            n += 1
        return a

    b = jq(year)
    c = {}
    for i in range(0, 25):
        c[b[i]] = b[i + 1]
    v = datetime.datetime(year, month, day, 23, 59, 0)
    jieqi_index = 0
    for i in range(0, 25):
        if v >= b[i] and v <= b[i + 1]:
            jieqi_index = i
            break
        else:
            continue
    jieqi_list = ["冬至",
                  "小寒", "大寒", "立春", "雨水", "惊蛰", "春分",
                  "清明", "谷雨", "立夏", "小满", "芒种", "夏至",
                  "小暑", "大暑", "立秋", "处暑", "白露", "秋分",
                  "寒露", "霜降", "立冬", "小雪", "大雪", "冬至", "小寒"]
    JQ = jieqi_list[jieqi_index]
    # print("输入日期的节气为：%s"%(JQ))
    # print("天干地支年"'\t''月''\t'' ''日''\t''     ''时辰''\t''节气')
    # print(' ''%s%s年''\t''  ''%s%s月''\t''%s%s日''\t''%s%s时''\t''%s' % (
    # tg, dz, yuetiangan, yuedizhi, ritiangan, ridizhi, shichengtiangan, shichengdizhi, JQ))
    # 重新计算年干
    shijianniangengxin = year
    jieqinianganjisuanlist = ["小寒", "大寒", "立春", "雨水", "惊蛰", "春分",
                              "清明", "谷雨", "立夏", "小满", "芒种", "夏至",
                              "小暑", "大暑", "立秋", "处暑", "白露", "秋分",
                              "寒露", "霜降", "立冬", "小雪", "大雪", "冬至"]
    for i in range(0, 24):
        if JQ == jieqinianganjisuanlist[i]:
            jieqi_nianganjisuan_index = i
    if jieqi_nianganjisuan_index <= 1:
        shijianniangengxin = shijianniangengxin - 1
    elif jieqi_nianganjisuan_index == 23:
        if month == 1:
            shijianniangengxin = shijianniangengxin - 1
    else:
        shijianniangengxin = shijianniangengxin
    a_tiangan = (shijianniangengxin - 3 - 1) % 10
    a_dizhi = (shijianniangengxin - 3 - 1) % 12
    tg = Tiangan[a_tiangan]
    dz = Dizhi[a_dizhi]
    tianganyue1 = ['甲', '己']
    tg1yue = ['丙', '丁', '戊', '己', '庚', '辛', '壬', '癸', '甲', '乙']
    tg1shicheng = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
    tianganyue2 = ['乙', '庚']
    tg2yue = ['戊', '己', '庚', '辛', '壬', '癸', '甲', '乙', '丙', '丁']
    tg2shicheng = ['丙', '丁', '戊', '己', '庚', '辛', '壬', '癸', '甲', '乙']
    tianganyue3 = ['丙', '辛']
    tg3yue = ['庚', '辛', '壬', '癸', '甲', '乙', '丙', '丁', '戊', '己']
    tg3shicheng = ['戊', '己', '庚', '辛', '壬', '癸', '甲', '乙', '丙', '丁']
    tianganyue4 = ['丁', '壬']
    tg4yue = ['壬', '癸', '甲', '乙', '丙', '丁', '戊', '己', '庚', '辛']
    tg4shicheng = ['庚', '辛', '壬', '癸', '甲', '乙', '丙', '丁', '戊', '己']
    tianganyue5 = ['戊', '癸']
    tg5yue = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
    tg5shicheng = ['壬', '癸', '甲', '乙', '丙', '丁', '戊', '己', '庚', '辛']
    yuetiangan = "甲"  # 初始化
    if tg in tianganyue1:
        yuetiangan = tg1yue[(shijianyue - 1) % 10]
    elif tg in tianganyue2:
        yuetiangan = tg2yue[(shijianyue - 1) % 10]
    elif tg in tianganyue3:
        yuetiangan = tg3yue[(shijianyue - 1) % 10]
    elif tg in tianganyue4:
        yuetiangan = tg4yue[(shijianyue - 1) % 10]
    elif tg in tianganyue5:
        yuetiangan = tg5yue[(shijianyue - 1) % 10]
    Yuedizhi = ['寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥', '子', '丑']
    yuedizhi = Yuedizhi[shijianyue - 1]

    # 以上为计算天干地支年和月
    # 以下为计算天干地支日
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
        index = 0
        if year == 1900:
            index = 0
        else:
            for i in range(1900, year):
                if calendar.isleap(i):
                    index = index + 6
                else:
                    index = index + 5
        ganzhi_tian_gan_index = (base_tian_gan_index + index) % 10
        ganzhi_di_zhi_index = (base_di_zhi_index + index) % 12
        tian_gan_char = tian_gan[ganzhi_tian_gan_index]
        di_zhi_char = di_zhi[ganzhi_di_zhi_index]
        return tian_gan_char, di_zhi_char, ganzhi_tian_gan_index, ganzhi_di_zhi_index

    ydgz = calculate_ganzhiyuandan(year)
    yuandan_ganzhi = ydgz[0] + ydgz[1]
    tiangan_index = [-1, 0, -2, -1, -1, 0, 0, 1, 2, 2, 3, 3]
    dizhi_index = [-1, 6, 10, 5, -1, 6, 0, 7, 2, 8, 3, 9]
    if year % 100 == 0 and year % 400 != 0 or year % 100 != 0 and year % 4 != 0:
        ritiangan_index = (ydgz[2] + 1 + day + tiangan_index[month - 1]) % 10
        ridizhi_index = (ydgz[3] + 1 + day + dizhi_index[month - 1]) % 12
    else:
        if month == 1 or month == 2:
            ritiangan_index = (ydgz[2] + 1 + day + tiangan_index[month - 1]) % 10
            ridizhi_index = (ydgz[3] + 1 + day + dizhi_index[month - 1]) % 12
        else:
            ritiangan_index = (ydgz[2] + 1 + day + tiangan_index[month - 1]) % 10 + 1
            ridizhi_index = (ydgz[3] + 1 + day + dizhi_index[month - 1]) % 12 + 1
    ritiangan = Tiangan[ritiangan_index - 1]
    ridizhi = Dizhi[ridizhi_index - 1]
    # 以下为计算天干地支时辰
    hour_to_dizhi = {}  # 创建一个空字典
    for i in range(0, 24):  # 循环1到24小时
        if i == 23 or i == 0:
            x = 1
        else:
            x = i + 2
        dizhi_index = (x - 1) // 2 % 12
        dizhiindex = Dizhi[dizhi_index]
        hour_to_dizhi[i] = dizhiindex
    for i in hour_to_dizhi:
        if hour == i:
            shichengdizhi = hour_to_dizhi[i]
            break
        else:
            continue
    p = 0
    for i in range(0, len(Dizhi)):
        if Dizhi[i] == shichengdizhi:
            p = i
            break
        else:
            continue
    if ritiangan in tianganyue1:
        shichengtiangan = tg1shicheng[p % 10]
    elif ritiangan in tianganyue2:
        shichengtiangan = tg2shicheng[p % 10]
    elif ritiangan in tianganyue3:
        shichengtiangan = tg3shicheng[p % 10]
    elif ritiangan in tianganyue4:
        shichengtiangan = tg4shicheng[p % 10]
    elif ritiangan in tianganyue5:
        shichengtiangan = tg5shicheng[p % 10]
    # print("输入日期的节气为：%s"%(JQ))
    # print("天干地支年"'\t''月''\t'' ''日''\t''     ''时辰''\t''节气')
    # print(' ''%s%s年''\t''  ''%s%s月''\t''%s%s日''\t''%s%s时''\t''%s' % (
    # tg, dz, yuetiangan, yuedizhi, ritiangan, ridizhi, shichengtiangan, shichengdizhi, JQ))
    # 第一步：定局
    # 以下为计算元日
    # 上元日列表
    SYR = [
        "甲子", "乙丑", "丙寅", "丁卯", "戊辰",
        "己卯", "庚辰", "辛巳", "壬午", "癸未",
        "甲午", "乙未", "丙申", "丁酉", "戊戌",
        "己酉", "庚戌", "辛亥", "壬子", "癸丑"
    ]

    # 中元日列表
    ZYR = [
        "己巳", "庚午", "辛未", "壬申", "癸酉",
        "甲申", "乙酉", "丙戌", "丁亥", "戊子",
        "己亥", "庚子", "辛丑", "壬寅", "癸卯",
        "甲寅", "乙卯", "丙辰", "丁巳", "戊午"
    ]

    # 下元日列表
    XYR = [
        "甲戌", "乙亥", "丙子", "丁丑", "戊寅",
        "己丑", "庚寅", "辛卯", "壬辰", "癸巳",
        "甲辰", "乙巳", "丙午", "丁未", "戊申",
        "己未", "庚申", "辛酉", "壬戌", "癸亥"
    ]
    i = ritiangan + ridizhi
    if i in SYR:
        yuanri = "上元"
    elif i in ZYR:
        yuanri = "中元"
    elif i in XYR:
        yuanri = "下元"
    # 计算太阳历下的干支月
    JQLIEBIAO = ["立春", "雨水", "惊蛰", "春分", "清明", "谷雨", "立夏", "小满", "芒种",
                 "夏至",
                 "小暑",
                 "大暑", "立秋", "处暑", "白露", "秋分", "寒露", "霜降", "立冬", "小雪",
                 "大雪",
                 "冬至",
                 "小寒", "大寒"]
    for i in range(0, 24):
        if JQLIEBIAO[i] == JQ:
            if i % 2 == 0:
                shijianyuegengxin = (i + 2) // 2
            else:
                shijianyuegengxin = (i + 1) // 2
            break
        else:
            continue
    if tg in tianganyue1:
        yuetiangangengxin = tg1yue[(shijianyuegengxin - 1) % 10]
    elif tg in tianganyue2:
        yuetiangangengxin = tg2yue[(shijianyuegengxin - 1) % 10]
    elif tg in tianganyue3:
        yuetiangangengxin = tg3yue[(shijianyuegengxin - 1) % 10]
    elif tg in tianganyue4:
        yuetiangangengxin = tg4yue[(shijianyuegengxin - 1) % 10]
    elif tg in tianganyue5:
        yuetiangangengxin = tg5yue[(shijianyuegengxin - 1) % 10]
    yuedizhigengxin = Yuedizhi[shijianyuegengxin - 1]
    shigan = []
    shigan.append(shichengtiangan)
    shigan.append(shichengdizhi)
    # 计算阴阳遁
    YD = 'yangdun'
    jieqiYangD = ["冬至", "小寒", "大寒", "立春", "雨水", "惊蛰", "春分", "清明", "谷雨",
                  "立夏",
                  "小满", "芒种"]
    jieqiYinD = ["夏至", "小暑", "大暑", "立秋", "处暑", "白露", "秋分", "寒露", "霜降", "立冬",
                 "小雪",
                 "大雪"]
    if JQ in jieqiYangD:
        YD = 'yangdun'
    else:
        YD = 'yindun'
    yangdunqiju = {
        '冬至上元': '坎一', '冬至中元': '兑七', '冬至下元': '巽四',
        '小寒上元': '坤二', '小寒中元': '艮八', '小寒下元': '中五',
        '大寒上元': '震三', '大寒中元': '离九', '大寒下元': '乾六',
        '立春上元': '艮八', '立春中元': '中五', '立春下元': '坤二',
        '雨水上元': '离九', '雨水中元': '乾六', '雨水下元': '震三',
        '惊蛰上元': '坎一', '惊蛰中元': '兑七', '惊蛰下元': '巽四',
        '春分上元': '震三', '春分中元': '离九', '春分下元': '乾六',
        '清明上元': '巽四', '清明中元': '坎一', '清明下元': '兑七',
        '谷雨上元': '中五', '谷雨中元': '坤二', '谷雨下元': '艮八',
        '立夏上元': '巽四', '立夏中元': '坎一', '立夏下元': '兑七',
        '小满上元': '中五', '小满中元': '坤二', '小满下元': '艮八',
        '芒种上元': '乾六', '芒种中元': '震三', '芒种下元': '离九'
    }
    yindunqiju = {
        '夏至上元': '离九', '夏至中元': '震三', '夏至下元': '乾六',
        '小暑上元': '艮八', '小暑中元': '坤二', '小暑下元': '中五',
        '大暑上元': '兑七', '大暑中元': '坎一', '大暑下元': '巽四',
        '立秋上元': '坤二', '立秋中元': '中五', '立秋下元': '艮八',
        '处暑上元': '坎一', '处暑中元': '巽四', '处暑下元': '兑七',
        '白露上元': '离九', '白露中元': '震三', '白露下元': '乾六',
        '秋分上元': '兑七', '秋分中元': '坎一', '秋分下元': '巽四',
        '寒露上元': '乾六', '寒露中元': '离九', '寒露下元': '震三',
        '霜降上元': '中五', '霜降中元': '艮八', '霜降下元': '坤二',
        '立冬上元': '乾六', '立冬中元': '离九', '立冬下元': '震三',
        '小雪上元': '中五', '小雪中元': '艮八', '小雪下元': '坤二',
        '大雪上元': '巽四', '大雪中元': '兑七', '大雪下元': '坎一'
    }
    qiju_index = JQ + yuanri
    if YD == 'yangdun':
        for key in yangdunqiju:
            if key == qiju_index:
                qiju = yangdunqiju[key]
                break
            else:
                continue
    elif YD == 'yindun':
        for key in yindunqiju:
            if key == qiju_index:
                qiju = yindunqiju[key]
                break
            else:
                continue
    gonghao = {'坎一': 0, '坤二': 1, '震三': 2, '巽四': 3, '中五': 4, '乾六': 5, '兑七': 6,
               '艮八': 7,
               '离九': 8}
    sanqiliuyi = ['甲子戊', '甲戌己', '甲申庚', '甲午辛', '甲辰壬', '甲寅癸', '丁', '丙', '乙']
    kanyishuchukuang = {}
    kunershuchukuang = {}
    zhensanshuchukuang = {}
    xunsishuchukuang = {}
    zhongwushuchukuang = {}
    qianliushuchukuang = {}
    duiqishuchukuang = {}
    genbashuchukuang = {}
    lijuishuchukuang = {}
    dingweigong = [kanyishuchukuang, kunershuchukuang, zhensanshuchukuang, xunsishuchukuang,
                   zhongwushuchukuang, qianliushuchukuang, duiqishuchukuang, genbashuchukuang,
                   lijuishuchukuang]
    dingweigongzhuangdong = [kanyishuchukuang, genbashuchukuang, zhensanshuchukuang,
                             xunsishuchukuang,
                             lijuishuchukuang, kunershuchukuang, duiqishuchukuang,
                             qianliushuchukuang]
    for key in gonghao:
        if qiju == key:
            dingweigong_index = gonghao[key]
            break
        else:
            continue
    sanqiliuyigong = {}
    if YD == 'yangdun':
        if dingweigong_index == 4:
            dipangong = dingweigong[dingweigong_index]
            dipangong["地盘"] = sanqiliuyi[0]
            sanqiliuyigong[4] = sanqiliuyi[0]
        elif dingweigong_index == 1:
            sanqiliuyigong[1] = sanqiliuyi[0]
        else:
            dipangong = dingweigong[dingweigong_index]
            dipangong["地盘"] = sanqiliuyi[0]
            sanqiliuyigong[dingweigong_index] = sanqiliuyi[0]
        for i in range(1, 9):
            dingweigong_index = dingweigong_index + 1
            if dingweigong_index == 4:
                dipangong = dingweigong[dingweigong_index]
                dipangong["地盘"] = sanqiliuyi[i]
                sanqiliuyigong[4] = sanqiliuyi[i]
            elif dingweigong_index == 1:
                sanqiliuyigong[1] = sanqiliuyi[i]
            elif dingweigong_index >= 9:
                dingweigong_index = dingweigong_index - 9
                if dingweigong_index == 4:
                    dipangong = dingweigong[dingweigong_index]
                    dipangong["地盘"] = sanqiliuyi[i]
                    sanqiliuyigong[4] = sanqiliuyi[i]
                elif dingweigong_index == 1:
                    sanqiliuyigong[1] = sanqiliuyi[i]
                else:
                    dipangong = dingweigong[dingweigong_index]
                    dipangong["地盘"] = sanqiliuyi[i]
                    sanqiliuyigong[dingweigong_index] = sanqiliuyi[i]
            else:
                dipangong = dingweigong[dingweigong_index]
                dipangong["地盘"] = sanqiliuyi[i]
                sanqiliuyigong[dingweigong_index] = sanqiliuyi[i]
    elif YD == 'yindun':
        if dingweigong_index == 4:
            dipangong = dingweigong[dingweigong_index]
            dipangong["地盘"] = sanqiliuyi[0]
            sanqiliuyigong[4] = sanqiliuyi[0]
        elif dingweigong_index == 1:
            sanqiliuyigong[1] = sanqiliuyi[0]
        else:
            dipangong = dingweigong[dingweigong_index]
            dipangong["地盘"] = sanqiliuyi[0]
            sanqiliuyigong[dingweigong_index] = sanqiliuyi[0]
        for i in range(1, 9):
            dingweigong_index = dingweigong_index - 1
            if dingweigong_index == 4:
                dipangong = dingweigong[dingweigong_index]
                dipangong["地盘"] = sanqiliuyi[i]
                sanqiliuyigong[4] = sanqiliuyi[i]
            elif dingweigong_index == 1:
                sanqiliuyigong[1] = sanqiliuyi[i]
            elif dingweigong_index < 0:
                dingweigong_index = dingweigong_index + 9
                if dingweigong_index == 4:
                    dipangong = dingweigong[dingweigong_index]
                    dipangong["地盘"] = sanqiliuyi[i]
                    sanqiliuyigong[4] = sanqiliuyi[i]
                elif dingweigong_index == 1:
                    sanqiliuyigong[1] = sanqiliuyi[i]
                else:
                    dipangong = dingweigong[dingweigong_index]
                    dipangong["地盘"] = sanqiliuyi[i]
                    sanqiliuyigong[dingweigong_index] = sanqiliuyi[i]
            else:
                dipangong = dingweigong[dingweigong_index]
                dipangong["地盘"] = sanqiliuyi[i]
                sanqiliuyigong[dingweigong_index] = sanqiliuyi[i]
    kunersanqiliuyi = f'{sanqiliuyigong[1]}\n{sanqiliuyigong[4]}'
    kunershuchukuang["地盘"] = kunersanqiliuyi

    if YD == 'yangdun':
        YD = '阳遁'
    else:
        YD = '阴遁'
    list1jiazi = ["甲子", "乙丑", "丙寅", "丁卯", "戊辰", "己巳", "庚午", "辛未", "壬申",
                  "癸酉"]
    list2jiaxu = ["甲戌", "乙亥", "丙子", "丁丑", "戊寅", "己卯", "庚辰", "辛巳", "壬午",
                  "癸未"]
    list3jiashen = ["甲申", "乙酉", "丙戌", "丁亥", "戊子", "己丑", "庚寅", "辛卯", "壬辰",
                    "癸巳"]
    list4jiawu = ["甲午", "乙未", "丙申", "丁酉", "戊戌", "己亥", "庚子", "辛丑", "壬寅",
                  "癸卯"]
    list5jiachen = ["甲辰", "乙巳", "丙午", "丁未", "戊申", "己酉", "庚戌", "辛亥", "壬子",
                    "癸丑"]
    list6jiayin = ["甲寅", "乙卯", "丙辰", "丁巳", "戊午", "己未", "庚申", "辛酉", "壬戌",
                   "癸亥"]
    shichengganzhi = shichengtiangan + shichengdizhi
    if shichengganzhi in list1jiazi:
        xuntou = "甲子戊"
        xuntouzi = '甲子'
    elif shichengganzhi in list2jiaxu:
        xuntou = "甲戌己"
        xuntouzi = '甲戌'
    elif shichengganzhi in list3jiashen:
        xuntou = "甲申庚"
        xuntouzi = '甲申'
    elif shichengganzhi in list4jiawu:
        xuntou = "甲午辛"
        xuntouzi = '甲午'
    elif shichengganzhi in list5jiachen:
        xuntou = "甲辰壬"
        xuntouzi = '甲辰'
    elif shichengganzhi in list6jiayin:
        xuntou = "甲寅癸"
        xuntouzi = "甲寅"
    xuntouzu = ["甲子", '甲戌', '甲申', '甲午', '甲辰', '甲寅']
    xuntouzu2 = ['戊', '己', '庚', '辛', '壬', '癸', '丁', '丙', '乙']
    if shichengtiangan == "甲":
        for i in range(0, 6):
            if shichengganzhi == xuntouzu[i]:
                sanqiliuyilaoda = sanqiliuyi[i]
                break
            else:
                continue
    else:
        for i in range(0, 9):
            if shichengtiangan == xuntouzu2[i]:
                sanqiliuyilaoda = sanqiliuyi[i]
    for key in sanqiliuyigong:
        if xuntou == sanqiliuyigong[key]:
            xuntougonghao = key
            break
        else:
            continue
    for key in sanqiliuyigong:
        if sanqiliuyilaoda == sanqiliuyigong[key]:
            sanqiliuyilaodagonghao = key
            break
        else:
            continue
    BASHEN = ["值符", "螣蛇", "太阴", "六合", "白虎", "玄武", "九地", "九天"]
    if xuntougonghao == 4:
        if sanqiliuyilaodagonghao == 4:
            a = 3
            if YD == '阳遁':
                for i in range(0, 8):
                    if dingweigong[1] == dingweigongzhuangdong[i]:
                        xuntougonghaozhuangdong = i
                        break
                    else:
                        continue
                for i in range(0, 8):
                    if dingweigong[1] == dingweigongzhuangdong[i]:
                        sanqiliuyilaodagonghaozhuandong = i
                        break
                    else:
                        continue

                sanqiliuyizhuangdonglist = []
                for i in range(xuntougonghaozhuangdong, 8 + xuntougonghaozhuangdong):
                    if (i % 8) == 5:
                        text = dingweigongzhuangdong[i % 8]["地盘"]
                        text_lines = text.split('\n')
                        multi_line_text = f'{text_lines[0]}\n{text_lines[1]}'

                        sanqiliuyizhuangdonglist.append(multi_line_text)
                    else:
                        sanqiliuyizhuangdongshuri = dingweigongzhuangdong[i % 8]["地盘"]
                        sanqiliuyizhuangdonglist.append(sanqiliuyizhuangdongshuri)
                for i in range(sanqiliuyilaodagonghaozhuandong,
                               sanqiliuyilaodagonghaozhuandong + 8):
                    dingweigongzhuangdong[i % 8]["八神"] = BASHEN[i - sanqiliuyilaodagonghaozhuandong]
                    dingweigongzhuangdong[i % 8]["天盘"] = sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]
            else:
                for i in range(0, 8):
                    if dingweigong[1] == dingweigongzhuangdong[i]:
                        xuntougonghaozhuangdong = i
                        break
                    else:
                        continue
                for i in range(0, 8):
                    if dingweigong[1] == dingweigongzhuangdong[i]:
                        sanqiliuyilaodagonghaozhuandong = i
                        break
                    else:
                        continue
                BASHENNI = []
                BASHENNI.append('值符')
                listdaoxu = [-1, -2, -3, -4, -5, -6, -7]
                for i in range(0, 7):
                    BASHENNI.append(BASHEN[listdaoxu[i]])
                sanqiliuyizhuangdonglist = []
                for i in range(xuntougonghaozhuangdong, 8 + xuntougonghaozhuangdong):
                    if (i % 8) == 5:
                        text = dingweigongzhuangdong[i % 8]["地盘"]
                        text_lines = text.split('\n')
                        multi_line_text = f'{text_lines[0]}\n{text_lines[1]}'
                        sanqiliuyizhuangdonglist.append(multi_line_text)
                    else:
                        sanqiliuyizhuangdongshuri = dingweigongzhuangdong[i % 8]["地盘"]
                        sanqiliuyizhuangdonglist.append(sanqiliuyizhuangdongshuri)
                for i in range(sanqiliuyilaodagonghaozhuandong,
                               sanqiliuyilaodagonghaozhuandong + 8):
                    dingweigongzhuangdong[i % 8]["八神"] = BASHENNI[i - sanqiliuyilaodagonghaozhuandong]
                    dingweigongzhuangdong[i % 8]["天盘"] = sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]
        else:
            a = 0
            if YD == '阳遁':
                for i in range(0, 8):
                    if dingweigong[1] == dingweigongzhuangdong[i]:
                        xuntougonghaozhuangdong = i
                        break
                    else:
                        continue
                for i in range(0, 8):
                    if dingweigong[sanqiliuyilaodagonghao] == dingweigongzhuangdong[i]:
                        sanqiliuyilaodagonghaozhuandong = i
                        break
                    else:
                        continue

                sanqiliuyizhuangdonglist = []
                for i in range(xuntougonghaozhuangdong, 8 + xuntougonghaozhuangdong):
                    if (i % 8) == 5:
                        text = dingweigongzhuangdong[i % 8]["地盘"]
                        text_lines = text.split('\n')
                        multi_line_text = f'{text_lines[0]}\n{text_lines[1]}'
                        sanqiliuyizhuangdonglist.append(multi_line_text)
                    else:
                        sanqiliuyizhuangdongshuri = dingweigongzhuangdong[i % 8]["地盘"]
                        sanqiliuyizhuangdonglist.append(sanqiliuyizhuangdongshuri)
                for i in range(sanqiliuyilaodagonghaozhuandong, sanqiliuyilaodagonghaozhuandong + 8):
                    dingweigongzhuangdong[i % 8]["八神"] = BASHEN[i - sanqiliuyilaodagonghaozhuandong]
                    dingweigongzhuangdong[i % 8]["天盘"] = sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]
            else:
                for i in range(0, 8):
                    if dingweigong[1] == dingweigongzhuangdong[i]:
                        xuntougonghaozhuangdong = i
                        break
                    else:
                        continue
                for i in range(0, 8):
                    if dingweigong[sanqiliuyilaodagonghao] == dingweigongzhuangdong[i]:
                        sanqiliuyilaodagonghaozhuandong = i
                        break
                    else:
                        continue
                BASHENNI = []
                BASHENNI.append('值符')
                listdaoxu = [-1, -2, -3, -4, -5, -6, -7]
                for i in range(0, 7):
                    BASHENNI.append(BASHEN[listdaoxu[i]])
                sanqiliuyizhuangdonglist = []
                for i in range(xuntougonghaozhuangdong, 8 + xuntougonghaozhuangdong):
                    if (i % 8) == 5:
                        text = dingweigongzhuangdong[i % 8]["地盘"]
                        text_lines = text.split('\n')
                        multi_line_text = f'{text_lines[0]}\n{text_lines[1]}'
                        sanqiliuyizhuangdonglist.append(multi_line_text)
                    else:
                        sanqiliuyizhuangdongshuri = dingweigongzhuangdong[i % 8]["地盘"]
                        sanqiliuyizhuangdonglist.append(sanqiliuyizhuangdongshuri)
                for i in range(sanqiliuyilaodagonghaozhuandong, sanqiliuyilaodagonghaozhuandong + 8):
                    dingweigongzhuangdong[i % 8]["八神"] = BASHENNI[i - sanqiliuyilaodagonghaozhuandong]
                    dingweigongzhuangdong[i % 8]["天盘"] = sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]

    else:
        if sanqiliuyilaodagonghao == 4:
            a = 8
            if YD == '阳遁':
                for i in range(0, 8):
                    if dingweigong[xuntougonghao] == dingweigongzhuangdong[i]:
                        xuntougonghaozhuangdong = i
                        break
                    else:
                        continue
                for i in range(0, 8):
                    if dingweigong[1] == dingweigongzhuangdong[i]:
                        sanqiliuyilaodagonghaozhuandong = i
                        break
                    else:
                        continue

                sanqiliuyizhuangdonglist = []
                for i in range(xuntougonghaozhuangdong, 8 + xuntougonghaozhuangdong):
                    if (i % 8) == 5:
                        text = dingweigongzhuangdong[i % 8]["地盘"]
                        text_lines = text.split('\n')
                        multi_line_text = f'{text_lines[0]}\n{text_lines[1]}'
                        sanqiliuyizhuangdonglist.append(multi_line_text)
                    else:
                        sanqiliuyizhuangdongshuri = dingweigongzhuangdong[i % 8]["地盘"]
                        sanqiliuyizhuangdonglist.append(sanqiliuyizhuangdongshuri)

                for i in range(sanqiliuyilaodagonghaozhuandong, sanqiliuyilaodagonghaozhuandong + 8):
                    dingweigongzhuangdong[i % 8]["八神"] = BASHEN[i - sanqiliuyilaodagonghaozhuandong]
                    dingweigongzhuangdong[i % 8]["天盘"] = sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]
            else:
                for i in range(0, 8):
                    if dingweigong[xuntougonghao] == dingweigongzhuangdong[i]:
                        xuntougonghaozhuangdong = i
                        break
                    else:
                        continue
                for i in range(0, 8):
                    if dingweigong[1] == dingweigongzhuangdong[i]:
                        sanqiliuyilaodagonghaozhuandong = i
                        break
                    else:
                        continue
                BASHENNI = []
                BASHENNI.append('值符')
                listdaoxu = [-1, -2, -3, -4, -5, -6, -7]
                for i in range(0, 7):
                    BASHENNI.append(BASHEN[listdaoxu[i]])
                sanqiliuyizhuangdonglist = []
                for i in range(xuntougonghaozhuangdong, 8 + xuntougonghaozhuangdong):
                    if (i % 8) == 5:
                        text = dingweigongzhuangdong[i % 8]["地盘"]
                        text_lines = text.split('\n')
                        multi_line_text = f'{text_lines[0]}\n{text_lines[1]}'
                        sanqiliuyizhuangdonglist.append(multi_line_text)
                    else:
                        sanqiliuyizhuangdongshuri = dingweigongzhuangdong[i % 8]["地盘"]
                        sanqiliuyizhuangdonglist.append(sanqiliuyizhuangdongshuri)

                for i in range(sanqiliuyilaodagonghaozhuandong, sanqiliuyilaodagonghaozhuandong + 8):
                    dingweigongzhuangdong[i % 8]["八神"] = BASHENNI[i - sanqiliuyilaodagonghaozhuandong]
                    dingweigongzhuangdong[i % 8]["天盘"] = sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]

        else:
            a = 19
            if YD == '阳遁':
                for i in range(0, 8):
                    if dingweigong[xuntougonghao] == dingweigongzhuangdong[i]:
                        xuntougonghaozhuangdong = i
                        break
                    else:
                        continue
                for i in range(0, 8):
                    if dingweigong[sanqiliuyilaodagonghao] == dingweigongzhuangdong[i]:
                        sanqiliuyilaodagonghaozhuandong = i
                        break
                    else:
                        continue

                sanqiliuyizhuangdonglist = []
                for i in range(xuntougonghaozhuangdong, 8 + xuntougonghaozhuangdong):
                    if (i % 8) == 5:
                        text = dingweigongzhuangdong[i % 8]["地盘"]
                        text_lines = text.split('\n')
                        multi_line_text = f'{text_lines[0]}\n{text_lines[1]}'
                        sanqiliuyizhuangdonglist.append(multi_line_text)
                    else:
                        sanqiliuyizhuangdongshuri = dingweigongzhuangdong[i % 8]["地盘"]
                        sanqiliuyizhuangdonglist.append(sanqiliuyizhuangdongshuri)
                for i in range(sanqiliuyilaodagonghaozhuandong, sanqiliuyilaodagonghaozhuandong + 8):
                    dingweigongzhuangdong[i % 8]["八神"] = BASHEN[i - sanqiliuyilaodagonghaozhuandong]
                    dingweigongzhuangdong[i % 8]["天盘"] = sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]
            else:
                for i in range(0, 8):
                    if dingweigong[xuntougonghao] == dingweigongzhuangdong[i]:
                        xuntougonghaozhuangdong = i
                        break
                    else:
                        continue
                for i in range(0, 8):
                    if dingweigong[sanqiliuyilaodagonghao] == dingweigongzhuangdong[i]:
                        sanqiliuyilaodagonghaozhuandong = i
                        break
                    else:
                        continue
                BASHENNI = []
                BASHENNI.append('值符')
                listdaoxu = [-1, -2, -3, -4, -5, -6, -7]
                for i in range(0, 7):
                    BASHENNI.append(BASHEN[listdaoxu[i]])
                sanqiliuyizhuangdonglist = []
                for i in range(xuntougonghaozhuangdong, 8 + xuntougonghaozhuangdong):
                    if (i % 8) == 5:
                        text = dingweigongzhuangdong[i % 8]["地盘"]
                        text_lines = text.split('\n')
                        multi_line_text = f'{text_lines[0]}\n{text_lines[1]}'
                        sanqiliuyizhuangdonglist.append(multi_line_text)
                    else:
                        sanqiliuyizhuangdongshuri = dingweigongzhuangdong[i % 8]["地盘"]
                        sanqiliuyizhuangdonglist.append(sanqiliuyizhuangdongshuri)

                for i in range(sanqiliuyilaodagonghaozhuandong, sanqiliuyilaodagonghaozhuandong + 8):
                    dingweigongzhuangdong[i % 8]["八神"] = BASHENNI[i - sanqiliuyilaodagonghaozhuandong]
                    dingweigongzhuangdong[i % 8]["天盘"] = sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]
    # 排九星So easy
    JUIXING = ["天蓬", "天芮", "天冲", "天辅", "天禽", "天心", "天柱", "天任", "天英"]
    JUIXINGSHURU = []
    for i in range(xuntougonghao, xuntougonghao + 9):
        JUIXINGSHURU.append(JUIXING[i % 9])
    for i in range(sanqiliuyilaodagonghao, sanqiliuyilaodagonghao + 9):
        if i % 9 == 4:
            dingweigong[i % 9]["九星"] = JUIXINGSHURU[i - sanqiliuyilaodagonghao]
        else:
            dingweigong[i % 9]["九星"] = JUIXINGSHURU[i - sanqiliuyilaodagonghao]
    # 八门入宫
    BAMEN = ["休", "生", "伤", "杜", "景", "死", "惊", "开"]
    if xuntouzi == list1jiazi[0]:
        DizhiZ = list1jiazi
    elif xuntouzi == list2jiaxu[0]:
        DizhiZ = list2jiaxu
    elif xuntouzi == list3jiashen[0]:
        DizhiZ = list3jiashen
    elif xuntouzi == list4jiawu[0]:
        DizhiZ = list4jiawu
    elif xuntouzi == list5jiachen[0]:
        DizhiZ = list5jiachen
    elif xuntouzi == list6jiayin[0]:
        DizhiZ = list6jiayin
    for i in range(0, 10):
        if DizhiZ[i] == shichengganzhi:
            shichengdizhiindex = i
            break
        else:
            continue
    for i in range(0, 10):
        if DizhiZ[i] == xuntouzi:
            xuntouzi1index = i
            break
        else:
            continue
    zhishiluozhongwugongjikungong=0
    if xuntougonghao == 4:

        b = 1

        shichengchazhi = abs(shichengdizhiindex - xuntouzi1index)
        if YD == '阳遁':
            zhishiweizhifeigongindex = (xuntougonghao + shichengchazhi) % 9
            if zhishiweizhifeigongindex == 4:
                zhishidingweizhuangdongindex = 5
                zhishiluozhongwugongjikungong = 5
            else:
                for i in range(0, 8):
                    if dingweigong[zhishiweizhifeigongindex] == dingweigongzhuangdong[i]:
                        zhishidingweizhuangdongindex = i
                        break
                    else:
                        continue


            zhishidingweilist = []
            BAMEN[5] = BAMEN[5] + "使"
            for i in range(5, 13):
                zhishidingweilist.append(BAMEN[i % 8])
            for i in range(zhishidingweizhuangdongindex, 8 + zhishidingweizhuangdongindex):
                dingweigongzhuangdong[i % 8]["八门"] = zhishidingweilist[i - zhishidingweizhuangdongindex]

        else:
            if xuntougonghao - shichengchazhi >= 0:
                zhishiweizhifeigongindex = xuntougonghao - shichengchazhi
            elif xuntougonghao - shichengchazhi < 0:
                zhishiweizhifeigongindex = xuntougonghao - shichengchazhi + 9
            zhishidingweilist = []
            if zhishiweizhifeigongindex == 4:
                zhishidingweizhuangdongindex = 5
                zhishiluozhongwugongjikungong = 5
            else:
                for i in range(0, 8):
                    if dingweigong[zhishiweizhifeigongindex] == dingweigongzhuangdong[i]:
                        zhishidingweizhuangdongindex = i
                        break
                    else:
                        continue

            zhishidingweilist = []
            BAMEN[5] = BAMEN[5] + "使"
            for i in range(5, 13):
                zhishidingweilist.append(BAMEN[i % 8])
            for i in range(zhishidingweizhuangdongindex, 8 + zhishidingweizhuangdongindex):
                dingweigongzhuangdong[i % 8]["八门"] = zhishidingweilist[i - zhishidingweizhuangdongindex]


    else:
        b = 4
        for i in range(0, 8):
            if dingweigong[xuntougonghao] == dingweigongzhuangdong[i]:
                xuntougonghaozhuangdong2 = i
                break
            else:
                continue

        shichengchazhi = abs(shichengdizhiindex - xuntouzi1index)
        if YD == '阳遁':
            zhishiweizhifeigongindex = (xuntougonghao + shichengchazhi) % 9
            if zhishiweizhifeigongindex == 4:
                zhishidingweizhuangdongindex = 5
                zhishiluozhongwugongjikungong = 5
            else:
                for i in range(0, 8):
                    if dingweigong[zhishiweizhifeigongindex] == dingweigongzhuangdong[i]:
                        zhishidingweizhuangdongindex = i
                        break
                    else:
                        continue

            zhishidingweilist = []
            BAMEN[xuntougonghaozhuangdong2] = BAMEN[xuntougonghaozhuangdong2] + "使"
            for i in range(xuntougonghaozhuangdong2, 8 + xuntougonghaozhuangdong2):
                zhishidingweilist.append(BAMEN[i % 8])
            for i in range(zhishidingweizhuangdongindex, 8 + zhishidingweizhuangdongindex):
                dingweigongzhuangdong[i % 8]["八门"] = zhishidingweilist[i - zhishidingweizhuangdongindex]
        else:
            if xuntougonghao - shichengchazhi >= 0:
                zhishiweizhifeigongindex = xuntougonghao - shichengchazhi
            elif xuntougonghao - shichengchazhi < 0:
                zhishiweizhifeigongindex = xuntougonghao - shichengchazhi + 9
            zhishidingweilist = []
            if zhishiweizhifeigongindex == 4:
                zhishidingweizhuangdongindex = 5
                zhishiluozhongwugongjikungong = 5
            else:
                for i in range(0, 8):
                    if dingweigong[zhishiweizhifeigongindex] == dingweigongzhuangdong[i]:
                        zhishidingweizhuangdongindex = i
                        break
                    else:
                        continue

            zhishidingweilist = []
            BAMEN[xuntougonghaozhuangdong2] = BAMEN[xuntougonghaozhuangdong2] + "使"
            for i in range(xuntougonghaozhuangdong2, 8 + xuntougonghaozhuangdong2):
                zhishidingweilist.append(BAMEN[i % 8])
            for i in range(zhishidingweizhuangdongindex, 8 + zhishidingweizhuangdongindex):
                dingweigongzhuangdong[i % 8]["八门"] = zhishidingweilist[i - zhishidingweizhuangdongindex]

    nianganzhi=tg+dz
    yueganzhi=yuetiangangengxin+yuedizhigengxin
    riganzhi=ritiangan+ridizhi
    for i in range(0, 9):
        if i == 4:
            pass
        else:
            bamenpanbiezhishi = dingweigong[i]["八门"]
            if "使" in bamenpanbiezhishi:
                zhishigongdingwei_index = i  # 这个编号代表值使所在宫的代号
    shichengganzhi=shichengtiangan+shichengdizhi
    yinyangdun_ganzhi=[YD,nianganzhi,yueganzhi,riganzhi,shichengganzhi,JQ,zhishigongdingwei_index,zhishiluozhongwugongjikungong,xuntou,qiju]
    nianyueriganzhi=f"{nianganzhi}年，{yueganzhi}月，{riganzhi}日"
    ff = yinyangdun_ganzhi[3]
    yd = yinyangdun_ganzhi[0]
    qiju = yinyangdun_ganzhi[9]
    yilingbalingju = f"{ff}-{yd}-{qiju}"
    print("--------进行中--------")
    return  dingweigong ,yinyangdun_ganzhi,nianyueriganzhi,yilingbalingju

