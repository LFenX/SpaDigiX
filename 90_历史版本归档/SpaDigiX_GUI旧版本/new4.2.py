# 作者：李峰
# 年份：2023年9月
# 学院：华南理工大学工商管理学院
# 联系电话：13786866211
# 电子邮件：lfie2022@outlook.com
# 地址：华南理工大学五山校区
# 版权声明：
# 本代码受版权保护，未经作者书面许可，禁止复制、修改、分发、传播、展示或发布本代码的任何部分。
'''
版权所有 © 2023 李峰

李峰，华南理工大学工商管理学院 版权所有。

访问者可将本网站内容用于个人信息获取或非商业用途。对于其他一切用途，包括但不限于复制、修改、分发、传播、展示或发布，均须得到李峰的书面许可。

未经许可，不得在与之相关的网站上展示本网站的任何部分。未经许可，不得在与之相关的计算机或服务器上存储本网站的任何部分。未经许可，不得通过任何媒体传播本网站的任何部分。

本网站的内容仅供参考。尽管我们努力确保信息准确无误，但不对信息的完整性、准确性、适用性或可靠性作出任何明示或暗示的陈述或保证。对于因使用本网站的信息而导致的任何损失或损害，李峰概不负责。

通过本网站提供的链接可能导致离开本网站。这些链接仅供参考。李峰对链接指向的任何网站的内容或隐私政策概不负责。

李峰 保留随时更改本网站及其所包含的条款和条件的权利，恕不另行通知。

本版权声明的最新版本将在本网站上发布并立即生效。请定期查看此版权声明，以确保您了解最新的条款和条件。

如有任何疑问或需要许可，请联系：

李峰
联系地址：华南理工大学工商管理学院，五山校区
联系电话：13786866211
电子邮件：lfie2022@outlook.com
'''
import configparser
import sys
import os
import calendar
from zhdate import ZhDate
from datetime import datetime
from ephem import *
import math
import datetime
import re
from PyQt6.QtWidgets import QTextBrowser, QApplication, QDialog, QMainWindow, QWidget, QVBoxLayout, QLabel, QHBoxLayout, \
    QLineEdit, QGridLayout, QPushButton, QFrame, QMessageBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QTimer, QDateTime, QSize
from PyQt6.QtGui import QPixmap, QColor, QBrush, QIcon, QMovie
from PyQt6.QtGui import QPalette
from PyQt6.QtWidgets import QComboBox, QScrollArea, QGraphicsDropShadowEffect, QInputDialog, QSizePolicy, QSpacerItem, \
    QSplashScreen


class InputWithComboBox(QWidget):
    def __init__(self, options=None):
        super().__init__()

        layout = QVBoxLayout()

        self.input_text = QLineEdit()
        self.combo_box = QComboBox()
        self.combo_box.setFixedWidth(69)

        if options:
            self.combo_box.addItems(options)

        layout.addWidget(self.input_text)

        # 创建左右箭头按钮
        self.left_arrow_button = QPushButton("<")
        self.right_arrow_button = QPushButton(">")
        self.right_arrow_button.setFixedWidth(15)
        self.left_arrow_button.setFixedWidth(15)
        self.left_arrow_button.clicked.connect(self.decrement_value)
        self.right_arrow_button.clicked.connect(self.increment_value)

        # 将按钮添加到水平布局中
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.left_arrow_button)
        button_layout.addWidget(self.combo_box)
        button_layout.addWidget(self.right_arrow_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

        # 连接槽函数，当选项变化时，将选项文本设置到输入框
        self.combo_box.currentTextChanged.connect(self.set_input_text)

    def set_input_text(self, text):
        self.input_text.setText(text)

    def increment_value(self):
        # 增加数字
        current_index = self.combo_box.currentIndex()
        if current_index < self.combo_box.count() - 1:
            self.combo_box.setCurrentIndex(current_index + 1)

    def decrement_value(self):
        # 减少数字
        current_index = self.combo_box.currentIndex()
        if current_index > 0:
            self.combo_box.setCurrentIndex(current_index - 1)


class TimeInfoApp(QMainWindow):
    def set_zhuye(self):
        base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
        # 访问数据文件的路径
        image_path1 = os.path.join(base_path, 'JGT.png')
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
        reply.setText('个人主页功能还未开发，敬请期待!')
        reply.setStandardButtons(QMessageBox.StandardButton.Ok)
        reply.exec()  # 阻塞应用程序直到用户关闭警告框

    def logout(self):
        # 在退出登录时，显示登录对话框
        self.close()

        self.login_dialog = LoginDialog()
        self.login_dialog.exec()
        self.show()

    def set_current_time(self):
        current_time = datetime.datetime.now()
        self.time_entry1.input_text.setText(str(current_time.year))
        self.time_entry2.input_text.setText(str(current_time.month))
        self.time_entry3.input_text.setText(str(current_time.day))
        self.time_entry4.input_text.setText(str(current_time.hour))
        self.time_entry5.input_text.setText(str(current_time.minute))

    def __init__(self):
        super().__init__()

        def createLineEditRightButton2(edit):
            base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
            # 访问数据文件的路径
            image_path1 = os.path.join(base_path, 'TGDI.png')
            left_button = QPushButton()
            left_button.setCursor(Qt.CursorShape.ArrowCursor)
            left_button.setFixedSize(25, 25)
            # left_button.setStyleSheet("border: none;")
            icon = QIcon(image_path1)  # 替换成您的图标文件路径
            left_button.setIcon(icon)
            left_button.setIconSize(left_button.size())
            layout = QHBoxLayout()
            style_sheet = "background-color: rgb(173, 216, 230);border: 2px solid gray;padding-left: 18px; "
            edit.setStyleSheet(style_sheet)
            edit.setReadOnly(True)
            style_sheet1 = "padding-left: 0px; border: none; "
            left_button.setStyleSheet(style_sheet1)
            layout.addWidget(left_button)
            layout.addStretch()
            layout.setContentsMargins(0, 0, 0, 0)
            edit.setLayout(layout)
            return left_button

        self.setWindowTitle("温氏奇门遁甲阴阳九局活用预测排盘")
        self.setGeometry(310, 30, 943, 770)  # 设置窗口大小和位置
        self.setMinimumSize(20, 20)  # 设置窗口的固定大小
        base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
        # 访问数据文件的路径
        image_path1 = os.path.join(base_path, 'TTB.jpg')
        image_path2 = os.path.join(base_path, 'JGT.png')
        image_path3 = os.path.join(base_path, 'YHTB.jpg')
        self.setWindowIcon(QIcon(image_path1))  # 替换成您的图标文件路径
        # 创建可滚动区域
        scroll_area = QScrollArea()
        central_widget = QWidget()
        layout = QVBoxLayout()
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(255, 255, 255))  # 背景颜色为白色
        # palette.setColor(QPalette.ColorRole.Window, QColor(200, 160, 120))  # 背景颜色为浅棕色
        self.setPalette(palette)
        horizontal_layout = QHBoxLayout()
        # 创建用于显示实时时间的 QLabel
        # self.time_label = QLabel()
        self.time_label = QLineEdit()
        self.tuichudenglu = QPushButton("退出登录")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)  # 设置阴影模糊半径，调整阴影的模糊程度
        shadow.setXOffset(5)  # 设置阴影在水平方向上的偏移
        shadow.setYOffset(5)  # 设置阴影在垂直方向上的偏移
        self.tuichudenglu.setGraphicsEffect(shadow)
        self.gerenzhuye = QPushButton()
        self.gerenzhuye.setFixedSize(33, 33)
        icon = QIcon(image_path3)
        self.gerenzhuye.setIcon(icon)
        self.gerenzhuye.setIconSize(self.gerenzhuye.size())  # 设置图标大小与按钮大小相同
        # 使用样式表去除按钮的边框
        # self.gerenzhuye.setStyleSheet("border: none;")
        self.time_label.setReadOnly(True)
        self.time_label.setFixedWidth(200)  # 设置标签的宽度为 100 像素
        horizontal_layout.addWidget(self.time_label)
        self.current_time_button = QPushButton("获取当前时间")
        font = QFont('SimSun', 10)
        font.setBold(True)
        self.tuichudenglu.setFont(font)
        self.current_time_button.setFont(font)
        self.time_label.setFont(font)
        # 设置按钮的背景颜色
        button_style = """
            QPushButton {
                background-color: white;  /* 设置背景颜色为灰色 */
                color: black;  /* 设置文字颜色为红色 */
                border: 3px solid gray;  /* 设置边框样式 */
                border-radius: 10px;  /* 设置边框圆角 */      
                padding: 6px;   /* 设置内边距 */                 
                 border-style: outset; /* 设置内边距 */           
            }

            QPushButton:hover {
                background-color: purple;  /* 设置鼠标悬停时的背景颜色 */color: white;  /* 设置文字颜色为白色 */
            }
        """
        self.current_time_button.setStyleSheet(button_style)
        button_style2 = """
                            QPushButton {
                                background-color: white;  /* 设置背景颜色为灰色 */
                                color: black;  /* 设置文字颜色为红色 */
                                border: 3px solid gray;  /* 设置边框样式 */
                                border-radius: 10px;  /* 设置边框圆角 */      
                                padding: 6px;   /* 设置内边距 */                 
                                 border-style: outset; /* 设置内边距 */           
                            }

                            QPushButton:hover {
                                background-color: purple;  /* 设置鼠标悬停时的背景颜色 */color: white;  /* 设置文字颜色为白色 */
                            }
                        """
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)  # 设置阴影模糊半径，调整阴影的模糊程度
        shadow.setXOffset(5)  # 设置阴影在水平方向上的偏移
        shadow.setYOffset(5)  # 设置阴影在垂直方向上的偏移
        self.current_time_button.setGraphicsEffect(shadow)
        self.tuichudenglu.setStyleSheet(button_style2)
        self.current_time_button.setFixedWidth(98)  # 设置标签的宽度为 100 像素
        self.tuichudenglu.setFixedWidth(80)
        font = QFont('SimSun', 10)
        font.setBold(True)
        self.tuichudenglu.setFont(font)
        self.current_time_button.setFont(font)
        self.gerenzhuye.clicked.connect(self.set_zhuye)
        self.current_time_button.clicked.connect(self.set_current_time)
        self.tuichudenglu.clicked.connect(self.logout)
        horizontal_layout.addWidget(self.current_time_button)

        self.show_info_button = QPushButton("一键排盘")
        self.show_info_button.setFixedWidth(80)
        # 创建阴影效果对象
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)  # 设置阴影模糊半径，调整阴影的模糊程度
        shadow.setXOffset(5)  # 设置阴影在水平方向上的偏移
        shadow.setYOffset(5)  # 设置阴影在垂直方向上的偏移
        # 将阴影效果应用于按钮
        # 设置按钮的样式
        button_style = """
                    QPushButton {
                        background-color: rgb(173, 216, 230);
                        color: red;
                        border: 3px solid gray;
                        border-radius: 10px;
                        padding: 6px;
                        border-style: outset;
                    }

                    QPushButton:hover {
                        background-color: rgb(200, 160, 120);
                        color: white;
                    }
                """
        self.show_info_button.setStyleSheet(button_style)
        # 点击按钮时执行的槽函数
        self.show_info_button.setGraphicsEffect(shadow)
        self.show_info_button.clicked.connect(self.show_info)
        # 设置按钮字体
        font = QFont('SimSun', 10)
        font.setBold(True)
        self.show_info_button.setFont(font)
        horizontal_layout.addWidget(self.show_info_button)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)  # 设置阴影模糊半径，调整阴影的模糊程度
        shadow.setXOffset(5)  # 设置阴影在水平方向上的偏移
        shadow.setYOffset(5)  # 设置阴影在垂直方向上的偏移
        # 创建一个按钮，用于清空所有输出框的内容
        self.clear_button = QPushButton("清空盘面")
        self.clear_button.setFixedWidth(80)
        self.clear_button.setGraphicsEffect(shadow)
        button_style = """
                            QPushButton {
                                background-color: rgb(255, 255, 230);
                                color: black;
                                border: 3px solid gray;
                                border-radius: 10px;
                                padding: 6px;
                                border-style: outset;
                            }

                            QPushButton:hover {
                                background-color: gray;
                                color: white;
                            }
                        """
        self.clear_button.setStyleSheet(button_style)
        # self.clear_button.setGraphicsEffect(shadow)
        self.clear_button.clicked.connect(self.clear_all_outputs)
        self.clear_button.setFont(font)
        horizontal_layout.addWidget(self.clear_button)

        horizontal_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        spacer = QSpacerItem(10, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        horizontal_layout.addItem(spacer)
        horizontal_layout.addWidget(self.tuichudenglu)
        horizontal_layout.addWidget(self.gerenzhuye)

        layout.addLayout(horizontal_layout)
        central_widget.setLayout(layout)
        # 创建定时器，每秒更新一次时间
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # 1000 毫秒 = 1 秒

        self.update_time()  # 初始更新一次时间
        grid_layout1 = QGridLayout()
        # 使用 InputWithComboBox 替代 QLineEdit
        self.time_entry1 = InputWithComboBox(options=[str(i) for i in range(1900, 2101)])
        self.time_entry2 = InputWithComboBox(options=[str(i) for i in range(1, 13)])
        self.time_entry3 = InputWithComboBox(options=[str(i) for i in range(1, 32)])
        self.time_entry4 = InputWithComboBox(options=[str(i) for i in range(0, 24)])
        self.time_entry5 = InputWithComboBox(options=[str(i) for i in range(0, 60)])
        # 设置样式和属性
        for entry in [self.time_entry1, self.time_entry2, self.time_entry3, self.time_entry4, self.time_entry5]:
            entry.input_text.setStyleSheet("border: 2px solid gray;")
            entry.input_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
            entry.input_text.setFixedHeight(30)
        self.time_entry1label = QLabel('年')
        self.time_entry2label = QLabel('月')
        self.time_entry3label = QLabel('日')
        self.time_entry4label = QLabel('时')
        self.time_entry5label = QLabel('分')
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
        self.time_entry1label.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.time_entry2label.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.time_entry3label.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.time_entry4label.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.time_entry5label.setAlignment(Qt.AlignmentFlag.AlignTop)
        margin = 15
        self.time_entry1label.setMargin(margin)
        self.time_entry2label.setMargin(margin)
        self.time_entry3label.setMargin(margin)
        self.time_entry4label.setMargin(margin)
        self.time_entry5label.setMargin(margin)
        layout.addLayout(grid_layout1)
        self.setLayout(layout)
        # 创建一个 QVBoxLayout 用于垂直对齐
        v_layout = QVBoxLayout()
        # 创建一个 QLabel
        self.solar_label = QLabel(
            "输入👆：<font color='red'>阳历</font> 年，月，日，时，分(<font color='purple'>可查范围：1900年2月1日0时0分至2100年12月31日23时59分</font>);")
        # 设置对齐方式为居中
        self.solar_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # 添加 QLabel 到垂直布局中
        v_layout.addWidget(self.solar_label)
        # 将垂直布局添加到父布局
        layout.addLayout(v_layout)
        layout.addWidget(self.solar_label)
        self.lunar_label = QLabel(
            "或者输入👇：<font color='red'>阴历</font> 年，月，日，时辰，节气(<font color='purple'>注意两个历法只能选择一个输入，输入要完整，另一个需留白，阴历输入功能还未实现</font>)。")
        # 设置对齐方式为居中
        self.lunar_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.lunar_label)
        # 添加 QLabel 到垂直布局中

        '''
        # 创建一个 QVBoxLayout 用于垂直对齐

        v_layout = QVBoxLayout()
        # 创建一个 QLabel

        self.lunar_label1 = QLabel("<font color='red'>阴历</font> 年，月，日，时辰")
        # 设置对齐方式为居中
        self.lunar_label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # 添加 QLabel 到垂直布局中
        v_layout.addWidget(self.lunar_label1)
        '''
        # layout.addLayout(v_layout)
        self.shuipingyinglishurushuchubuju = QHBoxLayout()
        self.NIANSHUCHUKUANG_shuru = QLineEdit()
        self.nianlabel = QLabel('年')
        self.YUESHUCHUKUANG_shuru = QLineEdit()
        self.yuelabel = QLabel('月')
        self.RISHUCHUKUANG_shuru = QLineEdit()
        self.rilabel = QLabel('日')
        self.SHISHUCHUKUANG_shuru = QLineEdit()
        self.shilabel = QLabel('时')
        self.JIEQIYDSHUCHU_shuru = QLineEdit()
        self.jieqilabel = QLabel('节气')
        self.YUANRISHUCHU_shuru = QLineEdit()
        self.yuanrilabel = QLabel('日')
        # 阴历输出框的格式
        # 阴历输出框字体调整
        font = QFont('SimSun', 10)
        self.NIANSHUCHUKUANG_shuru.setFont(font)
        self.YUESHUCHUKUANG_shuru.setFont(font)
        self.RISHUCHUKUANG_shuru.setFont(font)
        self.SHISHUCHUKUANG_shuru.setFont(font)
        self.JIEQIYDSHUCHU_shuru.setFont(font)
        self.YUANRISHUCHU_shuru.setFont(font)
        # 设定大小
        self.NIANSHUCHUKUANG_shuru.setFixedSize(114, 30)
        self.YUESHUCHUKUANG_shuru.setFixedSize(114, 30)
        self.RISHUCHUKUANG_shuru.setFixedSize(114, 30)
        self.SHISHUCHUKUANG_shuru.setFixedSize(114, 30)
        self.JIEQIYDSHUCHU_shuru.setFixedSize(114, 30)
        self.YUANRISHUCHU_shuru.setFixedSize(50, 30)
        # 设置不可编辑
        '''
        self.NIANSHUCHUKUANG_shuru.setReadOnly(True)
        self.YUESHUCHUKUANG_shuru.setReadOnly(True)
        self.SHISHUCHUKUANG_shuru.setReadOnly(True)
        self.RISHUCHUKUANG_shuru.setReadOnly(True)
        self.JIEQIYDSHUCHU_shuru.setReadOnly(True)
        self.YUANRISHUCHU_shuru.setReadOnly(True)
        '''

        # label字体调整
        font = QFont('Microsoft YaHei', 10)
        self.nianlabel.setFont(font)
        self.yuelabel.setFont(font)
        self.rilabel.setFont(font)
        self.shilabel.setFont(font)
        self.jieqilabel.setFont(font)
        self.yuanrilabel.setFont(font)
        # 设定边框样式和背景rgb(173, 216, 230)
        self.NIANSHUCHUKUANG_shuru.setStyleSheet("background-color: white;border: 2px solid gray;")  # 设置边框宽度和颜色
        self.YUESHUCHUKUANG_shuru.setStyleSheet("background-color: white;border: 2px solid gray;")  # 设置边框宽度和颜色
        self.RISHUCHUKUANG_shuru.setStyleSheet("background-color: white;border: 2px solid gray;")  # 设置边框宽度和颜色
        self.SHISHUCHUKUANG_shuru.setStyleSheet("background-color: white;border: 2px solid gray;")  # 设置边框宽度和颜色
        self.JIEQIYDSHUCHU_shuru.setStyleSheet("background-color: white;border: 2px solid gray;")  # 设置边框宽度和颜色
        self.YUANRISHUCHU_shuru.setStyleSheet("background-color: white;border: 2px solid gray;")  # 设置边框宽度和颜色
        # 设置对齐方式
        self.NIANSHUCHUKUANG_shuru.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.YUESHUCHUKUANG_shuru.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.RISHUCHUKUANG_shuru.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.SHISHUCHUKUANG_shuru.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.JIEQIYDSHUCHU_shuru.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.YUANRISHUCHU_shuru.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.nianlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.yuelabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.rilabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.shilabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.jieqilabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.yuanrilabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # 加入水平布局
        spacer = QSpacerItem(11, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.shuipingyinglishurushuchubuju.addItem(spacer)
        self.shuipingyinglishurushuchubuju.addWidget(self.NIANSHUCHUKUANG_shuru)
        self.shuipingyinglishurushuchubuju.addWidget(self.nianlabel)
        self.shuipingyinglishurushuchubuju.addWidget(self.YUESHUCHUKUANG_shuru)
        self.shuipingyinglishurushuchubuju.addWidget(self.yuelabel)
        self.shuipingyinglishurushuchubuju.addWidget(self.RISHUCHUKUANG_shuru)
        self.shuipingyinglishurushuchubuju.addWidget(self.rilabel)
        self.shuipingyinglishurushuchubuju.addWidget(self.SHISHUCHUKUANG_shuru)
        self.shuipingyinglishurushuchubuju.addWidget(self.shilabel)
        self.shuipingyinglishurushuchubuju.addWidget(self.JIEQIYDSHUCHU_shuru)
        self.shuipingyinglishurushuchubuju.addWidget(self.jieqilabel)
        # self.shuipingyinglishurushuchubuju.addWidget(self.YUANRISHUCHU_shuru)
        # self.shuipingyinglishurushuchubuju.addWidget(self.yuanrilabel)
        # 加入总布局

        layout.addLayout(self.shuipingyinglishurushuchubuju)
        self.lunar_output1 = QLineEdit()
        self.lunar_output1.setFixedHeight(30)
        self.lunar_output1.setStyleSheet("background-color: rgb(173, 216, 230);border: 2px solid gray;")  # 设置边框宽度和颜色
        self.lunar_output1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lunarjj = createLineEditRightButton2(self.lunar_output1)
        layout.addWidget(self.lunar_output1)

        def replyy():
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
            reply.setIcon(QMessageBox.Icon.NoIcon)
            reply.setWindowTitle("温馨提示")
            reply.setText('该框输出农历干支：天干地支年月日时辰，节气，阴阳遁以及元日等信息。')
            reply.setStandardButtons(QMessageBox.StandardButton.Ok)
            reply.exec()  # 阻塞应用程序直到用户关闭警告框

        lunarjj.clicked.connect(lambda: replyy())
        '''
        self.lunar_label1 = QLabel("<font color='red'>阴历</font> 年，月，日，时辰，节气/阴阳遁，元日")
        # 设置对齐方式为居中
        self.lunar_label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.lunar_label1)

        grid_layout = QGridLayout()
        font = QFont('Microsoft YaHei', 11)
        self.solar_label.setFont(font)  # 将字体应用于 QLabel
        #self.lunar_label1.setFont(font)
        self.lunar_output1.setFont(font)
        self.lunar_output1.setReadOnly(True)
        # 创建标签和第一个输出框，并将它们添加到网格布局
        label1 = QLabel("节气\t阴阳遁")
        label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lunar_output2 = QLineEdit()
        self.lunar_output2.setFixedHeight(30)
        self.lunar_output2.setStyleSheet("background-color: rgb(173, 216, 230);border: 2px solid gray;")  # 设置边框宽度和颜色
        self.lunar_output2.setReadOnly(True)
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
        self.lunar_output3.setReadOnly(True)
        grid_layout.addWidget(label2, 1, 1)  # 第一个参数是小部件，第二个和第三个参数是行和列
        grid_layout.addWidget(self.lunar_output3, 0, 1)
        label1.setFont(font)  # 将字体应用于 QLabel
        label2.setFont(font)
        font = QFont("SimSun", 11)
        self.lunar_output2.setFont(font)
        self.lunar_output3.setFont(font)
        # 将网格布局添加到主布局
        layout.addLayout(grid_layout)
        '''
        self.ws = QLabel('温氏奇门遁甲阴阳九局活用排盘')
        font = QFont('Microsoft YaHei', 20)
        self.ws.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ws.setFont(font)
        layout.addWidget(self.ws)
        # 创建九宫格
        # 创建一个水平布局放置九宫格，目的是为了让这个布局在layout水平方向上的中间位置
        grid_h_layout = QHBoxLayout()
        grid_layout = QGridLayout()
        font = QFont('SimSun', 11)
        tainruju = ['巽四', '离九', '坤二', '震三', '中五', '兑七', '艮八', '坎一', '乾六']
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
                frame.setFixedSize(180, 150)
                label = QLabel(f"格子 {row + 1}-{col + 1}")
                if row == 1 and col == 1:
                    # 创建一个内部的二维布局
                    inner_layout = QGridLayout()

                    output1 = QLabel()
                    #output1.setStyleSheet("background-color: white; border: 2px solid black;")
                    #output1.setFixedSize(75, 30)  # 设置宽度和高度
                    output1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output2 = QLabel()
                    #output2.setStyleSheet("background-color: white; border: 2px solid black;")
                    output2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    #output2.setFixedSize(75, 40)  # 设置宽度和高度
                    #output1.setReadOnly(True)
                    #output2.setReadOnly(True)
                    font = QFont('SimSun', 11)
                    output1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output1.setFont(font)
                    output2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output2.setFont(font)
                    box_names = [f"output_{row}_{col}_1", f"output_{row}_{col}_2"]
                    self.output_boxes.update(
                        {name: output for name, output in zip(box_names, [output1, output2])})
                    '''
                    out1 = QLineEdit()
                    out2 = QLineEdit()
                    out2.setReadOnly(True)
                    out1.setReadOnly(True)
                    out1.setFixedSize(33, 30)  # 设置宽度和高度
                    out2.setFixedSize(33, 40)  # 设置宽度和高度
                    out2.setStyleSheet("background-color: white; border: 2px solid white;")
                    out1.setStyleSheet("background-color: white; border: 2px solid white;")

                    # 添加输出框到二维布局
                    inner_layout.addWidget(out1, 0, 1, 1, 1)
                    inner_layout.addWidget(out2, 1, 1, 1, 1)
                    '''
                    zhongwuSPBJ1 = QHBoxLayout()
                    zhongwuSPBJ2 = QHBoxLayout()
                    zhongwuSPBJ1.addWidget(output1)
                    zhongwuSPBJ2.addWidget(output2)
                    inner_layout.addLayout(zhongwuSPBJ1, 0, 1, 1, 3)  # 左上角
                    inner_layout.addLayout(zhongwuSPBJ2, 1, 1, 1, 3)  # 中间
                    grid_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
                    output1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
                    output2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
                    # 创建长度为2的字符串
                    juzifuchuang = tainruju[row * 3 + col]
                    text1 = QLabel(juzifuchuang)
                    text1.setStyleSheet(" font-weight: bold;")
                    text2 = QLabel("寄二")
                    text2.setStyleSheet(" font-weight: bold;")
                    font = QFont('Microsoft YaHei', 15)
                    text1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    text2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    text1.setFont(font)  # 将字体应用于 QLabel
                    text2.setFont(font)
                    # 添加字符串到二维布局右下角
                    inner_layout.addWidget(text1, 2, 4)
                    inner_layout.addWidget(text2, 2, 0)
                    # 设置内部布局为frame的布局
                    frame.setLayout(inner_layout)
                    # 将QFrame添加到网格布局
                    grid_layout.addWidget(frame, row, col)
                elif row == 0 and col == 2:
                    # 创建一个内部的二维布局
                    inner_layout = QGridLayout()

                    output1 = QLabel()
                    #output1.setStyleSheet("background-color: white; border: 2px solid black;")
                    output1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    #output1.setFixedSize(50, 30)  # 设置宽度和高度
                    output2 = QLabel()
                    #output2.setStyleSheet("background-color: white; border: 2px solid black;")
                    output2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    #output2.setFixedSize(50, 30)
                    output3 = QLabel()
                    #output3.setStyleSheet("background-color: white; border: 2px solid black;")
                    output3.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    #output3.setFixedSize(50, 30)
                    #output2.setReadOnly(True)
                    #output1.setReadOnly(True)
                    #output3.setReadOnly(True)
                    output4 = QLabel()
                    #output4.setStyleSheet("background-color: white; border: 2px solid black;")
                    output4.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    #output4.setReadOnly(True)
                    #output4.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)  # 禁用垂直滚动条
                    #output4.setFixedSize(60, 45)  # 设置宽度和高度
                    output5 = QLabel()
                    #output5.setStyleSheet("background-color: white; border: 2px solid black;")
                    output5.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    #output5.setReadOnly(True)
                    #output5.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)  # 禁用垂直滚动条
                    #output5.setFixedSize(60, 45)  # 设置宽度和高度
                    font = QFont('SimSun', 11)
                    output1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output1.setFont(font)
                    output2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output2.setFont(font)
                    output3.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output3.setFont(font)
                    output4.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output4.setFont(font)
                    output5.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output5.setFont(font)
                    box_names = [f"output_{row}_{col}_1", f"output_{row}_{col}_2", f"output_{row}_{col}_3",
                                 f"output_{row}_{col}_4", f"output_{row}_{col}_5"]
                    self.output_boxes.update(
                        {name: output for name, output in
                         zip(box_names, [output1, output2, output3, output4, output5])})

                    # 添加输出框到二维布局
                    inner_layout.addWidget(output1, 0, 0)  # 左上角
                    inner_layout.addWidget(output2, 2, 0)  # 左下角
                    inner_layout.addWidget(output3, 0, 4)  # 右上角
                    '''
                    inner_layout.addWidget(output4, 1, 3, 1, 2)  # 中间
                    inner_layout.addWidget(output5, 1, 0, 1, 2)  # 中间
                    '''
                    # 创建两个水平布局并将两个输出框添加到水平布局中去
                    Q4 = QHBoxLayout()
                    output4.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    Q4.addWidget(output4)
                    Q5 = QHBoxLayout()
                    output5.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    Q5.addWidget(output5)
                    # 将两个水平布局添加到网格布局器中
                    inner_layout.addLayout(Q4, 1, 3, 1, 2)  # 中间
                    inner_layout.addLayout(Q5, 1, 0, 1, 2)  # 中间

                    # 创建长度为2的字符串
                    juzifuchuang = tainruju[row * 3 + col]
                    text = QLabel(juzifuchuang)
                    text.setStyleSheet(" font-weight: bold;")
                    text3 = QLabel('+')
                    text3.setFixedWidth(8)
                    font = QFont('SimSun', 18)
                    text3.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    font.setBold(True)
                    text3.setFont(font)
                    font = QFont('Microsoft YaHei', 15)
                    text.setFont(font)  # 将字体应用于 QLabel
                    text.setAlignment(Qt.AlignmentFlag.AlignCenter)
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

                    output1 = QLabel()
                    #output1.setStyleSheet("background-color: white; border: 2px solid black;")
                    output1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    #output1.setFixedSize(50, 30)  # 设置宽度和高度
                    output2 = QLabel()
                    #output2.setStyleSheet("background-color: white; border: 2px solid black;")
                    output2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    #output2.setFixedSize(50, 30)
                    output3 = QLabel()
                    #output3.setStyleSheet("background-color: white; border: 2px solid black;")
                    output3.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    #output3.setFixedSize(50, 30)
                    #output2.setReadOnly(True)
                    #output1.setReadOnly(True)
                    #output3.setReadOnly(True)
                    output4 = QLabel()
                    #output4.setStyleSheet("background-color: white; border: 2px solid black;")
                    output4.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    #output4.setReadOnly(True)
                    #output4.setFixedSize(60, 45)  # 设置宽度和高度
                    output5 = QLabel()
                    #output5.setStyleSheet("background-color: white; border: 2px solid black;")
                    output5.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    #output5.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
                    #output5.setReadOnly(True)
                    #output5.setFixedSize(60, 45)  # 设置宽度和高度
                    font = QFont('SimSun', 11)
                    output1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output1.setFont(font)
                    output2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output2.setFont(font)
                    output3.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output3.setFont(font)
                    output4.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output4.setFont(font)
                    output5.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output5.setFont(font)
                    box_names = [f"output_{row}_{col}_1", f"output_{row}_{col}_2", f"output_{row}_{col}_3",
                                 f"output_{row}_{col}_4", f"output_{row}_{col}_5"]
                    self.output_boxes.update(
                        {name: output for name, output in
                         zip(box_names, [output1, output2, output3, output4, output5])})

                    # 添加输出框到二维布局
                    inner_layout.addWidget(output1, 0, 0)  # 左上角
                    inner_layout.addWidget(output2, 2, 0)  # 左下角
                    inner_layout.addWidget(output3, 0, 4)  # 右上角
                    '''
                    inner_layout.addWidget(output4, 1, 3,1,2)  # 中间
                    inner_layout.addWidget(output5, 1, 0,1,2)  # 中间
                    '''
                    Q4 = QHBoxLayout()
                    output4.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    Q4.addWidget(output4)
                    Q5 = QHBoxLayout()
                    output5.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    Q5.addWidget(output5)
                    # 将两个水平布局添加到网格布局器中
                    inner_layout.addLayout(Q4, 1, 3, 1, 2)  # 中间
                    inner_layout.addLayout(Q5, 1, 0, 1, 2)  # 中间

                    # 创建长度为2的字符串
                    juzifuchuang = tainruju[row * 3 + col]
                    text = QLabel(juzifuchuang)
                    text.setStyleSheet(" font-weight: bold;")
                    text3 = QLabel('+')
                    text3.setFixedWidth(8)
                    font = QFont('SimSun', 18)
                    font.setBold(True)
                    text3.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    text.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    text3.setFont(font)
                    font = QFont('Microsoft YaHei', 15)
                    text.setFont(font)  # 将字体应用于 QLabel
                    # 添加字符串到二维布局右下角
                    inner_layout.addWidget(text, 2, 4)
                    inner_layout.addWidget(text3, 1, 2)

                    # 设置内部布局为frame的布局
                    frame.setLayout(inner_layout)
                    # 将QFrame添加到网格布局
                    grid_layout.addWidget(frame, row, col)
        grid_h_layout.addLayout(grid_layout)
        layout.addLayout(grid_h_layout)
        self.info_label = QLabel()
        layout.addWidget(self.info_label)
        central_widget.setLayout(layout)
        # 将内容窗口设置为可滚动区域的小部件
        scroll_area.setWidget(central_widget)
        # 将可滚动区域设置为主窗口的中央部件
        self.setCentralWidget(scroll_area)

    def update_time(self):
        # 获取当前时间
        current_time = QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")
        # 更新时间显示
        self.time_label.setText(f"当前时间: {current_time}")

    def show_info(self):
        base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
        # 访问数据文件的路径
        image_path1 = os.path.join(base_path, 'JGT.png')
        ye = self.time_entry1.input_text.text()
        mo = self.time_entry2.input_text.text()
        da = self.time_entry3.input_text.text()
        ho = self.time_entry4.input_text.text()
        mi = self.time_entry5.input_text.text()
        if ye == "" and mo == "" and da == "" and ho == "" and mi == "":
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
                                                style = "padding-top: 8px; border: 2px solid black;"
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
                                                style = "padding-top: 8px; border: 2px solid black;"
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
                                                         i - sanqiliuyilaodagonghaozhuandong]) <= 3:
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
                                                style = "padding-top: 10px; border: 2px solid black;"
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

                            self.lunar_output1.setText(
                                ' %s%s年(属%s,%s)''\t''%s%s月''\t''%s%s日''\t''%s%s时''\t''%s''\t''%s''\t''%s日' % (
                                    tg, dz, shengxiaonian, NIANFEN, yuetiangangengxin, yuedizhigengxin, ritiangan,
                                    ridizhi,
                                    shichengtiangan,
                                    shichengdizhi, JQ, YD, yuanri))
                            '''
                            self.lunar_output2.setText('%s''\t''%s' % (JQ, YD))
                            self.lunar_output3.setText('%s日' % (yuanri))
                            '''
                            # 阴历时间输出
                            self.NIANSHUCHUKUANG_shuru.setText(' %s%s' % (tg, dz))
                            self.YUESHUCHUKUANG_shuru.setText('%s%s' % (yuetiangangengxin, yuedizhigengxin))
                            self.RISHUCHUKUANG_shuru.setText('%s%s' % (ritiangan, ridizhi))
                            self.SHISHUCHUKUANG_shuru.setText('%s%s' % (shichengtiangan, shichengdizhi))
                            self.JIEQIYDSHUCHU_shuru.setText('%s' % (JQ))
                            # self.YUANRISHUCHU_shuru.setText('%s' % (yuanri))
                            info = f"你输入的时间是：{user_time}"
                            self.info_label.setText(info)
                            font = QFont('SimSun', 11)
                            self.output_boxes['output_0_2_4'].setAlignment(Qt.AlignmentFlag.AlignCenter)


                else:
                    # 用户输入的时间信息不正确，显示警告
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

                    reply.setText("输入的时间数值超出有效范围了呢，重新输入一下吧。")
                    reply.setStandardButtons(QMessageBox.StandardButton.Ok)
                    reply.exec()  # 阻塞应用程序直到用户关闭警告框

    '''
    def closeEvent(self, event):
        # 重定义窗口关闭事件，只有用户明确主动关闭窗口才会退出应用程序
        reply = QMessageBox.question(self, '用户提出退出请求', '确认退出应用程序吗？',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()
    '''

    def clear_all_outputs(self):
        self.time_entry1.input_text.clear()
        self.time_entry2.input_text.clear()
        self.time_entry3.input_text.clear()
        self.time_entry4.input_text.clear()
        self.time_entry5.input_text.clear()
        '''

        self.lunar_output2.clear()
        self.lunar_output3.clear()
        '''
        self.lunar_output1.clear()
        self.NIANSHUCHUKUANG_shuru.clear()
        self.YUESHUCHUKUANG_shuru.clear()
        self.RISHUCHUKUANG_shuru.clear()
        self.SHISHUCHUKUANG_shuru.clear()
        self.JIEQIYDSHUCHU_shuru.clear()
        self.YUANRISHUCHU_shuru.clear()

        for row in range(3):
            for col in range(3):
                if row == 1 and col == 1:
                    for i in range(1, 3):  # 清空output_0_0_1、output_0_0_2、output_0_0_3等
                        output_name = f"output_{row}_{col}_{i}"
                        self.output_boxes[output_name].clear()
                else:
                    for i in range(1, 6):  # 清空output_0_0_1、output_0_0_2、output_0_0_3等
                        output_name = f"output_{row}_{col}_{i}"
                        self.output_boxes[output_name].clear()


class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.config = configparser.ConfigParser()

        def createLineEditRightButton2(edit):
            base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
            # 访问数据文件的路径
            image_path1 = os.path.join(base_path, 'YHM.png')
            left_button = QPushButton()
            left_button.setCursor(Qt.CursorShape.ArrowCursor)
            # left_button.setStyleSheet("border: none;")
            icon = QIcon(image_path1)  # 替换成您的图标文件路径
            left_button.setIcon(icon)
            layout = QHBoxLayout()
            style_sheet = "padding-left: 18px; "
            edit.setStyleSheet(style_sheet)
            style_sheet1 = "padding-left: 0px; border: none; "
            left_button.setStyleSheet(style_sheet1)
            layout.addWidget(left_button)
            layout.addStretch()
            layout.setContentsMargins(0, 0, 0, 0)
            edit.setLayout(layout)
            return left_button

        def createLineEditRightButton(edit):
            left_button = QPushButton()

            left_button.setCursor(Qt.CursorShape.ArrowCursor)
            base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
            # 访问数据文件的路径
            image_path1 = os.path.join(base_path, 'MIM.jpg')
            image_path2 = os.path.join(base_path, 'YJ.png')
            # left_button.setStyleSheet("border: none;")
            icon = QIcon(image_path1)  # 替换成您的图标文件路径
            left_button.setIcon(icon)
            button = QPushButton()
            layout = QHBoxLayout()
            button.setCursor(Qt.CursorShape.ArrowCursor)
            # 设置按钮的图标
            icon = QIcon(image_path2)  # 替换成您的图标文件路径
            button.setIcon(icon)
            # 使用样式表去除按钮的边框
            button.setStyleSheet("border: none;")

            # layout.addWidget(left_button)
            style_sheet = "padding-left: 18px; "
            edit.setStyleSheet(style_sheet)
            style_sheet1 = "padding-left: 0px; border: none; "
            left_button.setStyleSheet(style_sheet1)
            layout.addWidget(left_button)
            layout.addStretch()
            layout.addWidget(button)
            layout.setContentsMargins(0, 0, 0, 0)
            edit.setLayout(layout)
            return button

        def togglePasswordVisibility(password_edit):
            if password_edit.echoMode() == QLineEdit.EchoMode.Normal:
                password_edit.setEchoMode(QLineEdit.EchoMode.Password)
            else:
                password_edit.setEchoMode(QLineEdit.EchoMode.Normal)

        base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
        # 访问数据文件的路径
        image_path1 = os.path.join(base_path, 'BJJ.png')
        image_path2 = os.path.join(base_path, 'TTB.jpg')

        background_image = QPixmap(image_path1)  # 替换为您的背景图像文件路径
        background_image = background_image.scaled(self.width(), self.height())

        # 将背景图像设置为窗口的背景
        pixmap = background_image.scaled(self.size(), Qt.AspectRatioMode.IgnoreAspectRatio)
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(pixmap))
        self.setPalette(palette)

        self.setWindowTitle("温氏奇门遁甲阴阳九局活用预测排盘登录")
        self.setGeometry(100, 100, 740, 480)  # 增加宽度以容纳图像
        self.setFixedSize(740, 480)  # 设置窗口的固定大小
        # 设置窗口图标
        self.setWindowIcon(QIcon(image_path2))  # 替换成您的图标文件路径

        # 设置窗口背景颜色为纯白
        # self.setStyleSheet("background-color: white;")
        layout = QHBoxLayout()  # 使用水平布局包含图像和登录部分

        # 添加图像到左边
        '''
        image_label = QLabel()
        pixmap = QPixmap(image_path2)  # 替换为你的图像文件路径
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        image_label.setFixedWidth(550)
        layout.addWidget(image_label)
        '''
        # 登录部分

        login_layout = QVBoxLayout()
        login_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)  # 登录部分居中
        label11 = QLabel("奇门遁甲")
        label22 = QLabel("阴阳九局预测排盘")
        label22.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label33 = QLabel("排盘帐号登录")
        label33.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font4 = QFont()
        font4.setFamily("KaiTi")  # 设置字体样式为Comic Sans MS，这是一种草书风格的字体
        font4.setPointSize(13)  # 设置字体大小
        font4.setBold(True)
        label33.setFont(font4)  # 应用字体到标签
        font = QFont()
        font.setFamily("KaiTi")  # 设置字体样式为Comic Sans MS，这是一种草书风格的字体
        font.setPointSize(16)  # 设置字体大小
        label11.setFont(font)  # 应用字体到标签
        label1 = QLabel("South China University Of Technology")
        label2 = QLabel("School of Business Administration")
        label3 = QLabel('LiFeng')
        label5 = QLabel('2023年9月')
        label4 = QLabel('phone: 13786866211 ')
        label6 = QLabel(' Email: lfie2022@outlook.com')
        label11.setFont(font)
        font2 = QFont()
        font2.setFamily("KaiTi")  # 设置字体样式为Comic Sans MS，这是一种草书风格的字体
        font2.setPointSize(15)  # 设置字体大小
        label22.setFont(font2)
        font1 = QFont()
        font1.setFamily("KaiTi")  # 设置字体样式为Comic Sans MS，这是一种草书风格的字体
        font1.setPointSize(8)  # 设置字体大小
        label1.setFont(font1)
        label2.setFont(font1)
        label3.setFont(font1)
        label4.setFont(font1)
        label5.setFont(font1)
        label6.setFont(font1)
        label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label1.setStyleSheet("color: white;")  # 设置文本颜色为红色
        label2.setStyleSheet("color: white;")  # 设置文本颜色为红色
        label3.setStyleSheet("color: white;")  # 设置文本颜色为红色
        label4.setStyleSheet("color: white;")  # 设置文本颜色为红色
        label5.setStyleSheet("color: white;")  # 设置文本颜色为红色
        label6.setStyleSheet("color: white;")  # 设置文本颜色为红色
        label11.setStyleSheet("color: rgb(255,255,155);")  # 设置文本颜色为红色
        label22.setStyleSheet("color: rgb(255,255,155);")  # 设置文本颜色为红色
        label33.setStyleSheet("color: rgb(255,255,255);")
        # 在登录部分上方添加一张图片
        '''
        top_image_label = QLabel()
        top_pixmap = QPixmap(image_path1)  # 替换为您的顶部图片文件路径
        top_image_label.setPixmap(top_pixmap)
        login_layout.addWidget(top_image_label)
        '''
        self.setStyleSheet('''
                            QLineEdit{
                                border: 2px solid gray;
                                border-radius: 12px;
                            }
                            ''')
        # 在登录部分中设置用户名和密码输入框的样式和提示文字

        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        username_button = createLineEditRightButton2(self.username_input)

        password_button = createLineEditRightButton(self.password_input)
        password_button.clicked.connect(lambda: togglePasswordVisibility(self.password_input))
        self.username_input.setFixedWidth(165)
        self.password_input.setFixedWidth(165)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        login_button = QPushButton("登录")
        register_button = QPushButton("注册")
        login_button.setFixedWidth(165)
        register_button.setFixedWidth(165)
        denglubuju = QHBoxLayout()
        zhucebuju = QHBoxLayout()
        zhuce_label = QLabel("没有帐户请申请注册↓")
        zhuce_label.setStyleSheet("color: red;")  # 设置文本颜色为红色
        zhuce_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        login_button.setStyleSheet("background-color: rgb(173, 216, 230); color: black;")
        register_button.setStyleSheet("background-color: rgb(173, 216, 230); color: black;")
        self.username_input.setPlaceholderText("用户名")
        self.password_input.setPlaceholderText("密码")
        # self.username_input.setStyleSheet("color: black;")
        # self.password_input.setStyleSheet("color: black;")
        denglubuju.addStretch(1)  # 添加一个伸缩项，将按钮推到布局的中间
        denglubuju.addWidget(login_button)
        denglubuju.addStretch(1)
        zhucebuju.addStretch(1)
        zhucebuju.addWidget(register_button)
        zhucebuju.addStretch(1)
        '''
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.username_input.setFixedWidth(150)
        self.password_input.setFixedWidth(150)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        login_button = QPushButton("登录")

        '''
        self.login_status_label = QLabel()  # 用于显示登录状态信息
        self.login_status_label.setStyleSheet("color: red;")  # 设置文本颜色为红色
        self.login_status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # username_label = QLabel("用户名:")
        username_layout = QHBoxLayout()
        # sername_layout.addWidget(username_label)
        username_layout.addWidget(self.username_input)
        # password_label = QLabel("密码:")
        password_layout = QHBoxLayout()
        # password_layout.addWidget(password_label)
        password_layout.addWidget(self.password_input)
        spacer = QSpacerItem(520, 1, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        layout.addItem(spacer)
        spacer = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        login_layout.addItem(spacer)
        login_layout.addWidget(label11)
        login_layout.addWidget(label22)
        spacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        login_layout.addItem(spacer)
        login_layout.addWidget(label33)

        login_layout.addLayout(username_layout)
        login_layout.addLayout(password_layout)
        login_layout.addLayout(denglubuju)
        login_layout.addWidget(zhuce_label)
        login_layout.addLayout(zhucebuju)
        login_layout.addWidget(self.login_status_label)
        spacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        login_layout.addItem(spacer)
        '''
        login_layout.addWidget(label1)
        login_layout.addWidget(label2)
        login_layout.addWidget(label3)
        login_layout.addWidget(label5)
        login_layout.addWidget(label4)
        login_layout.addWidget(label6)
        '''

        # 右侧登录部分占据右边总空间的1/3
        right_widget = QWidget()
        right_layout = QVBoxLayout()
        right_widget.setLayout(right_layout)
        right_widget.setFixedWidth(10)
        # layout.addWidget(right_widget)  # 添加右侧部分到布局中
        layout.addLayout(login_layout)  # 添加登录部分到布局中
        self.setLayout(layout)
        login_button.clicked.connect(self.login)
        register_button.clicked.connect(self.register)
        # 初始化注册代码和注册状态
        self.register_codes = {"LF2000": True, "CS0183": True}
        self.is_registered = False
        self.current_username = "lf"
        self.current_password = "20001122"
        self.load_config()  # 在初始化时加载配置
        self.original_username = "1"  # 初始用户名
        self.original_password = "1"  # 初始密码

    def login(self):
        # 在这里进行登录验证，比如检查用户名和密码是否正确
        username = self.username_input.text()
        password = self.password_input.text()

        if (username == self.original_username and password == self.original_password) or \
                (username == self.current_username and password == self.current_password):
            self.login_status_label.setText("登录成功")  # 设置登录成功提示
            self.accept()  # 用户登录成功，使用 accept() 方法来指示成功
        else:
            self.login_status_label.setText("用户名或密码不正确")  # 设置登录失败提示

    def register(self):
        code, ok = QInputDialog.getText(self, "注册", "请输入注册代码:")
        if ok and code in self.register_codes and self.register_codes[code]:
            new_username, ok1 = QInputDialog.getText(self, "注册", "请输入新用户名:")
            new_password, ok2 = QInputDialog.getText(self, "注册", "请输入新密码:")
            if ok1 and ok2 and new_username and new_password:
                # 注册成功，更新注册状态和用户名密码
                self.is_registered = True
                self.update_credentials(new_username, new_password)
                self.current_username = new_username
                self.current_password = new_password
                self.login_status_label.setText("注册成功")
                self.save_config()  # 保存配置
                # 将注册代码标记为已使用
                self.register_codes[code] = False
            else:
                self.login_status_label.setText("新用户名和密码不能为空")
        else:
            self.login_status_label.setText("未输入注册代码或注册代码错误")

    def update_credentials(self, new_username, new_password):
        self.username_input.setText(new_username)
        self.password_input.setText(new_password)

    def load_config(self):
        if os.path.exists('config.ini'):
            self.config.read('config.ini')
            credentials = self.config['Credentials']
            self.current_username = credentials.get('current_username', '')
            self.current_password = credentials.get('current_password', '')

    def save_config(self):
        self.config['Credentials'] = {
            'current_username': self.current_username,
            'current_password': self.current_password
        }

        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)

    def closeEvent(self, event):
        # 重定义窗口关闭事件，只有用户明确主动关闭窗口才会退出应用程序
        reply = QMessageBox.question(self, '用户提出退出请求', '确认退出应用程序吗？',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
            QApplication.instance().quit()
        else:
            event.ignore()


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