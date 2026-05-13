import sys
from zhdate import ZhDate
from datetime import datetime
from ephem import *
import math
import datetime
from skyfield.api import load
import re
import importlib.util
from PyQt6.QtWidgets import QFrame
from PyQt6.QtWidgets import QApplication,QDialog, QMainWindow, QWidget, QVBoxLayout, QLabel, QHBoxLayout,QLineEdit, QGridLayout, QPushButton, QFrame,QMessageBox,QTextEdit,QPlainTextEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QTimer, QDateTime
from PyQt6.QtGui import QPixmap, QColor, QPainter
from PyQt6.QtGui import QPalette,QImage
from PyQt5.QtGui import QIcon
from PyQt6.QtWidgets import QStackedWidget
from PIL import Image, ImageFilter
class TimeInfoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("温氏奇门遁甲排盘")
        self.setGeometry(100, 100, 400, 300)  # 设置窗口大小和位置
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(255, 255, 255))  # 背景颜色为白色
        #palette.setColor(QPalette.ColorRole.Window, QColor(200, 160, 120))  # 背景颜色为浅棕色
        self.setPalette(palette)


        # 创建用于显示实时时间的 QLabel
        self.time_label = QLabel()
        layout.addWidget(self.time_label)

        central_widget.setLayout(layout)

        # 创建定时器，每秒更新一次时间
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # 1000 毫秒 = 1 秒

        self.update_time()  # 初始更新一次时间
        grid_layout1= QGridLayout()
        self.time_entry1 = QLineEdit()
        self.time_entry1.setStyleSheet("border: 2px solid gray;")  # 设置边框宽度和颜色
        self.time_entry1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_entry1.setFixedHeight(30)
        self.time_entry1label=QLabel('年')
        self.time_entry2 = QLineEdit()
        self.time_entry2.setStyleSheet("border: 2px solid gray;")  # 设置边框宽度和颜色
        self.time_entry2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_entry2.setFixedHeight(30)
        self.time_entry2label = QLabel('月')
        self.time_entry3 = QLineEdit()
        self.time_entry3.setStyleSheet("border: 2px solid gray;")  # 设置边框宽度和颜色
        self.time_entry3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_entry3.setFixedHeight(30)
        self.time_entry3label = QLabel('日')
        self.time_entry4 = QLineEdit()
        self.time_entry4.setStyleSheet("background-color: rgb(173, 216, 230);border: 2px solid gray;")  # 设置边框宽度和颜色
        self.time_entry4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_entry4.setFixedHeight(30)
        self.time_entry4label = QLabel('时')
        self.time_entry5 = QLineEdit()
        self.time_entry5.setStyleSheet("border: 2px solid gray;")  # 设置边框宽度和颜色
        self.time_entry5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_entry5.setFixedHeight(30)
        self.time_entry5label = QLabel('节气')
        grid_layout1.addWidget(self.time_entry1, 0, 0)
        grid_layout1.addWidget(self.time_entry1label, 0, 1)
        grid_layout1.addWidget(self.time_entry2, 0, 2)
        grid_layout1.addWidget(self.time_entry2label, 0, 3)
        grid_layout1.addWidget(self.time_entry3, 0, 4)
        grid_layout1.addWidget(self.time_entry3label, 0, 5)
        grid_layout1.addWidget(self.time_entry4, 0, 6)
        grid_layout1.addWidget(self.time_entry4label, 0, 7)
        grid_layout1.addWidget(self.time_entry5, 0, 8)
        grid_layout1.addWidget(self.time_entry5label, 0, 9)
        layout.addLayout(grid_layout1)
        # 创建一个 QVBoxLayout 用于垂直对齐
        v_layout = QVBoxLayout()
        # 创建一个 QLabel
        self.solar_label = QLabel("输入：<font color='red'>阴历</font> 年，月，日，节气，例如： <font color='red'>癸卯年乙卯月庚申日雨水</font>；白底框为输入框")
        # 设置对齐方式为居中
        self.solar_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # 添加 QLabel 到垂直布局中
        v_layout.addWidget(self.solar_label)
        # 将垂直布局添加到父布局
        layout.addLayout(v_layout)
        layout.addWidget(self.solar_label)
        #去除
        '''
        self.lunar_output1 = QLineEdit()
        self.lunar_output1.setFixedHeight(30)
        self.lunar_output1.setStyleSheet("background-color: rgb(173, 216, 230);border: 2px solid gray;")  # 设置边框宽度和颜色
        self.lunar_output1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.lunar_output1)
        # 创建一个 QVBoxLayout 用于垂直对齐
        v_layout = QVBoxLayout()
        # 创建一个 QLabel
        self.lunar_label1 = QLabel("<font color='red'>阴历</font> 年，月，日，时辰")
        # 设置对齐方式为居中
        self.lunar_label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # 添加 QLabel 到垂直布局中
        v_layout.addWidget(self.lunar_label1)
        # 将垂直布局添加到父布局
        layout.addLayout(v_layout)
        layout.addWidget(self.lunar_label1)
        '''
        grid_layout = QGridLayout()
        font = QFont('KaiTi',11)
        self.solar_label.setFont(font)  # 将字体应用于 QLabel
        self.lunar_label1.setFont(font)
        # 创建标签和第一个输出框，并将它们添加到网格布局
        label1 = QLabel("阴阳遁")
        label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lunar_output2 = QLineEdit()
        self.lunar_output2.setFixedHeight(30)
        self.lunar_output2.setStyleSheet("background-color: rgb(173, 216, 230);border: 2px solid gray;")  # 设置边框宽度和颜色
        self.lunar_output2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        grid_layout.addWidget(label1, 1, 0)  # 第一个参数是小部件，第二个和第三个参数是行和列
        grid_layout.addWidget(self.lunar_output2, 0, 0)
        # 创建标签和第二个输出框，并将它们添加到网格布局
        label2 = QLabel("元日")
        label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lunar_output3 = QLineEdit()
        self.lunar_output3.setFixedHeight(30)
        self.lunar_output3.setStyleSheet("background-color: rgb(173, 216, 230);border: 2px solid gray;")  # 设置边框宽度和颜色
        self.lunar_output3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        grid_layout.addWidget(label2, 1, 1)  # 第一个参数是小部件，第二个和第三个参数是行和列
        grid_layout.addWidget(self.lunar_output3, 0, 1)
        label1.setFont(font)  # 将字体应用于 QLabel
        label2.setFont(font)
        # 将网格布局添加到主布局
        layout.addLayout(grid_layout)
        self.ws = QLabel('温氏奇门遁甲排盘')
        font=QFont('KaiTi',20)
        self.ws.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ws.setFont(font)
        layout.addWidget(self.ws)
        # 创建九宫格
        grid_layout = QGridLayout()
        tainruju=['巽四','离九','坤二','震三','中五','兑七','艮八','坎一','乾六']
        self.output_boxes = {}  # 用于存储输出框的字典
        colors = [Qt.GlobalColor.red, Qt.GlobalColor.green, Qt.GlobalColor.blue,
                  Qt.GlobalColor.cyan, Qt.GlobalColor.magenta, Qt.GlobalColor.yellow,
                  Qt.GlobalColor.gray, Qt.GlobalColor.darkYellow, Qt.GlobalColor.darkGreen]
        for row in range(3):
            for col in range(3):
                frame = QFrame()
                frame.setFrameShape(QFrame.Shape.Box)
                frame.setLineWidth(2)
                frame.setMidLineWidth(2)
                label = QLabel(f"格子 {row + 1}-{col + 1}")
                if row==1 and col==1:
                    # 创建一个内部的二维布局
                    inner_layout = QGridLayout()

                    output1 = QLineEdit()
                    output1.setStyleSheet("background-color: rgb(173, 216, 230); border: 2px solid gray;")
                    output1.setFixedSize(140, 32)  # 设置宽度和高度
                    output1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output2 = QLineEdit()
                    output2.setStyleSheet("background-color: rgb(255, 140, 0); border: 2px solid gray;")
                    output2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output2.setFixedSize(140, 40)  # 设置宽度和高度
                    output1.setReadOnly(True)
                    output2.setReadOnly(True)
                    box_names = [f"output_{row}_{col}_1", f"output_{row}_{col}_2"]
                    self.output_boxes.update(
                        {name: output for name, output in zip(box_names, [output1, output2, output3, output4])})

                    # 添加输出框到二维布局
                    inner_layout.addWidget(output1, 0, 1,1,3)  # 左上角
                    inner_layout.addWidget(output2, 1, 1,1,3)  # 中间
                    grid_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
                    output1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
                    output2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
                    # 创建长度为2的字符串
                    juzifuchuang = tainruju[row * 3 + col]
                    text1= QLabel(juzifuchuang)
                    text2=QLabel("寄二")
                    font = QFont('KaiTi',15)
                    text1.setFont(font)  # 将字体应用于 QLabel
                    text2.setFont(font)
                    # 添加字符串到二维布局右下角
                    inner_layout.addWidget(text1,2,4)
                    inner_layout.addWidget(text2,2,0)
                    # 设置内部布局为frame的布局
                    frame.setLayout(inner_layout)
                    # 将QFrame添加到网格布局
                    grid_layout.addWidget(frame, row, col)
                elif row==0 and col==2:
                    # 创建一个内部的二维布局
                    inner_layout = QGridLayout()

                    output1 = QLineEdit()
                    output1.setStyleSheet("background-color: rgb(173, 216, 230); border: 2px solid gray;")
                    output1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output1.setFixedSize(35, 30)  # 设置宽度和高度
                    output2 = QLineEdit()
                    output2.setStyleSheet("background-color: rgb(173, 216, 230); border: 2px solid gray;")
                    output2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output2.setFixedSize(35, 30)
                    output3 = QLineEdit()
                    output3.setStyleSheet("background-color: rgb(173, 216, 230); border: 2px solid gray;")
                    output3.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output3.setFixedSize(35, 30)
                    output2.setReadOnly(True)
                    output1.setReadOnly(True)
                    output3.setReadOnly(True)
                    output4 = QTextEdit()
                    output4.setStyleSheet("background-color: rgb(255, 140, 0); border: 2px solid gray;")
                    output4.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output4.setReadOnly(True)
                    output4.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)  # 禁用垂直滚动条
                    output4.setFixedSize(60, 40)  # 设置宽度和高度
                    output5 = QTextEdit()
                    output5.setStyleSheet("background-color: rgb(255, 140, 0); border: 2px solid gray;")
                    output5.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output5.setReadOnly(True)
                    output5.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)  # 禁用垂直滚动条
                    output5.setFixedSize(60, 40)  # 设置宽度和高度
                    box_names = [f"output_{row}_{col}_1", f"output_{row}_{col}_2", f"output_{row}_{col}_3",
                                 f"output_{row}_{col}_4",f"output_{row}_{col}_5"]
                    self.output_boxes.update(
                        {name: output for name, output in zip(box_names, [output1, output2, output3, output4,output5])})

                    # 添加输出框到二维布局
                    inner_layout.addWidget(output1, 0, 0)  # 左上角
                    inner_layout.addWidget(output2, 2, 0)  # 左下角
                    inner_layout.addWidget(output3, 0, 4)  # 右上角
                    inner_layout.addWidget(output4, 1, 3)  # 中间
                    inner_layout.addWidget(output5, 1, 1)  # 中间

                    # 创建长度为2的字符串
                    juzifuchuang = tainruju[row * 3 + col]
                    text= QLabel(juzifuchuang)
                    text3=QLabel('+')
                    font = QFont('KaiTi', 15)
                    text.setFont(font)  # 将字体应用于 QLabel
                    # 添加字符串到二维布局右下角
                    inner_layout.addWidget(text, 2, 4)
                    inner_layout.addWidget(text3, 1, 2)

                    # 设置内部布局为frame的布局
                    frame.setLayout(inner_layout)
                    # 将QFrame添加到网格布局
                    grid_layout.addWidget(frame, row, col)
                else:
                    # 创建一个内部的二维布局
                    inner_layout = QGridLayout()

                    output1 = QLineEdit()
                    output1.setStyleSheet("background-color: rgb(173, 216, 230); border: 2px solid gray;")
                    output1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output1.setFixedSize(35, 30)  # 设置宽度和高度
                    output2 = QLineEdit()
                    output2.setStyleSheet("background-color: rgb(173, 216, 230); border: 2px solid gray;")
                    output2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output2.setFixedSize(35, 30)
                    output3 = QLineEdit()
                    output3.setStyleSheet("background-color: rgb(173, 216, 230); border: 2px solid gray;")
                    output3.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output3.setFixedSize(35, 30)
                    output2.setReadOnly(True)
                    output1.setReadOnly(True)
                    output3.setReadOnly(True)
                    output4 = QLineEdit()
                    output4.setStyleSheet("background-color: rgb(255, 140, 0); border: 2px solid gray;")
                    output4.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output4.setReadOnly(True)
                    output4.setFixedSize(60, 40)  # 设置宽度和高度
                    output5 = QLineEdit()
                    output5.setStyleSheet("background-color: rgb(255, 140, 0); border: 2px solid gray;")
                    output5.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output5.setReadOnly(True)
                    output5.setFixedSize(60, 40)  # 设置宽度和高度
                    box_names = [f"output_{row}_{col}_1", f"output_{row}_{col}_2", f"output_{row}_{col}_3",
                                 f"output_{row}_{col}_4", f"output_{row}_{col}_5"]
                    self.output_boxes.update(
                        {name: output for name, output in
                         zip(box_names, [output1, output2, output3, output4, output5])})

                    # 添加输出框到二维布局
                    inner_layout.addWidget(output1, 0, 0)  # 左上角
                    inner_layout.addWidget(output2, 2, 0)  # 左下角
                    inner_layout.addWidget(output3, 0, 4)  # 右上角
                    inner_layout.addWidget(output4, 1, 3)  # 中间
                    inner_layout.addWidget(output5, 1, 1)  # 中间

                    # 创建长度为2的字符串
                    juzifuchuang = tainruju[row * 3 + col]
                    text = QLabel(juzifuchuang)
                    text3 = QLabel('+')
                    font = QFont('KaiTi', 15)
                    text.setFont(font)  # 将字体应用于 QLabel
                    # 添加字符串到二维布局右下角
                    inner_layout.addWidget(text, 2, 4)
                    inner_layout.addWidget(text3, 1, 2)

                    # 设置内部布局为frame的布局
                    frame.setLayout(inner_layout)
                    # 将QFrame添加到网格布局
                    grid_layout.addWidget(frame, row, col)
        print(self.output_boxes)
        layout.addLayout(grid_layout)
        self.show_info_button = QPushButton("一键排盘")
        red_color = QColor(255, 0, 0)
        # 设置按钮标签的颜色为红色
        self.show_info_button.setStyleSheet(f"color: {red_color.name()};")
        self.show_info_button.clicked.connect(self.show_info)
        font = QFont('KaiTi', 11)
        self.show_info_button.setFont(font)
        layout.addWidget(self.show_info_button)
        # 创建一个按钮，用于清空所有输出框的内容
        self.clear_button = QPushButton("清空盘面")
        self.clear_button.clicked.connect(self.clear_all_outputs)
        self.clear_button.setFont(font)
        layout.addWidget(self.clear_button)
        self.info_label = QLabel()
        layout.addWidget(self.info_label)
        central_widget.setLayout(layout)
    def update_time(self):
        # 获取当前时间
        current_time = QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")
        # 更新时间显示
        self.time_label.setText(f"当前时间: {current_time}")
    def show_info(self):
        nianganzhi= self.time_entry1.text()
        yueganzhi=self.time_entry2.text()
        riganzhi=self.time_entry3.text()
        shichengganzhi=self.time_entry4.text()
        ritiangan=riganzhi[0]
        JQ=self.time_entry5.text()
        Tiangan = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
        Dizhi = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
        shengxiao = ['鼠', '牛', '虎', '兔', '龙', '蛇', '马', '羊', '猴', '鸡', '狗', '猪']
        if matches:
                tianganyue1 = ['甲', '己']
                tg1shicheng = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
                tianganyue2 = ['乙', '庚']
                tg2shicheng = ['丙', '丁', '戊', '己', '庚', '辛', '壬', '癸', '甲', '乙']
                tianganyue3 = ['丙', '辛']
                tg3shicheng = ['戊', '己', '庚', '辛', '壬', '癸', '甲', '乙', '丙', '丁']
                tianganyue4 = ['丁', '壬']
                tg4shicheng = ['庚', '辛', '壬', '癸', '甲', '乙', '丙', '丁', '戊', '己']
                tianganyue5 = ['戊', '癸']
                tg5shicheng = ['壬', '癸', '甲', '乙', '丙', '丁', '戊', '己', '庚', '辛']
                yuetiangan = "甲"  # 初始化
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
                #计算阴阳遁
                YD='yangdun'
                jieqiYangD=["冬至","小寒", "大寒", "立春", "雨水", "惊蛰", "春分","清明", "谷雨", "立夏", "小满", "芒种"]
                jieqiYinD=["夏至","小暑", "大暑", "立秋", "处暑", "白露", "秋分", "寒露", "霜降", "立冬", "小雪", "大雪"]
                if JQ in jieqiYangD:
                    YD='yangdun'
                else:
                    YD='yindun'
                yangdunqiju={
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
                yindunqiju={
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
                qiju_index=JQ+yuanri
                if YD=='yangdun':
                    for key in yangdunqiju:
                        if key==qiju_index:
                            qiju=yangdunqiju[key]
                            break
                        else:
                            continue
                elif YD=='yindun':
                    for key in yindunqiju:
                        if key==qiju_index:
                            qiju=yindunqiju[key]
                            break
                        else:
                            continue
                gonghao={'坎一':0,'坤二':1,'震三':2,'巽四':3,'中五':4,'乾六':5,'兑七':6,'艮八':7,'离九':8}
                sanqiliuyi=['甲子戊','甲戌己','甲申庚','甲午辛','甲辰壬','甲寅癸','丁','丙','乙']
                kanyishuchukuang=['output_2_1_1','output_2_1_2','output_2_1_3','output_2_1_4','output_2_1_5']
                kunershuchukuang=['output_0_2_1','output_0_2_2','output_0_2_3','output_0_2_4','output_0_2_5']
                zhensanshuchukuang=['output_1_0_1','output_1_0_2','output_1_0_3','output_1_0_4','output_1_0_5']
                xunsishuchukuang=['output_0_0_1','output_0_0_2','output_0_0_3','output_0_0_4','output_0_0_5']
                zhongwushuchukuang=['output_1_1_1','output_1_1_2']
                qianliushuchukuang=['output_2_2_1','output_2_2_2','output_2_2_3','output_2_2_4','output_2_2_5']
                duiqishuchukuang=['output_1_2_1','output_1_2_2','output_1_2_3','output_1_2_4','output_1_2_5']
                genbashuchukuang=['output_2_0_1','output_2_0_2','output_2_0_3','output_2_0_4','output_2_0_5']
                lijuishuchukuang=['output_0_1_1','output_0_1_2','output_0_1_3','output_0_1_4','output_0_1_5']
                dingweigong=[kanyishuchukuang,kunershuchukuang,zhensanshuchukuang,xunsishuchukuang,zhongwushuchukuang,qianliushuchukuang,duiqishuchukuang,genbashuchukuang,lijuishuchukuang]
                for key in gonghao:
                    if qiju==key:
                        dingweigong_index=gonghao[key]
                        break
                    else:
                        continue
                sanqiliuyigong={}
                if YD=='yangdun':
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
                        if dingweigong_index==4:
                            dingweijushuchukuangMC=dingweigong[dingweigong_index][1]
                            self.output_boxes[dingweijushuchukuangMC].setText('%s'%(sanqiliuyi[i]))
                            sanqiliuyigong[4]=sanqiliuyi[i]
                        elif dingweigong_index==1:
                            sanqiliuyigong[1]=sanqiliuyi[i]
                        elif dingweigong_index>=9:
                            dingweigong_index=dingweigong_index-9
                            if dingweigong_index==4:
                                dingweijushuchukuangMC = dingweigong[dingweigong_index][1]
                                self.output_boxes[dingweijushuchukuangMC].setText('%s'%(sanqiliuyi[i]))
                                sanqiliuyigong[4] = sanqiliuyi[i]
                            elif dingweigong_index==1:
                                sanqiliuyigong[1] = sanqiliuyi[i]
                            else:
                                dingweijushuchukuangMC=dingweigong[dingweigong_index][3]
                                self.output_boxes[dingweijushuchukuangMC].setText('%s'%(sanqiliuyi[i]))
                                sanqiliuyigong[dingweigong_index]=sanqiliuyi[i]
                        else:
                            dingweijushuchukuangMC = dingweigong[dingweigong_index][3]
                            self.output_boxes[dingweijushuchukuangMC].setText('%s'%(sanqiliuyi[i]))
                            sanqiliuyigong[dingweigong_index] = sanqiliuyi[i]
                elif YD=='yindun':
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
                    for i in range(1,9):
                        dingweigong_index = dingweigong_index - 1
                        if dingweigong_index==4:
                            dingweijushuchukuangMC=dingweigong[dingweigong_index][1]
                            self.output_boxes[dingweijushuchukuangMC].setText('%s'%(sanqiliuyi[i]))
                            sanqiliuyigong[4]=sanqiliuyi[i]
                        elif dingweigong_index==1:
                            sanqiliuyigong[1]=sanqiliuyi[i]
                        elif dingweigong_index<0:
                            dingweigong_index=dingweigong_index+9
                            if dingweigong_index==4:
                                dingweijushuchukuangMC = dingweigong[dingweigong_index][1]
                                self.output_boxes[dingweijushuchukuangMC].setText('%s'%(sanqiliuyi[i]))
                                sanqiliuyigong[4] = sanqiliuyi[i]
                            elif dingweigong_index==1:
                                sanqiliuyigong[1] = sanqiliuyi[i]
                            else:
                                dingweijushuchukuangMC=dingweigong[dingweigong_index][3]
                                self.output_boxes[dingweijushuchukuangMC].setText('%s'%(sanqiliuyi[i]))
                                sanqiliuyigong[dingweigong_index]=sanqiliuyi[i]
                        else:
                            dingweijushuchukuangMC = dingweigong[dingweigong_index][3]
                            self.output_boxes[dingweijushuchukuangMC].setText('%s'%(sanqiliuyi[i]))
                            sanqiliuyigong[dingweigong_index] = sanqiliuyi[i]
                kunersanqiliuyi=f'{sanqiliuyigong[1]}\n{sanqiliuyigong[4]}'
                self.output_boxes['output_0_2_4'].setPlainText(kunersanqiliuyi)
                if YD=='yangdun':
                    YD='阳遁'
                else:
                    YD='阴遁'
                print(sanqiliuyigong)
                print(YD)
                print(dingweigong_index)
                print(dingweijushuchukuangMC)
                info = f"你输入的时间是：{user_time}"
                self.lunar_output1.setText(' %s%s年''\t''%s%s月''\t''%s%s日''\t''%s%s时' % (
                    tg, dz, yuetiangan, yuedizhi, ritiangan, ridizhi, shichengtiangan, shichengdizhi))
                self.lunar_output2.setText('%s''\t''%s' % (JQ,YD))
                self.lunar_output3.setText('%s日' % (yuanri))
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

    def clear_all_outputs(self):
        self.time_entry1.clear()
        self.time_entry2.clear()
        self.time_entry3.clear()
        self.time_entry4.clear()
        self.time_entry5.clear()
        self.lunar_output2.clear()
        self.lunar_output3.clear()

        for row in range(3):
            for col in range(3):
                if row==1 and col==1:
                    for i in range(1, 3):  # 清空output_0_0_1、output_0_0_2、output_0_0_3等
                        output_name = f"output_{row}_{col}_{i}"
                        self.output_boxes[output_name].clear()
                else:
                    for i in range(1, 5):  # 清空output_0_0_1、output_0_0_2、output_0_0_3等
                        output_name = f"output_{row}_{col}_{i}"
                        self.output_boxes[output_name].clear()

class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("温氏奇门遁甲排盘登录")
        self.setGeometry(100, 100, 700, 150)  # 增加宽度以容纳图像


        # 设置窗口背景颜色为纯白
        self.setStyleSheet("background-color: white;")
        layout = QHBoxLayout()  # 使用水平布局包含图像和登录部分

        # 添加图像到左边
        image_label = QLabel()
        pixmap = QPixmap("QMDJ.png")  # 替换为你的图像文件路径
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # 图像居中
        image_label.setFixedWidth(550)  # 图像占据窗口2/3的宽度
        layout.addWidget(image_label)
#登录部分

        login_layout = QVBoxLayout()
        login_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)  # 登录部分居中
        label1 = QLabel("South China University Of Technology")
        label2 = QLabel("School of Business Administration")
        label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label1.setStyleSheet("color: red;")  # 设置文本颜色为红色
        label2.setStyleSheet("color: purple;")  # 设置文本颜色为红色
        # 在登录部分上方添加一张图片
        top_image_label = QLabel()
        top_pixmap = QPixmap("HGXH2.png")  # 替换为您的顶部图片文件路径
        top_image_label.setPixmap(top_pixmap)
        login_layout.addWidget(top_image_label)
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.username_input.setFixedWidth(150)
        self.password_input.setFixedWidth(150)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        login_button = QPushButton("登录")
        username_label = QLabel("用户名:")
        username_layout = QHBoxLayout()
        username_layout.addWidget(username_label)
        username_layout.addWidget(self.username_input)
        password_label = QLabel("密码:")
        password_layout = QHBoxLayout()
        password_layout.addWidget(password_label)
        password_layout.addWidget(self.password_input)
        login_layout.addWidget(label1)
        login_layout.addWidget(label2)
        login_layout.addLayout(username_layout)
        login_layout.addLayout(password_layout)
        login_layout.addWidget(login_button)


        self.login_status_label = QLabel()  # 用于显示登录状态信息
        self.login_status_label.setStyleSheet("color: red;")  # 设置文本颜色为红色
        login_layout.addWidget(self.login_status_label)
        # 右侧登录部分占据右边总空间的1/3
        right_widget = QWidget()
        right_layout = QVBoxLayout()
        right_widget.setLayout(right_layout)
        right_widget.setFixedWidth(10)
        layout.addWidget(right_widget)  # 添加右侧部分到布局中
        layout.addLayout(login_layout)  # 添加登录部分到布局中

        self.setLayout(layout)
        login_button.clicked.connect(self.login)

    def login(self):
        # 在这里进行登录验证，比如检查用户名和密码是否正确
        username = self.username_input.text()
        password = self.password_input.text()

        if username == "LF" and password == '2000':
            self.login_status_label.setText("登录成功")  # 设置登录成功提示
            self.accept()  # 用户登录成功，使用 accept() 方法来指示成功
        else:
            self.login_status_label.setText("用户名或密码不正确")  # 设置登录失败提示
'''
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TimeInfoApp()
    window.show()
    sys.exit(app.exec())
'''
if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 创建登录窗口
    login_dialog = LoginDialog()
    # 显示登录窗口并等待用户登录
    if login_dialog.exec() == QDialog.DialogCode.Accepted:
        # 用户已成功登录，创建主应用程序窗口并显示
        main_window = TimeInfoApp()
        main_window.show()
    sys.exit(app.exec())
'''
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 创建登录窗口
    login_dialog = LoginDialog()

    # 显示登录窗口并等待用户登录
    result = login_dialog.exec()

    if result == QDialog.DialogCode.Accepted:
        # 用户已成功登录，创建主应用程序窗口并显示
        main_window = TimeInfoApp()
        main_window.show()

    sys.exit(app.exec())
'''