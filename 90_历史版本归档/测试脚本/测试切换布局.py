import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QStackedWidget

class ToggleLayoutsExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Toggle Layouts Example")
        self.setGeometry(100, 100, 400, 200)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.stacked_widget = QStackedWidget()

        widget1 = QWidget()
        layout1 = QVBoxLayout()
        button1 = QPushButton("Layout 1 Button")
        layout1.addWidget(button1)
        widget1.setLayout(layout1)
        self.stacked_widget.addWidget(widget1)

        widget2 = QWidget()
        layout2 = QVBoxLayout()
        button2 = QPushButton("Layout 2 Button")
        layout2.addWidget(button2)
        widget2.setLayout(layout2)
        self.stacked_widget.addWidget(widget2)

        widget3 = QWidget()
        layout3 = QVBoxLayout()
        button3 = QPushButton("Layout 3 Button")
        layout3.addWidget(button3)
        widget3.setLayout(layout3)
        self.stacked_widget.addWidget(widget3)

        central_layout = QVBoxLayout()
        central_layout.addWidget(self.stacked_widget)
        central_widget.setLayout(central_layout)

        self.current_layout = 0  # 当前可见的布局索引

        button_toggle_layouts = QPushButton("Toggle Layouts")
        button_toggle_layouts.clicked.connect(self.toggle_layouts)
        central_layout.addWidget(button_toggle_layouts)

    def toggle_layouts(self):
        # 切换到下一个布局
        self.current_layout = (self.current_layout + 1) % 3
        self.stacked_widget.setCurrentIndex(self.current_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToggleLayoutsExample()
    window.show()
    sys.exit(app.exec_())
    # 创建农历输入框
    self.shuipingnonglishurushuchubuju = QGridLayout()
    self.shuipingnonglishurushuchubuju.setSpacing(0)

    self.NIANSHUCHUKUANGNONGLI_shuru = InputWithComboBox(options=[
        "甲子", "甲戌", "甲申", "甲午", "甲辰", "甲寅",
        "乙丑", "乙亥", "乙酉", "乙未", "乙巳", "乙卯", "丙寅", "丙子", "丙戌", "丙申", "丙午", "丙辰",
        "丁卯", "丁丑", "丁亥", "丁酉", "丁未", "丁巳", "戊辰", "戊寅", "戊子", "戊戌", "戊申", "戊午",
        "己巳", "己卯", "己丑", "己亥", "己酉", "己未", "庚午", "庚辰", "庚寅", "庚子", "庚戌", "庚申",
        "辛未", "辛巳", "辛卯", "辛丑", "辛亥", "辛酉", "壬申", "壬午", "壬辰", "壬寅", "壬子", "壬戌",
        "癸酉", "癸未", "癸巳", "癸卯", "癸丑", "癸亥"
    ])
    self.nianlabelnongli = QLabel('年')
    self.YUESHUCHUKUANGNONGLI_shuru = InputWithComboBox(options=[
        "甲子", "甲戌", "甲申", "甲午", "甲辰", "甲寅",
        "乙丑", "乙亥", "乙酉", "乙未", "乙巳", "乙卯", "丙寅", "丙子", "丙戌", "丙申", "丙午", "丙辰",
        "丁卯", "丁丑", "丁亥", "丁酉", "丁未", "丁巳", "戊辰", "戊寅", "戊子", "戊戌", "戊申", "戊午",
        "己巳", "己卯", "己丑", "己亥", "己酉", "己未", "庚午", "庚辰", "庚寅", "庚子", "庚戌", "庚申",
        "辛未", "辛巳", "辛卯", "辛丑", "辛亥", "辛酉", "壬申", "壬午", "壬辰", "壬寅", "壬子", "壬戌",
        "癸酉", "癸未", "癸巳", "癸卯", "癸丑", "癸亥"
    ])
    self.yuelabelnongli = QLabel('月')
    self.RISHUCHUKUANGNONGLI_shuru = InputWithComboBox(options=[
        "甲子", "甲戌", "甲申", "甲午", "甲辰", "甲寅",
        "乙丑", "乙亥", "乙酉", "乙未", "乙巳", "乙卯", "丙寅", "丙子", "丙戌", "丙申", "丙午", "丙辰",
        "丁卯", "丁丑", "丁亥", "丁酉", "丁未", "丁巳", "戊辰", "戊寅", "戊子", "戊戌", "戊申", "戊午",
        "己巳", "己卯", "己丑", "己亥", "己酉", "己未", "庚午", "庚辰", "庚寅", "庚子", "庚戌", "庚申",
        "辛未", "辛巳", "辛卯", "辛丑", "辛亥", "辛酉", "壬申", "壬午", "壬辰", "壬寅", "壬子", "壬戌",
        "癸酉", "癸未", "癸巳", "癸卯", "癸丑", "癸亥"
    ])
    self.rilabelnongli = QLabel('日')
    self.SHISHUCHUKUANGNONGLI_shuru = InputWithComboBox(options=[
        "甲子", "甲戌", "甲申", "甲午", "甲辰", "甲寅",
        "乙丑", "乙亥", "乙酉", "乙未", "乙巳", "乙卯", "丙寅", "丙子", "丙戌", "丙申", "丙午", "丙辰",
        "丁卯", "丁丑", "丁亥", "丁酉", "丁未", "丁巳", "戊辰", "戊寅", "戊子", "戊戌", "戊申", "戊午",
        "己巳", "己卯", "己丑", "己亥", "己酉", "己未", "庚午", "庚辰", "庚寅", "庚子", "庚戌", "庚申",
        "辛未", "辛巳", "辛卯", "辛丑", "辛亥", "辛酉", "壬申", "壬午", "壬辰", "壬寅", "壬子", "壬戌",
        "癸酉", "癸未", "癸巳", "癸卯", "癸丑", "癸亥"
    ])
    self.shilabelnongli = QLabel('时')
    self.JIEQIYDSHUCHUNONGLI_shuru = InputWithComboBox(options=[
        "立春", "雨水", "惊蛰", "春分", "清明", "谷雨", "立夏", "小满", "芒种", "夏至",
        "小暑", "大暑", "立秋", "处暑", "白露", "秋分", "寒露", "霜降", "立冬", "小雪",
        "大雪", "冬至", "小寒", "大寒"
    ])
    self.jieqilabelnongli = QLabel('节')
    for entry in [self.NIANSHUCHUKUANG_shuru, self.YUESHUCHUKUANG_shuru, self.RISHUCHUKUANG_shuru,
                  self.SHISHUCHUKUANG_shuru, self.JIEQIYDSHUCHU_shuru]:
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
    image_path3 = os.path.join(base_path, 'TTB.png')
    self.TISHINONG = QPushButton()
    self.TISHINONG.setFixedSize(19, 19)
    icon = QIcon(image_path3)
    self.TISHINONG.setIcon(icon)
    self.TISHINONG.setIconSize(self.TISHIYIN.size())  # 设置图标大小与按钮大小相同
    self.TISHINONG.setStyleSheet("border: none;")
    self.shuipingnonglishurushuchubuju.addWidget(self.TISHINONG, 0, 1)

    # spacer = QSpacerItem(11, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
    # self.shuipingyinglishurushuchubuju.addItem(spacer)
    SSS = QLineEdit()
    SSS.setFixedSize(8, 30)
    SSS.setReadOnly(True)
    SSS.setStyleSheet("border:none;")
    self.shuipingnonglishurushuchubuju.addWidget(SSS, 0, 0)
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

    widget3 = QWidget()
    layout3 = QVBoxLayout()
    layout3.addLayout(self.shuipingnonglishurushuchubuju)
    '''