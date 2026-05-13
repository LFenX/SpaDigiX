import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QGridLayout, QMessageBox
from PyQt6.QtWidgets import QHBoxLayout
from PyQt6.QtWidgets import QGridLayout
from zhdate import ZhDate
from datetime import datetime
from ephem import *
import math
import datetime
from skyfield.api import load
import re
import importlib.util
class TimeInfoApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("温氏奇门遁甲排盘")
        self.setGeometry(100, 100, 400, 300)  # 设置窗口大小和位置

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.time_entry = QLineEdit()
        self.time_entry.setStyleSheet("border: 2px solid gray;")  # 设置边框宽度和颜色
        layout.addWidget(self.time_entry)
        self.solar_label = QLabel("<font color='red'>阳历</font> 年，月，日，时间(输入格式示例：2023年9月7日18时42分)")
        layout.addWidget(self.solar_label)


        self.lunar_output1 = QLineEdit()
        self.lunar_output1.setStyleSheet("border: 2px solid gray;")  # 设置边框宽度和颜色
        layout.addWidget(self.lunar_output1)

        self.lunar_label1 = QLabel("<font color='red'>阴历</font> 年，月，日，时辰")
        layout.addWidget(self.lunar_label1)

        '''# 创建水平布局管理器和垂直
        horizontal_layout = QHBoxLayout()
        vertical_layout = QVBoxLayout()
        # 创建第一个输出框
        self.lunar_output1 = QLineEdit()
        self.lunar_output1.setStyleSheet("border: 2px solid gray;")  # 设置边框宽度和颜色
        horizontal_layout.addWidget(self.lunar_output1)
        label1= QLabel("节气")
        vertical_layout.addWidget(label1)
        # 创建第二个输出框
        self.lunar_output2 = QLineEdit()
        self.lunar_output2.setStyleSheet("border: 2px solid gray;")  # 设置边框宽度和颜色
        horizontal_layout.addWidget(self.lunar_output2)
        label2 = QLabel("元日")
        vertical_layout.addWidget(label2)

        # 将水平布局管理器添加到主布局中
        layout.addLayout(horizontal_layout)
        horizontal_layout.addLayout(vertical_layout)
        '''
        grid_layout = QGridLayout()
        # 创建标签和第一个输出框，并将它们添加到网格布局
        label1 = QLabel("节气")
        self.lunar_output2 = QLineEdit()
        self.lunar_output2.setStyleSheet("border: 2px solid gray;")  # 设置边框宽度和颜色
        grid_layout.addWidget(label1, 1, 0)  # 第一个参数是小部件，第二个和第三个参数是行和列
        grid_layout.addWidget(self.lunar_output2, 0, 0)
        # 创建标签和第二个输出框，并将它们添加到网格布局
        label2 = QLabel("元日")
        self.lunar_output3 = QLineEdit()
        self.lunar_output3.setStyleSheet("border: 2px solid gray;")  # 设置边框宽度和颜色
        grid_layout.addWidget(label2, 1, 1)  # 第一个参数是小部件，第二个和第三个参数是行和列
        grid_layout.addWidget(self.lunar_output3, 0, 1)
        # 将网格布局添加到主布局
        layout.addLayout(grid_layout)

        self.show_info_button = QPushButton("一键排盘")
        self.show_info_button.clicked.connect(self.show_info)
        layout.addWidget(self.show_info_button)

        self.info_label = QLabel()
        layout.addWidget(self.info_label)

        central_widget.setLayout(layout)

    def show_info(self):
        user_time = self.time_entry.text()
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
            # 添加额外的检查以确保数值在有效范围内
            if 1 <= monthh <= 12 and 1 <= dayy <= 31 and 1 <= hourr <= 24 and 0 <= minutee <= 60:
                # 打印结果
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
                for i in range(1, 25):  # 循环1到24小时
                    if i == 23 or i == 24:
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

                planets = load('de422.bsp')
                tropicl_year = 365.24219647  # 回归年长度
                ts = load.timescale()
                earth = planets[399]
                # 24节气
                jieqi = ["春分", "清明", "谷雨", "立夏", "小满", "芒种", \
                         "夏至", "小暑", "大暑", "立秋", "处暑", "白露", \
                         "秋分", "寒露", "霜降", "立冬", "小雪", "大雪", \
                         "冬至", "小寒", "大寒", "立春", "雨水", "惊蛰"]

                # 计算黄经
                def ecliptic_lon(jd):
                    # sun = planets['SUN']
                    # astrometric = earth.at(jd).observe(sun)
                    # apparent = astrometric.apparent()
                    lat, lon, distance = earth.at(jd).observe(planets['SUN']).apparent().ecliptic_latlon(epoch='date')
                    # lat, lon, distance = apparent.ecliptic_latlon(epoch='date')#求太阳的视黄经经视黄纬和距离（epoch设为所求时间就是视赤经视赤纬）
                    # p=earth.at(jd).observe(planets['SUN']).astrometric.apparent().ecliptic_latlon(epoch='date')
                    # lon=p[0]
                    return lon._degrees * math.pi / 180.0  # 返回黄纬

                # 根据时间求太阳黄经，计算到了第几个节气，春分序号为0
                def sta(jd):
                    e = ecliptic_lon(jd)
                    n = int(e * 180.0 / math.pi / 15)
                    return n

                # 根据当前时间，求下个节气的发生时间
                def iteration(jd, sta):  # jd：要求的开始时间，sta：不同的状态函数
                    s1 = sta(jd)  # 初始状态(太阳处于什么位置)
                    s0 = s1
                    e = ecliptic_lon(jd)
                    # dt=((s1+1)*15.0-e*180.0/math.pi)/360.0*tropicl_year#初始时间改变量设为当前太阳黄经和下个节气点黄经相差度数换算为的天数
                    dt = 14  # 如果不是14天，下面有可能出现连续加两个14天，导致跳过了一个节气
                    # print(s1," ",dt," ",e*180.0/math.pi)
                    while True:
                        jd = ts.tai_jd(jd.tai + dt)
                        # jd+=dt
                        s = sta(jd)
                        if s0 != s:
                            s0 = s
                            dt = -dt / 2  # 使时间改变量折半减小
                        if abs(dt) < 0.000001 and s != s1:  # s!=s1是为了使时间跨到下个节气时间之后，方便接下来节气的计算，skyfield时间精度是微秒
                            break
                    return jd

                t = ts.now()
                tt = ts.tt(2023, 1, 1, 0, 0, 0)

                def jq(year):  # 从当前时间开始连续输出未来n个节气的时间
                    # jd=now()#获取当前时间的一个儒略日和1899/12/31 12:00:00儒略日的差值
                    # t = ts.now()
                    t = ts.tt(year - 1, 12, 15, 0, 0, 0)
                    # t= ts.tt(1501, 1, 1, 12, 0,0)
                    e = ecliptic_lon(t)
                    n = int(e * 180.0 / math.pi / 15) + 1
                    # print(' 年 -月-日 节气：时:分:秒')
                    a = []
                    for i in range(26):
                        if n >= 24:
                            n -= 24
                        t = iteration(t, sta)
                        e = ecliptic_lon(t)
                        # e=ecliptic_lon(t)
                        # d=Date(jd+1/3).tuple()
                        t1 = ts.tai_jd(t.tai + 1 / 3)
                        # print                                                             t1.utc.hour,t1.utc.minute, int(t1.utc.second),int(100*(t1.utc.second-int(t1.utc.second)))))
                        jieqishijian = datetime.datetime(t1.utc.year, t1.utc.month, t1.utc.day, t1.utc.hour, 0, 0)
                        a.append(jieqishijian)
                        print("{0}-{1:02d}-{2:02d} {3}：{4:02d}:{5:02d}:{6:03.1f}".format(t1.utc.year, t1.utc.month, t1.utc.day,jieqi[n],t1.utc.hour,t1.utc.minute, t1.utc.second))#秒数可能会出现60
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
                #print("天干地支年"'\t''月''\t'' ''日''\t''     ''时辰''\t''节气')
                #print(' ''%s%s年''\t''  ''%s%s月''\t''%s%s日''\t''%s%s时''\t''%s' % (
                    #tg, dz, yuetiangan, yuedizhi, ritiangan, ridizhi, shichengtiangan, shichengdizhi, JQ))
                info = f"你输入的时间是：{user_time}"
                self.lunar_output1.setText(' %s%s年''\t''%s%s月''\t''%s%s日''\t''%s%s时' % (
                    tg, dz, yuetiangan, yuedizhi, ritiangan, ridizhi, shichengtiangan, shichengdizhi))
                self.lunar_output2.setText('%s' % (JQ))
                self.info_label.setText(info)
            else:
                # 用户输入的时间信息不正确，显示警告
                reply = QMessageBox()
                reply.setIcon(QMessageBox.Icon.Critical)
                reply.setWindowTitle("警告")
                reply.setText("输入的时间数值超出有效范围，请重新输入。")
                reply.setStandardButtons(QMessageBox.StandardButton.Ok)
                reply.exec()  # 阻塞应用程序直到用户关闭警告框
        else:
                # 用户输入的时间信息不符合格式，显示警告
                reply = QMessageBox()
                reply.setIcon(QMessageBox.Icon.Critical)
                reply.setWindowTitle("警告")
                reply.setText("输入的时间信息格式不正确，请重新输入。")
                reply.setStandardButtons(QMessageBox.StandardButton.Ok)
                reply.exec()  # 阻塞应用程序直到用户关闭警告框

    def closeEvent(self, event):
        # 重定义窗口关闭事件，只有用户明确主动关闭窗口才会退出应用程序
        reply = QMessageBox.question(self, '确认退出', '确认退出应用程序吗？',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TimeInfoApp()
    window.show()
    sys.exit(app.exec())
