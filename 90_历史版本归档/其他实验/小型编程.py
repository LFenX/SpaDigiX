base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
# 访问数据文件的路径
image_path1 = os.path.join(base_path, 'JGT.png')
ye = self.time_entry1.input_text.text()
mo = self.time_entry2.input_text.text()
da = self.time_entry3.input_text.text()
ho = self.time_entry4.input_text.text()
mi = self.time_entry5.input_text.text()
if ye == "" and mo == "" and da == "" :
    reply = QMessageBox()
    style_sheet = """
                           QMessageBox {
                               background-color: rgb(173, 216, 230);
                           }
                           QLabel {
                               margin-top: 12px;
                               color: red;
                               font-size: 13px;
                               text-align: center;
                           }
                           QPushButton {
                               background-color: #FF5733;
                               color: white;
                               border: none;
                               padding: 10px 20px;
                               border-radius: 5px;
                           }
                           QPushButton:hover {
                               background-color: #FF844D;
                           }
                       """
    kai_ti_font = QFont("KaiTi", 13)
    # 将文本字体设置为楷体
    reply.setFont(kai_ti_font)
    reply.setWindowIcon(QIcon(image_path1))
    reply.setStyleSheet("QLabel { alignment: AlignCenter; }")
    reply.setStyleSheet(style_sheet)
    reply.setIcon(QMessageBox.Icon.Critical)
    reply.setWindowTitle("温馨提示")
    reply.setText('施主，”巧妇难为无米之炊“，您得输入点东西我才能为您运算啊。')
    reply.setStandardButtons(QMessageBox.StandardButton.Ok)
    reply.exec()  # 阻塞应用程序直到用户关闭警告框
elif ye == "" or mo == "" or da == "" or ho == "" or mi == "":
    # 用户输入的时间信息不符合格式，显示警告
    reply = QMessageBox()
    style_sheet = """
               QMessageBox {
                   background-color: rgb(173, 216, 230);
               }
               QLabel {
                   margin-top: 12px;
                   color: red;
                   font-size: 13px;
                   text-align: center;
               }
               QPushButton {
                   background-color: #FF5733;
                   color: white;
                   border: none;
                   padding: 10px 20px;
                   border-radius: 5px;
               }
               QPushButton:hover {
                   background-color: #FF844D;
               }
           """
    kai_ti_font = QFont("KaiTi", 13)
    reply.setWindowIcon(QIcon(image_path1))
    # 将文本字体设置为楷体
    reply.setFont(kai_ti_font)
    reply.setStyleSheet("QLabel { alignment: AlignCenter; }")
    reply.setStyleSheet(style_sheet)
    reply.setIcon(QMessageBox.Icon.Critical)
    reply.setWindowTitle("温馨提示")
    reply.setText("您输入的时间信息格式不正确哟，请完整输入所有时间信息。")
    reply.setStandardButtons(QMessageBox.StandardButton.Ok)
    reply.exec()  # 阻塞应用程序直到用户关闭警告框
else:
    user_time = ye + '年' + mo + '月' + da + '日' + ho + '时' + mi + '分'
    # 在这里添加根据用户输入生成信息的算法
    info = f"你输入的时间是：{user_time}"
    Tiangan = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
    Dizhi = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
    shengxiao = ['鼠', '牛', '虎', '兔', '龙', '蛇', '马', '羊', '猴', '鸡', '狗', '猪']
    # 给定的字符串
    input_str = user_time

    # 使用正则表达式匹配日期时间信息
    pattern = re.compile(r'(\d{0,5})年(\d{1,3})月(\d{1,3})[号日]?(\d{1,3})[点时]?(\d{1,3})分?')
    matches = pattern.search(input_str)

    if matches:
        yearr = matches.group(1)
        monthh = matches.group(2)
        dayy = matches.group(3)
        hourr = matches.group(4)
        minutee = matches.group(5)
        # 将提取的数字转换为整数
        yearr = int(yearr)
        monthh = int(monthh)
        dayy = int(dayy)
        hourr = int(hourr)
        minutee = int(minutee)
        yee = str(yearr)
        moo = str(monthh)
        daa = str(dayy)
        hoo = str(hourr)
        mii = str(minutee)
        if calendar.isleap(yearr):
            # 闰年的月份及对应的天数
            NIANFEN = "闰年"
            days_in_month = {
                1: 31,  # 1月有31天
                2: 29,  # 2月有28天
                3: 31,  # 3月有31天
                4: 30,  # 4月有30天
                5: 31,  # 5月有31天
                6: 30,  # 6月有30天
                7: 31,  # 7月有31天
                8: 31,  # 8月有31天
                9: 30,  # 9月有30天
                10: 31,  # 10月有31天
                11: 30,  # 11月有30天
                12: 31  # 12月有31天
            }
        else:
            # 平年的月份及对应的天数
            NIANFEN = '平年'
            days_in_month = {
                1: 31,  # 1月有31天
                2: 28,  # 2月有28天
                3: 31,  # 3月有31天
                4: 30,  # 4月有30天
                5: 31,  # 5月有31天
                6: 30,  # 6月有30天
                7: 31,  # 7月有31天
                8: 31,  # 8月有31天
                9: 30,  # 9月有30天
                10: 31,  # 10月有31天
                11: 30,  # 11月有30天
                12: 31  # 12月有31天
            }
        # 添加额外的检查以确保数值在有效范围内

        if yearr >= 1900 and yearr <= 2100 and 1 <= monthh <= 12 and 1 <= dayy <= 31 and 0 <= hourr <= 23 and 0 <= minutee <= 60:
            if yearr == 1900 and monthh == 1:
                reply = QMessageBox()
                style_sheet = """
                                       QMessageBox {
                                           background-color: rgb(173, 216, 230);
                                       }
                                       QLabel {
                                           margin-top: 12px;
                                           color: red;
                                           font-size: 13px;
                                           text-align: center;
                                       }
                                       QPushButton {
                                           background-color: #FF5733;
                                           color: white;
                                           border: none;
                                           padding: 10px 20px;
                                           border-radius: 5px;
                                       }
                                       QPushButton:hover {
                                           background-color: #FF844D;
                                       }
                                   """
                kai_ti_font = QFont("KaiTi", 13)
                # 将文本字体设置为楷体
                reply.setWindowIcon(QIcon(image_path1))
                reply.setFont(kai_ti_font)
                reply.setStyleSheet("QLabel { alignment: AlignCenter; }")
                reply.setStyleSheet(style_sheet)
                reply.setIcon(QMessageBox.Icon.Critical)
                reply.setWindowTitle("温馨提示")
                reply.setText("1900年2月1号0时0分以前的时间点不支持哦，重新选个时间点吧。")
                reply.setStandardButtons(QMessageBox.StandardButton.Ok)
                reply.exec()  # 阻塞应用程序直到用户关闭警告框
            else:
                if dayy > days_in_month[monthh]:
                    reply = QMessageBox()
                    style_sheet = """
                                                       QMessageBox {
                                                           background-color: rgb(173, 216, 230);
                                                       }
                                                       QLabel {
                                                           margin-top: 12px;
                                                           color: red;
                                                           font-size: 13px;
                                                           text-align: center;
                                                       }
                                                       QPushButton {
                                                           background-color: #FF5733;
                                                           color: white;
                                                           border: none;
                                                           padding: 10px 20px;
                                                           border-radius: 5px;
                                                       }
                                                       QPushButton:hover {
                                                           background-color: #FF844D;
                                                       }
                                                   """
                    kai_ti_font = QFont("KaiTi", 13)
                    reply.setWindowIcon(QIcon(image_path1))
                    # 将文本字体设置为楷体
                    reply.setFont(kai_ti_font)
                    reply.setStyleSheet("QLabel { alignment: AlignCenter; }")
                    reply.setStyleSheet(style_sheet)
                    reply.setIcon(QMessageBox.Icon.Critical)
                    reply.setWindowTitle("温馨提示")
                    if monthh == 2:
                        reply.setText("%s的%s月没有第%s天哦，重新输一下吧!" % (NIANFEN, str(monthh), str(dayy)))
                        reply.setStandardButtons(QMessageBox.StandardButton.Ok)
                        reply.exec()  # 阻塞应用程序直到用户关闭警告框
                    else:
                        reply.setText("%s月可没有第%s天哦，重新输一遍吧!" % (str(monthh), str(dayy)))
                        reply.setStandardButtons(QMessageBox.StandardButton.Ok)
                        reply.exec()  # 阻塞应用程序直到用户关闭警告框
                else:
                    year = yearr
                    month = monthh
                    day = dayy
                    hour = hourr
                    minute = minutee
                    # 注释掉的为起始输入时间数据为阴历
                    # shijiannian=int(input("请输入阴历年份："))
                    # shijianyue=int(input("请输入阴历月份："))
                    # shijianri=int(input("请输入阴历日期："))
                    # lunar_date= ZhDate(shijiannian,shijianyue,shijianri)
                    # Solar_date=lunar_date.to_datetime()
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
                    a_tiangan = (shijiannian - 3 - 1) % 10
                    a_dizhi = (shijiannian - 3 - 1) % 12
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
                    '''
                    该方法也可行但是下一种更加简单易懂，不过这一种算法速度会快那么一点点，但不多
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
                        year_diff = year - base_year
                        a = year_diff // 4
                        b = year_diff % 4

                        if a > 25 and a % 25 != 0:
                            lf = calculate_ganzhiyuandan(year - (a - 25 * (a // 25)) * 4 - b)
                            base_tian_gan_index = lf[2]
                            base_di_zhi_index = lf[3]
                            year_diff = (a - 25 * (a // 25)) * 4 + b
                            c = year - (a - 25 * (a // 25)) * 4 - b
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
                        elif a > 25 and a % 25 == 0:
                            lf = calculate_ganzhiyuandan(year - 100)
                            base_tian_gan_index = lf[2]
                            base_di_zhi_index = lf[3]
                            year_diff = 100
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
                            if b == 0:
                                # 计算元旦日期的天干地支索引
                                ganzhi_tian_gan_index = (base_tian_gan_index + 21 * a - 1) % len(tian_gan)
                                ganzhi_di_zhi_index = (base_di_zhi_index + 21 * a - 1) % len(di_zhi)
                            else:
                                ganzhi_tian_gan_index = (base_tian_gan_index + 21 * a + b * 5) % len(tian_gan)
                                ganzhi_di_zhi_index = (base_di_zhi_index + 21 * a + b * 5) % len(di_zhi)
                        # 获取对应的天干和地支字符
                        tian_gan_char = tian_gan[ganzhi_tian_gan_index]
                        di_zhi_char = di_zhi[ganzhi_di_zhi_index]
                        return tian_gan_char, di_zhi_char, ganzhi_tian_gan_index, ganzhi_di_zhi_index
    '''


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
                    v = datetime.datetime(year, month, day, hour, 0, 0)
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
                    JQLIEBIAO = ["立春", "雨水", "惊蛰", "春分", "清明", "谷雨", "立夏", "小满", "芒种", "夏至",
                                 "小暑",
                                 "大暑", "立秋", "处暑", "白露", "秋分", "寒露", "霜降", "立冬", "小雪", "大雪",
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
                    sanqiliuyi1 = ['甲子戊', '甲戌己', '甲申庚', '甲午辛', '甲辰壬', '甲寅癸', '丁', '丙', '乙']
                    max_length = len(max(sanqiliuyi1, key=len))  # 找到最长元素的长度
                    sanqiliuyi = [
                        (item.center(max_length) if item not in ['丁', '丙', '乙'] else (
                                '\u3000' + item + '\u3000'))
                        for item in sanqiliuyi1]
                    print(sanqiliuyi)
                    kanyishuchukuang = ['output_2_1_1', 'output_2_1_2', 'output_2_1_3', 'output_2_1_4',
                                        'output_2_1_5']
                    kunershuchukuang = ['output_0_2_1', 'output_0_2_2', 'output_0_2_3', 'output_0_2_4',
                                        'output_0_2_5']
                    zhensanshuchukuang = ['output_1_0_1', 'output_1_0_2', 'output_1_0_3', 'output_1_0_4',
                                          'output_1_0_5']
                    xunsishuchukuang = ['output_0_0_1', 'output_0_0_2', 'output_0_0_3', 'output_0_0_4',
                                        'output_0_0_5']
                    zhongwushuchukuang = ['output_1_1_1', 'output_1_1_2']
                    qianliushuchukuang = ['output_2_2_1', 'output_2_2_2', 'output_2_2_3', 'output_2_2_4',
                                          'output_2_2_5']
                    duiqishuchukuang = ['output_1_2_1', 'output_1_2_2', 'output_1_2_3', 'output_1_2_4',
                                        'output_1_2_5']
                    genbashuchukuang = ['output_2_0_1', 'output_2_0_2', 'output_2_0_3', 'output_2_0_4',
                                        'output_2_0_5']
                    lijuishuchukuang = ['output_0_1_1', 'output_0_1_2', 'output_0_1_3', 'output_0_1_4',
                                        'output_0_1_5']
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
                            dingweijushuchukuangMC = dingweigong[dingweigong_index][1]
                            self.output_boxes[dingweijushuchukuangMC].setText('%s' % (sanqiliuyi[0]))
                            sanqiliuyigong[4] = sanqiliuyi[0]
                        elif dingweigong_index == 1:
                            sanqiliuyigong[1] = sanqiliuyi[0]
                        else:
                            dingweijushuchukuangMC = dingweigong[dingweigong_index][3]
                            self.output_boxes[dingweijushuchukuangMC].setText('%s' % (sanqiliuyi[0]))
                            sanqiliuyigong[dingweigong_index] = sanqiliuyi[0]
                        for i in range(1, 9):
                            dingweigong_index = dingweigong_index + 1
                            if dingweigong_index == 4:
                                dingweijushuchukuangMC = dingweigong[dingweigong_index][1]
                                self.output_boxes[dingweijushuchukuangMC].setText('%s' % (sanqiliuyi[i]))
                                sanqiliuyigong[4] = sanqiliuyi[i]
                            elif dingweigong_index == 1:
                                sanqiliuyigong[1] = sanqiliuyi[i]
                            elif dingweigong_index >= 9:
                                dingweigong_index = dingweigong_index - 9
                                if dingweigong_index == 4:
                                    dingweijushuchukuangMC = dingweigong[dingweigong_index][1]
                                    self.output_boxes[dingweijushuchukuangMC].setText('%s' % (sanqiliuyi[i]))
                                    sanqiliuyigong[4] = sanqiliuyi[i]
                                elif dingweigong_index == 1:
                                    sanqiliuyigong[1] = sanqiliuyi[i]
                                else:
                                    dingweijushuchukuangMC = dingweigong[dingweigong_index][3]
                                    self.output_boxes[dingweijushuchukuangMC].setText('%s' % (sanqiliuyi[i]))
                                    sanqiliuyigong[dingweigong_index] = sanqiliuyi[i]
                            else:
                                dingweijushuchukuangMC = dingweigong[dingweigong_index][3]
                                self.output_boxes[dingweijushuchukuangMC].setText('%s' % (sanqiliuyi[i]))
                                sanqiliuyigong[dingweigong_index] = sanqiliuyi[i]
                    elif YD == 'yindun':
                        if dingweigong_index == 4:
                            dingweijushuchukuangMC = dingweigong[dingweigong_index][1]
                            self.output_boxes[dingweijushuchukuangMC].setText('%s' % (sanqiliuyi[0]))
                            sanqiliuyigong[4] = sanqiliuyi[0]
                        elif dingweigong_index == 1:
                            sanqiliuyigong[1] = sanqiliuyi[0]
                        else:
                            dingweijushuchukuangMC = dingweigong[dingweigong_index][3]
                            self.output_boxes[dingweijushuchukuangMC].setText('%s' % (sanqiliuyi[0]))
                            sanqiliuyigong[dingweigong_index] = sanqiliuyi[0]
                        for i in range(1, 9):
                            dingweigong_index = dingweigong_index - 1
                            if dingweigong_index == 4:
                                dingweijushuchukuangMC = dingweigong[dingweigong_index][1]
                                self.output_boxes[dingweijushuchukuangMC].setText('%s' % (sanqiliuyi[i]))
                                sanqiliuyigong[4] = sanqiliuyi[i]
                            elif dingweigong_index == 1:
                                sanqiliuyigong[1] = sanqiliuyi[i]
                            elif dingweigong_index < 0:
                                dingweigong_index = dingweigong_index + 9
                                if dingweigong_index == 4:
                                    dingweijushuchukuangMC = dingweigong[dingweigong_index][1]
                                    self.output_boxes[dingweijushuchukuangMC].setText('%s' % (sanqiliuyi[i]))
                                    sanqiliuyigong[4] = sanqiliuyi[i]
                                elif dingweigong_index == 1:
                                    sanqiliuyigong[1] = sanqiliuyi[i]
                                else:
                                    dingweijushuchukuangMC = dingweigong[dingweigong_index][3]
                                    self.output_boxes[dingweijushuchukuangMC].setText('%s' % (sanqiliuyi[i]))
                                    sanqiliuyigong[dingweigong_index] = sanqiliuyi[i]
                            else:
                                dingweijushuchukuangMC = dingweigong[dingweigong_index][3]
                                self.output_boxes[dingweijushuchukuangMC].setText('%s' % (sanqiliuyi[i]))
                                sanqiliuyigong[dingweigong_index] = sanqiliuyi[i]
                    kunersanqiliuyi = f'{sanqiliuyigong[1]}\n{sanqiliuyigong[4]}'
                    self.output_boxes['output_0_2_4'].setText("%s" % (kunersanqiliuyi))
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
                    font = QFont('SimSun', 11)
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
                                        text_edit = self.output_boxes[dingweigongzhuangdong[i % 8][3]]
                                        text = text_edit.toPlainText()
                                        text_lines = text.split('\n')
                                        multi_line_text = f'{text_lines[0]}\n{text_lines[1]}'
                                        # '\n'.join(text_lines)
                                        # f'{text_lines[0]}\n{text_lines[1]}'
                                        # 将这个变量添加到列表中
                                        sanqiliuyizhuangdonglist.append(multi_line_text)
                                    else:
                                        sanqiliuyizhuangdongshuri = self.output_boxes[
                                            dingweigongzhuangdong[i % 8][3]].text()
                                        sanqiliuyizhuangdonglist.append(sanqiliuyizhuangdongshuri)
                                    # sanqiliuyizhuangdongshuri=self.output_boxes[dingweigongzhuangdong[int(a)][3]].text()
                                    # sanqiliuyizhuangdonglist.append(sanqiliuyizhuangdongshuri)
                                '''
                                print(sanqiliuyizhuangdonglist)
                                print(dingweigongzhuangdong)
                                print(sanqiliuyigong)
                                print(sanqiliuyilaodagonghaozhuandong)
                                print(xuntougonghao)
                                print(sanqiliuyilaodagonghao)
                               '''
                                for i in range(sanqiliuyilaodagonghaozhuandong,
                                               sanqiliuyilaodagonghaozhuandong + 8):
                                    self.output_boxes[dingweigongzhuangdong[i % 8][0]].setText(
                                        '%s' % (BASHEN[i - sanqiliuyilaodagonghaozhuandong]))
                                    self.output_boxes[dingweigongzhuangdong[i % 8][0]].setAlignment(
                                        Qt.AlignmentFlag.AlignCenter)
                                    if len(sanqiliuyizhuangdonglist[
                                               i - sanqiliuyilaodagonghaozhuandong]) == 5 or len(
                                        sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]) == 7:
                                        sanqiliuyizhuangdongshuchugonghao = i % 8
                                        biaoshishuanghangwenben = sanqiliuyizhuangdongshuchugonghao
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setPlainText(
                                            '%s' % (
                                                sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]))
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setAlignment(
                                            Qt.AlignmentFlag.AlignCenter)
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setFont(
                                            font)
                                    elif len(sanqiliuyizhuangdonglist[
                                                 i - sanqiliuyilaodagonghaozhuandong]) == 3 or len(
                                        sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]) == 1:
                                        sanqiliuyizhuangdongshuchugonghao = i % 8
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setPlainText(
                                            '%s' % (
                                                sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]))
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setAlignment(
                                            Qt.AlignmentFlag.AlignCenter)
                                        style = "padding-top: 7.3px; border: 2px solid black;"
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setStyleSheet(
                                            style)
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setFont(
                                            font)
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
                                        text_edit = self.output_boxes[dingweigongzhuangdong[i % 8][3]]
                                        text = text_edit.toPlainText()
                                        text_lines = text.split('\n')
                                        multi_line_text = f'{text_lines[0]}\n{text_lines[1]}'
                                        # '\n'.join(text_lines)
                                        # f'{text_lines[0]}\n{text_lines[1]}'
                                        # 将这个变量添加到列表中
                                        sanqiliuyizhuangdonglist.append(multi_line_text)
                                    else:
                                        sanqiliuyizhuangdongshuri = self.output_boxes[
                                            dingweigongzhuangdong[i % 8][3]].text()
                                        sanqiliuyizhuangdonglist.append(sanqiliuyizhuangdongshuri)
                                    # sanqiliuyizhuangdongshuri=self.output_boxes[dingweigongzhuangdong[int(a)][3]].text()
                                    # sanqiliuyizhuangdonglist.append(sanqiliuyizhuangdongshuri)
                                '''
                                print(sanqiliuyizhuangdonglist)
                                print(dingweigongzhuangdong)
                                print(sanqiliuyigong)
                                print(sanqiliuyilaodagonghaozhuandong)
                                print(xuntougonghao)
                                print(sanqiliuyilaodagonghao)
                               '''
                                for i in range(sanqiliuyilaodagonghaozhuandong,
                                               sanqiliuyilaodagonghaozhuandong + 8):
                                    self.output_boxes[dingweigongzhuangdong[i % 8][0]].setText(
                                        '%s' % (BASHENNI[i - sanqiliuyilaodagonghaozhuandong]))
                                    self.output_boxes[dingweigongzhuangdong[i % 8][0]].setAlignment(
                                        Qt.AlignmentFlag.AlignCenter)
                                    if len(sanqiliuyizhuangdonglist[
                                               i - sanqiliuyilaodagonghaozhuandong]) == 5 or len(
                                        sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]) == 7:
                                        sanqiliuyizhuangdongshuchugonghao = i % 8
                                        biaoshishuanghangwenben = sanqiliuyizhuangdongshuchugonghao
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setPlainText(
                                            '%s' % (
                                                sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]))
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setAlignment(
                                            Qt.AlignmentFlag.AlignCenter)
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setFont(
                                            font)
                                    elif len(sanqiliuyizhuangdonglist[
                                                 i - sanqiliuyilaodagonghaozhuandong]) == 3 or len(
                                        sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]) == 1:
                                        sanqiliuyizhuangdongshuchugonghao = i % 8
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setPlainText(
                                            '%s' % (
                                                sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]))
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setAlignment(
                                            Qt.AlignmentFlag.AlignCenter)
                                        style = "padding-top: 7.3px; border: 2px solid black;"
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setStyleSheet(
                                            style)
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setFont(
                                            font)

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
                                        text_edit = self.output_boxes[dingweigongzhuangdong[i % 8][3]]
                                        text = text_edit.toPlainText()
                                        text_lines = text.split('\n')
                                        multi_line_text = f'{text_lines[0]}\n{text_lines[1]}'
                                        # '\n'.join(text_lines)
                                        # f'{text_lines[0]}\n{text_lines[1]}'
                                        # 将这个变量添加到列表中
                                        sanqiliuyizhuangdonglist.append(multi_line_text)
                                    else:
                                        sanqiliuyizhuangdongshuri = self.output_boxes[
                                            dingweigongzhuangdong[i % 8][3]].text()
                                        sanqiliuyizhuangdonglist.append(sanqiliuyizhuangdongshuri)
                                    # sanqiliuyizhuangdongshuri=self.output_boxes[dingweigongzhuangdong[int(a)][3]].text()
                                    # sanqiliuyizhuangdonglist.append(sanqiliuyizhuangdongshuri)
                                '''
                                print(sanqiliuyizhuangdonglist)
                                print(dingweigongzhuangdong)
                                print(sanqiliuyigong)
                                print(sanqiliuyilaodagonghaozhuandong)
                                print(xuntougonghao)
                                print(sanqiliuyilaodagonghao)
                               '''
                                for i in range(sanqiliuyilaodagonghaozhuandong,
                                               sanqiliuyilaodagonghaozhuandong + 8):
                                    self.output_boxes[dingweigongzhuangdong[i % 8][0]].setText(
                                        '%s' % (BASHEN[i - sanqiliuyilaodagonghaozhuandong]))
                                    self.output_boxes[dingweigongzhuangdong[i % 8][0]].setAlignment(
                                        Qt.AlignmentFlag.AlignCenter)
                                    if len(sanqiliuyizhuangdonglist[
                                               i - sanqiliuyilaodagonghaozhuandong]) == 5 or len(
                                        sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]) == 7:
                                        sanqiliuyizhuangdongshuchugonghao = i % 8
                                        biaoshishuanghangwenben = sanqiliuyizhuangdongshuchugonghao
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setPlainText(
                                            '%s' % (
                                                sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]))
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setAlignment(
                                            Qt.AlignmentFlag.AlignCenter)
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setFont(
                                            font)
                                    elif len(sanqiliuyizhuangdonglist[
                                                 i - sanqiliuyilaodagonghaozhuandong]) == 3 or len(
                                        sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]) == 1:
                                        sanqiliuyizhuangdongshuchugonghao = i % 8
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setPlainText(
                                            '%s' % (
                                                sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]))
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setAlignment(
                                            Qt.AlignmentFlag.AlignCenter)
                                        style = "padding-top: 7.3px; border: 2px solid black;"
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setStyleSheet(
                                            style)
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setFont(
                                            font)
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
                                        text_edit = self.output_boxes[dingweigongzhuangdong[i % 8][3]]
                                        text = text_edit.toPlainText()
                                        text_lines = text.split('\n')
                                        multi_line_text = f'{text_lines[0]}\n{text_lines[1]}'
                                        # '\n'.join(text_lines)
                                        # f'{text_lines[0]}\n{text_lines[1]}'
                                        # 将这个变量添加到列表中
                                        sanqiliuyizhuangdonglist.append(multi_line_text)
                                    else:
                                        sanqiliuyizhuangdongshuri = self.output_boxes[
                                            dingweigongzhuangdong[i % 8][3]].text()
                                        sanqiliuyizhuangdonglist.append(sanqiliuyizhuangdongshuri)
                                    # sanqiliuyizhuangdongshuri=self.output_boxes[dingweigongzhuangdong[int(a)][3]].text()
                                    # sanqiliuyizhuangdonglist.append(sanqiliuyizhuangdongshuri)
                                '''
                                print(sanqiliuyizhuangdonglist)
                                print(dingweigongzhuangdong)
                                print(sanqiliuyigong)
                                print(sanqiliuyilaodagonghaozhuandong)
                                print(xuntougonghao)
                                print(sanqiliuyilaodagonghao)
                               '''
                                for i in range(sanqiliuyilaodagonghaozhuandong,
                                               sanqiliuyilaodagonghaozhuandong + 8):
                                    self.output_boxes[dingweigongzhuangdong[i % 8][0]].setText(
                                        '%s' % (BASHENNI[i - sanqiliuyilaodagonghaozhuandong]))
                                    self.output_boxes[dingweigongzhuangdong[i % 8][0]].setAlignment(
                                        Qt.AlignmentFlag.AlignCenter)
                                    if len(sanqiliuyizhuangdonglist[
                                               i - sanqiliuyilaodagonghaozhuandong]) == 5 or len(
                                        sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]) == 7:
                                        sanqiliuyizhuangdongshuchugonghao = i % 8
                                        biaoshishuanghangwenben = sanqiliuyizhuangdongshuchugonghao
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setPlainText(
                                            '%s' % (
                                                sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]))
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setAlignment(
                                            Qt.AlignmentFlag.AlignCenter)
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setFont(
                                            font)
                                    elif len(sanqiliuyizhuangdonglist[
                                                 i - sanqiliuyilaodagonghaozhuandong]) == 3 or len(
                                        sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]) == 1:
                                        sanqiliuyizhuangdongshuchugonghao = i % 8
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setPlainText(
                                            '%s' % (
                                                sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]))
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setAlignment(
                                            Qt.AlignmentFlag.AlignCenter)
                                        style = "padding-top: 7.3px; border: 2px solid black;"
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setStyleSheet(
                                            style)
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setFont(
                                            font)

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
                                        text_edit = self.output_boxes[dingweigongzhuangdong[i % 8][3]]
                                        text = text_edit.toPlainText()
                                        text_lines = text.split('\n')
                                        multi_line_text = f'{text_lines[0]}\n{text_lines[1]}'
                                        # '\n'.join(text_lines)
                                        # f'{text_lines[0]}\n{text_lines[1]}'
                                        # 将这个变量添加到列表中
                                        sanqiliuyizhuangdonglist.append(multi_line_text)
                                    else:
                                        sanqiliuyizhuangdongshuri = self.output_boxes[
                                            dingweigongzhuangdong[i % 8][3]].text()
                                        sanqiliuyizhuangdonglist.append(sanqiliuyizhuangdongshuri)
                                    # sanqiliuyizhuangdongshuri=self.output_boxes[dingweigongzhuangdong[int(a)][3]].text()
                                    # sanqiliuyizhuangdonglist.append(sanqiliuyizhuangdongshuri)
                                '''
                                print(sanqiliuyizhuangdonglist)
                                print(dingweigongzhuangdong)
                                print(sanqiliuyigong)
                                print(sanqiliuyilaodagonghaozhuandong)
                                print(xuntougonghao)
                                print(sanqiliuyilaodagonghao)
                               '''
                                for i in range(sanqiliuyilaodagonghaozhuandong,
                                               sanqiliuyilaodagonghaozhuandong + 8):
                                    self.output_boxes[dingweigongzhuangdong[i % 8][0]].setText(
                                        '%s' % (BASHEN[i - sanqiliuyilaodagonghaozhuandong]))
                                    self.output_boxes[dingweigongzhuangdong[i % 8][0]].setAlignment(
                                        Qt.AlignmentFlag.AlignCenter)
                                    if len(sanqiliuyizhuangdonglist[
                                               i - sanqiliuyilaodagonghaozhuandong]) == 5 or len(
                                        sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]) == 7:
                                        sanqiliuyizhuangdongshuchugonghao = i % 8
                                        biaoshishuanghangwenben = sanqiliuyizhuangdongshuchugonghao
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setPlainText(
                                            '%s' % (
                                                sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]))
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setAlignment(
                                            Qt.AlignmentFlag.AlignCenter)
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setFont(
                                            font)
                                    elif len(sanqiliuyizhuangdonglist[
                                                 i - sanqiliuyilaodagonghaozhuandong]) == 3 or len(
                                        sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]) == 1:
                                        sanqiliuyizhuangdongshuchugonghao = i % 8
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setPlainText(
                                            '%s' % (
                                                sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]))
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setAlignment(
                                            Qt.AlignmentFlag.AlignCenter)
                                        style = "padding-top: 7.3px; border: 2px solid black;"
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setStyleSheet(
                                            style)
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setFont(
                                            font)
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
                                        text_edit = self.output_boxes[dingweigongzhuangdong[i % 8][3]]
                                        text = text_edit.toPlainText()
                                        text_lines = text.split('\n')
                                        multi_line_text = f'{text_lines[0]}\n{text_lines[1]}'
                                        # '\n'.join(text_lines)
                                        # f'{text_lines[0]}\n{text_lines[1]}'
                                        # 将这个变量添加到列表中
                                        sanqiliuyizhuangdonglist.append(multi_line_text)
                                    else:
                                        sanqiliuyizhuangdongshuri = self.output_boxes[
                                            dingweigongzhuangdong[i % 8][3]].text()
                                        sanqiliuyizhuangdonglist.append(sanqiliuyizhuangdongshuri)
                                    # sanqiliuyizhuangdongshuri=self.output_boxes[dingweigongzhuangdong[int(a)][3]].text()
                                    # sanqiliuyizhuangdonglist.append(sanqiliuyizhuangdongshuri)
                                '''
                                print(sanqiliuyizhuangdonglist)
                                print(dingweigongzhuangdong)
                                print(sanqiliuyigong)
                                print(sanqiliuyilaodagonghaozhuandong)
                                print(xuntougonghao)
                                print(sanqiliuyilaodagonghao)
                               '''
                                for i in range(sanqiliuyilaodagonghaozhuandong,
                                               sanqiliuyilaodagonghaozhuandong + 8):
                                    self.output_boxes[dingweigongzhuangdong[i % 8][0]].setText(
                                        '%s' % (BASHENNI[i - sanqiliuyilaodagonghaozhuandong]))
                                    self.output_boxes[dingweigongzhuangdong[i % 8][0]].setAlignment(
                                        Qt.AlignmentFlag.AlignCenter)
                                    if len(sanqiliuyizhuangdonglist[
                                               i - sanqiliuyilaodagonghaozhuandong]) == 5 or len(
                                        sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]) == 7:
                                        sanqiliuyizhuangdongshuchugonghao = i % 8
                                        biaoshishuanghangwenben = sanqiliuyizhuangdongshuchugonghao
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setPlainText(
                                            '%s' % (
                                                sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]))
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setAlignment(
                                            Qt.AlignmentFlag.AlignCenter)
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setFont(
                                            font)
                                    elif len(sanqiliuyizhuangdonglist[
                                                 i - sanqiliuyilaodagonghaozhuandong]) == 3 or len(
                                        sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]) == 1:
                                        sanqiliuyizhuangdongshuchugonghao = i % 8
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setPlainText(
                                            '%s' % (
                                                sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]))
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setAlignment(
                                            Qt.AlignmentFlag.AlignCenter)
                                        style = "padding-top: 7.3px; border: 2px solid black;"
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setStyleSheet(
                                            style)
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setFont(
                                            font)

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
                                        text_edit = self.output_boxes[dingweigongzhuangdong[i % 8][3]]
                                        text = text_edit.toPlainText()
                                        text_lines = text.split('\n')
                                        multi_line_text = f'{text_lines[0]}\n{text_lines[1]}'
                                        # '\n'.join(text_lines)
                                        # f'{text_lines[0]}\n{text_lines[1]}'
                                        # 将这个变量添加到列表中
                                        sanqiliuyizhuangdonglist.append(multi_line_text)
                                    else:
                                        sanqiliuyizhuangdongshuri = self.output_boxes[
                                            dingweigongzhuangdong[i % 8][3]].text()
                                        sanqiliuyizhuangdonglist.append(sanqiliuyizhuangdongshuri)
                                    # sanqiliuyizhuangdongshuri=self.output_boxes[dingweigongzhuangdong[int(a)][3]].text()
                                    # sanqiliuyizhuangdonglist.append(sanqiliuyizhuangdongshuri)
                                '''
                                print(sanqiliuyizhuangdonglist)
                                print(dingweigongzhuangdong)
                                print(sanqiliuyigong)
                                print(sanqiliuyilaodagonghaozhuandong)
                                print(xuntougonghao)
                                print(sanqiliuyilaodagonghao)
                               '''
                                for i in range(sanqiliuyilaodagonghaozhuandong,
                                               sanqiliuyilaodagonghaozhuandong + 8):
                                    self.output_boxes[dingweigongzhuangdong[i % 8][0]].setText(
                                        '%s' % (BASHEN[i - sanqiliuyilaodagonghaozhuandong]))
                                    self.output_boxes[dingweigongzhuangdong[i % 8][0]].setAlignment(
                                        Qt.AlignmentFlag.AlignCenter)
                                    if len(sanqiliuyizhuangdonglist[
                                               i - sanqiliuyilaodagonghaozhuandong]) == 5 or len(
                                        sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]) == 7:
                                        sanqiliuyizhuangdongshuchugonghao = i % 8
                                        biaoshishuanghangwenben = sanqiliuyizhuangdongshuchugonghao
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setPlainText(
                                            '%s' % (
                                                sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]))
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setAlignment(
                                            Qt.AlignmentFlag.AlignCenter)
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setFont(
                                            font)
                                    elif len(sanqiliuyizhuangdonglist[
                                                 i - sanqiliuyilaodagonghaozhuandong]) == 3 or len(
                                        sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]) == 1:
                                        sanqiliuyizhuangdongshuchugonghao = i % 8
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setPlainText(
                                            '%s' % (
                                                sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]))
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setAlignment(
                                            Qt.AlignmentFlag.AlignCenter)
                                        style = "padding-top: 7.3px; border: 2px solid black;"
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setStyleSheet(
                                            style)
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setFont(
                                            font)
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
                                        text_edit = self.output_boxes[dingweigongzhuangdong[i % 8][3]]
                                        text = text_edit.toPlainText()
                                        text_lines = text.split('\n')
                                        multi_line_text = f'{text_lines[0]}\n{text_lines[1]}'
                                        # '\n'.join(text_lines)
                                        # f'{text_lines[0]}\n{text_lines[1]}'
                                        # 将这个变量添加到列表中
                                        sanqiliuyizhuangdonglist.append(multi_line_text)
                                    else:
                                        sanqiliuyizhuangdongshuri = self.output_boxes[
                                            dingweigongzhuangdong[i % 8][3]].text()
                                        sanqiliuyizhuangdonglist.append(sanqiliuyizhuangdongshuri)
                                    # sanqiliuyizhuangdongshuri=self.output_boxes[dingweigongzhuangdong[int(a)][3]].text()
                                    # sanqiliuyizhuangdonglist.append(sanqiliuyizhuangdongshuri)
                                '''
                                print(sanqiliuyizhuangdonglist)
                                print(dingweigongzhuangdong)
                                print(sanqiliuyigong)
                                print(sanqiliuyilaodagonghaozhuandong)
                                print(xuntougonghao)
                                print(sanqiliuyilaodagonghao)
                               '''
                                for i in range(sanqiliuyilaodagonghaozhuandong,
                                               sanqiliuyilaodagonghaozhuandong + 8):
                                    self.output_boxes[dingweigongzhuangdong[i % 8][0]].setText(
                                        '%s' % (BASHENNI[i - sanqiliuyilaodagonghaozhuandong]))
                                    self.output_boxes[dingweigongzhuangdong[i % 8][0]].setAlignment(
                                        Qt.AlignmentFlag.AlignCenter)
                                    if len(sanqiliuyizhuangdonglist[
                                               i - sanqiliuyilaodagonghaozhuandong]) == 5 or len(
                                        sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]) == 7:
                                        sanqiliuyizhuangdongshuchugonghao = i % 8
                                        biaoshishuanghangwenben = sanqiliuyizhuangdongshuchugonghao
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setPlainText(
                                            '%s' % (
                                                sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]))
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setAlignment(
                                            Qt.AlignmentFlag.AlignCenter)
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setFont(
                                            font)
                                    elif len(sanqiliuyizhuangdonglist[
                                                 i - sanqiliuyilaodagonghaozhuandong]) == 3 or len(
                                        sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]) == 1:
                                        sanqiliuyizhuangdongshuchugonghao = i % 8
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setPlainText(
                                            '%s' % (
                                                sanqiliuyizhuangdonglist[i - sanqiliuyilaodagonghaozhuandong]))
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setAlignment(
                                            Qt.AlignmentFlag.AlignCenter)
                                        style = "padding-top: 7.3px; border: 2px solid black;"
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setStyleSheet(
                                            style)
                                        self.output_boxes[
                                            dingweigongzhuangdong[sanqiliuyizhuangdongshuchugonghao][
                                                4]].setFont(
                                            font)

                    # 排九星So easy
                    JUIXING = ["天蓬", "天芮", "天冲", "天辅", "天禽", "天心", "天柱", "天任", "天英"]
                    JUIXINGSHURU = []
                    for i in range(xuntougonghao, xuntougonghao + 9):
                        JUIXINGSHURU.append(JUIXING[i % 9])
                    for i in range(sanqiliuyilaodagonghao, sanqiliuyilaodagonghao + 9):
                        if i % 9 == 4:
                            self.output_boxes[dingweigong[i % 9][0]].setText(
                                '%s' % (JUIXINGSHURU[i - sanqiliuyilaodagonghao]))
                            self.output_boxes[dingweigong[i % 9][0]].setAlignment(Qt.AlignmentFlag.AlignCenter)
                        else:
                            self.output_boxes[dingweigong[i % 9][2]].setText(
                                '%s' % (JUIXINGSHURU[i - sanqiliuyilaodagonghao]))
                            self.output_boxes[dingweigong[i % 9][2]].setAlignment(Qt.AlignmentFlag.AlignCenter)

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
                    if xuntougonghao == 4:
                        b = 1
                        shichengchazhi = abs(shichengdizhiindex - xuntouzi1index)
                        if YD == '阳遁':
                            zhishiweizhifeigongindex = (xuntougonghao + shichengchazhi) % 9
                            if zhishiweizhifeigongindex == 4:
                                zhishidingweizhuangdongindex = 5
                            else:
                                for i in range(0, 8):
                                    if dingweigong[zhishiweizhifeigongindex] == dingweigongzhuangdong[i]:
                                        zhishidingweizhuangdongindex = i
                                        break
                                    else:
                                        continue
                                zhishidingweilist = []
                                BAMEN[5] = BAMEN[5] + "(使)"
                                for i in range(5, 13):
                                    zhishidingweilist.append(BAMEN[i % 8])
                                for i in range(zhishidingweizhuangdongindex, 8 + zhishidingweizhuangdongindex):
                                    self.output_boxes[dingweigongzhuangdong[i % 8][1]].setText(
                                        "%s" % (zhishidingweilist[i - zhishidingweizhuangdongindex]))
                        else:
                            if xuntougonghao - shichengchazhi >= 0:
                                zhishiweizhifeigongindex = xuntougonghao - shichengchazhi
                            elif xuntougonghao - shichengchazhi < 0:
                                zhishiweizhifeigongindex = xuntougonghao - shichengchazhi + 9
                            zhishidingweilist = []
                            if zhishiweizhifeigongindex == 4:
                                zhishidingweizhuangdongindex = 5
                            else:
                                for i in range(0, 8):
                                    if dingweigong[zhishiweizhifeigongindex] == dingweigongzhuangdong[i]:
                                        zhishidingweizhuangdongindex = i
                                        break
                                    else:
                                        continue

                            zhishidingweilist = []
                            BAMEN[5] = BAMEN[5] + "(使)"
                            for i in range(5, 13):
                                zhishidingweilist.append(BAMEN[i % 8])
                            for i in range(zhishidingweizhuangdongindex, 8 + zhishidingweizhuangdongindex):
                                self.output_boxes[dingweigongzhuangdong[i % 8][1]].setText(
                                    "%s" % (zhishidingweilist[i - zhishidingweizhuangdongindex]))


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
                            else:
                                for i in range(0, 8):
                                    if dingweigong[zhishiweizhifeigongindex] == dingweigongzhuangdong[i]:
                                        zhishidingweizhuangdongindex = i
                                        break
                                    else:
                                        continue

                            zhishidingweilist = []
                            BAMEN[xuntougonghaozhuangdong2] = BAMEN[xuntougonghaozhuangdong2] + "(使)"
                            for i in range(xuntougonghaozhuangdong2, 8 + xuntougonghaozhuangdong2):
                                zhishidingweilist.append(BAMEN[i % 8])
                            for i in range(zhishidingweizhuangdongindex, 8 + zhishidingweizhuangdongindex):
                                self.output_boxes[dingweigongzhuangdong[i % 8][1]].setText(
                                    "%s" % (zhishidingweilist[i - zhishidingweizhuangdongindex]))
                        else:
                            if xuntougonghao - shichengchazhi >= 0:
                                zhishiweizhifeigongindex = xuntougonghao - shichengchazhi
                            elif xuntougonghao - shichengchazhi < 0:
                                zhishiweizhifeigongindex = xuntougonghao - shichengchazhi + 9
                            zhishidingweilist = []
                            if zhishiweizhifeigongindex == 4:
                                zhishidingweizhuangdongindex = 5
                            else:
                                for i in range(0, 8):
                                    if dingweigong[zhishiweizhifeigongindex] == dingweigongzhuangdong[i]:
                                        zhishidingweizhuangdongindex = i
                                        break
                                    else:
                                        continue

                            zhishidingweilist = []
                            BAMEN[xuntougonghaozhuangdong2] = BAMEN[xuntougonghaozhuangdong2] + "(使)"
                            for i in range(xuntougonghaozhuangdong2, 8 + xuntougonghaozhuangdong2):
                                zhishidingweilist.append(BAMEN[i % 8])
                            for i in range(zhishidingweizhuangdongindex, 8 + zhishidingweizhuangdongindex):
                                self.output_boxes[dingweigongzhuangdong[i % 8][1]].setText(
                                    "%s" % (zhishidingweilist[i - zhishidingweizhuangdongindex]))

                    # print(b)
                    print(a)
                    print('旬头:%s' % (xuntou))
                    print('三奇六仪老大：%s' % (sanqiliuyilaoda))
                    # print(xuntougonghao)
                    # print(sanqiliuyilaodagonghao)
                    # print(xuntou)
                    # print(sanqiliuyilaoda)
                    # print(sanqiliuyigong)
                    # print(YD)
                    # print(dingweigong_index)
                    # print(dingweijushuchukuangMC)
                    info = f"你输入的时间是：{user_time}"
                    self.lunar_output1.setText(' %s%s年(属%s,%s)''\t''%s%s月''\t''%s%s日''\t''%s%s时' % (
                        tg, dz, shengxiaonian, NIANFEN, yuetiangangengxin, yuedizhigengxin, ritiangan, ridizhi,
                        shichengtiangan,
                        shichengdizhi))
                    self.lunar_output2.setText('%s''\t''%s' % (JQ, YD))
                    self.lunar_output3.setText('%s日' % (yuanri))
                    self.info_label.setText(info)
                    font = QFont('SimSun', 11)
                    self.output_boxes['output_0_2_4'].setAlignment(Qt.AlignmentFlag.AlignCenter)