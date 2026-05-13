import configparser
import sys
import os
import calendar
import datetime
import re
from zhdate import ZhDate

_SOLAR_INPUT_RE = re.compile(r'(\d{0,5})年(\d{1,3})月(\d{1,3})[号日]?(\d{1,3})[点时]?(\d{1,3})分?')

# 启动时确保"配置/"目录存在；登录、记住密码等模块会写入该目录。
try:
    os.makedirs('配置', exist_ok=True)
except OSError:
    pass
from spadigix_core import (
    LUNAR_DAY_TEXT_TO_NUMBER,
    LUNAR_MONTH_TEXT_TO_NUMBER,
    SIXTY_GANZHI,
    SOLAR_TERMS,
    build_chart_from_ganzhi,
    build_chart_from_lunar_date,
    build_chart_from_solar,
    fields_for_lunar_input_button,
)
from PyQt6.QtWidgets import QTextBrowser, QApplication, QDialog, QMainWindow, QWidget, QVBoxLayout, QLabel, QHBoxLayout, \
    QLineEdit, QGridLayout, QPushButton, QFrame, QMessageBox,QStackedWidget,QCheckBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QTimer, QDateTime
from PyQt6.QtGui import QPixmap, QBrush, QIcon,QPainter,QColor
from PyQt6.QtGui import QPalette
from PyQt6.QtWidgets import QComboBox, QScrollArea, QGraphicsDropShadowEffect, QInputDialog, QSizePolicy, QSpacerItem, \
    QSplashScreen


class InputWithComboBox(QWidget):
    def __init__(self, options=None):
        super().__init__()
        base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
        # 访问数据文件的路径
        image_path1 = os.path.join(base_path, '资源图片', 'XLJT.png')

        layout = QVBoxLayout()

        self.input_text = QLineEdit()
        self.combo_box = QComboBox()
        self.combo_box.setFixedSize(63,23)
        self.combo_box.setStyleSheet("""
            QComboBox {
                background-color: white; /* 设置背景颜色 */
                color: black; /* 设置文本颜色 */
                border: 1px solid #CCC; /* 设置边框样式 */
                padding: 5px; /* 设置内边距 */
            }
            QComboBox::drop-down {
                width: 20px; /* 设置下拉箭头的宽度 */

            }
             QComboBox::down-arrow {
        ; /* 设置下拉箭头的图像 */
            }
        """)

        if options:
            self.combo_box.addItems(options)

        layout.addWidget(self.input_text)

        # 创建左右箭头按钮
        self.left_arrow_button = QPushButton("<")
        self.right_arrow_button = QPushButton(">")
        button_style = """
                            QPushButton {
                                background-color: white;
                                color: black;
                                border: 1px solid gray;
                                border-radius: 2px;
                            }
                            QPushButton:hover {
                                background-color: white;
                                color: red;
                            }
                        """
        self.left_arrow_button.setStyleSheet(button_style)
        self.right_arrow_button.setStyleSheet(button_style)
        self.right_arrow_button.setFixedWidth(9)
        self.left_arrow_button.setFixedWidth(9)
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

    def clearr(self):
        self.input_text.clear()

    def setLineEditText(self, text):
        self.input_text.setText(text)

    def set_input_text(self, text):
        self.input_text.setText(text)

    def increment_value(self):
        current_index = self.combo_box.currentIndex()
        if current_index < self.combo_box.count() - 1:
            self.combo_box.setCurrentIndex(current_index + 1)

    def decrement_value(self):
        current_index = self.combo_box.currentIndex()
        if current_index > 0:
            self.combo_box.setCurrentIndex(current_index - 1)


class TimeInfoApp(QMainWindow):
    def toggle_layouts(self):
        self.current_layout = (self.current_layout + 1) % 3
        self.stacked_widget.setCurrentIndex(self.current_layout)
        self.cunfanghuoqushijianbuju.setCurrentIndex(self.current_layout)


    def set_zhuye(self):
        base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
        image_path1 = os.path.join(base_path, '资源图片', 'JGT.png')
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
    def set_current_time_nongli(self):
        current_datetime = datetime.datetime.now()
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
        self.NIANSHUCHUKUANGNONGLI_shuru.input_text.setText(str(lunar_year))
        self.YUESHUCHUKUANGNONGLI_shuru.input_text.setText(str(lunar_month))
        self.RISHUCHUKUANGNONGLI_shuru.input_text.setText(str(lunar_day))
        self.SHISHUCHUKUANGNONGLI_shuru.input_text.setText(str(solar_hour))
        self.JIEQIYDSHUCHUNONGLI_shuru.input_text.setText(str(solar_minute))


    def set_current_time_lunar(self):
        now = datetime.datetime.now()
        f_year, f_month, f_day, f_hour, f_jq = fields_for_lunar_input_button(
            now.year, now.month, now.day, now.hour
        )
        self.NIANSHUCHUKUANG_shuru.input_text.setText(f_year)
        self.YUESHUCHUKUANG_shuru.input_text.setText(f_month)
        self.RISHUCHUKUANG_shuru.input_text.setText(f_day)
        self.SHISHUCHUKUANG_shuru.input_text.setText(f_hour)
        self.JIEQIYDSHUCHU_shuru.input_text.setText(f_jq)

    def __init__(self):
        super().__init__()

        def createLineEditRightButton2(edit):
            base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
            # 访问数据文件的路径
            image_path1 = os.path.join(base_path, '资源图片', 'TGDI.png')
            left_button = QPushButton()
            left_button.setCursor(Qt.CursorShape.ArrowCursor)
            left_button.setFixedSize(25, 25)
            left_button.setStyleSheet("border: none;")
            icon = QIcon(image_path1)  # 替换成您的图标文件路径
            left_button.setIcon(icon)
            left_button.setIconSize(left_button.size())
            layout = QHBoxLayout()
            style_sheet = "background-color: rgb(173, 216, 230);border: 2px solid gray;padding-left: 18px; "
            edit.setStyleSheet(style_sheet)
            edit.setReadOnly(True)
            style_sheet1 = "padding-left: 1px; border: none; "
            left_button.setStyleSheet(style_sheet1)
            layout.addWidget(left_button)
            layout.addStretch()
            layout.setContentsMargins(0, 0, 0, 0)
            edit.setLayout(layout)
            return left_button

        def createLineEditRightButton3(edit):
            base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
            # 访问数据文件的路径
            image_path1 = os.path.join(base_path, '资源图片', 'TTB.png')
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
            # edit.setReadOnly(True)
            style_sheet1 = "padding-left: 0px; border: none; "
            left_button.setStyleSheet(style_sheet1)
            layout.addWidget(left_button)
            layout.addStretch()
            layout.setContentsMargins(0, 0, 0, 0)
            edit.setLayout(layout)
            return left_button

        self.setWindowTitle("温氏奇门遁甲阴阳九局活用预测排盘")
        self.setGeometry(310, 30, 838, 800)  # 设置窗口大小和位置
        self.setMinimumSize(20, 20)  # 设置窗口的固定大小
        #self.setStyleSheet("#centralwidget{border-image:url(./BJJ.png);}")


        scroll_area = QScrollArea()

        central_widget = QWidget()
        layout = QVBoxLayout()
        self.stacked_widget = QStackedWidget()
        base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
        # 访问数据文件的路径
        image_path1 = os.path.join(base_path, '资源图片', 'TTB.jpg')
        image_path2 = os.path.join(base_path, '资源图片', 'JGT.png')
        image_path3 = os.path.join(base_path, '资源图片', 'YHTB.jpg')
        im = os.path.join(base_path, '资源图片', 'BJJ.png')
        self.setWindowIcon(QIcon(image_path1))
        palette = QPalette()


        palette.setColor(QPalette.ColorRole.Window, QColor(255, 255, 255))  # 背景颜色为白色
        # palette.setColor(QPalette.ColorRole.Window, QColor(200, 160, 120))  # 背景颜色为浅棕色
        self.setPalette(palette)

        horizontal_layout = QHBoxLayout()
        background_image = QPixmap(im)
        #central_widget.background_image = background_image
        #central_widget.setStyleSheet("background-image: url(AAA.png); background-repeat: no-repeat;")
        #scroll_area.setStyleSheet("background: transparent;")
        layout.setContentsMargins(0, 0, 0, 0)

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
        self.time_label.setFixedWidth(290)  # 设置标签的宽度为 100 像素
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        horizontal_layout.addWidget(self.time_label)
        self.current_layout = 0  # 当前可见的布局索引
        button_toggle_layouts = QPushButton("切换输入历法")
        button_toggle_layouts.clicked.connect(self.toggle_layouts)
        button_toggle_layouts.clicked.connect(self.clear_all_outputs)

        self.cunfanghuoqushijianbuju=QStackedWidget()
        self.current_time_button = QPushButton("获取当前时间.阳")
        self.current_time_lunar_button = QPushButton("获取当前时间.阴")
        self.current_time_lunar_button_nongli=QPushButton("获取当前时间.农")
        font = QFont('SimSun', 10)
        font.setBold(True)
        self.tuichudenglu.setFont(font)
        self.current_time_lunar_button.setFont(font)
        self.current_time_button.setFont(font)
        self.current_time_lunar_button_nongli.setFont(font)
        self.time_label.setFont(font)
        button_toggle_layouts.setFont(font)
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
        self.current_time_lunar_button.setStyleSheet(button_style)
        self.current_time_lunar_button_nongli.setStyleSheet(button_style)
        button_toggle_layouts.setStyleSheet(button_style)
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
        shadow3 = QGraphicsDropShadowEffect(self)
        shadow3.setBlurRadius(10)  # 设置阴影模糊半径，调整阴影的模糊程度
        shadow3.setXOffset(0)  # 设置阴影在水平方向上的偏移
        shadow3.setYOffset(0)  # 设置阴影在垂直方向上的偏移
        self.current_time_button.setGraphicsEffect(shadow3)
        shadow2 = QGraphicsDropShadowEffect(self)
        shadow2.setBlurRadius(10)  # 设置阴影模糊半径，调整阴影的模糊程度
        shadow2.setXOffset(0)  # 设置阴影在水平方向上的偏移
        shadow2.setYOffset(0)  # 设置阴影在垂直方向上的偏移
        self.current_time_lunar_button.setGraphicsEffect(shadow2)
        shadow1 = QGraphicsDropShadowEffect(self)
        shadow1.setBlurRadius(10)  # 设置阴影模糊半径，调整阴影的模糊程度
        shadow1.setXOffset(0)  # 设置阴影在水平方向上的偏移
        shadow1.setYOffset(0)  # 设置阴影在垂直方向上的偏移
        self.current_time_lunar_button_nongli.setGraphicsEffect(shadow1)
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(10)  # 设置阴影模糊半径，调整阴影的模糊程度
        shadow.setXOffset(5)  # 设置阴影在水平方向上的偏移
        shadow.setYOffset(5)  # 设置阴影在垂直方向上的偏移
        button_toggle_layouts.setGraphicsEffect(shadow)
        self.tuichudenglu.setStyleSheet(button_style2)
        self.current_time_button.setFixedWidth(120)  # 设置标签的宽度为 100 像素
        self.current_time_lunar_button.setFixedWidth(120)
        self.current_time_lunar_button_nongli.setFixedWidth(120)
        button_toggle_layouts.setFixedWidth(110)
        self.tuichudenglu.setFixedWidth(80)
        font = QFont('SimSun', 10)
        font.setBold(True)
        self.tuichudenglu.setFont(font)
        self.current_time_button.setFont(font)
        self.gerenzhuye.clicked.connect(self.set_zhuye)
        self.current_time_button.clicked.connect(self.set_current_time)
        self.current_time_lunar_button.clicked.connect(self.set_current_time_lunar)
        #获取能力时间函数连接
        self.current_time_lunar_button_nongli.clicked.connect(self.set_current_time_nongli)


        self.tuichudenglu.clicked.connect(self.logout)
        #将获取时间按钮放入切换容器
        self.cunfanghuoqushijianbuju.addWidget(self.current_time_button)
        self.cunfanghuoqushijianbuju.addWidget(self.current_time_lunar_button)
        self.cunfanghuoqushijianbuju.addWidget(self.current_time_lunar_button_nongli)

        horizontal_layout.addWidget(self.cunfanghuoqushijianbuju)
        horizontal_layout.addWidget(button_toggle_layouts)
        self.current_time_button.setGraphicsEffect(shadow3)
        self.current_time_lunar_button.setGraphicsEffect(shadow2)
        self.current_time_lunar_button_nongli.setGraphicsEffect(shadow1)

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
        horizontal_layout.addWidget(self.tuichudenglu)
        horizontal_layout.addWidget(self.gerenzhuye)

        layout.addLayout(horizontal_layout)
        central_widget.setLayout(layout)
        # 创建定时器，每秒更新一次时间
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # 1000 毫秒 = 1 秒

        self.update_time()  # 初始更新一次时间
        grid_layout1shuipingbuju = QHBoxLayout()
        grid_layout1 = QGridLayout()
        grid_layout1.setSpacing(0)

        # 使用 InputWithComboBox 替代 QLineEdit
        self.time_entry1 = InputWithComboBox(options=[str(i) for i in range(1900, 2101)])
        '''
        lunarjj2 = createLineEditRightButton3(self.time_entry1)
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
        lunarjj2.clicked.connect(replyy())
        '''
        self.time_entry2 = InputWithComboBox(options=[str(i) for i in range(1, 13)])
        self.time_entry3 = InputWithComboBox(options=[str(i) for i in range(1, 32)])
        self.time_entry4 = InputWithComboBox(options=[str(i) for i in range(0, 24)])
        self.time_entry5 = InputWithComboBox(options=[str(i) for i in range(0, 60)])
        # 设置样式和属性
        base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
        image_path3 = os.path.join(base_path, '资源图片', 'TTB.png')
        self.TISHIYANG = QPushButton()
        self.TISHIYANG.setFixedSize(19, 19)
        icon = QIcon(image_path3)
        self.TISHIYANG.setIcon(icon)
        self.TISHIYANG.setIconSize(self.TISHIYANG.size())  # 设置图标大小与按钮大小相同
        self.TISHIYANG.setStyleSheet("border: none;")

        def replyyy():
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
            reply.setText(
                '输入👉：<font color=red>阳历</font> 年，月，日，时，分(<font color=purple>可查范围：1900年2月1日0时0分至2100年12月31日23时59分</font>)。')
            reply.setStandardButtons(QMessageBox.StandardButton.Ok)
            reply.exec()  # 阻塞应用程序直到用户关闭警告框

        self.TISHIYANG.clicked.connect(lambda: replyyy())

        for entry in [self.time_entry1, self.time_entry2, self.time_entry3, self.time_entry4, self.time_entry5]:
            entry.input_text.setStyleSheet("border: 2px solid gray;")
            entry.input_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
            entry.input_text.setFixedSize(90, 25)
        self.time_entry1label = QLabel('年')
        self.time_entry2label = QLabel('月')
        self.time_entry3label = QLabel('日')
        self.time_entry4label = QLabel('时')
        self.time_entry5label = QLabel('分')
        font = QFont('Microsoft YaHei', 10)
        self.time_entry1label.setFont(font)
        self.time_entry2label.setFont(font)
        self.time_entry3label.setFont(font)
        self.time_entry4label.setFont(font)
        self.time_entry5label.setFont(font)
        # self.TISHIYANG.setStyleSheet("padding-left:10px;")
        SS=QLineEdit()
        SS.setFixedSize(8,30)
        SS.setReadOnly(True)
        SS.setStyleSheet("border:none")
        grid_layout1.addWidget(SS, 0, 0)


        grid_layout1.addWidget(self.TISHIYANG, 0, 1)
        grid_layout1.addWidget(self.time_entry1, 0, 2)
        grid_layout1.addWidget(self.time_entry1label, 0, 3)
        grid_layout1.addWidget(self.time_entry2, 0, 4)
        grid_layout1.addWidget(self.time_entry2label, 0, 5)
        grid_layout1.addWidget(self.time_entry3, 0, 6)
        grid_layout1.addWidget(self.time_entry3label, 0, 7)
        grid_layout1.addWidget(self.time_entry4, 0, 8)
        grid_layout1.addWidget(self.time_entry4label, 0, 9)
        grid_layout1.addWidget(self.time_entry5, 0, 10)
        grid_layout1.addWidget(self.time_entry5label, 0, 11)
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
        grid_layout1shuipingbuju.addLayout(grid_layout1)
        FANGYANGLIRONGQI=QWidget()
        FANGYANGLIRONGQI.setLayout(grid_layout1shuipingbuju)
        self.stacked_widget.addWidget(FANGYANGLIRONGQI)

        # 创建一个空的垂直间隔部件，并设置大小策略以控制垂直距离

        '''
        # 创建一个 QVBoxLayout 用于垂直对齐
        v_layout = QVBoxLayout()
        # 创建一个 QLabel
        self.solar_label = QLabel(
            "输入👉：<font color='red'>阳历</font> 年，月，日，时，分(<font color='purple'>可查范围：1900年2月1日0时0分至2100年12月31日23时59分</font>);")
        # 设置对齐方式为居中
        self.solar_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # 添加 QLabel 到垂直布局中
        v_layout.addWidget(self.solar_label)
        # 将垂直布局添加到父布局
        layout.addLayout(v_layout)
        layout.addWidget(self.solar_label)
        self.lunar_label = QLabel(
            "或者输入👉：<font color='red'>阴历</font> 年，月，日，时辰，节气(<font color='purple'>注意两个历法只能选择一个输入，输入要完整，另一个需留白，阴历输入功能还未实现</font>)。")
        # 设置对齐方式为居中
        self.lunar_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.lunar_label)
        # 添加 QLabel 到垂直布局中
        '''

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
        self.shuipingyinglishurushuchubuju = QGridLayout()
        self.shuipingyinglishurushuchubuju.setSpacing(0)

        self.NIANSHUCHUKUANG_shuru = InputWithComboBox(options=[
            "甲子", "甲戌", "甲申", "甲午", "甲辰", "甲寅",
            "乙丑", "乙亥", "乙酉", "乙未", "乙巳", "乙卯", "丙寅", "丙子", "丙戌", "丙申", "丙午", "丙辰",
            "丁卯", "丁丑", "丁亥", "丁酉", "丁未", "丁巳", "戊辰", "戊寅", "戊子", "戊戌", "戊申", "戊午",
            "己巳", "己卯", "己丑", "己亥", "己酉", "己未", "庚午", "庚辰", "庚寅", "庚子", "庚戌", "庚申",
            "辛未", "辛巳", "辛卯", "辛丑", "辛亥", "辛酉", "壬申", "壬午", "壬辰", "壬寅", "壬子", "壬戌",
            "癸酉", "癸未", "癸巳", "癸卯", "癸丑", "癸亥"
            ])
        self.nianlabel = QLabel('年')
        self.YUESHUCHUKUANG_shuru = InputWithComboBox(options=[
            "甲子", "甲戌", "甲申", "甲午", "甲辰", "甲寅",
            "乙丑", "乙亥", "乙酉", "乙未", "乙巳", "乙卯", "丙寅", "丙子", "丙戌", "丙申", "丙午", "丙辰",
            "丁卯", "丁丑", "丁亥", "丁酉", "丁未", "丁巳", "戊辰", "戊寅", "戊子", "戊戌", "戊申", "戊午",
            "己巳", "己卯", "己丑", "己亥", "己酉", "己未", "庚午", "庚辰", "庚寅", "庚子", "庚戌", "庚申",
            "辛未", "辛巳", "辛卯", "辛丑", "辛亥", "辛酉", "壬申", "壬午", "壬辰", "壬寅", "壬子", "壬戌",
            "癸酉", "癸未", "癸巳", "癸卯", "癸丑", "癸亥"
            ])
        self.yuelabel = QLabel('月')
        self.RISHUCHUKUANG_shuru = InputWithComboBox(options=[
            "甲子", "甲戌", "甲申", "甲午", "甲辰", "甲寅",
            "乙丑", "乙亥", "乙酉", "乙未", "乙巳", "乙卯", "丙寅", "丙子", "丙戌", "丙申", "丙午", "丙辰",
            "丁卯", "丁丑", "丁亥", "丁酉", "丁未", "丁巳", "戊辰", "戊寅", "戊子", "戊戌", "戊申", "戊午",
            "己巳", "己卯", "己丑", "己亥", "己酉", "己未", "庚午", "庚辰", "庚寅", "庚子", "庚戌", "庚申",
            "辛未", "辛巳", "辛卯", "辛丑", "辛亥", "辛酉", "壬申", "壬午", "壬辰", "壬寅", "壬子", "壬戌",
            "癸酉", "癸未", "癸巳", "癸卯", "癸丑", "癸亥"
            ])
        self.rilabel = QLabel('日')
        self.SHISHUCHUKUANG_shuru = InputWithComboBox(options=[
            "甲子", "甲戌", "甲申", "甲午", "甲辰", "甲寅",
            "乙丑", "乙亥", "乙酉", "乙未", "乙巳", "乙卯", "丙寅", "丙子", "丙戌", "丙申", "丙午", "丙辰",
            "丁卯", "丁丑", "丁亥", "丁酉", "丁未", "丁巳", "戊辰", "戊寅", "戊子", "戊戌", "戊申", "戊午",
            "己巳", "己卯", "己丑", "己亥", "己酉", "己未", "庚午", "庚辰", "庚寅", "庚子", "庚戌", "庚申",
            "辛未", "辛巳", "辛卯", "辛丑", "辛亥", "辛酉", "壬申", "壬午", "壬辰", "壬寅", "壬子", "壬戌",
            "癸酉", "癸未", "癸巳", "癸卯", "癸丑", "癸亥"
            ])
        self.shilabel = QLabel('时')
        self.JIEQIYDSHUCHU_shuru = InputWithComboBox(options=[
            "立春", "雨水", "惊蛰", "春分", "清明", "谷雨", "立夏", "小满", "芒种", "夏至",
            "小暑", "大暑", "立秋", "处暑", "白露", "秋分", "寒露", "霜降", "立冬", "小雪",
            "大雪", "冬至", "小寒", "大寒"
        ])
        self.jieqilabel = QLabel('节')
        self.YUANRISHUCHU_shuru = InputWithComboBox(options=[
            "立春", "雨水", "惊蛰", "春分", "清明", "谷雨", "立夏", "小满", "芒种", "夏至",
            "小暑", "大暑", "立秋", "处暑", "白露", "秋分", "寒露", "霜降", "立冬", "小雪",
            "大雪", "冬至", "小寒", "大寒"
        ])
        self.yuanrilabel = QLabel('日')
        for entry in [self.NIANSHUCHUKUANG_shuru, self.YUESHUCHUKUANG_shuru, self.RISHUCHUKUANG_shuru,
                      self.SHISHUCHUKUANG_shuru, self.JIEQIYDSHUCHU_shuru]:
            entry.input_text.setStyleSheet("border: 2px solid gray;")
            entry.input_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
            entry.input_text.setFixedSize(90, 25)
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
        '''
        self.NIANSHUCHUKUANG_shuru.setFixedSize(114, 30)
        self.YUESHUCHUKUANG_shuru.setFixedSize(114, 30)
        self.RISHUCHUKUANG_shuru.setFixedSize(114, 30)
        self.SHISHUCHUKUANG_shuru.setFixedSize(114, 30)
        self.JIEQIYDSHUCHU_shuru.setFixedSize(114, 30)
        self.YUANRISHUCHU_shuru.setFixedSize(50, 30)
        # 设置不可编辑

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
        self.nianlabel.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.yuelabel.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.rilabel.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.shilabel.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.jieqilabel.setAlignment(Qt.AlignmentFlag.AlignTop)
        margin = 15
        self.nianlabel.setMargin(margin)
        self.yuelabel.setMargin(margin)
        self.rilabel.setMargin(margin)
        self.shilabel.setMargin(margin)

        self.jieqilabel.setMargin(margin)

        # 加入水平布局
        base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
        image_path3 = os.path.join(base_path, '资源图片', 'TTB.png')
        self.TISHIYIN = QPushButton()
        self.TISHIYIN.setFixedSize(19, 19)
        icon = QIcon(image_path3)
        self.TISHIYIN.setIcon(icon)
        self.TISHIYIN.setIconSize(self.TISHIYIN.size())  # 设置图标大小与按钮大小相同
        self.TISHIYIN.setStyleSheet("border: none;")
        self.shuipingyinglishurushuchubuju.addWidget(self.TISHIYIN, 0, 1)

        # spacer = QSpacerItem(11, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        # self.shuipingyinglishurushuchubuju.addItem(spacer)
        SSS = QLineEdit()
        SSS.setFixedSize(8, 30)
        SSS.setReadOnly(True)
        SSS.setStyleSheet("border:none;")
        self.shuipingyinglishurushuchubuju.addWidget(SSS, 0, 0)
        self.shuipingyinglishurushuchubuju.addWidget(self.NIANSHUCHUKUANG_shuru, 0, 2)
        self.shuipingyinglishurushuchubuju.addWidget(self.nianlabel, 0, 3)
        self.shuipingyinglishurushuchubuju.addWidget(self.YUESHUCHUKUANG_shuru, 0, 4)
        self.shuipingyinglishurushuchubuju.addWidget(self.yuelabel, 0, 5)
        self.shuipingyinglishurushuchubuju.addWidget(self.RISHUCHUKUANG_shuru, 0, 6)
        self.shuipingyinglishurushuchubuju.addWidget(self.rilabel, 0, 7)
        self.shuipingyinglishurushuchubuju.addWidget(self.SHISHUCHUKUANG_shuru, 0, 8)
        self.shuipingyinglishurushuchubuju.addWidget(self.shilabel, 0, 9)
        self.shuipingyinglishurushuchubuju.addWidget(self.JIEQIYDSHUCHU_shuru, 0, 10)
        self.shuipingyinglishurushuchubuju.addWidget(self.jieqilabel, 0, 11)







        FANGYINGLIRONGQI=QWidget()
        FANGYINGLIRONGQI.setLayout(self.shuipingyinglishurushuchubuju)
        self.stacked_widget.addWidget(FANGYINGLIRONGQI)
        widget3 = QWidget()
        #创建农历输入框
        self.shuipingnonglishurushuchubuju = QGridLayout()
        self.shuipingnonglishurushuchubuju.setSpacing(0)

        self.NIANSHUCHUKUANGNONGLI_shuru = InputWithComboBox(options=[str(i) for i in range(1900, 2100)])
        self.nianlabelnongli = QLabel('年')
        self.YUESHUCHUKUANGNONGLI_shuru = InputWithComboBox(options=["一", "二", "三", "四", "五", "六", "七", "八", "九", "十", "十一", "十二"])
        self.yuelabelnongli = QLabel('月')
        self.RISHUCHUKUANGNONGLI_shuru = InputWithComboBox(options=["初一", "初二", "初三", "初四", "初五",
                "初六", "初七", "初八", "初九", "初十",
                "十一", "十二", "十三", "十四", "十五",
                "十六", "十七", "十八", "十九", "二十",
                "廿一", "廿二", "廿三", "廿四", "廿五",
                "廿六", "廿七", "廿八", "廿九", "三十"])
        self.rilabelnongli = QLabel('日')
        self.SHISHUCHUKUANGNONGLI_shuru = InputWithComboBox(options=[str(i) for i in range(0, 24)])
        self.shilabelnongli = QLabel('时')
        self.JIEQIYDSHUCHUNONGLI_shuru = InputWithComboBox(options=[str(i) for i in range(0, 60)])
        self.jieqilabelnongli = QLabel('分')
        for entry in [self.NIANSHUCHUKUANGNONGLI_shuru, self.YUESHUCHUKUANGNONGLI_shuru, self.RISHUCHUKUANGNONGLI_shuru,
                      self.SHISHUCHUKUANGNONGLI_shuru, self.JIEQIYDSHUCHUNONGLI_shuru]:
            entry.input_text.setStyleSheet("border: 2px solid gray;")
            entry.input_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
            entry.input_text.setFixedSize(90, 25)
        # 阴历输出框的格式
        # 阴历输出框字体调整
        font = QFont('SimSun', 10)
        self.NIANSHUCHUKUANGNONGLI_shuru.setFont(font)
        self.YUESHUCHUKUANGNONGLI_shuru.setFont(font)
        self.RISHUCHUKUANGNONGLI_shuru.setFont(font)
        self.SHISHUCHUKUANGNONGLI_shuru.setFont(font)
        self.JIEQIYDSHUCHUNONGLI_shuru.setFont(font)
        # 设定大小

        # label字体调整
        font = QFont('Microsoft YaHei', 10)
        self.nianlabelnongli.setFont(font)
        self.yuelabelnongli.setFont(font)
        self.rilabelnongli.setFont(font)
        self.shilabelnongli.setFont(font)
        self.jieqilabelnongli.setFont(font)
        # 设定边框样式和背景rgb(173, 216, 230)
        self.NIANSHUCHUKUANGNONGLI_shuru.setStyleSheet("background-color: white;border: 2px solid gray;")  # 设置边框宽度和颜色
        self.YUESHUCHUKUANGNONGLI_shuru.setStyleSheet("background-color: white;border: 2px solid gray;")  # 设置边框宽度和颜色
        self.RISHUCHUKUANGNONGLI_shuru.setStyleSheet("background-color: white;border: 2px solid gray;")  # 设置边框宽度和颜色
        self.SHISHUCHUKUANGNONGLI_shuru.setStyleSheet("background-color: white;border: 2px solid gray;")  # 设置边框宽度和颜色
        self.JIEQIYDSHUCHUNONGLI_shuru.setStyleSheet("background-color: white;border: 2px solid gray;")  # 设置边框宽度和颜色

        # 设置对齐方式
        self.nianlabelnongli.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.yuelabelnongli.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.rilabelnongli.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.shilabelnongli.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.jieqilabelnongli.setAlignment(Qt.AlignmentFlag.AlignTop)
        margin = 15
        self.nianlabelnongli.setMargin(margin)
        self.yuelabelnongli.setMargin(margin)
        self.rilabelnongli.setMargin(margin)
        self.shilabelnongli.setMargin(margin)
        self.jieqilabelnongli.setMargin(margin)
        # 加入水平布局
        base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
        image_path3 = os.path.join(base_path, '资源图片', 'TTB.png')
        self.TISHINONG = QPushButton()
        self.TISHINONG.setFixedSize(19, 19)
        icon = QIcon(image_path3)
        self.TISHINONG.setIcon(icon)
        self.TISHINONG.setIconSize(self.TISHIYIN.size())  # 设置图标大小与按钮大小相同
        self.TISHINONG.setStyleSheet("border: none;")
        self.shuipingnonglishurushuchubuju.addWidget(self.TISHINONG, 0, 1)

        # spacer = QSpacerItem(11, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        # self.shuipingyinglishurushuchubuju.addItem(spacer)
        SSSS = QLineEdit()
        SSSS.setFixedSize(8, 30)
        SSSS.setReadOnly(True)
        SSSS.setStyleSheet("border:none;")
        self.shuipingnonglishurushuchubuju.addWidget(SSSS, 0, 0)
        self.shuipingnonglishurushuchubuju.addWidget(self.NIANSHUCHUKUANGNONGLI_shuru, 0, 2)
        self.shuipingnonglishurushuchubuju.addWidget(self.nianlabelnongli, 0, 3)
        self.shuipingnonglishurushuchubuju.addWidget(self.YUESHUCHUKUANGNONGLI_shuru, 0, 4)
        self.shuipingnonglishurushuchubuju.addWidget(self.yuelabelnongli, 0, 5)
        self.shuipingnonglishurushuchubuju.addWidget(self.RISHUCHUKUANGNONGLI_shuru, 0, 6)
        self.shuipingnonglishurushuchubuju.addWidget(self.rilabelnongli, 0, 7)
        self.shuipingnonglishurushuchubuju.addWidget(self.SHISHUCHUKUANGNONGLI_shuru, 0, 8)
        self.shuipingnonglishurushuchubuju.addWidget(self.shilabelnongli, 0, 9)
        self.shuipingnonglishurushuchubuju.addWidget(self.JIEQIYDSHUCHUNONGLI_shuru, 0, 10)
        self.shuipingnonglishurushuchubuju.addWidget(self.jieqilabelnongli, 0, 11)


        widget3.setLayout(self.shuipingnonglishurushuchubuju)
        self.stacked_widget.addWidget(widget3)
        layout.addWidget(self.stacked_widget)

        def replyyyy():
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
            reply.setText(
                '输入👉：<font color=red>阴历</font> 年，月，日，时辰，节气(<font color=purple>例如癸卯年辛酉月戊寅日壬戌时白露节(气)</font>)。')
            reply.setStandardButtons(QMessageBox.StandardButton.Ok)
            reply.exec()  # 阻塞应用程序直到用户关闭警告框

        self.TISHIYIN.clicked.connect(lambda: replyyyy())





        def replyyyyy():
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
            reply.setText(
                '输入👉：<font color=red>农历</font> 年，月，日，时,分(<font color=purple>例如2023年九月廿二日13时7分</font>)。')
            reply.setStandardButtons(QMessageBox.StandardButton.Ok)
            reply.exec()  # 阻塞应用程序直到用户关闭警告框

        self.TISHINONG.clicked.connect(lambda: replyyyyy())
        # self.shuipingyinglishurushuchubuju.addWidget(self.YUANRISHUCHU_shuru)
        # self.shuipingyinglishurushuchubuju.addWidget(self.yuanrilabel)
        # 加入总布局

        self.lunar_output1shuipingbuju = QHBoxLayout()
        self.lunar_output1 = QLineEdit()
        self.lunar_output1.setFixedSize(800, 30)
        self.lunar_output1.setStyleSheet("background-color: rgb(173, 216, 230);border: 2px solid gray;")  # 设置边框宽度和颜色
        self.lunar_output1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lunarjj = createLineEditRightButton2(self.lunar_output1)
        self.lunar_output1shuipingbuju.addWidget(self.lunar_output1)
        layout.addLayout(self.lunar_output1shuipingbuju)

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
            reply.setText('该框输出阴历干支：天干地支年月日时辰，节气，阴阳遁以及元日等信息。')
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

        self.ws = QLabel('温氏奇门遁甲阴阳九局活用排盘')
        font = QFont('Microsoft YaHei', 20)
        self.ws.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ws.setFont(font)
        layout.addWidget(self.ws)
        '''
        # 创建九宫格
        # 创建一个水平布局放置九宫格，目的是为了让这个布局在layout水平方向上的中间位置
        gridrongqi = QWidget()

        '''
        grameyaofangtupian = QFrame()
        grameyaofangtupian.setGeometry(100, 100, 400, 300)
        grameyaofangtupian.setStyleSheet(
            f"background-image: url({image_path3}); background-repeat: no-repeat; background-position: center;")
            '''

        grid_h_layout = QHBoxLayout()
        grid_layout = QGridLayout()
        font = QFont('SimSun', 11)
        tainruju = ['巽四', '离九', '坤二', '震三', '中宫', '兑七', '艮八', '坎一', '乾六']
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
                frame.setFixedSize(235, 200)
                frame.setObjectName("customFrame")
                if row==0 and col==0:
                    frame.setStyleSheet("""
                                                QFrame#customFrame {
                                                    border-left: 2px solid black;  /* 左边虚线边框 */
                                                    border-right: 1.5px dashed white;  /* 右边虚线边框 */
                                                    border-top: 2px solid black;  /* 上边实线边框 */
                                                    border-bottom: 1.5px dashed white;  /* 下边实线边框 */
                                                    background-color: rgba(0, 0, 0, 0);  /* 透明背景 */
                                                }
                                            """)
                elif row==0 and col==1:
                    frame.setStyleSheet("""
                                                QFrame#customFrame {
                                                    border-left: 1.5px dashed black;  /* 左边虚线边框 */
                                                    border-right: 1.5px dashed white;  /* 右边虚线边框 */
                                                    border-top: 2px solid black;  /* 上边实线边框 */
                                                    border-bottom: 1.5px dashed white;  /* 下边实线边框 */
                                                    background-color: rgba(0, 0, 0, 0);  /* 透明背景 */
                                                }
                                            """)
                elif row==0 and col==2:
                    frame.setStyleSheet("""
                                                QFrame#customFrame {
                                                    border-left: 1.5px dashed black;  /* 左边虚线边框 */
                                                    border-right: 2px solid black;  /* 右边虚线边框 */
                                                    border-top: 2px solid black;  /* 上边实线边框 */
                                                    border-bottom: 1.5px dashed white;  /* 下边实线边框 */
                                                    background-color: rgba(0, 0, 0, 0);  /* 透明背景 */
                                                }
                                            """)
                elif row==1 and col==0:
                    frame.setStyleSheet("""
                                                QFrame#customFrame {
                                                    border-left: 2px solid black;  /* 左边虚线边框 */
                                                    border-right: 1.5px dashed white;  /* 右边虚线边框 */
                                                    border-top: 1.5px dashed black;  /* 上边实线边框 */
                                                    border-bottom: 1.5px dashed white;  /* 下边实线边框 */
                                                    background-color: rgba(0, 0, 0, 0);  /* 透明背景 */
                                                }
                                            """)
                elif row==1 and col==1:
                    frame.setStyleSheet("""
                                                                    QFrame#customFrame {
                                                                        border-left:1.5px dashed black;  /* 左边虚线边框 */
                                                                        border-right: 1.5px dashed white;  /* 右边虚线边框 */
                                                                        border-top: 1.5px dashed black;  /* 上边实线边框 */
                                                                        border-bottom: 1.5px dashed white;  /* 下边实线边框 */
                                                                        background-color: rgba(0, 0, 0, 0);  /* 透明背景 */
                                                                    }
                                                                """)
                elif row==1 and col==2:
                    frame.setStyleSheet("""
                                                                                      QFrame#customFrame {
                                                                                          border-left:1.5px dashed black;  /* 左边虚线边框 */
                                                                                          border-right: 2px solid black;  /* 右边虚线边框 */
                                                                                          border-top: 1.5px dashed black;  /* 上边实线边框 */
                                                                                          border-bottom: 1.5px dashed white;  /* 下边实线边框 */
                                                                                          background-color: rgba(0, 0, 0, 0);  /* 透明背景 */
                                                                                      }
                                                                                  """)
                elif row==2 and col==0:
                    frame.setStyleSheet(""" QFrame#customFrame {
                                                                border-left:2px solid black;  /* 左边虚线边框 */
                                                                border-right: 1.5px dashed white;  /* 右边虚线边框 */
                                                                border-top: 1.5px dashed black;  /* 上边实线边框 */
                                                                border-bottom: 2px solid black;  /* 下边实线边框 */
                                                                background-color: rgba(0, 0, 0, 0);  /* 透明背景 */
                                                                                        }
                                                                                    """)
                elif row==2 and col==1:
                    frame.setStyleSheet(""" QFrame#customFrame {
                                                                border-left:1.5px dashed black;  /* 左边虚线边框 */
                                                                border-right: 1.5px dashed white;  /* 右边虚线边框 */
                                                                border-top: 1.5px dashed black;  /* 上边实线边框 */
                                                                border-bottom: 2px solid black;  /* 下边实线边框 */
                                                                background-color: rgba(0, 0, 0, 0);  /* 透明背景 */
                                                                                                          }
                                                                                                      """)
                elif row==2 and col==2:
                    frame.setStyleSheet(""" QFrame#customFrame {
                                                                border-left:1.5px dashed black;  /* 左边虚线边框 */
                                                                border-right: 2px solid black;  /* 右边虚线边框 */
                                                                border-top: 1.5px dashed black;  /* 上边实线边框 */
                                                                border-bottom: 2px solid black;  /* 下边实线边框 */
                                                                background-color: rgba(0, 0, 0, 0);  /* 透明背景 */
                                                                                                                             }
                                                                                                                         """)




                if row == 1 and col == 1:
                    # 创建一个内部的二维布局
                    inner_layout = QGridLayout()

                    output1 = QLineEdit()
                    output1.setStyleSheet("background-color:rgb(192,192,192);color:black;border-radius: 22px;border: none;")
                    output1.setFixedSize(45, 45)  # 设置宽度和高度
                    output1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output2 = QLineEdit()
                    output2.setStyleSheet("background-color: white; border: 2px solid black;")
                    output2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output2.setFixedSize(53, 45)  # 设置宽度和高度
                    output1.setReadOnly(True)
                    output2.setReadOnly(True)
                    font = QFont('SimSun', 11)
                    output1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output1.setFont(font)
                    output2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output2.setFont(font)
                    output2.setStyleSheet("border: none;")
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
                    out1 = QLineEdit()
                    out1.setReadOnly(True)
                    out1.setFixedSize(50, 45)  # 设置宽度和高度
                    out1.setStyleSheet("background-color: transparent; border: none;")
                    inner_layout.addWidget(out1, 2, 1, 1, 3)
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
                    text1.setStyleSheet(" font-weight: bold;border:none;")
                    text2 = QLabel("寄二")
                    text2.setStyleSheet(" font-weight: bold;border:none;")
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

                    output1 = QLineEdit()
                    output1.setStyleSheet("background-color: rgb(192,192,192); color:black;border-radius: 22px;border: none;")
                    output1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output1.setFixedSize(45, 45)  # 设置宽度和高度
                    output2 = QLineEdit()
                    output2.setStyleSheet("background-color: white; ")
                    output2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output2.setFixedSize(50, 45)
                    output3 = QLineEdit()
                    output3.setStyleSheet("background-color: rgb(192,192,192); color:black;border-radius: 22px;border: none;")
                    output3.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output3.setFixedSize(45, 45)
                    output2.setReadOnly(True)
                    output1.setReadOnly(True)
                    output3.setReadOnly(True)
                    output4 = QTextBrowser()
                    output4.setStyleSheet("background-color: white; ")
                    output4.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output4.setReadOnly(True)
                    output4.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)  # 禁用垂直滚动条
                    output4.setFixedSize(53, 45)  # 设置宽度和高度
                    output5 = QTextBrowser()
                    output5.setStyleSheet("background-color: white; ")
                    output5.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output5.setReadOnly(True)
                    output5.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)  # 禁用垂直滚动条
                    output5.setFixedSize(53, 45)  # 设置宽度和高度
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
                    output6 = QLineEdit()
                    output6.setStyleSheet("background-color: white;")
                    output6.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output6.setFixedSize(20, 45)
                    font = QFont("SimSun", 18)
                    font.setBold(True)
                    output6.setFont(font)

                    output2.setStyleSheet("border: none;")

                    output4.setStyleSheet("border: none;")
                    output5.setStyleSheet("border: none;")
                    output6.setStyleSheet("border: none;")
                    output6.setReadOnly(True)
                    box_names = [f"output_{row}_{col}_1", f"output_{row}_{col}_2", f"output_{row}_{col}_3",
                                 f"output_{row}_{col}_4", f"output_{row}_{col}_5", f"output_{row}_{col}_6"]
                    self.output_boxes.update(
                        {name: output for name, output in
                         zip(box_names, [output1, output2, output3, output4, output5, output6])})

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
                    text.setStyleSheet(" font-weight: bold;border:none;")
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
                    inner_layout.addWidget(output6, 1, 2)

                    # 设置内部布局为frame的布局
                    frame.setLayout(inner_layout)
                    # 将QFrame添加到网格布局
                    grid_layout.addWidget(frame, row, col)
                else:
                    # 创建一个内部的二维布局
                    inner_layout = QGridLayout()

                    output1 = QLineEdit()
                    output1.setStyleSheet("background-color: rgb(192,192,192); color:black;border-radius: 22px;border: none;")
                    output1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output1.setFixedSize(45, 45)  # 设置宽度和高度
                    output2 = QLineEdit()
                    output2.setStyleSheet("background-color: white; ")
                    output2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output2.setFixedSize(50, 45)
                    output3 = QLineEdit()
                    output3.setStyleSheet("background-color: rgb(192,192,192); color:black;border-radius: 22px;border: none;")
                    output3.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output3.setFixedSize(45, 45)
                    output2.setReadOnly(True)
                    output1.setReadOnly(True)
                    output3.setReadOnly(True)
                    output4 = QLineEdit()
                    output4.setStyleSheet("background-color: white; ")
                    output4.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output4.setReadOnly(True)
                    output4.setFixedSize(53, 45)  # 设置宽度和高度
                    output5 = QTextBrowser()
                    output5.setStyleSheet("background-color: white;")
                    output5.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output5.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
                    output5.setReadOnly(True)
                    output5.setFixedSize(53, 45)  # 设置宽度和高度
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
                    output6 = QLineEdit()
                    output6.setStyleSheet("background-color: white;")
                    output6.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    output6.setReadOnly(True)
                    output6.setFixedSize(20, 45)
                    font = QFont("SimSun", 18)
                    font.setBold(True)
                    output6.setFont(font)

                    output2.setStyleSheet("border: none;")

                    output4.setStyleSheet("border: none;")
                    output5.setStyleSheet("border: none;")
                    output6.setStyleSheet("border: none;")

                    box_names = [f"output_{row}_{col}_1", f"output_{row}_{col}_2", f"output_{row}_{col}_3",
                                 f"output_{row}_{col}_4", f"output_{row}_{col}_5", f"output_{row}_{col}_6"]
                    self.output_boxes.update(
                        {name: output for name, output in
                         zip(box_names, [output1, output2, output3, output4, output5, output6])})

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
                    text.setStyleSheet(" font-weight: bold;border:none;")
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
                    inner_layout.addWidget(output6, 1, 2)

                    # 设置内部布局为frame的布局
                    frame.setLayout(inner_layout)
                    # 将QFrame添加到网格布局
                    grid_layout.addWidget(frame, row, col)
        grid_layout.setSpacing(0)
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
        self.time_label.setText(f"温氏奇门当前时间: {current_time}")

    def _show_warning(self, text, image_path1=None):
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
        if image_path1:
            reply.setWindowIcon(QIcon(image_path1))
        reply.setFont(kai_ti_font)
        reply.setStyleSheet(style_sheet)
        reply.setIcon(QMessageBox.Icon.Critical)
        reply.setWindowTitle("温馨提示")
        reply.setText(text)
        reply.setStandardButtons(QMessageBox.StandardButton.Ok)
        reply.exec()

    def _render_chart_result(self, result):
        # 与原始主程序 show_info 一致：直接覆写每个格子，不先 clear()。
        # 原因：QTextBrowser.clear() 会重置文档 block format，再 setText 时单行
        # 文字会贴框顶，与旁边的"+"号错位。每次排盘 result.output_boxes 都包含
        # 全部 50 个键，覆写完全等价于"先清再设"。
        self.lunar_output1.setText(result.header_text)
        self.info_label.setText(result.info_text)
        for output_name, text in result.output_boxes.items():
            box = self.output_boxes[output_name]
            # 复刻原始 _show_info 对 QTextBrowser 的单行/多行差异化样式：
            #   单行(无 \n) 文字会贴框顶，需要 padding-top:10px 把它顶到中央，与
            #   同行 "+" (QLineEdit 天然垂直居中) 对齐。
            #   多行(有 \n) 已能填满 45px 高度，保持初始 border:none 即可。
            if isinstance(box, QTextBrowser):
                if "\n" in text:
                    box.setStyleSheet("border: none;")
                else:
                    box.setStyleSheet("border:none;padding-top: 10px;")
            box.setText(text)

    def _parse_solar_inputs(self, ye, mo, da, ho, mi, image_path1):
        user_time = ye + '年' + mo + '月' + da + '日' + ho + '时' + mi + '分'
        matches = _SOLAR_INPUT_RE.search(user_time)
        if not matches:
            self._show_warning("您输入的阳历时间信息格式不正确哟，请完整输入所有时间信息。", image_path1)
            return None
        yearr, monthh, dayy, hourr, minutee = [int(matches.group(i)) for i in range(1, 6)]
        nianfen = "闰年" if calendar.isleap(yearr) else "平年"
        days_in_month = {
            1: 31, 2: 29 if calendar.isleap(yearr) else 28, 3: 31, 4: 30,
            5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31,
        }
        if not (1900 <= yearr <= 2100 and 1 <= monthh <= 12 and 1 <= dayy <= 31 and 0 <= hourr <= 23 and 0 <= minutee <= 60):
            self._show_warning("输入的时间不存在，请重新输入!", image_path1)
            return None
        if yearr == 1900 and monthh == 1:
            self._show_warning("1900年2月1号0时0分以前的时间点不支持哦，重新选个时间点吧。", image_path1)
            return None
        if dayy > days_in_month[monthh]:
            if monthh == 2:
                self._show_warning("%s的%s月没有第%s天哦，重新输一下吧!" % (nianfen, str(monthh), str(dayy)), image_path1)
            else:
                self._show_warning("%s月可没有第%s天哦，重新输一遍吧!" % (str(monthh), str(dayy)), image_path1)
            return None
        return yearr, monthh, dayy, hourr, minutee

    def show_info(self):
        base_path = os.path.dirname(__file__)
        image_path1 = os.path.join(base_path, '资源图片', 'JGT.png')

        ye = self.time_entry1.input_text.text()
        mo = self.time_entry2.input_text.text()
        da = self.time_entry3.input_text.text()
        ho = self.time_entry4.input_text.text()
        mi = self.time_entry5.input_text.text()

        ye_lunar = self.NIANSHUCHUKUANG_shuru.input_text.text()
        mo_lunar = self.YUESHUCHUKUANG_shuru.input_text.text()
        da_lunar = self.RISHUCHUKUANG_shuru.input_text.text()
        ho_lunar = self.SHISHUCHUKUANG_shuru.input_text.text()
        jieqi_lunar = self.JIEQIYDSHUCHU_shuru.input_text.text()

        ye_nongli = self.NIANSHUCHUKUANGNONGLI_shuru.input_text.text()
        mo_nonglii = self.YUESHUCHUKUANGNONGLI_shuru.input_text.text()
        da_nonglii = self.RISHUCHUKUANGNONGLI_shuru.input_text.text()
        ho_nongli = self.SHISHUCHUKUANGNONGLI_shuru.input_text.text()
        jieqi_nongli = self.JIEQIYDSHUCHUNONGLI_shuru.input_text.text()

        solar_inputs = [ye, mo, da, ho, mi]
        ganzhi_inputs = [ye_lunar, mo_lunar, da_lunar, ho_lunar, jieqi_lunar]
        nongli_inputs = [ye_nongli, mo_nonglii, da_nonglii, ho_nongli, jieqi_nongli]

        if not any(solar_inputs + ganzhi_inputs + nongli_inputs):
            self._show_warning('施主，”巧妇难为无米之炊“，您得输入点东西我才能为您运算啊。', image_path1)
            return

        if not any(ganzhi_inputs + nongli_inputs) and any(solar_inputs):
            if not all(solar_inputs):
                self._show_warning("请完整输入所有时间信息。", image_path1)
                return
            parsed = self._parse_solar_inputs(ye, mo, da, ho, mi, image_path1)
            if parsed is None:
                return
            self._render_chart_result(build_chart_from_solar(*parsed))
            return

        if not any(solar_inputs + nongli_inputs) and any(ganzhi_inputs):
            if not all(ganzhi_inputs):
                self._show_warning("您输入的阴历时间信息格式不正确哟，请完整输入所有时间信息。", image_path1)
                return
            if all(value in SIXTY_GANZHI for value in ganzhi_inputs[:4]) and jieqi_lunar in SOLAR_TERMS:
                self._render_chart_result(build_chart_from_ganzhi(*ganzhi_inputs))
                return
            self._show_warning("输入的阴历时间不存在(请检查干支是否在六十干支里，节气是否在二十四节气里)，请重新输入!", image_path1)
            return

        if not any(solar_inputs + ganzhi_inputs) and any(nongli_inputs):
            if not all(nongli_inputs):
                self._show_warning("请完整输入所有时间信息。", image_path1)
                return
            if (
                ye_nongli in [str(i) for i in range(1900, 2101)]
                and mo_nonglii in LUNAR_MONTH_TEXT_TO_NUMBER
                and da_nonglii in LUNAR_DAY_TEXT_TO_NUMBER
                and ho_nongli in [str(i) for i in range(0, 24)]
                and jieqi_nongli in [str(i) for i in range(0, 60)]
            ):
                self._render_chart_result(
                    build_chart_from_lunar_date(
                        int(ye_nongli),
                        LUNAR_MONTH_TEXT_TO_NUMBER[mo_nonglii],
                        LUNAR_DAY_TEXT_TO_NUMBER[da_nonglii],
                        int(ho_nongli),
                        int(jieqi_nongli),
                    )
                )
                return
            self._show_warning("您输入的农历时间信息格式不正确哟，请完整输入所有时间信息。", image_path1)

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
        self.NIANSHUCHUKUANG_shuru.clearr()
        self.YUESHUCHUKUANG_shuru.clearr()
        self.RISHUCHUKUANG_shuru.clearr()
        self.SHISHUCHUKUANG_shuru.clearr()
        self.JIEQIYDSHUCHU_shuru.clearr()
        self.YUANRISHUCHU_shuru.clearr()

        self.NIANSHUCHUKUANGNONGLI_shuru.clearr()
        self.YUESHUCHUKUANGNONGLI_shuru.clearr()
        self.RISHUCHUKUANGNONGLI_shuru.clearr()
        self.SHISHUCHUKUANGNONGLI_shuru.clearr()
        self.JIEQIYDSHUCHUNONGLI_shuru.clearr()

        for row in range(3):
            for col in range(3):
                if row == 1 and col == 1:
                    for i in range(1, 3):  # 清空output_0_0_1、output_0_0_2、output_0_0_3等
                        output_name = f"output_{row}_{col}_{i}"
                        self.output_boxes[output_name].clear()
                else:
                    for i in range(1, 7):  # 清空output_0_0_1、output_0_0_2、output_0_0_3等
                        output_name = f"output_{row}_{col}_{i}"
                        self.output_boxes[output_name].clear()


class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.config = configparser.ConfigParser()

        def createLineEditRightButton2(edit):
            base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
            # 访问数据文件的路径
            image_path1 = os.path.join(base_path, '资源图片', 'YHM.png')
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
            image_path1 = os.path.join(base_path, '资源图片', 'MIM.jpg')
            image_path2 = os.path.join(base_path, '资源图片', 'YJ.png')
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
        image_path1 = os.path.join(base_path, '资源图片', 'BJJ.png')
        image_path2 = os.path.join(base_path, '资源图片', 'TTB.jpg')

        background_image = QPixmap(image_path1)  # 替换为您的背景图像文件路径
        background_image = background_image.scaled(self.width(), self.height())

        # 将背景图像设置为窗口的背景
        pixmap = background_image.scaled(self.size(), Qt.AspectRatioMode.IgnoreAspectRatio)
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(pixmap))
        self.setPalette(palette)

        self.setWindowTitle("温氏奇门遁甲阴阳九局活用预测排盘登录")
        self.setGeometry(400, 100, 740, 480)  # 增加宽度以容纳图像
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
        font2 = QFont()
        font2.setFamily("KaiTi")
        font2.setPointSize(15)
        label22.setFont(font2)
        label11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label11.setStyleSheet("color: rgb(255,255,155);")
        label22.setStyleSheet("color: rgb(255,255,155);")
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
        spacer = QSpacerItem(520, 50, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        layout.addItem(spacer)
        login_layout.addWidget(label11)
        login_layout.addWidget(label22)
        spacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        login_layout.addItem(spacer)
        login_layout.addWidget(label33)
        self.remember_password_checkbox = QCheckBox("记住密码", self)
        forget_password_button = QPushButton("忘记密码？")
        forget_password_button.clicked.connect(self.show_forget_password_prompt)
        forget_password_button.setStyleSheet("background:transparent;color: rgb(255,255,255);")
        font5=QFont()
        font5.setPointSize(7)
        self.remember_password_checkbox.setFont(font5)
        forget_password_button.setFont(font5)
        self.remember_password_checkbox.setStyleSheet("color: rgb(255,255,255);")  # 将颜色设置为红色或其他颜色
        QQQ=QLabel("👈")

        login_layout.addLayout(username_layout)
        login_layout.addLayout(password_layout)
        jizhumimabuju=QHBoxLayout()
        jizhumimabuju.addStretch(5)
        jizhumimabuju.addWidget(self.remember_password_checkbox)
        jizhumimabuju.addStretch(9)

        jizhumimabuju.addWidget(forget_password_button)
        jizhumimabuju.addStretch(1)
        login_layout.addLayout(jizhumimabuju)
        login_layout.addLayout(denglubuju)
        login_layout.addWidget(zhuce_label)
        login_layout.addLayout(zhucebuju)
        login_layout.addWidget(self.login_status_label)
        spacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        login_layout.addItem(spacer)

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
        self.load_remember_password_status()
        # 如果已勾选"记住密码"，则尝试自动填充已保存的用户名和密码
        if self.remember_password_checkbox.isChecked():
            self.load_saved_credentials()

    def closeEvent(self, event):
        # 重写窗口关闭事件，在窗口关闭时保存"记住密码"的状态
        self.save_remember_password_status()
        event.accept()
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
        if self.remember_password_checkbox.isChecked():
            username1 = self.username_input.text()
            password1 = self.password_input.text()
            self.save_credentials(username1, password1)
        self.save_remember_password_status()

    def show_forget_password_prompt(self):
        # 创建文字提示框
        base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
        # 访问数据文件的路径
        image_path1 = os.path.join(base_path, '资源图片', 'TTB.jpg')
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
        reply.setText(
            '<font color=red>请用注册码重新注册一个帐号</font> 。')
        reply.setStandardButtons(QMessageBox.StandardButton.Ok)


        reply.exec()  # 阻塞应用程序直到用户关闭警告框

    def save_credentials(self, username, password):
        # 将用户名和密码保存到配置文件或数据库
        config = configparser.ConfigParser()
        config.read('配置/credentials.ini')

        if not config.has_section('Credentials'):
            config.add_section('Credentials')

        config.set('Credentials', 'username', username)
        config.set('Credentials', 'password', password)

        with open('配置/credentials.ini', 'w') as configfile:
            config.write(configfile)

    def load_saved_credentials(self):
        # 从配置文件中加载已保存的用户名和密码
        config = configparser.ConfigParser()
        config.read('配置/credentials.ini')

        if config.has_section('Credentials'):
            username = config.get('Credentials', 'username')
            password = config.get('Credentials', 'password')
            self.username_input.setText(username)
            self.password_input.setText(password)

    def save_remember_password_status(self):
        # 保存"记住密码"的状态到配置文件
        config = configparser.ConfigParser()
        config.read('配置/remember_password.ini')
        if not config.has_section('RememberPassword'):
            config.add_section('RememberPassword')
        config.set('RememberPassword', 'status', str(int(self.remember_password_checkbox.isChecked())))

        with open('配置/remember_password.ini', 'w') as configfile:
            config.write(configfile)

    def load_remember_password_status(self):
        # 从配置文件加载"记住密码"的状态
        config = configparser.ConfigParser()
        config.read('配置/remember_password.ini')
        if config.has_section('RememberPassword'):
            status = config.get('RememberPassword', 'status')
            if status == '1':
                self.remember_password_checkbox.setChecked(True)
            else:
                self.remember_password_checkbox.setChecked(False)
            print(status)

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
        if os.path.exists('配置/config.ini'):
            self.config.read('配置/config.ini')
            credentials = self.config['Credentials']
            self.current_username = credentials.get('current_username', '')
            self.current_password = credentials.get('current_password', '')

    def save_config(self):
        self.config['Credentials'] = {
            'current_username': self.current_username,
            'current_password': self.current_password
        }

        with open('配置/config.ini', 'w') as configfile:
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
    login_dialog = LoginDialog()
    if login_dialog.exec() == QDialog.DialogCode.Accepted:
        main_window = TimeInfoApp()
        main_window.show()
    sys.exit(app.exec())
