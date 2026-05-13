import sys
import datetime
from functionSpaDigiXAPPONE import getthebasicmessageofnineGrids
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QHBoxLayout, QVBoxLayout, QLineEdit, QLabel, QPushButton
from PyQt6.QtCore import Qt  # 导入Qt模块
class DateCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("SDXAPP1")
        # 总体垂直布局
        mainLayout = QVBoxLayout(self)

        # 原始的水平布局
        inputLayout = QHBoxLayout()

        # 创建输入框和对应的标签，并设置高度
        self.yearEdit = QLineEdit(self)
        self.yearEdit.setFixedHeight(30)
        self.yearEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)  # 设置文本居中
        inputLayout.addWidget(self.yearEdit)

        inputLayout.addWidget(QLabel("年"))

        self.monthEdit = QLineEdit(self)
        self.monthEdit.setFixedHeight(30)
        inputLayout.addWidget(self.monthEdit)
        self.monthEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)  # 设置文本居中
        inputLayout.addWidget(QLabel("月"))

        self.dayEdit = QLineEdit(self)
        self.dayEdit.setFixedHeight(30)
        inputLayout.addWidget(self.dayEdit)
        self.dayEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)  # 设置文本居中
        inputLayout.addWidget(QLabel("日"))

        self.hourEdit = QLineEdit(self)
        self.hourEdit.setFixedHeight(30)
        inputLayout.addWidget(self.hourEdit)
        self.hourEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)  # 设置文本居中
        inputLayout.addWidget(QLabel("时"))



        # 将原始水平布局添加到总布局
        mainLayout.addLayout(inputLayout)

        # 创建网格布局
        gridLayout = QGridLayout()

        # 特定标签名称的列表
        labelNames =  [
         "1.1 落内外遁 ：", "1.2 宫落驿马 ：", "1.3 同边要素 ：", "1.4 值使空亡 ：", "1.5 支冲得数 ：",
            "1.6 甲子戊吉 ：", "2.0 吉凶格数 ：", "3.0 单宫天盘 ：", "4.0 单宫九星 ：", "5.0 单宫八门 ：",
         "6.0 单宫八神 ：", "7.0 十二宫数 ："
            ]

        # 左侧12个水平布局
        self.outputEdits = []  # 创建一个列表来保存输出框的引用

        for i in range(12):
            horLayout = QHBoxLayout()
            label = QLabel(labelNames[i], self)
            edit = QLineEdit(self)
            edit.setFixedHeight(30)
            edit.setReadOnly(True)
            edit.setAlignment(Qt.AlignmentFlag.AlignCenter)
            horLayout.addWidget(label)
            horLayout.addWidget(edit)
            self.outputEdits.append(edit)  # 将输出框添加到列表中
            gridLayout.addLayout(horLayout, i, 0)

        # 右侧布局
        # 获取双干时辰标签
        # 获取双干时辰标签
        titleLabel = QLabel("获取双干时辰", self)
        titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)  # 设置标签居中
        titleLabel.setStyleSheet("font-family: KaiTi; font-size: 15pt;")  # 设置字体为楷书
        gridLayout.addWidget(titleLabel, 0, 1, 1, 2)  # 让标签跨越两列

        # 年月日输入及标签的水平布局
        dateInputLayout = QHBoxLayout()

        # 年输入及标签
        self.yearEdit2 = QLineEdit(self)
        self.yearEdit2.setFixedHeight(30)
        self.yearEdit2.setAlignment(Qt.AlignmentFlag.AlignCenter)  # 设置文本居中
        dateInputLayout.addWidget(self.yearEdit2)
        dateInputLayout.addWidget(QLabel("年"))

        # 月输入及标签
        self.monthEdit2 = QLineEdit(self)
        self.monthEdit2.setFixedHeight(30)
        self.monthEdit2.setAlignment(Qt.AlignmentFlag.AlignCenter)  # 设置文本居中
        dateInputLayout.addWidget(self.monthEdit2)
        dateInputLayout.addWidget(QLabel("月"))

        # 日输入及标签
        self.dayEdit2 = QLineEdit(self)
        self.dayEdit2.setFixedHeight(30)
        self.dayEdit2.setAlignment(Qt.AlignmentFlag.AlignCenter)  # 设置文本居中
        dateInputLayout.addWidget(self.dayEdit2)
        dateInputLayout.addWidget(QLabel("日"))

        # 将年月日的水平布局添加到网格布局
        gridLayout.addLayout(dateInputLayout, 1, 1, 1, 2)

        # 创建水平布局并添加按钮
        buttonLayout = QHBoxLayout()
        getCurrentDateButton = QPushButton("获取当前日期", self)
        getCurrentDateButton.setFixedHeight(30)
        button_style = """
                                    QPushButton {
                                        background-color: white;
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
        getCurrentDateButton.setStyleSheet(button_style)
        getCurrentDateButton.clicked.connect(self.getCurrentDate)
        buttonLayout.addWidget(getCurrentDateButton)

        calculateButton2 = QPushButton("获取双干具体时间", self)
        calculateButton2.setFixedHeight(30)
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
        calculateButton2.setStyleSheet(button_style)
        calculateButton2.clicked.connect(self.calculateDoubleTime)
        buttonLayout.addWidget(calculateButton2)
        # 将按钮布局添加到网格布局中
        gridLayout.addLayout(buttonLayout, 2, 1, 1, 4)  # 适当调整列的跨度以适应两个按钮
        # 两个输出框
        self.edit1 = QLineEdit(self)
        self.edit1.setFixedHeight(30)
        self.edit1.setReadOnly(True)
        self.edit1.setAlignment(Qt.AlignmentFlag.AlignCenter)  # 设置文本居中
        self.edit2 = QLineEdit(self)
        self.edit2.setFixedHeight(30)
        self.edit2.setReadOnly(True)
        self.edit2.setAlignment(Qt.AlignmentFlag.AlignCenter)  # 设置文本居中
        gridLayout.addWidget(self.edit1, 3, 1)
        gridLayout.addWidget(self.edit2, 3, 2)

        # 将以上时间导入定位输入框按钮
        importButton = QPushButton("将以上时间导入定位输入框", self)
        importButton.setFixedHeight(30)
        button_style = """
                                    QPushButton {
                                        background-color: white;
                                        color: black;
                                        border: 3px solid gray;
                                        border-radius: 10px;
                                        padding: 6px;
                                        border-style: outset;
                                    }

                                    QPushButton:hover {
                                        background-color: rgb(160, 160, 120);
                                        color: white;
                                    }
                                """
        importButton.setStyleSheet(button_style)
        importButton.clicked.connect(self.importData)
        gridLayout.addWidget(importButton, 4, 1, 1, 2)
        # 创建并添加按钮
        self.calculateButton = QPushButton("获取定位结果", self)
        self.calculateButton.setFixedHeight(30)
        button_style = """
                            QPushButton {
                                background-color: white;
                                color: black;
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
        self.calculateButton.setStyleSheet(button_style)
        self.calculateButton.clicked.connect(self.calculateLocationResults)  # 连接点击事件到计算方法
        gridLayout.addWidget(self.calculateButton, 5, 1, 1, 2)
        # 创建清空内容的按钮
        self.clearButton = QPushButton("清空所有内容", self)
        self.clearButton.setFixedHeight(30)
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
        self.clearButton.setStyleSheet(button_style2)
        self.clearButton.clicked.connect(self.clearAllContents)  # 连接点击事件到清空方法
        gridLayout.addWidget(self.clearButton, 6, 1, 1, 2)  # 添加按钮到网格布局

        # 大的输出框
        self.largeEdit = QLineEdit(self)
        self.largeEdit.setFixedHeight(255)  # 大输出框设置更高的高度
        self.largeEdit.setReadOnly(True)
        self.largeEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)  # 设置文本居中
        self.largeEdit.setStyleSheet("""
                background-color: grey;
                color: black;  /* 设置文本颜色为红色 */
                font-size: 50px;  /* 设置字体大小为140像素 */
                font-weight: bold;  /* 设置字体粗细为粗体 */
            """)
        gridLayout.addWidget(self.largeEdit, 7, 1, 5, 2)  # 添加大输出框到布局

        # 将网格布局添加到总布局
        mainLayout.addLayout(gridLayout)

    def getCurrentDate(self):
        # 获取当前日期和时间
        current_datetime = datetime.datetime.now()

        # 获取年、月、日
        current_year = current_datetime.year
        current_month = current_datetime.month
        current_day = current_datetime.day

        # 将年、月、日设置到输入框中
        self.yearEdit2.setText(str(current_year))
        self.monthEdit2.setText(str(current_month))
        self.dayEdit2.setText(str(current_day))

    def importData(self):
        # 将右侧输入框的数据导入到左侧定位输入框
        self.yearEdit.setText(self.yearEdit2.text())
        self.monthEdit.setText(self.monthEdit2.text())
        self.dayEdit.setText(self.dayEdit2.text())
        self.hourEdit.setText(self.edit1.text())  # 将输出框 self.edit1 的内容导入到 self.hourEdit 输入框

    def calculateDoubleTime(self):
        # 获取年、月、日的输入值
        year2 = int(self.yearEdit2.text())
        month2 = int(self.monthEdit2.text())
        day2 = int(self.dayEdit2.text())

        # 执行计算，这里只是示例，您需要根据您的实际计算规则来编写代码
        def calculate_double_time(year, month, day):
            year = int(year)
            month = int(month)
            day = int(day)
            for i in range(0, 12):
                riganzhi = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][3]
                shichengganzhi = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][4]
                if riganzhi == "甲子" and shichengganzhi == "甲子":
                    for j in range(0, 12):
                        panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                        shichengganzhizhi = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4]
                        if panduanwugan == "戊":
                            hourr = 2 * j
                            ssc = shichengganzhizhi
                            break
                elif riganzhi == "甲戌" and shichengganzhi == "甲戌":
                    for j in range(0, 12):
                        panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                        shichengganzhizhi = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4]
                        if panduanwugan == "己":
                            hourr = 2 * j
                            ssc = shichengganzhizhi
                            break
                elif riganzhi == "甲申" and shichengganzhi == "甲申":
                    for j in range(0, 12):
                        panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                        shichengganzhizhi = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4]
                        if panduanwugan == "庚":
                            hourr = 2 * j
                            ssc = shichengganzhizhi
                            break
                elif riganzhi == "甲寅" and shichengganzhi == "甲子":
                    for j in range(0, 12):
                        panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                        shichengganzhizhi = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4]
                        if panduanwugan == "癸":
                            hourr = 2 * j
                            ssc = shichengganzhizhi
                            break
                elif riganzhi == "甲午" and shichengganzhi == "甲午":
                    for j in range(0, 12):
                        panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                        shichengganzhizhi = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4]
                        if panduanwugan == "辛":
                            hourr = 2 * j
                            ssc = shichengganzhizhi
                            break
                elif riganzhi == "甲辰" and shichengganzhi == "甲辰":
                    for j in range(0, 12):
                        panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                        shichengganzhizhi = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4]
                        if panduanwugan == "壬":
                            hourr = 2 * j
                            ssc = shichengganzhizhi
                            break
                elif riganzhi[0] == "甲" and shichengganzhi[0] == "甲":
                    if riganzhi == "甲子":
                        for j in range(0, 12):
                            panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                            shichengganzhizhi = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4]
                            if panduanwugan == "戊":
                                shuanggan = "戊"
                                hourr = 2 * j
                                ssc = shichengganzhizhi
                                break
                    elif riganzhi == "甲戌":
                        for j in range(0, 12):
                            panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                            shichengganzhizhi = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4]
                            if panduanwugan == "己":
                                shuanggan = "己"
                                hourr = 2 * j
                                ssc = shichengganzhizhi
                                break
                    elif riganzhi == "甲辰":
                        for j in range(0, 12):
                            panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                            shichengganzhizhi = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4]
                            if panduanwugan == "壬":
                                shuanggan = "壬"
                                hourr = 2 * j
                                ssc = shichengganzhizhi
                                break
                    elif riganzhi == "甲寅":
                        for j in range(0, 12):
                            panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                            shichengganzhizhi = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4]
                            if panduanwugan == "癸":
                                shuanggan = "癸"
                                hourr = 2 * j
                                ssc = shichengganzhizhi
                                break
                    elif riganzhi == "甲申":
                        for j in range(0, 12):
                            panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                            shichengganzhizhi = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4]
                            if panduanwugan == "庚":
                                shuanggan = "庚"
                                hourr = 2 * j
                                ssc = shichengganzhizhi
                                break
                    elif riganzhi == "甲午":
                        for j in range(0, 12):
                            panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                            shichengganzhizhi=getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4]
                            if panduanwugan == "辛":
                                shuanggan = "辛"
                                hourr = 2 * j
                                ssc=shichengganzhizhi
                                break
                else:
                    if riganzhi[0] == shichengganzhi[0]:
                        hourr = 2 * i
                        ssc = shichengganzhi
                        break
            return hourr,ssc,riganzhi

        result = calculate_double_time(year2, month2, day2)
        # 将计算结果设置到 self.edit1 输出框中
        self.edit1.setText(str(result[0]))
        self.edit2.setText(f"{result[2]}日，{result[1]}时")

    def clearAllContents(self):
        # 清空所有输入框和输出框
        self.yearEdit.clear()
        self.monthEdit.clear()
        self.dayEdit.clear()
        self.hourEdit.clear()
        self.yearEdit2.clear()
        self.monthEdit2.clear()
        self.dayEdit2.clear()
        self.edit1.clear()
        self.edit2.clear()
        self.largeEdit.clear()
        for edit in self.outputEdits:  # 清空左侧的所有输出框
            edit.clear()



    def calculateLocationResults(self):
        # 获取年、月、日、时的输入值
        def getSpaDigiXdingweideshu(year, month, day, hour):
            year = year
            month = month
            day = day
            hour = hour
            fanhuixinxi = getthebasicmessageofnineGrids(year, month, day, hour)  # 通过应用0获得排盘的基本信息
            ninegridsbasicmessage = fanhuixinxi[0]  # 九宫基本信息
            yinyangdun_ganzhi = fanhuixinxi[1]  # 阴阳遁和干支信息
            for i in range(0, 9):
                if i == 4:
                    pass
                else:
                    bamenpanbiezhishi = ninegridsbasicmessage[i]["八门"]
                    if "使" in bamenpanbiezhishi:
                        zhishigongdingwei_index = i  # 这个编号代表值使所在宫的代号
            SpaDigiX_APPONE_Value = 0
            # 第一套基础编码
            # 请在此处调整数据
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # 1 全盘初判
            # 1.1 值使宫（值使用神），落内遁-1，落外遁+1
            luoneidun = -1  # 落内遁
            luowaidun = +1  # 落外遁
            # -----------------------------------------------------------------------------------------------------------------------
            # 同边要素
            yitong = +2
            ertong = +1
            sitongqietonggong = -1
            wutongqietonggong = -1
            liutong = -1
            qitong = -2
            batong = -2
            # -----------------------------------------------------------------------------------------------------------------------
            # 1.4 驿马落（冲）用神宫
            yimaluoyongshengong = -1  # 落用神宫
            yimachongyongshengong = -1  # 冲用神宫
            # -----------------------------------------------------------------------------------------------------------------------
            # 1.5 用神宫空亡
            yongshengongdankong = +1  # 单空
            yongshengongshuangkong = +2  # 双空
            yongshengongsikong = +4  # 四空
            # -----------------------------------------------------------------------------------------------------------------------
            # 支冲
            zhichongone = +1
            zhichongtwo = +2
            # -----------------------------------------------------------------------------------------------------------------------
            # 2 单宫部分
            # -----------------------------------------------------------------------------------------------------------------------
            # 2.1 吉格
            wubing = -3  # 戊＋丙
            bingwu = -3  # 丙＋戊
            bingding = -1  # 丙＋丁
            yiwu_kaimen = -1  # 乙＋戊（开门）
            yiji_kaimen = -1  # 乙＋己（开门）
            tianpanding_xiumen_taiyin = -1  # 丁（休门）＋ 太阴神
            yi_kaixiusheng_xunsi = -1  # 乙（开门或休门或生门）＋巽四宫
            yixin_kaixiusheng = -1  # 乙＋辛（开门或休门或生门）
            yi_kaixiusheng_kanyigui = -1  # 乙（开门或休门或生门）＋坎一宫或癸
            yixin_xiusheng_genba = -1  # 乙＋辛（休门或生门）＋艮八宫
            yi_du_jiudi = -1  # 乙（杜门）＋九地神
            bing_sheng_jiutian = -1  # 丙（生门）＋九天神
            # -----------------------------------------------------------------------------------------------------------------------
            # 2.2 三奇得使
            yijiaxu = -1  # 乙＋甲戌
            dingjiachen = -1  # 丁＋甲辰
            # -----------------------------------------------------------------------------------------------------------------------
            # 2.3 玉女守门 （暂不考虑）
            # -----------------------------------------------------------------------------------------------------------------------
            # 2.4 三诈
            yiorbingording_kai_taiyin = -1  # 乙、丙、丁（开门）十神盘（太阴）
            yiorbingording_xiu_jiudi = -1  # 乙、丙、丁（体门）十神盘（九地）
            yiorbingording_sheng_liuhe = -1  # 乙、丙、丁（生门）十神盘（六合）
            # -----------------------------------------------------------------------------------------------------------------------
            # 2.5 五假
            yiorbingording_jing_jiutian = -1  # 乙、丙、丁十景门（九天）
            dingorjiorgui_du_jiuditaiyinliuhe = -1  # 丁、已、癸十杜门（九地、太阴、六合）
            dingorjiorgui_du_shang_liuhe = -1  # 丁、已、癸十伤门（六合）
            ren_jing_jiutian = -1  # 六壬十惊门（九天）
            dingorjiorgui_si_jiudi = -1  # 丁、已、癸十死门（九地）
            # -----------------------------------------------------------------------------------------------------------------------
            # 2.6 三奇升殿、奇游禄位 均为-1
            yi_kaixiusheng_zhengsan = -1  # 乙（震）（开、休、生）
            bing_kaixiusheng_lijiu = -1  # 丙（离）（开、休、生）
            ding_kaixiusheng_duiqi = -1  # 丁（兑）（开、休、生）
            bing_kaixiusheng_xunsi = -1  # 丙（巽）（开、休、生）
            ding_kaixiusheng_lijiu = -1  # 丁（离）（开、休、生）
            # -----------------------------------------------------------------------------------------------------------------------
            # 2.7 奇仪相合 加0 不考虑
            # -----------------------------------------------------------------------------------------------------------------------
            # 2.8 交泰格、天运格
            yiding = -1  # 乙十丁
            dingbing = -1  # 丁十丙
            dingyi = -1  # 丁十乙
            # -----------------------------------------------------------------------------------------------------------------------
            # 2.9 欢怡、相佐
            yiordingjiaziwu = -1  # 乙、丙、丁十六甲值符 ----->去掉丙，改六甲值符为甲子戊
            jiaziwuyiording = -1  # 六甲值符十乙、丙、丁 ----->去掉丙，改六甲值符为甲子戊
            # -----------------------------------------------------------------------------------------------------------------------
            # 2.10 凶格
            gengbing = +3  # 庚十丙
            binggeng = +3  # 丙十庚
            yixin = +1  # 乙十辛
            xinyi = +1  # 辛十乙
            guiding = +1  # 癸十丁
            dinggui = +1  # 丁十癸
            jiaziwugeng = +3  # 六甲值符十庚 ----->改六甲值符为甲子戊
            gengjiaziwu = +3  # 庚十六甲值符 ----->改六甲值符为甲子戊
            # -----------------------------------------------------------------------------------------------------------------------
            # 2.11 其他凶格（更凶）
            gengji = +2  # 刑格
            genggui = +2  # 大格
            gengren = +2  # 小格
            gengniangan = +2  # 岁格
            gengyuegan = +2  # 月格
            gengrigan = +2  # 日格
            gengshigan = +2  # 时格
            rigangeng = +2  # 飞干格
            # -----------------------------------------------------------------------------------------------------------------------
            # 2.12 三奇入暮、时干入暮
            yi_qiankun = +1  # 乙（乾、坤）
            bing_qianliu = +1  # 丙（乾）
            ding_genqian = +1  # 丁（艮、乾）
            shiganwuxu = +1  # 戊戌
            shiganrencheng = +1  # 壬辰
            shiganbingxu = +1  # 丙戌
            shiganguiwei = +1  # 癸未
            shigandingchou = +1  # 丁丑
            # -----------------------------------------------------------------------------------------------------------------------
            # 2.13 六仪击刑
            jiaziwu_zhengsan = +1  # 甲子戊（震）
            jiaxuji_kuner = +1  # 甲戌已（坤）
            jiashengeng_genba = +1  # 甲申庚（艮）
            jiawuxin_lijiu = +1  # 甲午辛（离）
            jiachenren_xunsi = +1  # 甲辰王（巽）
            jiayingui_xunsi = +1  # 甲寅癸（巽）
            # -----------------------------------------------------------------------------------------------------------------------
            # 2.14 奇格
            gengyiorbingording = +1  # 庚十乙、丙、丁
            # -----------------------------------------------------------------------------------------------------------------------
            # 2.15 天网
            jiaziwugui = +1  # 六甲值符十癸 ----->六甲值符改为甲子戊
            guigui = +1  # 癸十癸
            # -----------------------------------------------------------------------------------------------------------------------
            # 2.16 五不遇时  （暂时不考虑）
            # -----------------------------------------------------------------------------------------------------------------------
            # 2.17 其他格
            # -----------------------------------------------------------------------------------------------------------------------
            # 2.17.1 甲
            jiayi_jimen = -1  # 甲十乙(门吉)
            jiayi_xiongmen = +1  # 甲十乙(门凶)
            jiaxin_xiongmen = +1  # 甲十辛（门凶）
            jiaren = +1  # 甲十壬
            jiagui_jimen = -1  # 甲+癸(门吉)
            jiagui_xiongmen = +1  # 甲+癸(门凶)
            # -----------------------------------------------------------------------------------------------------------------------
            # 2.17.2 乙
            yijia = -1  # 乙十甲
            yibing = -1  # 乙十丙
            yibing_xiongmenxiongxin = +1  # 乙十丙（凶门星凶）
            yiding = -1  # 乙十丁
            yiyi = -1  # 乙+乙
            yiwu = -1  # 乙十戊
            yiwu_xiongmenmenpo = +1  # 乙十戊（门凶门迫）
            yiji_jimen = -1  # 乙十己（三吉门）
            yiji_jimenchuwai = +1  # 乙十己（吉门除外）
            yigeng_kai_xun = -1  # 乙十庚（巽宫开门）
            yigeng_qita = +1  # 乙十庚（其他情况）
            yixin_sheng_gen = -1  # 乙十辛(艮宫、生门)
            yixin_kai_kun = -1  # 乙十辛(坤宫、开门)
            yixin_qita = +1  # 乙十辛(其他情况)
            yiren_xiongmen = +1  # 乙十壬（门凶）
            yiren_jimen = -1  # 乙十壬（门吉）
            yigui_jimen = -1  # 乙十癸(门吉)
            yigui_qita = +1  # 乙十癸(其他情况)
            # -----------------------------------------------------------------------------------------------------------------------
            # 2.17.3 丙
            bingyi = -1  # 丙十乙
            bingbing = +1  # 丙十丙
            bingding = -1  # 丙十丁
            bingji_jimen = -1  # 丙十已（吉门)
            bingji_xiongmen = +1  # 丙十已（凶门)
            bingxin = +1  # 丙十辛
            bingren = +1  # 丙十壬
            binggui = +1  # 丙十癸
            # -----------------------------------------------------------------------------------------------------------------------
            # 2.17.4 丁
            dingjia = -1  # 丁十甲
            dingding = -1  # 丁十丁
            dingwu = -1  # 丁十戊
            dingji = +1  # 丁十己
            dinggeng = +1  # 丁十庚
            dingxin = +1  # 丁十辛
            # -----------------------------------------------------------------------------------------------------------------------
            # 2.17.5 戊
            wujia_jimen = -1  # 戊十甲（门吉）
            wuyi_jimen = -1  # 戊十乙(门吉)
            wuyi_xiongmen = +1  # 戊十乙(门凶)
            wuding = +1  # 戊十丁
            wuwu = +1  # 戊十戊
            wuxin_jimen = -1  # 戊十辛(门吉)
            wuxin_xiongmen = +1  # 戊十辛(门凶)
            wuren = +1  # 戊十壬
            jiaziwugui_mengongxiangshen = -1  # 戊十癸(门宫相生)
            # -----------------------------------------------------------------------------------------------------------------------
            # 2.17.6 己
            jijia = +1  # 己十甲
            jiyi = +1  # 己十乙
            jibing = +1  # 己十丙
            jiding = -1  # 己十丁
            jiji = +1  # 己十己
            jigeng = +1  # 己十庚
            jixin = +1  # 己十辛
            jiren = +1  # 己十壬
            jigui = +1  # 己十癸
            # -----------------------------------------------------------------------------------------------------------------------、
            # 2.17.7 庚
            gengding = +1  # 庚十丁
            gengding_jimen = -1  # 庚十丁（吉门）
            genggeng = +2  # 庚十庚
            gengwu = +3  # 庚+戊
            gengxin = +2  # 庚十辛
            # -----------------------------------------------------------------------------------------------------------------------
            # 2.17.8 辛
            xinjia = +1  # 辛十甲
            xinbing_jimen = -1  # 辛十丙（门吉）
            xinbing_qita = +1  # 辛十丙（其他门）
            xinding = -1  # 辛十丁
            xinwu = +1  # 辛十戊
            xinji = +1  # 辛十己
            xingeng = +2  # 辛十庚
            xinxin = +1  # 辛十辛
            xinren = +1  # 辛十壬
            xingui = +1  # 辛十癸
            # -----------------------------------------------------------------------------------------------------------------------
            # 2.17.9 壬
            renjia = +1  # 壬十甲
            renyi = +1  # 壬十乙
            renbing = +1  # 壬十丙
            renwu = +1  # 壬十戊
            renji = +1  # 壬十己
            renxin = +1  # 壬十辛
            rengui = +1  # 壬十癸
            rending = +1  # 壬+丁
            rengeng = +1  # 壬+庚
            renren = +1  # 壬+壬
            # -----------------------------------------------------------------------------------------------------------------------
            # 2.17.10 癸
            guijia = -1  # 癸十甲
            guiyi_jimen = -1  # 癸十乙（门吉）
            guiyi_qita = +1  # 癸十乙（其他门）
            guibing = +1  # 癸十丙
            guiding = +1  # 癸十丁
            guiwu = -1  # 癸十戊
            guiwu_xiongmenpozhi = +1  # 癸十戊（门凶廹制）
            guiji = +1  # 癸十己
            guigeng = +2  # 癸十庚
            guixin = +1  # 癸十辛
            guiren = +1  # 癸十壬
            # -----------------------------------------------------------------------------------------------------------------------
            # 3 单宫天盘干定数
            # -----------------------------------------------------------------------------------------------------------------------
            # 3.1 十二个月份各干定数数据
            month_dict_dangongtianpangandingshu = {
                "寅": {"甲": -1, "乙": -1, "丙": -1, "丁": -1, "戊": 1, "己": 1, "庚": 1, "辛": 1, "壬": 0, "癸": 0},
                "卯": {"甲": -1, "乙": -1, "丙": -1, "丁": -1, "戊": 1, "己": 1, "庚": 1, "辛": 1, "壬": 0, "癸": 0},
                "辰": {"甲": 1, "乙": 1, "丙": 0, "丁": 0, "戊": -1, "己": -1, "庚": -1, "辛": -1, "壬": 1, "癸": 1},
                "巳": {"甲": 0, "乙": 0, "丙": -1, "丁": -1, "戊": -1, "己": -1, "庚": 1, "辛": 1, "壬": 1, "癸": 1},
                "午": {"甲": 0, "乙": 0, "丙": -1, "丁": -1, "戊": -1, "己": -1, "庚": 1, "辛": 1, "壬": 1, "癸": 1},
                "未": {"甲": 1, "乙": 1, "丙": 0, "丁": 0, "戊": -1, "己": -1, "庚": -1, "辛": -1, "壬": 1, "癸": 1},
                "申": {"甲": 1, "乙": 1, "丙": 1, "丁": 1, "戊": 0, "己": 0, "庚": -1, "辛": -1, "壬": -1, "癸": -1},
                "酉": {"甲": 1, "乙": 1, "丙": 1, "丁": 1, "戊": 0, "己": 0, "庚": -1, "辛": -1, "壬": -1, "癸": -1},
                "戌": {"甲": 1, "乙": 1, "丙": 0, "丁": 0, "戊": -1, "己": -1, "庚": -1, "辛": -1, "壬": 1, "癸": 1},
                "亥": {"甲": -1, "乙": -1, "丙": 1, "丁": 1, "戊": 1, "己": 1, "庚": 0, "辛": 0, "壬": -1, "癸": -1},
                "子": {"甲": -1, "乙": -1, "丙": 1, "丁": 1, "戊": 1, "己": 1, "庚": 0, "辛": 0, "壬": -1, "癸": -1},
                "丑": {"甲": 1, "乙": 1, "丙": 0, "丁": 0, "戊": -1, "己": -1, "庚": -1, "辛": -1, "壬": 1, "癸": 1}
            }
            # -----------------------------------------------------------------------------------------------------------------------
            # 3.2 九宫各天盘干定数数据
            palace_dict_dangongtianpangandingshu = {
                0: {"甲": -1, "乙": -1, "丙": 1, "丁": 1, "戊": 1, "己": 1, "庚": 0, "辛": 0, "壬": -1, "癸": -1},
                1: {"甲": 1, "乙": 1, "丙": 0, "丁": 0, "戊": -1, "己": -1, "庚": -1, "辛": -1, "壬": 1, "癸": 1},
                2: {"甲": -1, "乙": -1, "丙": -1, "丁": -1, "戊": 1, "己": 1, "庚": 1, "辛": 1, "壬": 0, "癸": 0},
                3: {"甲": -1, "乙": -1, "丙": -1, "丁": -1, "戊": 1, "己": 1, "庚": 1, "辛": 1, "壬": 0, "癸": 0},
                5: {"甲": 1, "乙": 1, "丙": 1, "丁": 1, "戊": 0, "己": 0, "庚": -1, "辛": -1, "壬": -1, "癸": -1},
                6: {"甲": 1, "乙": 1, "丙": 1, "丁": 1, "戊": 0, "己": 0, "庚": -1, "辛": -1, "壬": -1, "癸": -1},
                7: {"甲": 1, "乙": 1, "丙": 0, "丁": 0, "戊": -1, "己": -1, "庚": -1, "辛": -1, "壬": 1, "癸": 1},
                8: {"甲": 0, "乙": 0, "丙": -1, "丁": -1, "戊": -1, "己": -1, "庚": 1, "辛": 1, "壬": 1, "癸": 1}
            }
            # -----------------------------------------------------------------------------------------------------------------------
            # 3.3天盘干与地盘干五行力量消长定数数据
            tianpandingwei_dict_dangongtianpangandingshu = {
                "甲": {"甲": -1, "乙": -1, "丙": -1, "丁": -1, "戊": 1, "己": 1, "庚": 1, "辛": 1, "壬": -1, "癸": -1},
                "乙": {"甲": -1, "乙": -1, "丙": 0, "丁": 0, "戊": 1, "己": 1, "庚": 1, "辛": 1, "壬": -1, "癸": -1},
                "丙": {"甲": -1, "乙": -1, "丙": -1, "丁": -1, "戊": 0, "己": 0, "庚": 1, "辛": 1, "壬": 1, "癸": 1},
                "丁": {"甲": -1, "乙": -1, "丙": -1, "丁": -1, "戊": 0, "己": 0, "庚": 1, "辛": 1, "壬": 1, "癸": 1},
                "戊": {"甲": 1, "乙": 1, "丙": -1, "丁": -1, "戊": -1, "己": -1, "庚": 0, "辛": 0, "壬": 1, "癸": 1},
                "己": {"甲": 0, "乙": 1, "丙": -1, "丁": -1, "戊": -1, "己": -1, "庚": 0, "辛": 0, "壬": 1, "癸": 1},
                "庚": {"甲": 1, "乙": 1, "丙": 1, "丁": 1, "戊": -1, "己": -1, "庚": -1, "辛": -1, "壬": 0, "癸": 0},
                "辛": {"甲": 1, "乙": 1, "丙": 1, "丁": 1, "戊": -1, "己": -1, "庚": -1, "辛": -1, "壬": 0, "癸": 0},
                "壬": {"甲": 0, "乙": 0, "丙": 1, "丁": 1, "戊": 1, "己": 1, "庚": -1, "辛": -1, "壬": -1, "癸": -1},
                "癸": {"甲": 0, "乙": 0, "丙": 1, "丁": 1, "戊": 1, "己": 1, "庚": -1, "辛": -1, "壬": -1, "癸": -1}
            }
            # -----------------------------------------------------------------------------------------------------------------------
            # 3.4 天盘干 长生 帝旺 墓 绝 十二宫得数：
            changshenglinguandiwang = -2  # 天盘干位于 长生 临官 帝旺
            guandaishuai = -1  # 天盘干位于 冠带 衰
            taiyangmuyu = 0  # 天盘干位于 胎 养 沐浴
            bingsijue = +2  # 天盘干位于 病 死 绝
            mu = +1  # 天盘干位于 墓
            # 动物宫与天盘干对应表
            tianpanganduiyingongweishengxiao = {
                "甲": ["亥", "子", "丑", "寅", "卯", "辰", "已", "午", "未", "申", "酉", "戌"],
                "乙": ["午", "已", "辰", "卯", "寅", "丑", "子", "亥", "戌", "酉", "申", "未"],
                "丙": ["寅", "卯", "辰", "已", "午", "未", "申", "酉", "戌", "亥", "子", "丑"],
                "丁": ["酉", "申", "未", "午", "已", "辰", "卯", "寅", "丑", "子", "亥", "戌"],
                "戊": ["寅", "卯", "辰", "已", "午", "未", "申", "酉", "戌", "亥", "子", "丑"],
                "己": ["酉", "申", "未", "午", "已", "辰", "卯", "寅", "丑", "子", "亥", "戌"],
                "庚": ["已", "午", "未", "申", "酉", "戌", "亥", "子", "丑", "寅", "卯", "辰"],
                "辛": ["子", "亥", "戌", "酉", "申", "未", "午", "已", "辰", "卯", "寅", "丑"],
                "壬": ["申", "酉", "戌", "亥", "子", "丑", "寅", "卯", "辰", "已", "午", "未"],
                "癸": ["卯", "寅", "丑", "子", "亥", "戌", "酉", "申", "未", "午", "已", "辰"]
            }
            # -----------------------------------------------------------------------------------------------------------------------
            # 4 单宫九星力量消长定数
            # -----------------------------------------------------------------------------------------------------------------------
            # 4.1 十二月各星力量
            yuefenduiyingjiuxingliliang = {
                "寅": {"天蓬": -1, "天芮": 1, "天冲": -1, "天辅": -1, "天禽": 1, "天心": 1, "天柱": 1, "天任": 1,
                       "天英": 1},
                "卯": {"天蓬": -1, "天芮": 1, "天冲": -1, "天辅": -1, "天禽": 1, "天心": 0, "天柱": 1, "天任": 1,
                       "天英": 1},
                "辰": {"天蓬": 1, "天芮": -1, "天冲": 1, "天辅": -1, "天禽": -1, "天心": 1, "天柱": 1, "天任": -1,
                       "天英": -1},
                "巳": {"天蓬": 1, "天芮": 1, "天冲": -1, "天辅": -1, "天禽": 1, "天心": 1, "天柱": 1, "天任": 1,
                       "天英": -1},
                "午": {"天蓬": 1, "天芮": 1, "天冲": -1, "天辅": -1, "天禽": 1, "天心": 1, "天柱": 1, "天任": 1,
                       "天英": -1},
                "未": {"天蓬": 1, "天芮": -1, "天冲": 1, "天辅": 0, "天禽": -1, "天心": 1, "天柱": 1, "天任": -1,
                       "天英": -1},
                "申": {"天蓬": 1, "天芮": -1, "天冲": 1, "天辅": 1, "天禽": -1, "天心": -1, "天柱": -1, "天任": -1,
                       "天英": 1},
                "酉": {"天蓬": 1, "天芮": -1, "天冲": 1, "天辅": 1, "天禽": -1, "天心": -1, "天柱": -1, "天任": -1,
                       "天英": 0},
                "戌": {"天蓬": 1, "天芮": -1, "天冲": 1, "天辅": 0, "天禽": -1, "天心": 1, "天柱": 1, "天任": -1,
                       "天英": -1},
                "亥": {"天蓬": -1, "天芮": 0, "天冲": 1, "天辅": 1, "天禽": 1, "天心": -1, "天柱": -1, "天任": 0,
                       "天英": 1},
                "子": {"天蓬": -1, "天芮": 1, "天冲": 1, "天辅": 1, "天禽": 1, "天心": -1, "天柱": -1, "天任": 1,
                       "天英": 1},
                "丑": {"天蓬": 1, "天芮": -1, "天冲": 1, "天辅": 1, "天禽": -1, "天心": 1, "天柱": 1, "天任": -1,
                       "天英": -1}
            }
            # -----------------------------------------------------------------------------------------------------------------------
            # 4.2 九宫各星力量
            jiugonggexingliliangshuju = {
                0: {"天蓬": -1, "天芮": 1, "天冲": 1, "天辅": 1, "天禽": 0, "天心": -1, "天柱": -1, "天任": 1,
                    "天英": 1},
                1: {"天蓬": 1, "天芮": -1, "天冲": 1, "天辅": 1, "天禽": -1, "天心": 1, "天柱": 1, "天任": -1,
                    "天英": -1},
                2: {"天蓬": -1, "天芮": 1, "天冲": -1, "天辅": -1, "天禽": 1, "天心": 1, "天柱": 1, "天任": 1,
                    "天英": 1},
                3: {"天蓬": -1, "天芮": 1, "天冲": -1, "天辅": -1, "天禽": 1, "天心": 1, "天柱": 1, "天任": 1,
                    "天英": 1},
                5: {"天蓬": 1, "天芮": -1, "天冲": 1, "天辅": 1, "天禽": -1, "天心": -1, "天柱": -1, "天任": -1,
                    "天英": 1},
                6: {"天蓬": 1, "天芮": -1, "天冲": 1, "天辅": 1, "天禽": -1, "天心": -1, "天柱": -1, "天任": -1,
                    "天英": 1},
                7: {"天蓬": 1, "天芮": -1, "天冲": 1, "天辅": 0, "天禽": -1, "天心": 1, "天柱": 1, "天任": -1,
                    "天英": -1},
                8: {"天蓬": 1, "天芮": 1, "天冲": -1, "天辅": -1, "天禽": 1, "天心": 1, "天柱": 1, "天任": 1,
                    "天英": -1}
            }
            # -----------------------------------------------------------------------------------------------------------------------
            # 4.3 吉凶星变化
            jiuxingyutianpanganbianhuashuju = {
                "天辅": {"甲": -1, "乙": -1, "丙": -1, "丁": -1},
                "天禽": {"戊": -1, "己": -1, "庚": -1, "辛": -1},
                "天心": {"庚": -1, "辛": -1, "壬": -1, "癸": -1},
                "天冲": {"甲": -1, "乙": -1, "丙": -1, "丁": -1},
                "天英": {"丙": -1, "丁": -1, "戊": -1, "己": -1},
                "天蓬": {"甲": 1, "乙": 1, "戊": 1, "己": 1},
                "天芮": {"丙": 1, "丁": 1, "壬": 1, "癸": 1},
                "天柱": {"丙": 1, "丁": 1, "戊": 1, "己": 1},
                "天任": {"戊": -1, "己": -1, "庚": -1, "辛": -1}
            }
            # -----------------------------------------------------------------------------------------------------------------------
            # 5 单宫八门力量消长定数
            # -----------------------------------------------------------------------------------------------------------------------
            # 5.1 八门在十二个月力量
            bamenshieryueshuju = {
                "寅": {"开": 0, "休": -1, "生": 1, "伤": -1, "杜": -1, "景": -1, "死": 1, "惊": 1},
                "卯": {"开": 0, "休": -1, "生": 1, "伤": -1, "杜": -1, "景": -1, "死": 1, "惊": 1},
                "辰": {"开": -1, "休": 1, "生": -1, "伤": +1, "杜": +1, "景": 0, "死": -1, "惊": -1},
                "巳": {"开": 1, "休": 1, "生": -1, "伤": -1, "杜": -1, "景": -1, "死": 0, "惊": 1},
                "午": {"开": 1, "休": 1, "生": -1, "伤": 0, "杜": -1, "景": -1, "死": -1, "惊": 1},
                "未": {"开": -1, "休": 1, "生": -1, "伤": 1, "杜": 1, "景": -1, "死": -1, "惊": -1},
                "申": {"开": -1, "休": -1, "生": -1, "伤": 1, "杜": 1, "景": 1, "死": 0, "惊": -1},
                "酉": {"开": -1, "休": -1, "生": -1, "伤": 1, "杜": 1, "景": 1, "死": 0, "惊": -1},
                "戌": {"开": -1, "休": 1, "生": -1, "伤": 1, "杜": 1, "景": 1, "死": -1, "惊": -1},
                "亥": {"开": -1, "休": -1, "生": 1, "伤": -1, "杜": -1, "景": 1, "死": 1, "惊": 1},
                "子": {"开": -1, "休": -1, "生": 1, "伤": -1, "杜": -1, "景": 1, "死": 1, "惊": 1},
                "丑": {"开": -1, "休": 1, "生": -1, "伤": 1, "杜": 1, "景": 0, "死": -1, "惊": -1}
            }
            # -----------------------------------------------------------------------------------------------------------------------
            # 5.2 八门在九宫中力量消长
            bamenjiugongliliangxiaozhangshuju = {
                0: {"开": -1, "休": -1, "生": 1, "伤": -1, "杜": -1, "景": 1, "死": 1, "惊": 0},
                1: {"开": -1, "休": 1, "生": -1, "伤": 1, "杜": 1, "景": -1, "死": -1, "惊": -1},
                2: {"开": 1, "休": -1, "生": 1, "伤": -1, "杜": -1, "景": -1, "死": 1, "惊": 1},
                3: {"开": 1, "休": -1, "生": 1, "伤": -1, "杜": -1, "景": -1, "死": 1, "惊": 1},
                5: {"开": -1, "休": -1, "生": -1, "伤": 1, "杜": 1, "景": 1, "死": -1, "惊": -1},
                6: {"开": -1, "休": -1, "生": -1, "伤": 1, "杜": 1, "景": 1, "死": -1, "惊": -1},
                7: {"开": -1, "休": 1, "生": -1, "伤": 1, "杜": 1, "景": -1, "死": -1, "惊": -1},
                8: {"开": 1, "休": 1, "生": -1, "伤": -1, "杜": -1, "景": -1, "死": -1, "惊": 1}
            }
            # -----------------------------------------------------------------------------------------------------------------------
            # 5.3 几种特殊门遇天盘干 地盘干的变化
            # 遇地盘干
            menyudipanganshuju = {
                "开": {"丙": -1, "丁": -1, "戊": -1, "己": -1},
                "休": {"庚": -1, "辛": -1, "戊": -1, "己": -1},
                "生": {"甲": -1, "乙": -1, "壬": -1, "癸": -1},
                "死": {"庚": 1, "辛": 1, "戊": 1, "己": 1},
                "惊": {"壬": 1, "癸": 1, "庚": 1, "辛": 1}
            }
            # 遇天盘干
            menyutianpanganshuju = {
                "开": {"庚": -1, "辛": -1, "壬": -1, "癸": -1},
                "休": {"甲": -1, "乙": -1, "壬": -1, "癸": -1},
                "生": {"庚": -1, "辛": -1, "戊": -1, "己": -1},
                "死": {"壬": 1, "癸": 1, "甲": 1, "乙": 1},
                "惊": {"甲": 1, "乙": 1, "丙": 1, "丁": 1}
            }
            # -----------------------------------------------------------------------------------------------------------------------
            # 6 八神单宫力量消长定数
            # -----------------------------------------------------------------------------------------------------------------------
            # 6.1 八神在十二月力量消长
            bashenshieryueliliangxiaozhangshuju = {
                "寅": {"值符": -1, "螣蛇": -1, "太阴": 1, "六合": -1, "白虎": 1, "玄武": 0, "九地": 1, "九天": 1},
                "卯": {"值符": -1, "螣蛇": -1, "太阴": 1, "六合": -1, "白虎": 1, "玄武": 0, "九地": 1, "九天": 1},
                "辰": {"值符": 1, "螣蛇": 0, "太阴": -1, "六合": 1, "白虎": -1, "玄武": 1, "九地": -1, "九天": -1},
                "巳": {"值符": 0, "螣蛇": -1, "太阴": 1, "六合": 0, "白虎": 1, "玄武": 1, "九地": -1, "九天": 1},
                "午": {"值符": -1, "螣蛇": -1, "太阴": 1, "六合": 0, "白虎": 1, "玄武": 1, "九地": -1, "九天": 1},
                "未": {"值符": 1, "螣蛇": 0, "太阴": -1, "六合": 1, "白虎": -1, "玄武": 1, "九地": -1, "九天": -1},
                "申": {"值符": 1, "螣蛇": 1, "太阴": -1, "六合": 1, "白虎": -1, "玄武": -1, "九地": 0, "九天": -1},
                "酉": {"值符": 1, "螣蛇": 0, "太阴": -1, "六合": 1, "白虎": -1, "玄武": -1, "九地": 0, "九天": -1},
                "戌": {"值符": 0, "螣蛇": 1, "太阴": -1, "六合": 1, "白虎": -1, "玄武": 1, "九地": -1, "九天": -1},
                "亥": {"值符": -1, "螣蛇": 1, "太阴": 0, "六合": -1, "白虎": 0, "玄武": -1, "九地": 1, "九天": 0},
                "子": {"值符": -1, "螣蛇": 1, "太阴": 0, "六合": -1, "白虎": 0, "玄武": -1, "九地": 1, "九天": 0},
                "丑": {"值符": 1, "螣蛇": 0, "太阴": -1, "六合": 1, "白虎": -1, "玄武": 1, "九地": -1, "九天": -1}
            }
            # -----------------------------------------------------------------------------------------------------------------------
            # 6.2 八神在九宫内力量消长
            bashenzaijiugongliliangxiaozhangshuju = {
                0: {"值符": 0, "螣蛇": 1, "太阴": -1, "六合": 0, "白虎": -1, "玄武": -1, "九地": 1, "九天": -1},
                1: {"值符": 1, "螣蛇": -1, "太阴": 0, "六合": 1, "白虎": 0, "玄武": 1, "九地": -1, "九天": 0},
                2: {"值符": -1, "螣蛇": 0, "太阴": 1, "六合": -1, "白虎": 1, "玄武": -1, "九地": 1, "九天": 1},
                3: {"值符": -1, "螣蛇": 0, "太阴": 1, "六合": -1, "白虎": 1, "玄武": -1, "九地": 1, "九天": 1},
                5: {"值符": 1, "螣蛇": 1, "太阴": -1, "六合": 1, "白虎": -1, "玄武": 0, "九地": -1, "九天": -1},
                6: {"值符": 1, "螣蛇": 1, "太阴": -1, "六合": 1, "白虎": -1, "玄武": 0, "九地": -1, "九天": -1},
                7: {"值符": 0, "螣蛇": -1, "太阴": 0, "六合": 1, "白虎": 0, "玄武": 1, "九地": -1, "九天": 0},
                8: {"值符": -1, "螣蛇": -1, "太阴": 1, "六合": -1, "白虎": 1, "玄武": 1, "九地": 0, "九天": 1}
            }
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------

            # 一、全盘初判
            print("-------------------------------------\n1 全盘初判")
            # -----------------------------------------------------------------------------------------------------------------------
            # 1.1 值使宫（值使用神），落内遁-1，落外遁+1
            # ------------------------------------
            zuocegonghao = [0, 7, 2, 3]
            youcegonghao = [8, 1, 6, 5]
            yinyangdun = yinyangdun_ganzhi[0]
            JQ = yinyangdun_ganzhi[5]
            if yinyangdun == "阳遁":
                if zhishigongdingwei_index in zuocegonghao:
                    BIAN = 0
                    dun = "内遁"
                elif zhishigongdingwei_index in youcegonghao:
                    BIAN = 1
                    dun = "外遁"
            else:
                if zhishigongdingwei_index in zuocegonghao:
                    BIAN = 0
                    dun = "外遁"
                elif zhishigongdingwei_index in youcegonghao:
                    BIAN = 1
                    dun = "内遁"
            if dun == "内遁":
                SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + luoneidun  ###落在内遁
                if luoneidun >= 0:
                    dunjian = f"{luoneidun}"
                else:
                    dunjian = f"{luoneidun}"
            elif dun == "外遁":
                SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + luowaidun  ###落在外遁
                if luowaidun >= 0:
                    dunjian = f"{luowaidun}"
                else:
                    dunjian = f"{luowaidun}"
            print("----------------------")
            print(f"落{dun}--->{dunjian}")
            neiwaidunSDX = SpaDigiX_APPONE_Value
            # -------------------------------------
            # 1.2 值使为用神，同边八要素加减规则
            # -------------------------------------
            # 八要素所在宫号获取
            # 值符
            for i in range(0, 9):
                if i == 4:
                    pass
                else:
                    bashenpanbiezhifu = ninegridsbasicmessage[i]["八神"]
                    if bashenpanbiezhifu == "值符":
                        zhifugongdingwei_index = i  # 值符所在宫号
            # 生门
            for i in range(0, 9):
                if i == 4:
                    pass
                else:
                    bamenpanbieshengmen = ninegridsbasicmessage[i]["八门"]
                    if bamenpanbieshengmen == "生" or bamenpanbieshengmen == "生使":
                        shengmendingwei_index = i  # 生门所在宫号
                    else:
                        pass
            # 甲子戊
            for i in range(0, 9):
                if i == 4:
                    pass
                else:
                    tianpanpanbiejiaziwu = ninegridsbasicmessage[i]["天盘"]
                    if len(tianpanpanbiejiaziwu) == 1:
                        pass
                    elif len(tianpanpanbiejiaziwu) == 3:
                        if tianpanpanbiejiaziwu == "甲子戊":
                            jiaziwudingwei_index = i
                    else:
                        tianpanchaifenliebiao = tianpanpanbiejiaziwu.split("\n")
                        if len(tianpanchaifenliebiao[0]) == 1:
                            if tianpanchaifenliebiao[1] == "甲子戊":
                                jiaziwudingwei_index = i  # 甲子戊所在宫号
                        elif len(tianpanchaifenliebiao[1]) == 1:
                            if tianpanchaifenliebiao[0] == "甲子戊":
                                jiaziwudingwei_index = i  # 甲子戊所在宫号
                        else:
                            if tianpanchaifenliebiao[0] == "甲子戊" or tianpanchaifenliebiao[1] == "甲子戊":
                                jiaziwudingwei_index = i  # 甲子戊所在宫号

            # 干支
            nianganzhi = yinyangdun_ganzhi[1]
            yueganzhi = yinyangdun_ganzhi[2]
            riganzhi = yinyangdun_ganzhi[3]
            shichengganzhi = yinyangdun_ganzhi[4]
            # 年干宫号
            for i in range(0, 9):
                if i == 4:
                    pass
                else:
                    tianpanpanbieniangan = ninegridsbasicmessage[i]["天盘"]
                    if nianganzhi[0] == "甲":
                        if len(tianpanpanbieniangan) == 1:
                            pass
                        elif len(tianpanpanbieniangan) == 3:
                            if nianganzhi == tianpanpanbieniangan[0:2]:
                                niangandingwei_index = i
                        else:
                            tianpanpanbienianganliebiao = tianpanpanbieniangan.split("\n")
                            if len(tianpanpanbienianganliebiao[0]) == 1:
                                if nianganzhi == tianpanpanbienianganliebiao[1][0:2]:
                                    niangandingwei_index = i
                            elif len(tianpanpanbienianganliebiao[1]) == 1:
                                if nianganzhi == tianpanpanbienianganliebiao[0][0:2]:
                                    niangandingwei_index = i
                            else:
                                if nianganzhi == tianpanpanbienianganliebiao[0][0:2] or nianganzhi == \
                                        tianpanpanbienianganliebiao[1][0:2]:
                                    niangandingwei_index = i
                    else:
                        if len(tianpanpanbieniangan) == 1:
                            if nianganzhi[0] == tianpanpanbieniangan:
                                niangandingwei_index = i
                        elif len(tianpanpanbieniangan) == 3:
                            if nianganzhi[0] == tianpanpanbieniangan[-1]:
                                niangandingwei_index = i
                        else:
                            tianpanpanbienianganliebiao = tianpanpanbieniangan.split("\n")
                            if nianganzhi[0] == tianpanpanbienianganliebiao[0][-1] or nianganzhi[0] == \
                                    tianpanpanbienianganliebiao[1][-1]:
                                niangandingwei_index = i
            # 月干宫号
            for i in range(0, 9):
                if i == 4:
                    pass
                else:
                    tianpanpanbieyuegan = ninegridsbasicmessage[i]["天盘"]
                    if yueganzhi[0] == "甲":
                        if len(tianpanpanbieyuegan) == 1:
                            pass
                        elif len(tianpanpanbieyuegan) == 3:
                            if yueganzhi == tianpanpanbieyuegan[0:2]:
                                yuegandingwei_index = i
                        else:
                            tianpanpanbieyueganliebiao = tianpanpanbieyuegan.split("\n")
                            if len(tianpanpanbieyueganliebiao[0]) == 1:
                                if yueganzhi == tianpanpanbieyueganliebiao[1][0:2]:
                                    yuegandingwei_index = i
                            elif len(tianpanpanbieyueganliebiao[1]) == 1:
                                if yueganzhi == tianpanpanbieyueganliebiao[0][0:2]:
                                    yuegandingwei_index = i
                            else:
                                if yueganzhi == tianpanpanbieyueganliebiao[0][0:2] or yueganzhi == \
                                        tianpanpanbieyueganliebiao[
                                            1][0:2]:
                                    yuegandingwei_index = i
                    else:
                        if len(tianpanpanbieyuegan) == 1:
                            if yueganzhi[0] == tianpanpanbieyuegan:
                                yuegandingwei_index = i
                        elif len(tianpanpanbieyuegan) == 3:
                            if yueganzhi[0] == tianpanpanbieyuegan[-1]:
                                yuegandingwei_index = i
                        else:
                            tianpanpanbieyueganliebiao = tianpanpanbieyuegan.split("\n")
                            if yueganzhi[0] == tianpanpanbieyueganliebiao[0][-1] or yueganzhi[0] == \
                                    tianpanpanbieyueganliebiao[1][-1]:
                                yuegandingwei_index = i

            # 日干宫号
            for i in range(0, 9):
                if i == 4:
                    pass
                else:
                    tianpanpanbierigan = ninegridsbasicmessage[i]["天盘"]
                    if riganzhi[0] == "甲":
                        if len(tianpanpanbierigan) == 1:
                            pass
                        elif len(tianpanpanbierigan) == 3:
                            if riganzhi == tianpanpanbierigan[0:2]:
                                rigandingwei_index = i
                        else:
                            tianpanpanbieriganliebiao = tianpanpanbierigan.split("\n")
                            if len(tianpanpanbieriganliebiao[0]) == 1:
                                if riganzhi == tianpanpanbieriganliebiao[1][0:2]:
                                    rigandingwei_index = i
                            elif len(tianpanpanbieriganliebiao[1]) == 1:
                                if riganzhi == tianpanpanbieriganliebiao[0][0:2]:
                                    rigandingwei_index = i
                            else:
                                if riganzhi == tianpanpanbieriganliebiao[0][0:2] or riganzhi == \
                                        tianpanpanbieriganliebiao[
                                            1][
                                        0:2]:
                                    rigandingwei_index = i
                    else:
                        if len(tianpanpanbierigan) == 1:
                            if riganzhi[0] == tianpanpanbierigan:
                                rigandingwei_index = i
                        elif len(tianpanpanbierigan) == 3:
                            if riganzhi[0] == tianpanpanbierigan[-1]:
                                rigandingwei_index = i
                        else:
                            tianpanpanbieriganliebiao = tianpanpanbierigan.split("\n")
                            if riganzhi[0] == tianpanpanbieriganliebiao[0][-1] or riganzhi[0] == \
                                    tianpanpanbieriganliebiao[1][
                                        -1]:
                                rigandingwei_index = i
            # 时干宫号
            for i in range(0, 9):
                if i == 4:
                    pass
                else:
                    tianpanpanbieshichenggan = ninegridsbasicmessage[i]["天盘"]
                    if shichengganzhi[0] == "甲":
                        if len(tianpanpanbieshichenggan) == 1:
                            pass
                        elif len(tianpanpanbieshichenggan) == 3:
                            if shichengganzhi == tianpanpanbieshichenggan[0:2]:
                                shichenggandingwei_index = i
                        else:
                            tianpanpanbieshichengganliebiao = tianpanpanbieshichenggan.split("\n")
                            if len(tianpanpanbieshichengganliebiao[0]) == 1:
                                if shichengganzhi == tianpanpanbieshichengganliebiao[1][0:2]:
                                    shichenggandingwei_index = i
                            elif len(tianpanpanbieshichengganliebiao[1]) == 1:
                                if shichengganzhi == tianpanpanbieshichengganliebiao[0][0:2]:
                                    shichenggandingwei_index = i
                            else:
                                if shichengganzhi == tianpanpanbieshichengganliebiao[0][0:2] or shichengganzhi == \
                                        tianpanpanbieshichengganliebiao[1][0:2]:
                                    shichenggandingwei_index = i
                    else:
                        if len(tianpanpanbieshichenggan) == 1:
                            if shichengganzhi[0] == tianpanpanbieshichenggan:
                                shichenggandingwei_index = i
                        elif len(tianpanpanbieshichenggan) == 3:
                            if shichengganzhi[0] == tianpanpanbieshichenggan[-1]:
                                shichenggandingwei_index = i
                        else:
                            tianpanpanbieshichengganliebiao = tianpanpanbieshichenggan.split("\n")
                            if shichengganzhi[0] == tianpanpanbieshichengganliebiao[0][-1] or shichengganzhi[0] == \
                                    tianpanpanbieshichengganliebiao[1][-1]:
                                shichenggandingwei_index = i
            tongbianbayaosu = [zhifugongdingwei_index, zhishigongdingwei_index, niangandingwei_index,
                               yuegandingwei_index,
                               rigandingwei_index, shichenggandingwei_index, shengmendingwei_index,
                               jiaziwudingwei_index]
            # 六十甲子+空亡
            list1jiazi = ["甲子", "乙丑", "丙寅", "丁卯", "戊辰", "己巳", "庚午", "辛未", "壬申",
                          "癸酉", "戌亥"]
            list2jiaxu = ["甲戌", "乙亥", "丙子", "丁丑", "戊寅", "己卯", "庚辰", "辛巳", "壬午",
                          "癸未", "申酉"]
            list3jiashen = ["甲申", "乙酉", "丙戌", "丁亥", "戊子", "己丑", "庚寅", "辛卯", "壬辰",
                            "癸巳", "午未"]
            list4jiawu = ["甲午", "乙未", "丙申", "丁酉", "戊戌", "己亥", "庚子", "辛丑", "壬寅",
                          "癸卯", "辰巳"]
            list5jiachen = ["甲辰", "乙巳", "丙午", "丁未", "戊申", "己酉", "庚戌", "辛亥", "壬子",
                            "癸丑", "寅卯"]
            list6jiayin = ["甲寅", "乙卯", "丙辰", "丁巳", "戊午", "己未", "庚申", "辛酉", "壬戌",
                           "癸亥", "子丑"]
            listliushijiazi = [list1jiazi, list2jiaxu, list3jiashen, list4jiawu, list5jiachen, list6jiayin]
            gongshengxiaoduiying = {0: "子", 1: "未申", 2: "卯", 3: "辰巳", 5: "亥戌", 6: "酉", 7: "丑寅", 8: "午"}
            # 日干空
            for i in listliushijiazi:
                for j in i:
                    if riganzhi == j:
                        rikongzifuchuang = i[-1]
                        fshibierigan = i
                        break
                    else:
                        pass
            # 时干空
            for i in listliushijiazi:
                for j in i:
                    if shichengganzhi == j:
                        shikongzifuchuang = i[-1]
                        fshibieshigan = i
                        break
                    else:
                        pass
            kongwanglist = []
            for i in rikongzifuchuang:
                kongwanglist.append(i)
            for i in shikongzifuchuang:
                kongwanglist.append(i)
            if BIAN == 0:
                Panbietongbianlist = zuocegonghao
            elif BIAN == 1:
                Panbietongbianlist = youcegonghao
            tongbianjici = 0
            TONGBIANKONGWANGSHU = 0
            for i in range(0, 8):
                if tongbianbayaosu[i] in Panbietongbianlist:
                    tongbianshengxiaodizhi = gongshengxiaoduiying[tongbianbayaosu[i]]
                    for j in kongwanglist:
                        if j in tongbianshengxiaodizhi:
                            TONGBIANKONGWANGSHU = TONGBIANKONGWANGSHU + 1
                        else:
                            pass
                    tongbianjici = tongbianjici + 1
            zhishigongshengxiaodizhi = gongshengxiaoduiying[zhishigongdingwei_index]
            KONGWANGSHU = 0
            for i in kongwanglist:
                if i in zhishigongshengxiaodizhi:
                    KONGWANGSHU = KONGWANGSHU + 1
                else:
                    pass
            zhishigongtianpan = ninegridsbasicmessage[zhishigongdingwei_index]["天盘"]
            # 1.4驿马落用神宫
            Yimadist = {"申子辰": "寅", "亥卯未": "巳", "寅午戌": "申", "巳酉丑": "亥"}
            for key in Yimadist:
                if shichengganzhi[1] in key:
                    yima = Yimadist[key]
                    break
                else:
                    pass
            for key in gongshengxiaoduiying:
                if yima in gongshengxiaoduiying[key]:
                    yimagonghao = key
            chongyongshenggonglist = {7: 1, 3: 5, 1: 7, 5: 3}
            if yimagonghao == zhishigongdingwei_index:
                SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + yimaluoyongshengong
                print(f"驿马落用神宫--->{yimaluoyongshengong}")
            elif yimagonghao != zhishigongdingwei_index:
                if zhishigongdingwei_index == 7 or zhishigongdingwei_index == 3 or zhishigongdingwei_index == 1 or zhishigongdingwei_index == 5:
                    if yimagonghao == chongyongshenggonglist[zhishigongdingwei_index]:
                        SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + yimachongyongshengong
                        if yimachongyongshengong >= 0:
                            yimachongyongshengong = f"+{yimachongyongshengong}"

                        print(f"驿马冲用神宫--->{yimachongyongshengong}")
                    else:
                        print("驿马没有落在用神宫或冲用神宫")
                else:
                    print("驿马没有落在用神宫或冲用神宫")
            yimaSDX = SpaDigiX_APPONE_Value - neiwaidunSDX
            # 同边要素规则
            ccccc = SpaDigiX_APPONE_Value
            tonggongjici = 0
            tonggongbayaosudingwei = [zhishigongdingwei_index, zhifugongdingwei_index, shengmendingwei_index,
                                      shichenggandingwei_index, rigandingwei_index, yuegandingwei_index,
                                      niangandingwei_index,
                                      jiaziwudingwei_index]
            for i in range(0, 8):
                if tonggongbayaosudingwei[i] == zhishigongdingwei_index:
                    tonggongjici = tonggongjici + 1
            if tongbianjici == 1:
                SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + yitong
            elif tongbianjici == 2:
                SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + ertong
            elif tongbianjici == 4:
                if tonggongjici == 4:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + sitongqietonggong
            elif tongbianjici == 5:
                if tonggongjici == 5:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + wutongqietonggong
            elif tongbianjici == 6:
                SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + liutong
            elif tongbianjici == 7:
                SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + qitong
            elif tongbianjici == 8:
                SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + batong
            print(f"同边要素：{SpaDigiX_APPONE_Value - ccccc}")
            tongbianyaosuSDX = SpaDigiX_APPONE_Value - (yimaSDX + neiwaidunSDX)

            # -----------------------------------------------------------------------------------------------------------------------
            # 1.5用神宫空亡
            # -----------------------------------------------------------------------------------------------------------------------
            if KONGWANGSHU == 1:
                SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + yongshengongdankong
                print(f"用神宫单空--->{yongshengongdankong}")
            elif KONGWANGSHU == 2:
                SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + yongshengongshuangkong
                print(f"用神宫双空--->{yongshengongshuangkong}")
            elif KONGWANGSHU == 4:
                SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + yongshengongsikong
                print(f"用神宫四空--->{yongshengongsikong}")
            else:
                print("用神宫没有空亡情况")
            kongwangSDX = SpaDigiX_APPONE_Value - (tongbianyaosuSDX + yimaSDX + neiwaidunSDX)
            # 支冲
            zhichongchushi = SpaDigiX_APPONE_Value
            zhishigongtianpanshuju = ninegridsbasicmessage[zhishigongdingwei_index]["天盘"]
            zhishigongdipanshuju = ninegridsbasicmessage[zhishigongdingwei_index]["地盘"]
            zhichongonelist = ["甲子戊", "甲午辛"]
            zhichongtwolist = ["甲寅癸", "甲申庚"]
            zhichongthreelist = ["甲辰壬", "甲戌己"]
            if len(zhishigongtianpanshuju) == 3 and len(zhishigongdipanshuju) == 3:
                if zhishigongtianpanshuju == zhishigongdipanshuju:
                    ccccccc = 0
                elif zhishigongtianpanshuju in zhichongonelist and zhishigongdipanshuju in zhichongonelist:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + zhichongone
                elif zhishigongtianpanshuju in zhichongtwolist and zhishigongdipanshuju in zhichongtwolist:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + zhichongone
                elif zhishigongtianpanshuju in zhichongthreelist and zhishigongdipanshuju in zhichongthreelist:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + zhichongone
            elif len(zhishigongtianpanshuju) > 3 and len(zhishigongdipanshuju) == 3:
                zhishigongtianpanshujulist = zhishigongtianpanshuju.split("\n")
                if (zhishigongtianpanshujulist[0] in zhichongonelist or zhishigongtianpanshujulist[
                    1] in zhichongonelist) and zhishigongdipanshuju in zhichongonelist:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + zhichongone
                elif (zhishigongtianpanshujulist[0] in zhichongtwolist or zhishigongtianpanshujulist[
                    1] in zhichongtwolist) and zhishigongdipanshuju in zhichongtwolist:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + zhichongone
                elif (zhishigongtianpanshujulist[0] in zhichongthreelist or zhishigongtianpanshujulist[
                    1] in zhichongthreelist) and zhishigongdipanshuju in zhichongthreelist:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + zhichongone
                if zhishigongtianpanshujulist[0] in zhichongonelist and zhishigongtianpanshujulist[
                    1] in zhichongonelist:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + zhichongone
                elif zhishigongtianpanshujulist[0] in zhichongtwolist and zhishigongtianpanshujulist[
                    1] in zhichongtwolist:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + zhichongone
                elif zhishigongtianpanshujulist[0] in zhichongthreelist and zhishigongtianpanshujulist[
                    1] in zhichongthreelist:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + zhichongone
            elif len(zhishigongtianpanshuju) == 3 and len(zhishigongdipanshuju) > 3:
                zhishigongdipanshujulist = zhishigongdipanshuju.split("\n")
                if zhishigongtianpanshuju in zhichongonelist and (
                        zhishigongdipanshujulist[0] in zhichongonelist or zhishigongdipanshujulist[
                    1] in zhichongonelist):
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + zhichongone
                elif zhishigongtianpanshuju in zhichongtwolist and (
                        zhishigongdipanshujulist[0] in zhichongtwolist or zhishigongdipanshujulist[
                    1] in zhichongtwolist):
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + zhichongone
                elif zhishigongtianpanshuju in zhichongthreelist and (
                        zhishigongdipanshujulist[0] in zhichongthreelist or zhishigongdipanshujulist[
                    1] in zhichongthreelist):
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + zhichongone
                if zhishigongdipanshujulist[0] in zhichongonelist and zhishigongdipanshujulist[1] in zhichongonelist:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + zhichongone
                elif zhishigongdipanshujulist[0] in zhichongtwolist and zhishigongdipanshujulist[1] in zhichongtwolist:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + zhichongone
                elif zhishigongdipanshujulist[0] in zhichongthreelist and zhishigongdipanshujulist[
                    1] in zhichongthreelist:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + zhichongone
            elif len(zhishigongtianpanshuju) > 3 and len(zhishigongdipanshuju) > 3:
                zhishigongtianpanshujulist = zhishigongtianpanshuju.split("\n")
                zhishigongdipanshujulist = zhishigongdipanshuju.split("\n")
                if zhishigongtianpanshuju == zhishigongdipanshuju:
                    if zhishigongdipanshujulist[0] in zhichongonelist and zhishigongdipanshujulist[
                        1] in zhichongonelist:
                        SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + zhichongone
                    elif zhishigongdipanshujulist[0] in zhichongtwolist and zhishigongdipanshujulist[
                        1] in zhichongtwolist:
                        SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + zhichongone
                    elif zhishigongdipanshujulist[0] in zhichongthreelist and zhishigongdipanshujulist[
                        1] in zhichongthreelist:
                        SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + zhichongone
                    if zhishigongtianpanshujulist[0] in zhichongonelist and zhishigongtianpanshujulist[
                        1] in zhichongonelist:
                        SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + zhichongone
                    elif zhishigongtianpanshujulist[0] in zhichongtwolist and zhishigongtianpanshujulist[
                        1] in zhichongtwolist:
                        SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + zhichongone
                    elif zhishigongtianpanshujulist[0] in zhichongthreelist and zhishigongtianpanshujulist[
                        1] in zhichongthreelist:
                        SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + zhichongone
                if (zhishigongtianpanshujulist[0] in zhichongonelist or zhishigongtianpanshujulist[
                    1] in zhichongonelist) and (
                        zhishigongdipanshujulist[0] in zhichongonelist or zhishigongdipanshujulist[
                    1] in zhichongonelist):
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + zhichongone
                if (zhishigongtianpanshujulist[0] in zhichongtwolist or zhishigongtianpanshujulist[
                    1] in zhichongtwolist) and (
                        zhishigongdipanshujulist[0] in zhichongtwolist or zhishigongdipanshujulist[
                    1] in zhichongtwolist):
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + zhichongone
                if (zhishigongtianpanshujulist[0] in zhichongthreelist or zhishigongtianpanshujulist[
                    1] in zhichongthreelist) and (
                        zhishigongdipanshujulist[0] in zhichongtwolist or zhishigongdipanshujulist[
                    1] in zhichongthreelist):
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + zhichongone
                if zhishigongdipanshujulist[0] in zhichongonelist and zhishigongdipanshujulist[1] in zhichongonelist:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + zhichongone
                elif zhishigongdipanshujulist[0] in zhichongtwolist and zhishigongdipanshujulist[1] in zhichongtwolist:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + zhichongone
                elif zhishigongdipanshujulist[0] in zhichongthreelist and zhishigongdipanshujulist[
                    1] in zhichongthreelist:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + zhichongone
                if zhishigongtianpanshujulist[0] in zhichongonelist and zhishigongtianpanshujulist[
                    1] in zhichongonelist:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + zhichongone
                elif zhishigongtianpanshujulist[0] in zhichongtwolist and zhishigongtianpanshujulist[
                    1] in zhichongtwolist:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + zhichongone
                elif zhishigongtianpanshujulist[0] in zhichongthreelist and zhishigongtianpanshujulist[
                    1] in zhichongthreelist:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + zhichongone
            elif len(zhishigongtianpanshuju) == 1 and len(zhishigongdipanshuju) > 3:
                zhishigongdipanshujulist = zhishigongdipanshuju.split("\n")
                if zhishigongdipanshujulist[0] in zhichongonelist and zhishigongdipanshujulist[1] in zhichongonelist:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + zhichongone
                elif zhishigongdipanshujulist[0] in zhichongtwolist and zhishigongdipanshujulist[1] in zhichongtwolist:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + zhichongone
                elif zhishigongdipanshujulist[0] in zhichongthreelist and zhishigongdipanshujulist[
                    1] in zhichongthreelist:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + zhichongone
            elif len(zhishigongtianpanshuju) > 3 and len(zhishigongdipanshuju) == 1:
                zhishigongtianpanshujulist = zhishigongtianpanshuju.split("\n")
                if zhishigongtianpanshujulist[0] in zhichongonelist and zhishigongtianpanshujulist[
                    1] in zhichongonelist:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + zhichongone
                elif zhishigongtianpanshujulist[0] in zhichongtwolist and zhishigongtianpanshujulist[
                    1] in zhichongtwolist:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + zhichongone
                elif zhishigongtianpanshujulist[0] in zhichongthreelist and zhishigongtianpanshujulist[
                    1] in zhichongthreelist:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + zhichongone
            zhichongzuizhong = SpaDigiX_APPONE_Value - zhichongchushi
            if zhichongzuizhong > 2:
                chaochuxiuzheng = zhichongzuizhong - 2
                zhichongzuizhong = 2
                SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value - chaochuxiuzheng

            print(f"支冲：{zhichongzuizhong}")
            zhichongSDX = SpaDigiX_APPONE_Value - (kongwangSDX + tongbianyaosuSDX + yimaSDX + neiwaidunSDX)
            # -----------------------------------------------------------------------------------------------------------------------
            quanpanchupanjieguo = SpaDigiX_APPONE_Value
            jixionggejishuchushi = SpaDigiX_APPONE_Value
            # -----------------------------------------------------------------------------------------------------------------------
            # 2 单宫部分（以值使做用神为例）
            print(
                "----------------------------------------------------------------------------------------------------------")

            def getjixiongge(SpaDigiX_APPONE_Value, zhishigongtianpan, zhishigongdipan):
                zhishigongshuju = ninegridsbasicmessage[zhishigongdingwei_index]  # 读取值使所在宫的数据
                # -----------------------------------------------------------------------------------------------------------------------
                # 2.1 吉格

                # -----------------------------------------------------------------------------------------------------------------------
                # 戊＋丙
                zhishigongtianpan = zhishigongtianpan
                zhishigongtianpanjishu = 0
                zhishigongdipan = zhishigongdipan
                zhishigongdipanjishu = 0
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲子戊" or zhishigongtianpanlist[1] == "甲子戊":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲子戊":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "丙" or zhishigongdipanlist[1] == "丙":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 1:
                    if zhishigongdipan == "丙":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + wubing
                # 丙＋戊
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲子戊" or zhishigongdipanlist[1] == "甲子戊":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲子戊":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0

                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "丙" or zhishigongtianpanlist[1] == "丙":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 1:
                    if zhishigongtianpan == "丙":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0

                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + bingwu
                zhishigongbamen = zhishigongshuju["八门"]
                zhishigongbamenjishu = 0
                zhishigongbashen = zhishigongshuju["八神"]
                zhishigongbashenjishu = 0
                zhishigonggonghaojishu = 0

                # -----------------------------------------------------------------------------------------------------------------------
                # -----------------------------------------------------------------------------------------------------------------------
                # 三奇得使
                # 丁+甲辰壬
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "丁" or zhishigongtianpanlist[1] == "丁":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 1:
                    if zhishigongtianpan == "丁":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0

                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲辰壬" or zhishigongdipanlist[1] == "甲辰壬":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲辰壬":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0

                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + dingjiachen
                # 2.4 三诈
                # 乙、丙、丁（开门）十神盘（太阴）
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "丁" or zhishigongtianpanlist[1] == "丁" or zhishigongtianpanlist[
                        0] == "丙" or \
                            zhishigongtianpanlist[1] == "丙" or zhishigongtianpanlist[0] == "乙" or \
                            zhishigongtianpanlist[
                                1] == "乙":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 1:
                    if zhishigongtianpan == "丁" or zhishigongtianpan == "丙" or zhishigongtianpan == "乙":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0
                if zhishigongbamen == "开使":
                    zhishigongbamenjishu = 1
                else:
                    zhishigongbamenjishu = 0
                if zhishigongbashen == "太阴":
                    zhishigongbashenjishu = 1
                else:
                    zhishigongbashenjishu = 0

                if zhishigongtianpanjishu == 1 and zhishigongbamenjishu == 1 and zhishigongbashenjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + yiorbingording_kai_taiyin
                # 乙、丙、丁（休门）十神盘（九地）
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "丁" or zhishigongtianpanlist[1] == "丁" or zhishigongtianpanlist[
                        0] == "丙" or \
                            zhishigongtianpanlist[1] == "丙" or zhishigongtianpanlist[0] == "乙" or \
                            zhishigongtianpanlist[
                                1] == "乙":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 1:
                    if zhishigongtianpan == "丁" or zhishigongtianpan == "丙" or zhishigongtianpan == "乙":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0

                if zhishigongbamen == "休使":
                    zhishigongbamenjishu = 1
                else:
                    zhishigongbamenjishu = 0
                if zhishigongbashen == "九地":
                    zhishigongbashenjishu = 1
                else:
                    zhishigongbashenjishu = 0

                if zhishigongtianpanjishu == 1 and zhishigongbamenjishu == 1 and zhishigongbashenjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + yiorbingording_xiu_jiudi
                # 乙、丙、丁（生门）十神盘（六合）
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "丁" or zhishigongtianpanlist[1] == "丁" or zhishigongtianpanlist[
                        0] == "丙" or \
                            zhishigongtianpanlist[1] == "丙" or zhishigongtianpanlist[0] == "乙" or \
                            zhishigongtianpanlist[
                                1] == "乙":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 1:
                    if zhishigongtianpan == "丁" or zhishigongtianpan == "丙" or zhishigongtianpan == "乙":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0
                if zhishigongbamen == "生使":
                    zhishigongbamenjishu = 1
                else:
                    zhishigongbamenjishu = 0
                if zhishigongbashen == "六合":
                    zhishigongbashenjishu = 1
                else:
                    zhishigongbashenjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongbamenjishu == 1 and zhishigongbashenjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + yiorbingording_sheng_liuhe
                # 2.8 交泰格、天运格。-1
                # 丁十丙
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "丁" or zhishigongtianpanlist[1] == "丁":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                elif len(zhishigongtianpan) == 1:
                    if zhishigongtianpan == "丁":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                else:
                    zhishigongtianpanjishu1 = 0

                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "丙" or zhishigongdipanlist[1] == "丙":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 1:
                    if zhishigongdipan == "丙":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0

                if zhishigongtianpanjishu1 == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + dingbing
                # 丁十乙
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "丁" or zhishigongtianpanlist[1] == "丁":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                elif len(zhishigongtianpan) == 1:
                    if zhishigongtianpan == "丁":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                else:
                    zhishigongtianpanjishu1 = 0

                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "乙" or zhishigongdipanlist[1] == "乙":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 1:
                    if zhishigongdipan == "乙":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0

                if zhishigongtianpanjishu1 == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + dingyi
                '''
                #六甲值符十乙、丙、丁
                if len(zhishigongtianpan)>3:
                    zhishigongtianpanlist=zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0]=="甲子戊" or zhishigongtianpanlist[1]=="甲子戊":
                        zhishigongtianpanjishu=1
                    else:
                        zhishigongtianpanjishu=0
                elif len(zhishigongtianpan)==3:
                    if zhishigongtianpan=="甲子戊":
                        zhishigongtianpanjishu=1
                    else:
                        zhishigongtianpanjishu=0
                else:
                    zhishigongtianpanjishu=0
                if len(zhishigongdipan)>3:
                    zhishigongdipanlist=zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0]=="乙" or zhishigongdipanlist[1]=="乙"  or zhishigongdipanlist[0]=="丁" or zhishigongdipanlist[1]=="丁":
                        zhishigongdipanjishu=1
                    else:
                        zhishigongdipanjishu=0
                elif len(zhishigongdipan)==1:
                    if zhishigongdipan=="乙" or zhishigongdipan=="丁":
                        zhishigongdipanjishu=1
                    else:
                        zhishigongdipanjishu=0
                else:
                    zhishigongdipanjishu=0
                if zhishigongtianpanjishu==1 and zhishigongdipanjishu==1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + jiaziwuyiording
                '''
                # 2.10 凶格
                # 庚十丙+3
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲申庚" or zhishigongtianpanlist[1] == "甲申庚":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲申庚":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0

                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "丙" or zhishigongdipanlist[1] == "丙":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 1:
                    if zhishigongdipan == "丙":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    agengbing = 1
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + gengbing
                else:
                    agengbing = 0
                # 丙十庚+3
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "丙" or zhishigongtianpanlist[1] == "丙":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                elif len(zhishigongtianpan) == 1:
                    if zhishigongtianpan == "丙":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                else:
                    zhishigongtianpanjishu1 = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲申庚" or zhishigongdipanlist[1] == "甲申庚":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲申庚":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu1 == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + binggeng
                # 辛十乙
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲午辛" or zhishigongtianpanlist[1] == "甲午辛":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲午辛":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0

                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "乙" or zhishigongdipanlist[1] == "乙":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 1:
                    if zhishigongdipan == "乙":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + xinyi

                # 丁十癸
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "丁" or zhishigongtianpanlist[1] == "丁":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                elif len(zhishigongtianpan) == 1:
                    if zhishigongtianpan == "丁":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                else:
                    zhishigongtianpanjishu1 = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲寅癸" or zhishigongdipanlist[1] == "甲寅癸":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲寅癸":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu1 == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + dinggui

                # 六甲值符十庚 改为甲子戊+庚
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲子戊" or zhishigongtianpanlist[1] == "甲子戊":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲子戊":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0

                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲申庚" or zhishigongdipanlist[1] == "甲申庚":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲申庚":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0

                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + jiaziwugeng

                # 2.11 其他凶格
                # 刑格 庚+己
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲申庚" or zhishigongtianpanlist[1] == "甲申庚":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲申庚":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0

                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲戌己" or zhishigongdipanlist[1] == "甲戌己":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲戌己":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0

                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    xingge = 1
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + gengji
                else:
                    xingge = 0

                # 大格 庚+癸
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲申庚" or zhishigongtianpanlist[1] == "甲申庚":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲申庚":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0

                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲寅癸" or zhishigongdipanlist[1] == "甲寅癸":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲寅癸":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0

                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    dage = 1
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + genggui
                else:
                    dage = 0

                # 小格 庚+壬
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲申庚" or zhishigongtianpanlist[1] == "甲申庚":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲申庚":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0

                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲辰壬" or zhishigongdipanlist[1] == "甲辰壬":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲辰壬":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0

                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    xiaoge = 1
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + gengren
                else:
                    xiaoge = 0

                # 岁格 庚 +年干
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲申庚" or zhishigongtianpanlist[1] == "甲申庚":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲申庚":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0

                niangan = nianganzhi[0]
                zhishigongdipangan1 = zhishigongdipan
                zhishigongdipangan2 = zhishigongdipan
                if len(zhishigongdipan) == 1:
                    if niangan == zhishigongdipan:
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲子戊":
                        if zhishigongbashen == "值符":
                            zhishigongdipangan = "甲"
                        else:
                            zhishigongdipangan = "戊"
                    else:
                        zhishigongdipangan = zhishigongdipan[-1]
                    if zhishigongdipangan == niangan:
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if len(zhishigongdipanlist[0]) == 1:
                        zhishigongdipangan1 == zhishigongdipanlist[0]
                    elif len(zhishigongdipanlist[0]) == 3:
                        if zhishigongdipanlist[0] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongdipangan1 = "甲"
                            else:
                                zhishigongdipangan1 = "戊"
                        else:
                            zhishigongdipangan1 = zhishigongdipanlist[-1]
                    if len(zhishigongdipanlist[1]) == 1:
                        zhishigongdipangan2 == zhishigongdipanlist[1]
                    elif len(zhishigongdipanlist[1]) == 3:
                        if zhishigongdipanlist[1] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongdipangan2 = "甲"
                            else:
                                zhishigongdipangan2 = "戊"
                        else:
                            zhishigongdipangan2 = zhishigongdipanlist[-1]
                    if zhishigongdipangan1 == niangan or zhishigongdipangan2 == niangan:
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0

                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    suige = 1
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + gengniangan
                else:
                    suige = 0
                #  月格 庚+月干
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲申庚" or zhishigongtianpanlist[1] == "甲申庚":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲申庚":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0

                yuegan = yueganzhi[0]
                zhishigongdipangan1 = zhishigongdipan
                zhishigongdipangan2 = zhishigongdipan
                if len(zhishigongdipan) == 1:
                    if yuegan == zhishigongdipan:
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲子戊":
                        if zhishigongbashen == "值符":
                            zhishigongdipangan = "戊"
                        else:
                            zhishigongdipangan = "戊"
                    else:
                        zhishigongdipangan = zhishigongdipan[-1]
                    if zhishigongdipangan == yuegan:
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if len(zhishigongdipanlist[0]) == 1:
                        zhishigongdipangan1 == zhishigongdipanlist[0]
                    elif len(zhishigongdipanlist[0]) == 3:
                        if zhishigongdipanlist[0] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongdipangan1 = "戊"
                            else:
                                zhishigongdipangan1 = "戊"
                        else:
                            zhishigongdipangan1 = zhishigongdipanlist[-1]
                    if len(zhishigongdipanlist[1]) == 1:
                        zhishigongdipangan2 == zhishigongdipanlist[1]
                    elif len(zhishigongdipanlist[1]) == 3:
                        if zhishigongdipanlist[1] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongdipangan2 = "戊"
                            else:
                                zhishigongdipangan2 = "戊"
                        else:
                            zhishigongdipangan2 = zhishigongdipanlist[-1]
                    if zhishigongdipangan1 == yuegan or zhishigongdipangan2 == yuegan:
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0

                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    yuege = 1
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + gengyuegan
                else:
                    yuege = 0
                # 日格 庚+日干
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲申庚" or zhishigongtianpanlist[1] == "甲申庚":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲申庚":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0

                rigan = riganzhi[0]
                zhishigongdipangan1 = zhishigongdipan
                zhishigongdipangan2 = zhishigongdipan
                if len(zhishigongdipan) == 1:
                    if rigan == zhishigongdipan:
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲子戊":
                        if zhishigongbashen == "值符":
                            zhishigongdipangan = "戊"
                        else:
                            zhishigongdipangan = "戊"
                    else:
                        zhishigongdipangan = zhishigongdipan[-1]
                    if zhishigongdipangan == rigan:
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if len(zhishigongdipanlist[0]) == 1:
                        zhishigongdipangan1 == zhishigongdipanlist[0]
                    elif len(zhishigongdipanlist[0]) == 3:
                        if zhishigongdipanlist[0] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongdipangan1 = "戊"
                            else:
                                zhishigongdipangan1 = "戊"
                        else:
                            zhishigongdipangan1 = zhishigongdipanlist[-1]
                    if len(zhishigongdipanlist[1]) == 1:
                        zhishigongdipangan2 == zhishigongdipanlist[1]
                    elif len(zhishigongdipanlist[1]) == 3:
                        if zhishigongdipanlist[1] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongdipangan2 = "戊"
                            else:
                                zhishigongdipangan2 = "戊"
                        else:
                            zhishigongdipangan2 = zhishigongdipanlist[-1]
                    if zhishigongdipangan1 == rigan or zhishigongdipangan2 == rigan:
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0

                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    rige = 1
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + gengrigan
                else:
                    rige = 0
                # 时格 庚+时干
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲申庚" or zhishigongtianpanlist[1] == "甲申庚":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲申庚":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0

                shichenggan = shichengganzhi[0]
                zhishigongdipangan1 = zhishigongdipan
                zhishigongdipangan2 = zhishigongdipan
                if len(zhishigongdipan) == 1:
                    if shichenggan == zhishigongdipan:
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲子戊":
                        if zhishigongbashen == "值符":
                            zhishigongdipangan = "戊"
                        else:
                            zhishigongdipangan = "戊"
                    else:
                        zhishigongdipangan = zhishigongdipan[-1]
                    if zhishigongdipangan == shichenggan:
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if len(zhishigongdipanlist[0]) == 1:
                        zhishigongdipangan1 == zhishigongdipanlist[0]
                    elif len(zhishigongdipanlist[0]) == 3:
                        if zhishigongdipanlist[0] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongdipangan1 = "戊"
                            else:
                                zhishigongdipangan1 = "戊"
                        else:
                            zhishigongdipangan1 = zhishigongdipanlist[-1]
                    if len(zhishigongdipanlist[1]) == 1:
                        zhishigongdipangan2 == zhishigongdipanlist[1]
                    elif len(zhishigongdipanlist[1]) == 3:
                        if zhishigongdipanlist[1] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongdipangan2 = "戊"
                            else:
                                zhishigongdipangan2 = "戊"
                        else:
                            zhishigongdipangan2 = zhishigongdipanlist[-1]
                    if zhishigongdipangan1 == shichenggan or zhishigongdipangan2 == shichenggan:
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0

                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    shige = 1
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + gengshigan
                else:
                    shige = 0
                gegegege = [suige, yuege, rige, shige]
                gegegegejishu = 0
                gegegan = ["丙", "己", "癸", "壬"]
                for i in range(0, 4):
                    if gegegege[i] == 1:
                        gegegegejishu = gegegegejishu + 1
                if (agengbing == 1 or xingge == 1 or dage == 1 or xiaoge == 1) and (
                        niangan in gegegan or yuegan in gegegan or rigan in gegegan or shichenggan in gegegan):
                    if gegegegejishu > 1:
                        SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value - 2 * (gegegegejishu - 1)
                # 飞干格 日干+庚
                rigan = riganzhi[0]
                zhishigongtianpangan1 = zhishigongtianpan
                zhishigongtianpangan2 = zhishigongtianpan
                if len(zhishigongtianpan) == 1:
                    if rigan == zhishigongtianpan:
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲子戊":
                        if zhishigongbashen == "值符":
                            zhishigongtianpangan = "戊"
                        else:
                            zhishigongtianpangan = "戊"
                    else:
                        zhishigongtianpangan = zhishigongtianpan[-1]
                    if zhishigongtianpangan == rigan:
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if len(zhishigongtianpanlist[0]) == 1:
                        zhishigongtianpangan1 == zhishigongtianpanlist[0]
                    elif len(zhishigongtianpanlist[0]) == 3:
                        if zhishigongtianpanlist[0] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongtianpangan1 = "戊"
                            else:
                                zhishigongtianpangan1 = "戊"
                        else:
                            zhishigongtianpangan1 = zhishigongtianpanlist[-1]
                    if len(zhishigongtianpanlist[1]) == 1:
                        zhishigongtianpangan2 == zhishigongtianpanlist[1]
                    elif len(zhishigongtianpanlist[1]) == 3:
                        if zhishigongtianpanlist[1] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongtianpangan2 = "戊"
                            else:
                                zhishigongtianpangan2 = "戊"
                        else:
                            zhishigongtianpangan2 = zhishigongtianpanlist[-1]
                    if zhishigongtianpangan1 == rigan or zhishigongtianpangan2 == rigan:
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0

                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲申庚" or zhishigongdipanlist[1] == "甲申庚":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲申庚":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0

                if zhishigongdipanjishu == 1 and zhishigongtianpanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + rigangeng
                # 2.14 奇格
                # 庚+乙、丁
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲申庚" or zhishigongtianpanlist[1] == "甲申庚":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲申庚":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0

                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "乙" or zhishigongdipanlist[1] == "乙" or zhishigongdipanlist[
                        0] == "丁" or \
                            zhishigongdipanlist[1] == "丁":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 1:
                    if zhishigongdipan == "乙" or zhishigongdipan == "丁":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + gengyiorbingording
                # 2.15 天网
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲寅癸" or zhishigongtianpanlist[1] == "甲寅癸":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲寅癸":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0

                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲寅癸" or zhishigongdipanlist[1] == "甲寅癸":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲寅癸":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + guigui
                # 其他格
                jimen = ["开使", "休使", "生使"]
                xiongmen = ["死使", "惊使", "伤使", "杜使"]
                qitamen = ["死使", "惊使", "伤使", "杜使", "景使"]
                xiongxin = ["天蓬", "天芮", "天柱"]
                menpo = {"惊使": "23", "开使": "23", "休使": "8", "生使": "0", "死使": "0", "景使": "56", "杜使": "17",
                         "伤使": "17"}
                gongpo = {6: ["杜使", "伤使"], 5: ["杜使", "伤使"], 0: ["景使"], 7: ["休使"], 1: ["休使"],
                          8: ["惊使", "开使"],
                          3: ["生使", "死使"], 2: ["生使", "死使"]}
                mengongxiangshen = {"惊使": "17", "开使": "17", "休使": "56", "生使": "8", "死使": "8", "景使": "23",
                                    "杜使": "0",
                                    "伤使": "0"}
                # 2.17.2 乙
                # 乙+甲
                zhishigongdipanjishu1 = 0
                zhishigongdipanjishu2 = 0
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "乙" or zhishigongtianpanlist[1] == "乙":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                elif len(zhishigongtianpan) == 1:
                    if zhishigongtianpan == "乙":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                else:
                    zhishigongtianpanjishu1 = 0

                if len(zhishigongdipan) == 1:
                    zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲子戊":
                        if zhishigongbashen == "值符":
                            zhishigongdipanjishu = 0
                        else:
                            zhishigongdipanjishu = 0
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if len(zhishigongdipanlist[0]) == 1:
                        zhishigongdipanjishu1 = 0
                    elif len(zhishigongdipanlist[0]) == 3:
                        if zhishigongdipanlist[0] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongdipanjishu1 = 0
                            else:
                                zhishigongdipanjishu1 = 0
                        else:
                            zhishigongdipanjishu1 = 0
                    if len(zhishigongdipanlist[1]) == 1:
                        zhishigongdipanjishu2 = 0
                    elif len(zhishigongdipanlist[1]) == 3:
                        if zhishigongdipanlist[1] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongdipanjishu2 = 0
                            else:
                                zhishigongdipanjishu2 = 0
                        else:
                            zhishigongdipanjishu2 = 0
                    if zhishigongdipanjishu1 == 1 or zhishigongdipanjishu2 == 1:
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                if zhishigongtianpanjishu1 == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + yijia
                # 乙+乙
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "乙" or zhishigongtianpanlist[1] == "乙":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                elif len(zhishigongtianpan) == 1:
                    if zhishigongtianpan == "乙":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                else:
                    zhishigongtianpanjishu1 = 0

                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "乙" or zhishigongdipanlist[1] == "乙":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 1:
                    if zhishigongdipan == "乙":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu1 == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + yiyi
                # 乙+丙
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "乙" or zhishigongtianpanlist[1] == "乙":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                elif len(zhishigongtianpan) == 1:
                    if zhishigongtianpan == "乙":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                else:
                    zhishigongtianpanjishu1 = 0

                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "丙" or zhishigongdipanlist[1] == "丙":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 1:
                    if zhishigongdipan == "丙":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                zhishigongjiuxin = zhishigongshuju["九星"]
                if zhishigongtianpanjishu1 == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + yibing

                # 乙+丁
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "乙" or zhishigongtianpanlist[1] == "乙":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                elif len(zhishigongtianpan) == 1:
                    if zhishigongtianpan == "乙":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                else:
                    zhishigongtianpanjishu1 = 0

                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "丁" or zhishigongdipanlist[1] == "丁":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 1:
                    if zhishigongdipan == "丁":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu1 == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + yiding

                # 乙+戊
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "乙" or zhishigongtianpanlist[1] == "乙":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                elif len(zhishigongtianpan) == 1:
                    if zhishigongtianpan == "乙":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                else:
                    zhishigongtianpanjishu1 = 0
                if len(zhishigongdipan) == 1:
                    zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲子戊":
                        if zhishigongbashen == "值符":
                            zhishigongdipanjishu = 1
                        else:
                            zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if len(zhishigongdipanlist[0]) == 1:
                        zhishigongdipanjishu1 = 0
                    elif len(zhishigongdipanlist[0]) == 3:
                        if zhishigongdipanlist[0] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongdipanjishu1 = 1
                            else:
                                zhishigongdipanjishu1 = 1
                        else:
                            zhishigongdipanjishu1 = 0
                    if len(zhishigongdipanlist[1]) == 1:
                        zhishigongdipanjishu2 = 0
                    elif len(zhishigongdipanlist[1]) == 3:
                        if zhishigongdipanlist[1] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongdipanjishu2 = 1
                            else:
                                zhishigongdipanjishu2 = 1
                        else:
                            zhishigongdipanjishu2 = 0
                    if zhishigongdipanjishu1 == 1 or zhishigongdipanjishu2 == 1:
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                if zhishigongbamen in xiongmen:
                    bamenxiongjishu = 1
                else:
                    bamenxiongjishu = 0
                if zhishigongtianpanjishu1 == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + yiwu

                # 乙＋辛
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "乙" or zhishigongtianpanlist[1] == "乙":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                elif len(zhishigongtianpan) == 1:
                    if zhishigongtianpan == "乙":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                else:
                    zhishigongtianpanjishu1 = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲午辛" or zhishigongdipanlist[1] == "甲午辛":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲午辛":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu1 == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + yixin_qita
                # 乙+壬
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "乙" or zhishigongtianpanlist[1] == "乙":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                elif len(zhishigongtianpan) == 1:
                    if zhishigongtianpan == "乙":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                else:
                    zhishigongtianpanjishu1 = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲辰壬" or zhishigongdipanlist[1] == "甲辰壬":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲辰壬":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu1 == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + yiren_jimen
                # 乙+庚
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "乙" or zhishigongtianpanlist[1] == "乙":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                elif len(zhishigongtianpan) == 1:
                    if zhishigongtianpan == "乙":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                else:
                    zhishigongtianpanjishu1 = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲申庚" or zhishigongdipanlist[1] == "甲申庚":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲申庚":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu1 == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + yigeng_qita
                # 乙+癸
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "乙" or zhishigongtianpanlist[1] == "乙":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                elif len(zhishigongtianpan) == 1:
                    if zhishigongtianpan == "乙":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                else:
                    zhishigongtianpanjishu1 = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲寅癸" or zhishigongdipanlist[1] == "甲寅癸":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲寅癸":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu1 == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + yigui_qita
                # 2.17.3 丙
                # 丙+乙
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "丙" or zhishigongtianpanlist[1] == "丙":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                elif len(zhishigongtianpan) == 1:
                    if zhishigongtianpan == "丙":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                else:
                    zhishigongtianpanjishu1 = 0

                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "乙" or zhishigongdipanlist[1] == "乙":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 1:
                    if zhishigongdipan == "乙":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu1 == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + bingyi
                # 丙+丙
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "丙" or zhishigongtianpanlist[1] == "丙":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                elif len(zhishigongtianpan) == 1:
                    if zhishigongtianpan == "丙":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                else:
                    zhishigongtianpanjishu1 = 0

                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "丙" or zhishigongdipanlist[1] == "丙":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 1:
                    if zhishigongdipan == "丙":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu1 == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + bingbing

                # 丙+丁
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "丙" or zhishigongtianpanlist[1] == "丙":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                elif len(zhishigongtianpan) == 1:
                    if zhishigongtianpan == "丙":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                else:
                    zhishigongtianpanjishu1 = 0

                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "丁" or zhishigongdipanlist[1] == "丁":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 1:
                    if zhishigongdipan == "丁":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu1 == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + bingding
                # 丙+辛
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "丙" or zhishigongtianpanlist[1] == "丙":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                elif len(zhishigongtianpan) == 1:
                    if zhishigongtianpan == "丙":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                else:
                    zhishigongtianpanjishu1 = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲午辛" or zhishigongdipanlist[1] == "甲午辛":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲午辛":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu1 == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + bingxin
                # 丙+壬
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "丙" or zhishigongtianpanlist[1] == "丙":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                elif len(zhishigongtianpan) == 1:
                    if zhishigongtianpan == "丙":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                else:
                    zhishigongtianpanjishu1 = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲辰壬" or zhishigongdipanlist[1] == "甲辰壬":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲辰壬":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu1 == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + bingren
                # 丙+癸
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "丙" or zhishigongtianpanlist[1] == "丙":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                elif len(zhishigongtianpan) == 1:
                    if zhishigongtianpan == "丙":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                else:
                    zhishigongtianpanjishu1 = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲寅癸" or zhishigongdipanlist[1] == "甲寅癸":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲寅癸":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu1 == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + binggui
                # 2.17.4 丁
                # 丁+甲
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "丁" or zhishigongtianpanlist[1] == "丁":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                elif len(zhishigongtianpan) == 1:
                    if zhishigongtianpan == "丁":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                else:
                    zhishigongtianpanjishu1 = 0

                if len(zhishigongdipan) == 1:
                    zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲子戊":
                        if zhishigongbashen == "值符":
                            zhishigongdipanjishu = 0
                        else:
                            zhishigongdipanjishu = 0
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if len(zhishigongdipanlist[0]) == 1:
                        zhishigongdipanjishu1 = 0
                    elif len(zhishigongdipanlist[0]) == 3:
                        if zhishigongdipanlist[0] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongdipanjishu1 = 0
                            else:
                                zhishigongdipanjishu1 = 0
                        else:
                            zhishigongdipanjishu1 = 0
                    if len(zhishigongdipanlist[1]) == 1:
                        zhishigongdipanjishu2 = 0
                    elif len(zhishigongdipanlist[1]) == 3:
                        if zhishigongdipanlist[1] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongdipanjishu2 = 0
                            else:
                                zhishigongdipanjishu2 = 0
                        else:
                            zhishigongdipanjishu2 = 0
                    if zhishigongdipanjishu1 == 1 or zhishigongdipanjishu2 == 1:
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                if zhishigongtianpanjishu1 == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + dingjia
                # 丁+丁
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "丁" or zhishigongtianpanlist[1] == "丁":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                elif len(zhishigongtianpan) == 1:
                    if zhishigongtianpan == "丁":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                else:
                    zhishigongtianpanjishu1 = 0

                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "丁" or zhishigongdipanlist[1] == "丁":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 1:
                    if zhishigongdipan == "丁":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu1 == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + dingding
                # 丁+戊
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "丁" or zhishigongtianpanlist[1] == "丁":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                elif len(zhishigongtianpan) == 1:
                    if zhishigongtianpan == "丁":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                else:
                    zhishigongtianpanjishu1 = 0

                if len(zhishigongdipan) == 1:
                    zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲子戊":
                        if zhishigongbashen == "值符":
                            zhishigongdipanjishu = 1
                        else:
                            zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if len(zhishigongdipanlist[0]) == 1:
                        zhishigongdipanjishu1 = 0
                    elif len(zhishigongdipanlist[0]) == 3:
                        if zhishigongdipanlist[0] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongdipanjishu1 = 1
                            else:
                                zhishigongdipanjishu1 = 1
                        else:
                            zhishigongdipanjishu1 = 0
                    if len(zhishigongdipanlist[1]) == 1:
                        zhishigongdipanjishu2 = 0
                    elif len(zhishigongdipanlist[1]) == 3:
                        if zhishigongdipanlist[1] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongdipanjishu2 = 1
                            else:
                                zhishigongdipanjishu2 = 1
                        else:
                            zhishigongdipanjishu2 = 0
                    if zhishigongdipanjishu1 == 1 or zhishigongdipanjishu2 == 1:
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                if zhishigongtianpanjishu1 == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + dingwu
                # 丁+己
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "丁" or zhishigongtianpanlist[1] == "丁":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                elif len(zhishigongtianpan) == 1:
                    if zhishigongtianpan == "丁":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                else:
                    zhishigongtianpanjishu1 = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲戌己" or zhishigongdipanlist[1] == "甲戌己":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲戌己":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu1 == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + dingji
                # 丁+庚
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "丁" or zhishigongtianpanlist[1] == "丁":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                elif len(zhishigongtianpan) == 1:
                    if zhishigongtianpan == "丁":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                else:
                    zhishigongtianpanjishu1 = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲申庚" or zhishigongdipanlist[1] == "甲申庚":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲申庚":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu1 == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + dinggeng
                # 丁+辛
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "丁" or zhishigongtianpanlist[1] == "丁":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                elif len(zhishigongtianpan) == 1:
                    if zhishigongtianpan == "丁":
                        zhishigongtianpanjishu1 = 1
                    else:
                        zhishigongtianpanjishu1 = 0
                else:
                    zhishigongtianpanjishu1 = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲午辛" or zhishigongdipanlist[1] == "甲午辛":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲午辛":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu1 == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + dingxin
                # 2.17.5 戊

                # 戊+乙
                if len(zhishigongtianpan) == 1:
                    zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲子戊":
                        if zhishigongbashen == "值符":
                            zhishigongtianpanjishu = 1
                        else:
                            zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if len(zhishigongtianpanlist[0]) == 1:
                        zhishigongtianpanjishu1 = 0
                    elif len(zhishigongtianpanlist[0]) == 3:
                        if zhishigongtianpanlist[0] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongtianpanjishu1 = 1
                            else:
                                zhishigongtianpanjishu1 = 1
                        else:
                            zhishigongtianpanjishu1 = 0
                    if len(zhishigongtianpanlist[1]) == 1:
                        zhishigongtianpanjishu2 = 0
                    elif len(zhishigongtianpanlist[1]) == 3:
                        if zhishigongtianpanlist[1] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongtianpanjishu2 = 1
                            else:
                                zhishigongtianpanjishu2 = 1
                        else:
                            zhishigongtianpanjishu2 = 0
                    if zhishigongtianpanjishu1 == 1 or zhishigongtianpanjishu2 == 1:
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0

                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "乙" or zhishigongdipanlist[1] == "乙":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 1:
                    if zhishigongdipan == "乙":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongbamen in jimen:
                    bamenjilijishu = 1
                else:
                    bamenjilijishu = 0
                if zhishigongbamen in xiongmen:
                    bamenxiongjishu = 1
                else:
                    bamenxiongjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + wuyi_xiongmen
                # 戊＋丁
                if len(zhishigongtianpan) == 1:
                    zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲子戊":
                        if zhishigongbashen == "值符":
                            zhishigongtianpanjishu = 1
                        else:
                            zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if len(zhishigongtianpanlist[0]) == 1:
                        zhishigongtianpanjishu1 = 0
                    elif len(zhishigongtianpanlist[0]) == 3:
                        if zhishigongtianpanlist[0] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongtianpanjishu1 = 1
                            else:
                                zhishigongtianpanjishu1 = 1
                        else:
                            zhishigongtianpanjishu1 = 0
                    if len(zhishigongtianpanlist[1]) == 1:
                        zhishigongtianpanjishu2 = 0
                    elif len(zhishigongtianpanlist[1]) == 3:
                        if zhishigongtianpanlist[1] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongtianpanjishu2 = 1
                            else:
                                zhishigongtianpanjishu2 = 1
                        else:
                            zhishigongtianpanjishu2 = 0
                    if zhishigongtianpanjishu1 == 1 or zhishigongtianpanjishu2 == 1:
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "丁" or zhishigongdipanlist[1] == "丁":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 1:
                    if zhishigongdipan == "丁":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + wuding
                # 戊+戊
                if len(zhishigongtianpan) == 1:
                    zhishigongtianpanjishu == 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲子戊":
                        if zhishigongbashen == "值符":
                            zhishigongtianpanjishu = 1
                        else:
                            zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if len(zhishigongtianpanlist[0]) == 1:
                        zhishigongtianpanjishu1 = 0
                    elif len(zhishigongtianpanlist[0]) == 3:
                        if zhishigongtianpanlist[0] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongtianpanjishu1 = 1
                            else:
                                zhishigongtianpanjishu1 = 1
                        else:
                            zhishigongtianpanjishu1 = 0
                    if len(zhishigongtianpanlist[1]) == 1:
                        zhishigongtianpanjishu2 = 0
                    elif len(zhishigongtianpanlist[1]) == 3:
                        if zhishigongtianpanlist[1] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongtianpanjishu2 = 1
                            else:
                                zhishigongtianpanjishu2 = 1
                        else:
                            zhishigongtianpanjishu2 = 0
                    if zhishigongtianpanjishu1 == 1 or zhishigongtianpanjishu2 == 1:
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲子戊" or zhishigongdipanlist[1] == "甲子戊":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲子戊":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + wuwu
                # 戊+辛
                if len(zhishigongtianpan) == 1:
                    zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲子戊":
                        if zhishigongbashen == "值符":
                            zhishigongtianpanjishu = 1
                        else:
                            zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if len(zhishigongtianpanlist[0]) == 1:
                        zhishigongtianpanjishu1 = 0
                    elif len(zhishigongtianpanlist[0]) == 3:
                        if zhishigongtianpanlist[0] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongtianpanjishu1 = 1
                            else:
                                zhishigongtianpanjishu1 = 1
                        else:
                            zhishigongtianpanjishu1 = 0
                    if len(zhishigongtianpanlist[1]) == 1:
                        zhishigongtianpanjishu2 = 0
                    elif len(zhishigongtianpanlist[1]) == 3:
                        if zhishigongtianpanlist[1] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongtianpanjishu2 = 1
                            else:
                                zhishigongtianpanjishu2 = 1
                        else:
                            zhishigongtianpanjishu2 = 0
                    if zhishigongtianpanjishu1 == 1 or zhishigongtianpanjishu2 == 1:
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲午辛" or zhishigongdipanlist[1] == "甲午辛":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲午辛":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongbashen in jimen:
                    bamenjilijishu = 1
                else:
                    bamenjilijishu = 0
                if zhishigongbashen in xiongmen:
                    bamenxiongjishu = 1
                else:
                    bamenxiongjishu = 0

                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + wuxin_xiongmen
                # 戊+癸
                if len(zhishigongtianpan) == 1:
                    zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲子戊":
                        if zhishigongbashen == "值符":
                            zhishigongtianpanjishu = 1
                        else:
                            zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if len(zhishigongtianpanlist[0]) == 1:
                        zhishigongtianpanjishu1 = 0
                    elif len(zhishigongtianpanlist[0]) == 3:
                        if zhishigongtianpanlist[0] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongtianpanjishu1 = 1
                            else:
                                zhishigongtianpanjishu1 = 1
                        else:
                            zhishigongtianpanjishu1 = 0
                    if len(zhishigongtianpanlist[1]) == 1:
                        zhishigongtianpanjishu2 = 0
                    elif len(zhishigongtianpanlist[1]) == 3:
                        if zhishigongtianpanlist[1] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongtianpanjishu2 = 1
                            else:
                                zhishigongtianpanjishu2 = 1
                        else:
                            zhishigongtianpanjishu2 = 0
                    if zhishigongtianpanjishu1 == 1 or zhishigongtianpanjishu2 == 1:
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲寅癸" or zhishigongdipanlist[1] == "甲寅癸":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲寅癸":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongbashen in jimen:
                    bamenjilijishu = 1
                else:
                    bamenjilijishu = 0
                if zhishigongbashen in xiongmen:
                    bamenxiongjishu = 1
                else:
                    bamenxiongjishu = 0

                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + jiaziwugui
                # 戊+壬
                if len(zhishigongtianpan) == 1:
                    zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲子戊":
                        if zhishigongbashen == "值符":
                            zhishigongtianpanjishu = 1
                        else:
                            zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if len(zhishigongtianpanlist[0]) == 1:
                        zhishigongtianpanjishu1 = 0
                    elif len(zhishigongtianpanlist[0]) == 3:
                        if zhishigongtianpanlist[0] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongtianpanjishu1 = 1
                            else:
                                zhishigongtianpanjishu1 = 1
                        else:
                            zhishigongtianpanjishu1 = 0
                    if len(zhishigongtianpanlist[1]) == 1:
                        zhishigongtianpanjishu2 = 0
                    elif len(zhishigongtianpanlist[1]) == 3:
                        if zhishigongtianpanlist[1] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongtianpanjishu2 = 1
                            else:
                                zhishigongtianpanjishu2 = 1
                        else:
                            zhishigongtianpanjishu2 = 0

                    if zhishigongtianpanjishu1 == 1 or zhishigongtianpanjishu2 == 1:
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲辰壬" or zhishigongdipanlist[1] == "甲辰壬":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲辰壬":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + wuren

                # 2.17.6 己
                # 己+乙
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲戌己" or zhishigongtianpanlist[1] == "甲戌己":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲戌己":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "乙" or zhishigongdipanlist[1] == "乙":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 1:
                    if zhishigongdipan == "乙":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + jiyi
                # 己+丙
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲戌己" or zhishigongtianpanlist[1] == "甲戌己":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲戌己":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "丙" or zhishigongdipanlist[1] == "丙":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 1:
                    if zhishigongdipan == "丙":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + jibing
                # 己+丁
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲戌己" or zhishigongtianpanlist[1] == "甲戌己":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲戌己":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "丁" or zhishigongdipanlist[1] == "丁":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 1:
                    if zhishigongdipan == "丁":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + jiding
                # 己+己
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲戌己" or zhishigongtianpanlist[1] == "甲戌己":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲戌己":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲戌己" or zhishigongdipanlist[1] == "甲戌己":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲戌己":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + jiji
                # 己+庚
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲戌己" or zhishigongtianpanlist[1] == "甲戌己":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲戌己":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲申庚" or zhishigongdipanlist[1] == "甲申庚":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲申庚":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + jigeng
                # 己+辛
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲戌己" or zhishigongtianpanlist[1] == "甲戌己":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲戌己":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲午辛" or zhishigongdipanlist[1] == "甲午辛":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲午辛":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + jixin
                # 己+壬
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲戌己" or zhishigongtianpanlist[1] == "甲戌己":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲戌己":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲辰壬" or zhishigongdipanlist[1] == "甲辰壬":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲辰壬":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + jiren

                # 己+癸
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲戌己" or zhishigongtianpanlist[1] == "甲戌己":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲戌己":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲寅癸" or zhishigongdipanlist[1] == "甲寅癸":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲寅癸":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + jigui

                # 2.17.7 庚

                # 庚+庚
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲申庚" or zhishigongtianpanlist[1] == "甲申庚":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲申庚":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲申庚" or zhishigongdipanlist[1] == "甲申庚":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲申庚":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + genggeng
                # 庚+戊

                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲申庚" or zhishigongtianpanlist[1] == "甲申庚":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲申庚":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲子戊" or zhishigongdipanlist[1] == "甲子戊":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲子戊":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + gengwu
                # 庚+辛
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲申庚" or zhishigongtianpanlist[1] == "甲申庚":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲申庚":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲午辛" or zhishigongdipanlist[1] == "甲午辛":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲午辛":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + gengxin

                # 2.17.8 辛

                # 辛+甲
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲午辛" or zhishigongtianpanlist[1] == "甲午辛":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲午辛":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0

                if len(zhishigongdipan) == 1:
                    zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲子戊":
                        if zhishigongbashen == "值符":
                            zhishigongdipanjishu = 0
                        else:
                            zhishigongdipanjishu = 0
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if len(zhishigongdipanlist[0]) == 1:
                        zhishigongdipanjishu1 = 0
                    elif len(zhishigongdipanlist[0]) == 3:
                        if zhishigongdipanlist[0] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongdipanjishu1 = 0
                            else:
                                zhishigongdipanjishu1 = 0
                        else:
                            zhishigongdipanjishu1 = 0
                    if len(zhishigongdipanlist[1]) == 1:
                        zhishigongdipanjishu2 = 0
                    elif len(zhishigongdipanlist[1]) == 3:
                        if zhishigongdipanlist[1] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongdipanjishu2 = 0
                            else:
                                zhishigongdipanjishu2 = 0
                        else:
                            zhishigongdipanjishu2 == 0
                    if zhishigongdipanjishu1 == 1 or zhishigongdipanjishu2 == 1:
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + xinjia

                # 辛+丙
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲午辛" or zhishigongtianpanlist[1] == "甲午辛":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲午辛":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "丙" or zhishigongdipanlist[1] == "丙":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 1:
                    if zhishigongdipan == "丙":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongbamen in jimen:
                    bamenjilijishu = 1
                else:
                    bamenjilijishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + xinbing_qita
                # 辛+丁
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲午辛" or zhishigongtianpanlist[1] == "甲午辛":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲午辛":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "丁" or zhishigongdipanlist[1] == "丁":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 1:
                    if zhishigongdipan == "丁":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + xinding

                # 辛+戊
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲午辛" or zhishigongtianpanlist[1] == "甲午辛":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲午辛":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0
                if len(zhishigongdipan) == 1:
                    zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲子戊":
                        if zhishigongbashen == "值符":
                            zhishigongdipanjishu = 1
                        else:
                            zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if len(zhishigongdipanlist[0]) == 1:
                        zhishigongdipanjishu1 = 0
                    elif len(zhishigongdipanlist[0]) == 3:
                        if zhishigongdipanlist[0] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongdipanjishu1 = 1
                            else:
                                zhishigongdipanjishu1 = 1
                        else:
                            zhishigongdipanjishu1 = 0
                    if len(zhishigongdipanlist[1]) == 1:
                        zhishigongdipanjishu2 = 0
                    elif len(zhishigongdipanlist[1]) == 3:
                        if zhishigongdipanlist[1] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongdipanjishu2 = 1
                            else:
                                zhishigongdipanjishu2 = 1
                        else:
                            zhishigongdipanjishu2 = 0
                    if zhishigongdipanjishu1 == 1 or zhishigongdipanjishu2 == 1:
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + xinwu

                # 辛+己
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲午辛" or zhishigongtianpanlist[1] == "甲午辛":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲午辛":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲戌己" or zhishigongdipanlist[1] == "甲戌己":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲戌己":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + xinji
                # 辛+庚
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲午辛" or zhishigongtianpanlist[1] == "甲午辛":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲午辛":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲申庚" or zhishigongdipanlist[1] == "甲申庚":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲申庚":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + xingeng

                # 辛+辛
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲午辛" or zhishigongtianpanlist[1] == "甲午辛":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲午辛":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲午辛" or zhishigongdipanlist[1] == "甲午辛":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲午辛":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + xinxin
                # 辛+壬
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲午辛" or zhishigongtianpanlist[1] == "甲午辛":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲午辛":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲辰壬" or zhishigongdipanlist[1] == "甲辰壬":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲辰壬":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + xinren

                # 辛+癸
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲午辛" or zhishigongtianpanlist[1] == "甲午辛":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲午辛":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲寅癸" or zhishigongdipanlist[1] == "甲寅癸":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲寅癸":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + xingui

                # 2.17.9  壬
                # 壬+乙
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲辰壬" or zhishigongtianpanlist[1] == "甲辰壬":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲辰壬":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "乙" or zhishigongdipanlist[1] == "乙":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 1:
                    if zhishigongdipan == "乙":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + renyi

                # 壬+丙
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲辰壬" or zhishigongtianpanlist[1] == "甲辰壬":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲辰壬":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "丙" or zhishigongdipanlist[1] == "丙":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 1:
                    if zhishigongdipan == "丙":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + renbing
                # 壬+戊
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲辰壬" or zhishigongtianpanlist[1] == "甲辰壬":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲辰壬":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0
                if len(zhishigongdipan) == 1:
                    zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲子戊":
                        if zhishigongbashen == "值符":
                            zhishigongdipanjishu = 1
                        else:
                            zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if len(zhishigongdipanlist[0]) == 1:
                        zhishigongdipanjishu1 = 0
                    elif len(zhishigongdipanlist[0]) == 3:
                        if zhishigongdipanlist[0] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongdipanjishu1 = 1
                            else:
                                zhishigongdipanjishu1 = 1
                        else:
                            zhishigongdipanjishu1 = 0
                    if len(zhishigongdipanlist[1]) == 1:
                        zhishigongdipanjishu2 = 0
                    elif len(zhishigongdipanlist[1]) == 3:
                        if zhishigongdipanlist[1] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongdipanjishu2 = 1
                            else:
                                zhishigongdipanjishu2 = 1
                        else:
                            zhishigongdipanjishu2 = 0
                    if zhishigongdipanjishu1 == 1 or zhishigongdipanjishu2 == 1:
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + renwu

                # 壬+己
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲辰壬" or zhishigongtianpanlist[1] == "甲辰壬":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲辰壬":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲戌己" or zhishigongdipanlist[1] == "甲戌己":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲戌己":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + renji

                # 壬+辛
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲辰壬" or zhishigongtianpanlist[1] == "甲辰壬":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲辰壬":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲午辛" or zhishigongdipanlist[1] == "甲午辛":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲午辛":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + renxin
                # 壬+丁
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲辰壬" or zhishigongtianpanlist[1] == "甲辰壬":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲辰壬":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "丁" or zhishigongdipanlist[1] == "丁":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 1:
                    if zhishigongdipan == "丁":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + rending
                # 壬+庚
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲辰壬" or zhishigongtianpanlist[1] == "甲辰壬":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲辰壬":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲申庚" or zhishigongdipanlist[1] == "甲申庚":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲申庚":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + rengeng
                # 壬+壬
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲辰壬" or zhishigongtianpanlist[1] == "甲辰壬":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲辰壬":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲辰壬" or zhishigongdipanlist[1] == "甲辰壬":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲辰壬":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + renren
                # 壬+癸
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲辰壬" or zhishigongtianpanlist[1] == "甲辰壬":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲辰壬":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲寅癸" or zhishigongdipanlist[1] == "甲寅癸":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲寅癸":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + rengui

                # 2.17.10 癸

                # 癸+甲
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲寅癸" or zhishigongtianpanlist[1] == "甲寅癸":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲寅癸":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0

                if len(zhishigongdipan) == 1:
                    zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲子戊":
                        if zhishigongbashen == "值符":
                            zhishigongdipanjishu = 0
                        else:
                            zhishigongdipanjishu = 0
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if len(zhishigongdipanlist[0]) == 1:
                        zhishigongdipanjishu1 = 0
                    elif len(zhishigongdipanlist[0]) == 3:
                        if zhishigongdipanlist[0] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongdipanjishu1 = 0
                            else:
                                zhishigongdipanjishu1 = 0
                        else:
                            zhishigongdipanjishu1 = 0
                    if len(zhishigongdipanlist[1]) == 1:
                        zhishigongdipanjishu2 = 0
                    elif len(zhishigongdipanlist[1]) == 3:
                        if zhishigongdipanlist[1] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongdipanjishu2 = 0
                            else:
                                zhishigongdipanjishu2 = 0
                        else:
                            zhishigongdipanjishu2 = 0
                    if zhishigongdipanjishu1 == 1 or zhishigongdipanjishu2 == 1:
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + guijia

                # 癸+乙
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲寅癸" or zhishigongtianpanlist[1] == "甲寅癸":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲寅癸":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "乙" or zhishigongdipanlist[1] == "乙":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 1:
                    if zhishigongdipan == "乙":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongbamen in jimen:
                    bamenjilijishu = 1
                else:
                    bamenjilijishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1 and bamenjilijishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + guiyi_qita

                elif zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1 and bamenjilijishu == 0:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + guiyi_qita
                # 癸+丙
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲寅癸" or zhishigongtianpanlist[1] == "甲寅癸":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲寅癸":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "丙" or zhishigongdipanlist[1] == "丙":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 1:
                    if zhishigongdipan == "丙":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + guibing
                # 癸+丁
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲寅癸" or zhishigongtianpanlist[1] == "甲寅癸":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲寅癸":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "丁" or zhishigongdipanlist[1] == "丁":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 1:
                    if zhishigongdipan == "丁":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + guiding

                # 癸+戊
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲寅癸" or zhishigongtianpanlist[1] == "甲寅癸":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲寅癸":
                        zhishigongtianpanjishu = 1

                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0
                if len(zhishigongdipan) == 1:
                    zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲子戊":
                        if zhishigongbashen == "值符":
                            zhishigongdipanjishu = 1
                        else:
                            zhishigongdipanjishu = 1

                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if len(zhishigongdipanlist[0]) == 1:
                        zhishigongdipanjishu1 = 0
                    elif len(zhishigongdipanlist[0]) == 3:
                        if zhishigongdipanlist[0] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongdipanjishu1 = 1
                            else:
                                zhishigongdipanjishu1 = 1
                        else:
                            zhishigongdipanjishu1 = 0
                    if len(zhishigongdipanlist[1]) == 1:
                        zhishigongdipanjishu2 = 0
                    elif len(zhishigongdipanlist[1]) == 3:
                        if zhishigongdipanlist[1] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongdipanjishu2 = 1
                            else:
                                zhishigongdipanjishu2 = 1
                        else:
                            zhishigongdipanjishu2 = 0
                    if zhishigongdipanjishu1 == 1 or zhishigongdipanjishu2 == 1:
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0

                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + guiwu_xiongmenpozhi
                # 癸+己
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲寅癸" or zhishigongtianpanlist[1] == "甲寅癸":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲寅癸":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲戌己" or zhishigongdipanlist[1] == "甲戌己":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲戌己":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + guiji
                # 癸+庚
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲寅癸" or zhishigongtianpanlist[1] == "甲寅癸":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲寅癸":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲申庚" or zhishigongdipanlist[1] == "甲申庚":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲申庚":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + guigeng
                # 癸+辛
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲寅癸" or zhishigongtianpanlist[1] == "甲寅癸":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲寅癸":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲午辛" or zhishigongdipanlist[1] == "甲午辛":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲午辛":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + guixin
                # 癸+壬
                if len(zhishigongtianpan) > 3:
                    zhishigongtianpanlist = zhishigongtianpan.split("\n")
                    if zhishigongtianpanlist[0] == "甲寅癸" or zhishigongtianpanlist[1] == "甲寅癸":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                elif len(zhishigongtianpan) == 3:
                    if zhishigongtianpan == "甲寅癸":
                        zhishigongtianpanjishu = 1
                    else:
                        zhishigongtianpanjishu = 0
                else:
                    zhishigongtianpanjishu = 0
                if len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if zhishigongdipanlist[0] == "甲辰壬" or zhishigongdipanlist[1] == "甲辰壬":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲辰壬":
                        zhishigongdipanjishu = 1
                    else:
                        zhishigongdipanjishu = 0
                else:
                    zhishigongdipanjishu = 0
                if zhishigongtianpanjishu == 1 and zhishigongdipanjishu == 1:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + guiren
                return SpaDigiX_APPONE_Value

            zhishigongshuju = ninegridsbasicmessage[zhishigongdingwei_index]  # 读取值使所在宫的数据
            zhishigongtianpanpanduan = zhishigongshuju["天盘"]
            zhishigongdipanpanduan = zhishigongshuju["地盘"]
            if len(zhishigongtianpanpanduan) > 3 and len(zhishigongdipanpanduan) > 3:
                zhishigongtianpanshurulist = zhishigongtianpanpanduan.split("\n")
                zhishigongdipanshurulist = zhishigongdipanpanduan.split("\n")
                SS = getjixiongge(SpaDigiX_APPONE_Value, zhishigongtianpanshurulist[0], zhishigongdipanshurulist[0])
                SpaDigiX_APPONE_Value = SS
                SS = getjixiongge(SpaDigiX_APPONE_Value, zhishigongtianpanshurulist[1], zhishigongdipanshurulist[1])
                SpaDigiX_APPONE_Value = SS
            else:
                SS = getjixiongge(SpaDigiX_APPONE_Value, zhishigongtianpanpanduan, zhishigongdipanpanduan)
                SpaDigiX_APPONE_Value = SS
            jixionggejishuzuizhong = SpaDigiX_APPONE_Value - jixionggejishuchushi
            print(f'2 吉凶格：{jixionggejishuzuizhong}')
            jixionggeSDX = SpaDigiX_APPONE_Value - zhichongSDX
            # -----------------------------------------------------------------------------------------------------------------------
            # 3 单宫天盘干定数
            print(
                "----------------------------------------------------------------------------------------------------------")
            # 十二个月份各干定数
            zhishigongtianpan = zhishigongshuju["天盘"]
            zhishigongdipan = zhishigongshuju["地盘"]
            zhishigongbamen = zhishigongshuju["八门"]
            zhishigongjiuxing = zhishigongshuju["九星"]
            zhishigongbashen = zhishigongshuju["八神"]
            # -----------------------------------------------------------------------------------------------------------------------
            dangongtianpangandingshuchushi = SpaDigiX_APPONE_Value
            for key in month_dict_dangongtianpangandingshu:
                if key == yueganzhi[1]:
                    yuefen = key
                    yuefen_dangongtianpangandingshu = month_dict_dangongtianpangandingshu[key]
                else:
                    pass
            if len(zhishigongtianpan) == 1:
                zhishigongtianpangan = zhishigongtianpan
                for key in yuefen_dangongtianpangandingshu:
                    if zhishigongtianpangan == key:
                        shieryuefengegandingshu = yuefen_dangongtianpangandingshu[key]
                        SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + shieryuefengegandingshu
            elif len(zhishigongtianpan) == 3:
                if zhishigongtianpan == "甲子戊":
                    if zhishigongbashen == "值符":
                        zhishigongtianpangan = "戊"
                    else:
                        zhishigongtianpangan = "戊"
                else:
                    zhishigongtianpangan = zhishigongtianpan[-1]
                for key in yuefen_dangongtianpangandingshu:
                    if zhishigongtianpangan == key:
                        shieryuefengegandingshu = yuefen_dangongtianpangandingshu[key]
                        SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + shieryuefengegandingshu
            else:
                zhishigongtianpanlist = zhishigongtianpan.split("\n")
                # 1
                if len(zhishigongtianpanlist[0]) == 1:
                    zhishigongtianpangan1 = zhishigongtianpanlist[0]
                    for key in yuefen_dangongtianpangandingshu:
                        if zhishigongtianpangan1 == key:
                            shieryuefengegandingshu1 = yuefen_dangongtianpangandingshu[key]
                elif len(zhishigongtianpanlist[0]) == 3:
                    if zhishigongtianpanlist[0] == "甲子戊":
                        if zhishigongbashen == "值符":
                            zhishigongtianpangan1 = "戊"
                        else:
                            zhishigongtianpangan1 = "戊"
                    else:
                        zhishigongtianpangan1 = zhishigongtianpanlist[0][-1]
                    for key in yuefen_dangongtianpangandingshu:
                        if zhishigongtianpangan1 == key:
                            shieryuefengegandingshu1 = yuefen_dangongtianpangandingshu[key]

                if len(zhishigongtianpanlist[1]) == 1:
                    zhishigongtianpangan2 = zhishigongtianpanlist[1]
                    for key in yuefen_dangongtianpangandingshu:
                        if zhishigongtianpangan2 == key:
                            shieryuefengegandingshu2 = yuefen_dangongtianpangandingshu[key]
                elif len(zhishigongtianpanlist[1]) == 3:
                    if zhishigongtianpanlist[1] == "甲子戊":
                        if zhishigongbashen == "值符":
                            zhishigongtianpangan2 = "戊"
                        else:
                            zhishigongtianpangan2 = "戊"
                    else:
                        zhishigongtianpangan2 = zhishigongtianpanlist[1][-1]
                    for key in yuefen_dangongtianpangandingshu:
                        if zhishigongtianpangan2 == key:
                            shieryuefengegandingshu2 = yuefen_dangongtianpangandingshu[key]
                shieryuefengegandingshu = (shieryuefengegandingshu2 + shieryuefengegandingshu1) / 2
                SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + shieryuefengegandingshu
            # 九宫各天盘干定数
            # -----------------------------------------------------------------------------------------------------------------------
            gongweixuhaoduiying = {0: "坎一宫", 1: "坤二宫", 2: "震三宫", 3: "巽四宫", 5: "乾六宫", 6: "兑七宫",
                                   7: "艮八宫",
                                   8: "离九宫"}
            for key in palace_dict_dangongtianpangandingshu:
                if key == zhishigongdingwei_index:
                    gongming = gongweixuhaoduiying[key]
                    gongwei_dangongtianpangandingshu = palace_dict_dangongtianpangandingshu[key]
                else:
                    pass
            if len(zhishigongtianpan) == 1:
                zhishigongtianpangan = zhishigongtianpan
                for key in gongwei_dangongtianpangandingshu:
                    if zhishigongtianpangan == key:
                        jiugonggetianpangandingshu = gongwei_dangongtianpangandingshu[key]
                        SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + jiugonggetianpangandingshu
            elif len(zhishigongtianpan) == 3:
                if zhishigongtianpan == "甲子戊":
                    if zhishigongbashen == "值符":
                        zhishigongtianpangan = "戊"
                    else:
                        zhishigongtianpangan = "戊"
                else:
                    zhishigongtianpangan = zhishigongtianpan[-1]
                for key in gongwei_dangongtianpangandingshu:
                    if zhishigongtianpangan == key:
                        jiugonggetianpangandingshu = gongwei_dangongtianpangandingshu[key]
                        SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + jiugonggetianpangandingshu
            else:
                zhishigongtianpanlist = zhishigongtianpan.split("\n")
                # 1
                if len(zhishigongtianpanlist[0]) == 1:
                    zhishigongtianpangan1 = zhishigongtianpanlist[0]
                    for key in gongwei_dangongtianpangandingshu:
                        if zhishigongtianpangan1 == key:
                            jiugonggetianpangandingshu1 = gongwei_dangongtianpangandingshu[key]
                elif len(zhishigongtianpanlist[0]) == 3:
                    if zhishigongtianpanlist[0] == "甲子戊":
                        if zhishigongbashen == "值符":
                            zhishigongtianpangan1 = "戊"
                        else:
                            zhishigongtianpangan1 = "戊"
                    else:
                        zhishigongtianpangan1 = zhishigongtianpanlist[0][-1]
                    for key in gongwei_dangongtianpangandingshu:
                        if zhishigongtianpangan1 == key:
                            jiugonggetianpangandingshu1 = gongwei_dangongtianpangandingshu[key]

                if len(zhishigongtianpanlist[1]) == 1:
                    zhishigongtianpangan2 = zhishigongtianpanlist[1]
                    for key in gongwei_dangongtianpangandingshu:
                        if zhishigongtianpangan2 == key:
                            jiugonggetianpangandingshu2 = gongwei_dangongtianpangandingshu[key]
                elif len(zhishigongtianpanlist[1]) == 3:
                    if zhishigongtianpanlist[1] == "甲子戊":
                        if zhishigongbashen == "值符":
                            zhishigongtianpangan2 = "戊"
                        else:
                            zhishigongtianpangan2 = "戊"
                    else:
                        zhishigongtianpangan2 = zhishigongtianpanlist[1][-1]
                    for key in gongwei_dangongtianpangandingshu:
                        if zhishigongtianpangan2 == key:
                            jiugonggetianpangandingshu2 = gongwei_dangongtianpangandingshu[key]
                jiugonggetianpangandingshu = (jiugonggetianpangandingshu2 + jiugonggetianpangandingshu1) / 2
                SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + jiugonggetianpangandingshu
            # -----------------------------------------------------------------------------------------------------------------------
            # 天盘干与地盘干五行力量消长定数
            # -----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------------------------------------------------------------------------------
            if len(zhishigongtianpan) == 1:
                zhishigongtianpangan = zhishigongtianpan
                for key in tianpandingwei_dict_dangongtianpangandingshu:
                    if zhishigongtianpangan == key:
                        tianpandingwei_dipan_dangongtianpangandingshu = tianpandingwei_dict_dangongtianpangandingshu[
                            key]
                    else:
                        pass
                if len(zhishigongdipan) == 1:
                    zhishigongdipangan = zhishigongdipan
                    for key in tianpandingwei_dipan_dangongtianpangandingshu:
                        if zhishigongdipangan == key:
                            tiandiwuxingliliangxiaozhangdingshu = tianpandingwei_dipan_dangongtianpangandingshu[key]
                            SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + tiandiwuxingliliangxiaozhangdingshu
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲子戊":
                        if zhishigongbashen == "值符":
                            zhishigongdipangan = "戊"
                        else:
                            zhishigongdipangan = "戊"
                    else:
                        zhishigongdipangan = zhishigongdipan[-1]
                    for key in tianpandingwei_dipan_dangongtianpangandingshu:
                        if zhishigongdipangan == key:
                            tiandiwuxingliliangxiaozhangdingshu = tianpandingwei_dipan_dangongtianpangandingshu[key]
                            SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + tiandiwuxingliliangxiaozhangdingshu
                elif len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if len(zhishigongdipanlist[0]) == 1:
                        zhishigongdipangan1 = zhishigongdipanlist[0]
                        for key in tianpandingwei_dipan_dangongtianpangandingshu:
                            if zhishigongdipangan1 == key:
                                tiandiwuxingliliangxiaozhangdingshu1 = tianpandingwei_dipan_dangongtianpangandingshu[
                                    key]
                            else:
                                pass
                    elif len(zhishigongdipanlist[0]) == 3:
                        if zhishigongdipanlist[0] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongdipangan1 = "戊"
                            else:
                                zhishigongdipangan1 = "戊"
                        else:
                            zhishigongdipangan1 = zhishigongdipanlist[0][-1]
                        for key in tianpandingwei_dipan_dangongtianpangandingshu:
                            if zhishigongdipangan1 == key:
                                tiandiwuxingliliangxiaozhangdingshu1 = tianpandingwei_dipan_dangongtianpangandingshu[
                                    key]
                            else:
                                pass
                    if len(zhishigongdipanlist[1]) == 1:
                        zhishigongdipangan2 = zhishigongdipanlist[1]
                        for key in tianpandingwei_dipan_dangongtianpangandingshu:
                            if zhishigongdipangan2 == key:
                                tiandiwuxingliliangxiaozhangdingshu2 = tianpandingwei_dipan_dangongtianpangandingshu[
                                    key]
                            else:
                                pass
                    elif len(zhishigongdipanlist[1]) == 3:
                        if zhishigongdipanlist[1] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongdipangan2 = "戊"
                            else:
                                zhishigongdipangan2 = "戊"
                        else:
                            zhishigongdipangan2 = zhishigongdipanlist[1][-1]
                        for key in tianpandingwei_dipan_dangongtianpangandingshu:
                            if zhishigongdipangan2 == key:
                                tiandiwuxingliliangxiaozhangdingshu2 = tianpandingwei_dipan_dangongtianpangandingshu[
                                    key]
                    tiandiwuxingliliangxiaozhangdingshu = (
                                                                  tiandiwuxingliliangxiaozhangdingshu1 + tiandiwuxingliliangxiaozhangdingshu2) / 2
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + tiandiwuxingliliangxiaozhangdingshu
            elif len(zhishigongtianpan) == 3:
                if zhishigongtianpan == "甲子戊":
                    if zhishigongbashen == "值符":
                        zhishigongtianoangan = "戊"
                    else:
                        zhishigongtianpangan = "戊"
                else:
                    zhishigongtianpangan = zhishigongtianpan[-1]
                for key in tianpandingwei_dict_dangongtianpangandingshu:
                    if zhishigongtianpangan == key:
                        tianpandingwei_dipan_dangongtianpangandingshu = tianpandingwei_dict_dangongtianpangandingshu[
                            key]
                    else:
                        pass
                if len(zhishigongdipan) == 1:
                    zhishigongdipangan = zhishigongdipan
                    for key in tianpandingwei_dipan_dangongtianpangandingshu:
                        if zhishigongdipangan == key:
                            tiandiwuxingliliangxiaozhangdingshu = tianpandingwei_dipan_dangongtianpangandingshu[key]
                            SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + tiandiwuxingliliangxiaozhangdingshu
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲子戊":
                        if zhishigongbashen == "值符":
                            zhishigongdipangan = "戊"
                        else:
                            zhishigongdipangan = "戊"
                    else:
                        zhishigongdipangan = zhishigongdipan[-1]
                    for key in tianpandingwei_dipan_dangongtianpangandingshu:
                        if zhishigongdipangan == key:
                            tiandiwuxingliliangxiaozhangdingshu = tianpandingwei_dipan_dangongtianpangandingshu[key]
                            SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + tiandiwuxingliliangxiaozhangdingshu
                elif len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if len(zhishigongdipanlist[0]) == 1:
                        zhishigongdipangan1 = zhishigongdipanlist[0]
                        for key in tianpandingwei_dipan_dangongtianpangandingshu:
                            if zhishigongdipangan1 == key:
                                tiandiwuxingliliangxiaozhangdingshu1 = tianpandingwei_dipan_dangongtianpangandingshu[
                                    key]
                            else:
                                pass
                    elif len(zhishigongdipanlist[0]) == 3:
                        if zhishigongdipanlist[0] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongdipangan1 = "戊"
                            else:
                                zhishigongdipangan1 = "戊"
                        else:
                            zhishigongdipangan1 = zhishigongdipanlist[0][-1]
                        for key in tianpandingwei_dipan_dangongtianpangandingshu:
                            if zhishigongdipangan1 == key:
                                tiandiwuxingliliangxiaozhangdingshu1 = tianpandingwei_dipan_dangongtianpangandingshu[
                                    key]
                            else:
                                pass
                    if len(zhishigongdipanlist[1]) == 1:
                        zhishigongdipangan2 = zhishigongdipanlist[1]
                        for key in tianpandingwei_dipan_dangongtianpangandingshu:
                            if zhishigongdipangan2 == key:
                                tiandiwuxingliliangxiaozhangdingshu2 = tianpandingwei_dipan_dangongtianpangandingshu[
                                    key]
                            else:
                                pass
                    elif len(zhishigongdipanlist[1]) == 3:
                        if zhishigongdipanlist[1] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongdipangan2 = "戊"
                            else:
                                zhishigongdipangan2 = "戊"
                        else:
                            zhishigongdipangan2 = zhishigongdipanlist[1][-1]
                        for key in tianpandingwei_dipan_dangongtianpangandingshu:
                            if zhishigongdipangan2 == key:
                                tiandiwuxingliliangxiaozhangdingshu2 = tianpandingwei_dipan_dangongtianpangandingshu[
                                    key]
                    tiandiwuxingliliangxiaozhangdingshu = (
                                                                  tiandiwuxingliliangxiaozhangdingshu1 + tiandiwuxingliliangxiaozhangdingshu2) / 2
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + tiandiwuxingliliangxiaozhangdingshu
            else:
                zhishigongtianpanlist = zhishigongtianpan.split("\n")
                if len(zhishigongtianpanlist[0]) == 1:
                    zhishigongtianpangan1 = zhishigongtianpanlist[0]
                elif len(zhishigongtianpanlist[0]) == 3:
                    if zhishigongtianpanlist[0] == "甲子戊":
                        if zhishigongbashen == "值符":
                            zhishigongtianpangan1 = "戊"
                        else:
                            zhishigongtianpangan1 = "戊"
                    else:
                        zhishigongtianpangan1 = zhishigongtianpanlist[0][-1]
                for key in tianpandingwei_dict_dangongtianpangandingshu:
                    if zhishigongtianpangan1 == key:
                        tianpandingwei_dipan2_dangongtianpangandingshu = tianpandingwei_dict_dangongtianpangandingshu[
                            key]
                    else:
                        pass
                if len(zhishigongdipan) == 1:
                    zhishigongdipangan = zhishigongdipan
                    for key in tianpandingwei_dipan2_dangongtianpangandingshu:
                        if zhishigongdipangan == key:
                            tiandiwuxingliliangxiaozhangdingshu1 = tianpandingwei_dipan2_dangongtianpangandingshu[key]
                        else:
                            pass
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲子戊":
                        if zhishigongbashen == "值符":
                            zhishigongdipangan = "戊"
                        else:
                            zhishigongdipangan = "戊"
                    else:
                        zhishigongdipangan = zhishigongdipan[-1]
                    for key in tianpandingwei_dipan2_dangongtianpangandingshu:
                        if zhishigongdipangan == key:
                            tiandiwuxingliliangxiaozhangdingshu1 = tianpandingwei_dipan2_dangongtianpangandingshu[key]
                elif len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if len(zhishigongdipanlist[0]) == 1:
                        zhishigongdipangan1 = zhishigongdipanlist[0]
                        for key in tianpandingwei_dipan2_dangongtianpangandingshu:
                            if zhishigongdipangan1 == key:
                                tiandiwuxingliliangxiaozhangdingshu1 = tianpandingwei_dipan2_dangongtianpangandingshu[
                                    key]
                            else:
                                pass
                    elif len(zhishigongdipanlist[0]) == 3:
                        if zhishigongdipanlist[0] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongdipangan1 = "戊"
                            else:
                                zhishigongdipangan1 = "戊"
                        else:
                            zhishigongdipangan1 = zhishigongdipanlist[0][-1]
                        for key in tianpandingwei_dipan2_dangongtianpangandingshu:
                            if zhishigongdipangan1 == key:
                                tiandiwuxingliliangxiaozhangdingshu1 = tianpandingwei_dipan2_dangongtianpangandingshu[
                                    key]
                            else:
                                pass
                    if len(zhishigongdipanlist[1]) == 1:
                        zhishigongdipangan2 = zhishigongdipanlist[1]
                        for key in tianpandingwei_dipan2_dangongtianpangandingshu:
                            if zhishigongdipangan2 == key:
                                tiandiwuxingliliangxiaozhangdingshu2 = tianpandingwei_dipan2_dangongtianpangandingshu[
                                    key]
                            else:
                                pass
                    elif len(zhishigongdipanlist[1]) == 3:
                        if zhishigongdipanlist[1] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongdipangan2 = "戊"
                            else:
                                zhishigongdipangan2 = "戊"
                        else:
                            zhishigongdipangan2 = zhishigongdipanlist[1][-1]
                        for key in tianpandingwei_dipan2_dangongtianpangandingshu:
                            if zhishigongdipangan2 == key:
                                tiandiwuxingliliangxiaozhangdingshu2 = tianpandingwei_dipan2_dangongtianpangandingshu[
                                    key]

                if len(zhishigongtianpanlist[1]) == 1:
                    zhishigongtianpangan2 = zhishigongtianpanlist[1]
                elif len(zhishigongtianpanlist[1]) == 3:
                    if zhishigongtianpanlist[1] == "甲子戊":
                        if zhishigongbashen == "值符":
                            zhishigongtianpangan2 = "戊"
                        else:
                            zhishigongtianpangan2 = "戊"
                    else:
                        zhishigongtianpangan2 = zhishigongtianpanlist[1][-1]
                for key in tianpandingwei_dict_dangongtianpangandingshu:
                    if zhishigongtianpangan2 == key:
                        tianpandingwei_dipan3_dangongtianpangandingshu = tianpandingwei_dict_dangongtianpangandingshu[
                            key]
                    else:
                        pass

                if len(zhishigongdipan) == 1:
                    zhishigongdipangan = zhishigongdipan
                    for key in tianpandingwei_dipan3_dangongtianpangandingshu:
                        if zhishigongdipangan == key:
                            tiandiwuxingliliangxiaozhangdingshu3 = tianpandingwei_dipan3_dangongtianpangandingshu[key]
                        else:
                            pass
                elif len(zhishigongdipan) == 3:
                    if zhishigongdipan == "甲子戊":
                        if zhishigongbashen == "值符":
                            zhishigongdipangan = "戊"
                        else:
                            zhishigongdipangan = "戊"
                    else:
                        zhishigongdipangan = zhishigongdipan[-1]
                    for key in tianpandingwei_dipan3_dangongtianpangandingshu:
                        if zhishigongdipangan == key:
                            tiandiwuxingliliangxiaozhangdingshu3 = tianpandingwei_dipan3_dangongtianpangandingshu[key]
                elif len(zhishigongdipan) > 3:
                    zhishigongdipanlist = zhishigongdipan.split("\n")
                    if len(zhishigongdipanlist[0]) == 1:
                        zhishigongdipangan1 = zhishigongdipanlist[0]
                        for key in tianpandingwei_dipan3_dangongtianpangandingshu:
                            if zhishigongdipangan1 == key:
                                tiandiwuxingliliangxiaozhangdingshu3 = tianpandingwei_dipan3_dangongtianpangandingshu[
                                    key]
                            else:
                                pass
                    elif len(zhishigongdipanlist[0]) == 3:
                        if zhishigongdipanlist[0] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongdipangan1 = "戊"
                            else:
                                zhishigongdipangan1 = "戊"
                        else:
                            zhishigongdipangan1 = zhishigongdipanlist[0][-1]
                        for key in tianpandingwei_dipan3_dangongtianpangandingshu:
                            if zhishigongdipangan1 == key:
                                tiandiwuxingliliangxiaozhangdingshu3 = tianpandingwei_dipan3_dangongtianpangandingshu[
                                    key]
                            else:
                                pass
                    if len(zhishigongdipanlist[1]) == 1:
                        zhishigongdipangan2 = zhishigongdipanlist[1]
                        for key in tianpandingwei_dipan3_dangongtianpangandingshu:
                            if zhishigongdipangan2 == key:
                                tiandiwuxingliliangxiaozhangdingshu4 = tianpandingwei_dipan3_dangongtianpangandingshu[
                                    key]
                            else:
                                pass
                    elif len(zhishigongdipanlist[1]) == 3:
                        if zhishigongdipanlist[1] == "甲子戊":
                            if zhishigongbashen == "值符":
                                zhishigongdipangan2 = "戊"
                            else:
                                zhishigongdipangan2 = "戊"
                        else:
                            zhishigongdipangan2 = zhishigongdipanlist[1][-1]
                        for key in tianpandingwei_dipan3_dangongtianpangandingshu:
                            if zhishigongdipangan2 == key:
                                tiandiwuxingliliangxiaozhangdingshu4 = tianpandingwei_dipan3_dangongtianpangandingshu[
                                    key]

                try:
                    # 尝试获取变量的值
                    variable_value = zhishigongdipangan
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + (
                            tiandiwuxingliliangxiaozhangdingshu1 + tiandiwuxingliliangxiaozhangdingshu3) / 2
                except NameError:
                    SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + (
                            tiandiwuxingliliangxiaozhangdingshu1 + tiandiwuxingliliangxiaozhangdingshu4) / 2
            dangongtianpangandingshuzuizhong = SpaDigiX_APPONE_Value - dangongtianpangandingshuchushi
            print(f"3 单宫天盘干定数：{dangongtianpangandingshuzuizhong}")
            tianpanganSDX = SpaDigiX_APPONE_Value - jixionggeSDX
            # 4 单宫九星力量消长定数
            print(
                "----------------------------------------------------------------------------------------------------------")
            dangongjiuxingliliangjishuchushi = SpaDigiX_APPONE_Value
            # -----------------------------------------------------------------------------------------------------------------------
            jixing = ["天辅", "天禽", "天心", "天任"]
            xiongxing = ["天蓬", "天芮", "天柱"]
            # 十二月各星力量
            zhishigongjiuxing = zhishigongshuju["九星"]
            # 特殊情况
            if zhishigongjiuxing == "天蓬" and zhishigongdingwei_index == 8 and (
                    yueganzhi[1] == "巳" or yueganzhi[1] == "午"):
                SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value - 1
            elif (
                    zhishigongjiuxing == "天芮" or zhishigongjiuxing == "天禽" or zhishigongjiuxing == "天任") and zhishigongdingwei_index == 0 and (
                    yueganzhi[1] == "子" or yueganzhi[1] == "亥"):
                SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value - 1
            elif (zhishigongjiuxing == "天冲" or zhishigongjiuxing == "天辅") and (
                    zhishigongdingwei_index == 1 or zhishigongdingwei_index == 7) and (
                    yueganzhi[1] == "丑" or yueganzhi[1] == "辰" or yueganzhi[1] == "未" or yueganzhi[1] == "戌"):
                SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value - 1
            elif (zhishigongjiuxing == "天心" or zhishigongjiuxing == "天柱") and (
                    zhishigongdingwei_index == 2 or zhishigongdingwei_index == 3) and (
                    yueganzhi[1] == "寅" or yueganzhi[1] == "卯"):
                SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value - 1
            elif zhishigongjiuxing == "天英" and (zhishigongdingwei_index == 6 or zhishigongdingwei_index == 5) and (
                    yueganzhi[1] == "申" or yueganzhi[1] == "酉"):
                SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value - 1
            else:
                # 各星力量

                for key in yuefenduiyingjiuxingliliang:
                    if yueganzhi[1] == key:
                        yuefenduiyingjiuxingliliang_benyuelist = yuefenduiyingjiuxingliliang[key]
                jiuxinggeyueliliangdingshu = yuefenduiyingjiuxingliliang_benyuelist[zhishigongjiuxing]
                SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + jiuxinggeyueliliangdingshu
                # -----------------------------------------------------------------------------------------------------------------------
                # 4.2 九宫各星力量
                # -----------------------------------------------------------------------------------------------------------------------
                # 九宫各星力量数据
                zhishiduiyinggongjiuxingdist = jiugonggexingliliangshuju[zhishigongdingwei_index]
                zhishigongduiyingjiuxingliliangdingshu = zhishiduiyinggongjiuxingdist[zhishigongjiuxing]
                SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + zhishigongduiyingjiuxingliliangdingshu
            dangongjiuxingliliangjishuzuizhong = SpaDigiX_APPONE_Value - dangongjiuxingliliangjishuchushi
            print(f"4 单宫九星力量消长定数：{dangongjiuxingliliangjishuzuizhong}")
            jiuxingSDX = SpaDigiX_APPONE_Value - tianpanganSDX
            # -----------------------------------------------------------------------------------------------------------------------
            # 5 单宫八门力量消长
            print(
                "----------------------------------------------------------------------------------------------------------")
            dangongbamenliliangjishuchushi = SpaDigiX_APPONE_Value
            # -----------------------------------------------------------------------------------------------------------------------
            # 5.1 八门在十二个月的力量
            dangyuebamenzidian = bamenshieryueshuju[yueganzhi[1]]
            bamengeyueliliangdingshu = dangyuebamenzidian[zhishigongbamen[0]]
            SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + bamengeyueliliangdingshu
            # -----------------------------------------------------------------------------------------------------------------------
            # 5.2 八门在九宫中的力量消长
            # -----------------------------------------------------------------------------------------------------------------------
            zhishigongduiyingmenzidian = bamenjiugongliliangxiaozhangshuju[zhishigongdingwei_index]
            bamenjiugongliliangxiaozhangdingshu = zhishigongduiyingmenzidian[zhishigongbamen[0]]
            SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + bamenjiugongliliangxiaozhangdingshu
            # -----------------------------------------------------------------------------------------------------------------------
            # 八门与天盘干关系
            bamentianpanganguanxishuju = {
                "乙": {"开": 0, "休": -1, "生": 0, "伤": -1, "杜": -1, "景": 0, "死": 1, "惊": 1},
                "丙": {"开": 0, "休": 0, "生": 0, "伤": -1, "杜": -1, "景": -1, "死": 0, "惊": 1},
                "丁": {"开": 0, "休": 0, "生": 0, "伤": -1, "杜": -1, "景": -1, "死": 0, "惊": 1},
                "戊": {"开": 0, "休": 1, "生": -1, "伤": 1, "杜": 1, "景": -1, "死": -1, "惊": 0},
                "己": {"开": 0, "休": 1, "生": -1, "伤": 1, "杜": 1, "景": -1, "死": -1, "惊": 0},
                "庚": {"开": -1, "休": 0, "生": -1, "伤": 1, "杜": 1, "景": 1, "死": -1, "惊": -1},
                "辛": {"开": -1, "休": 0, "生": -1, "伤": 1, "杜": 1, "景": 1, "死": -1, "惊": -1},
                "壬": {"开": -1, "休": -1, "生": 1, "伤": 0, "杜": 0, "景": 1, "死": 1, "惊": -1},
                "癸": {"开": -1, "休": -1, "生": 1, "伤": 0, "杜": 0, "景": 1, "死": 1, "惊": -1}
            }
            if len(zhishigongtianpan) == 1 or len(zhishigongtianpan) == 3:
                for key in bamentianpanganguanxishuju:
                    if zhishigongtianpan[-1] == key:
                        SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + bamentianpanganguanxishuju[key][
                            zhishigongbamen[0]]
            else:
                zhishigongtianpanlist = zhishigongtianpan.split("\n")
                for key in bamentianpanganguanxishuju:
                    if zhishigongtianpanlist[0][-1] == key:
                        SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + bamentianpanganguanxishuju[key][
                            zhishigongbamen[0]] / 2
                for key in bamentianpanganguanxishuju:
                    if zhishigongtianpanlist[1][-1] == key:
                        SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + bamentianpanganguanxishuju[key][
                            zhishigongbamen[0]] / 2
            dangongbamenliliangjishuzuizhong = SpaDigiX_APPONE_Value - dangongbamenliliangjishuchushi
            print(f"5 单宫八门力量消长定数：{dangongbamenliliangjishuzuizhong}")
            bamenSDX = SpaDigiX_APPONE_Value - jiuxingSDX
            # -----------------------------------------------------------------------------------------------------------------------
            # 6 八神单宫力量消长定数
            print(
                "----------------------------------------------------------------------------------------------------------")
            # -----------------------------------------------------------------------------------------------------------------------
            # 6.1十二个月八神力量消长
            # -----------------------------------------------------------------------------------------------------------------------
            dangongbashenliliangjishuchushi = SpaDigiX_APPONE_Value
            dangyuebashenzidian = bashenshieryueliliangxiaozhangshuju[yueganzhi[1]]
            bashendangyueliliangxiaozhangdingshu = dangyuebashenzidian[zhishigongbashen]
            if zhishigongbashen == "值符" and (
                    yueganzhi[1] == "丑" or yueganzhi[1] == "辰" or yueganzhi[1] == "未" or yueganzhi[1] == "戌") and (
                    zhishigongdingwei_index == 1 or zhishigongdingwei_index == 7):
                SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value
            else:
                SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + bashendangyueliliangxiaozhangdingshu
                # 6.2 八神在九宫内力量消长
                # -----------------------------------------------------------------------------------------------------------------------
                zhishigongbashenzidian = bashenzaijiugongliliangxiaozhangshuju[zhishigongdingwei_index]
                bashendanggongdingshu = zhishigongbashenzidian[zhishigongbashen]
                SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + bashendanggongdingshu
            dangongbashenliliangxiaozhangjishuzuizhong = SpaDigiX_APPONE_Value - dangongbashenliliangjishuchushi
            # -----------------------------------------------------------------------------------------------------------------------
            print(f"6 单宫八神力量消长定数：{dangongbashenliliangxiaozhangjishuzuizhong}")
            bashenSDX = SpaDigiX_APPONE_Value - bamenSDX
            print(
                "----------------------------------------------------------------------------------------------------------")
            changshengshiergongchushi = SpaDigiX_APPONE_Value
            changshenshiergongshuju = {
                '甲': [1, -1, -2, -1, -1, 1, 2, -1],
                '乙': [1, 1, -2, -1, -1, 1, 2, 2],
                '丙': [0, -1, -1, -2, -2, -1, 1, 2],
                '丁': [2, 1, -1, -2, -2, 1, -1, 0],
                '戊': [0, -1, 1, -1, -2, -1, 1, 2],
                '己': [0, 1, 1, -2, 0, 0, -1, 0],
                '庚': [1, 1, 2, -1, 2, -1, -2, -2],
                '辛': [-1, 1, 2, 1, 2, -1, -2, 0],
                '壬': [-2, -1, 1, 1, 1, -2, -1, -2],
                '癸': [-2, 1, -1, 1, 2, 1, -1, -2],
            }
            nigonghaoduiyingzidian = {0: 0, 1: 5, 2: 2, 3: 3, 5: 7, 6: 6, 7: 1, 8: 4}
            if len(zhishigongtianpan) == 1:
                for key in changshenshiergongshuju:
                    if zhishigongtianpan == key:
                        zhishigongdipanlist = []
                        if len(zhishigongdipan) == 1 or len(zhishigongdipan) == 3:
                            zhishigongdipanlist.append(zhishigongdipan[-1])
                        else:
                            zhishigongdipanganlist = zhishigongdipan.split("\n")
                            for i in range(0, 2):
                                zhishigongdipanlist.append(zhishigongdipanganlist[i][-1])
                        if key == "乙" and "庚" in zhishigongdipanlist:
                            listll = [0, -2, +1, +1, +1, -2, -1, -1]
                            listll_dingwei_index = listll[nigonghaoduiyingzidian[zhishigongdingwei_index]]
                        elif key == "丙" and "辛" in zhishigongdipanlist:
                            listll = [0, +1, 0, -2, -2, 0, -2, 2]
                            listll_dingwei_index = listll[nigonghaoduiyingzidian[zhishigongdingwei_index]]
                        else:
                            listll = changshenshiergongshuju[key]
                            listll_dingwei_index = listll[nigonghaoduiyingzidian[zhishigongdingwei_index]]
                        SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + listll_dingwei_index
            elif len(zhishigongtianpan) == 3:
                zhishigongtianpangan = zhishigongtianpan[2]
                for key in changshenshiergongshuju:
                    if zhishigongtianpangan == key:
                        zhishigongdipanlist = []
                        if len(zhishigongdipan) == 1 or len(zhishigongdipan) == 3:
                            zhishigongdipanlist.append(zhishigongdipan[-1])
                        else:
                            zhishigongdipanganlist = zhishigongdipan.split("\n")
                            for i in range(0, 2):
                                zhishigongdipanlist.append(zhishigongdipanganlist[i][-1])
                        if key == "乙" and "庚" in zhishigongdipanlist:
                            listll = [0, -2, +1, +1, +1, -2, -1, -1]
                            listll_dingwei_index = listll[nigonghaoduiyingzidian[zhishigongdingwei_index]]
                        elif key == "庚" and "乙" in zhishigongdipanlist:
                            listll = [0, -2, +1, +1, +1, -2, -1, -1]
                            listll_dingwei_index = listll[nigonghaoduiyingzidian[zhishigongdingwei_index]]
                        elif key == "丙" and "辛" in zhishigongdipanlist:
                            listll = [0, +1, 0, -2, -2, 0, -2, 2]
                            listll_dingwei_index = listll[nigonghaoduiyingzidian[zhishigongdingwei_index]]
                        elif key == "辛" and "丙" in zhishigongdipanlist:
                            listll = [0, +1, 0, -2, -2, 0, -2, 2]
                            listll_dingwei_index = listll[nigonghaoduiyingzidian[zhishigongdingwei_index]]
                        elif key == "戊" and "癸" in zhishigongdipanlist:
                            listll = [+1, -1, -2, -1, -1, 0, 0, -1]
                            listll_dingwei_index = listll[nigonghaoduiyingzidian[zhishigongdingwei_index]]
                        elif key == "癸" and "戊" in zhishigongdipanlist:
                            listll = [+1, -1, -2, -1, -1, 0, 0, -1]
                            listll_dingwei_index = listll[nigonghaoduiyingzidian[zhishigongdingwei_index]]
                        else:
                            listll = changshenshiergongshuju[key]
                            listll_dingwei_index = listll[nigonghaoduiyingzidian[zhishigongdingwei_index]]
                        SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + listll_dingwei_index
            else:
                zhishigongtianpanganlist = zhishigongtianpan.split("\n")
                for key in changshenshiergongshuju:
                    if zhishigongtianpanganlist[0][-1] == key:
                        zhishigongdipanlist = []
                        if len(zhishigongdipan) == 1 or len(zhishigongdipan) == 3:
                            zhishigongdipanlist.append(zhishigongdipan[-1])
                        else:
                            zhishigongdipanganlist = zhishigongdipan.split("\n")
                            zhishigongdipanlist.append(zhishigongdipanganlist[0][-1])
                        if key == "乙" and "庚" in zhishigongdipanlist:
                            listll1 = [0, -2, +1, +1, +1, -2, -1, -1]
                            listll_dingwei_index1 = listll1[nigonghaoduiyingzidian[zhishigongdingwei_index]]
                        elif key == "庚" and "乙" in zhishigongdipanlist:
                            listll1 = [0, -2, +1, +1, +1, -2, -1, -1]
                            listll_dingwei_index1 = listll1[nigonghaoduiyingzidian[zhishigongdingwei_index]]
                        elif key == "丙" and "辛" in zhishigongdipanlist:
                            listll1 = [0, +1, 0, -2, -2, 0, -2, 2]
                            listll_dingwei_index1 = listll1[nigonghaoduiyingzidian[zhishigongdingwei_index]]
                        elif key == "辛" and "丙" in zhishigongdipanlist:
                            listll1 = [0, +1, 0, -2, -2, 0, -2, 2]
                            listll_dingwei_index1 = listll1[nigonghaoduiyingzidian[zhishigongdingwei_index]]
                        elif key == "戊" and "癸" in zhishigongdipanlist:
                            listll1 = [+1, -1, -2, -1, -1, 0, 0, -1]
                            listll_dingwei_index1 = listll1[nigonghaoduiyingzidian[zhishigongdingwei_index]]
                        elif key == "癸" and "戊" in zhishigongdipanlist:
                            listll1 = [+1, -1, -2, -1, -1, 0, 0, -1]
                            listll_dingwei_index1 = listll1[nigonghaoduiyingzidian[zhishigongdingwei_index]]
                        else:
                            listll1 = changshenshiergongshuju[key]
                            listll_dingwei_index1 = listll1[nigonghaoduiyingzidian[zhishigongdingwei_index]]
                    if zhishigongtianpanganlist[1][-1] == key:
                        zhishigongdipanlist = []
                        if len(zhishigongdipan) == 1 or len(zhishigongdipan) == 3:
                            zhishigongdipanlist.append(zhishigongdipan[-1])
                        else:
                            zhishigongdipanganlist = zhishigongdipan.split("\n")
                            zhishigongdipanlist.append(zhishigongdipanganlist[1][-1])
                        if key == "乙" and "庚" in zhishigongdipanlist:
                            listll2 = [0, -2, +1, +1, +1, -2, -1, -1]
                            listll_dingwei_index2 = listll2[nigonghaoduiyingzidian[zhishigongdingwei_index]]
                        elif key == "庚" and "乙" in zhishigongdipanlist:
                            listll2 = [0, -2, +1, +1, +1, -2, -1, -1]
                            listll_dingwei_index2 = listll2[nigonghaoduiyingzidian[zhishigongdingwei_index]]
                        elif key == "丙" and "辛" in zhishigongdipanlist:
                            listll2 = [0, +1, 0, -2, -2, 0, -2, 2]
                            listll_dingwei_index2 = listll2[nigonghaoduiyingzidian[zhishigongdingwei_index]]
                        elif key == "辛" and "丙" in zhishigongdipanlist:
                            listll2 = [0, +1, 0, -2, -2, 0, -2, 2]
                            listll_dingwei_index2 = listll2[nigonghaoduiyingzidian[zhishigongdingwei_index]]
                        elif key == "戊" and "癸" in zhishigongdipanlist:
                            listll2 = [+1, -1, -2, -1, -1, 0, 0, -1]
                            listll_dingwei_index2 = listll2[nigonghaoduiyingzidian[zhishigongdingwei_index]]
                        elif key == "癸" and "戊" in zhishigongdipanlist:
                            listll2 = [+1, -1, -2, -1, -1, 0, 0, -1]
                            listll_dingwei_index2 = listll2[nigonghaoduiyingzidian[zhishigongdingwei_index]]
                        else:
                            listll2 = changshenshiergongshuju[key]
                            listll_dingwei_index2 = listll2[nigonghaoduiyingzidian[zhishigongdingwei_index]]
                listll_index = (listll_dingwei_index1 + listll_dingwei_index2) / 2
                SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + listll_index
            # 天盘干与月令
            tian_gan_dict = {
                "乙": {
                    "寅": -1, "卯": -1, "辰": -1, "巳": -1, "午": 0, "未": 1, "申": 2, "酉": 2, "戌": 1, "亥": -1,
                    "子": -1,
                    "丑": 1
                },
                "丙": {
                    "寅": -1, "卯": -1, "辰": 0, "巳": -1, "午": -1, "未": -1, "申": 1, "酉": 1, "戌": 0, "亥": 2,
                    "子": 1,
                    "丑": 0
                },
                "丁": {
                    "寅": -1, "卯": -1, "辰": 0, "巳": -1, "午": -1, "未": -1, "申": 1, "酉": 1, "戌": 0, "亥": 1,
                    "子": 1,
                    "丑": 0
                },
                "戊": {
                    "寅": 1, "卯": 0, "辰": -1, "巳": 0, "午": -1, "未": -1, "申": 0, "酉": 0, "戌": -1, "亥": 1,
                    "子": 1,
                    "丑": -1
                },
                "己": {
                    "寅": 0, "卯": 2, "辰": -1, "巳": -1, "午": -1, "未": -1, "申": -1, "酉": 0, "戌": -1, "亥": 1,
                    "子": 1,
                    "丑": -1
                },
                "庚": {
                    "寅": -1, "卯": 1, "辰": 0, "巳": 1, "午": 2, "未": -1, "申": -1, "酉": -1, "戌": -1, "亥": 0,
                    "子": 0,
                    "丑": -1
                },
                "辛": {
                    "寅": 1, "卯": 1, "辰": 0, "巳": 1, "午": 1, "未": -1, "申": -1, "酉": -2, "戌": 0, "亥": 0,
                    "子": 0,
                    "丑": 2
                },
                "壬": {
                    "寅": 0, "卯": -1, "辰": 0, "巳": 0, "午": 0, "未": 1, "申": -2, "酉": -1, "戌": 2, "亥": -1,
                    "子": -1,
                    "丑": 2
                },
                "癸": {
                    "寅": -1, "卯": 0, "辰": 0, "巳": 1, "午": 1, "未": 2, "申": -1, "酉": -1, "戌": 2, "亥": -1,
                    "子": -1,
                    "丑": 0
                }
            }
            if len(zhishigongtianpan) == 1 or len(zhishigongtianpan) == 3:
                for key in tian_gan_dict:
                    if zhishigongtianpan[-1] == key:
                        zhishigongdipanlist = []
                        if len(zhishigongdipan) == 1 or len(zhishigongdipan) == 3:
                            zhishigongdipanlist.append(zhishigongdipan[-1])
                        else:
                            zhishigongdipanganlist = zhishigongdipan.split("\n")
                            for i in range(0, 2):
                                zhishigongdipanlist.append(zhishigongdipanganlist[i][-1])
                        if key == "乙" and "庚" in zhishigongdipanlist:
                            distll = {"子": 0, "丑": -2, "寅": 1, "卯": 1, "辰": -1, "巳": 1, "午": 1, "未": 0,
                                      "申": -1,
                                      "酉": 0, "戌": 0, "亥": 0}
                            changshengshiergongtianganyuevalue = distll[yueganzhi[1]]
                        elif key == "庚" and "乙" in zhishigongdipanlist:
                            distll = {"子": 0, "丑": -2, "寅": 1, "卯": 1, "辰": -1, "巳": 1, "午": 1, "未": 0,
                                      "申": -1,
                                      "酉": 0, "戌": 0, "亥": 0}
                            changshengshiergongtianganyuevalue = distll[yueganzhi[1]]
                        elif key == "丙" and "辛" in zhishigongdipanlist:
                            distll = {"子": -1, "丑": 1, "寅": 0, "卯": 0, "辰": 1, "巳": 2, "午": 1, "未": 0, "申": -1,
                                      "酉": 0, "戌": -1, "亥": -1}
                            changshengshiergongtianganyuevalue = distll[yueganzhi[1]]
                        elif key == "辛" and "丙" in zhishigongdipanlist:
                            distll = {"子": -1, "丑": 1, "寅": 0, "卯": 0, "辰": 1, "巳": 2, "午": 1, "未": 0, "申": -1,
                                      "酉": 0, "戌": -1, "亥": -1}
                            changshengshiergongtianganyuevalue = distll[yueganzhi[1]]
                        elif key == "戊" and "癸" in zhishigongdipanlist:
                            distll = {"子": 1, "丑": 0, "寅": -1, "卯": -1, "辰": 0, "巳": -1, "午": -1, "未": 0,
                                      "申": 1,
                                      "酉": 1, "戌": 1, "亥": 1}
                            changshengshiergongtianganyuevalue = distll[yueganzhi[1]]
                        elif key == "癸" and "戊" in zhishigongdipanlist:
                            distll = {"子": 1, "丑": 0, "寅": -1, "卯": -1, "辰": 0, "巳": -1, "午": -1, "未": 0,
                                      "申": 1,
                                      "酉": 1, "戌": 1, "亥": 1}
                            changshengshiergongtianganyuevalue = distll[yueganzhi[1]]
                        else:
                            distll = tian_gan_dict[key]
                            changshengshiergongtianganyuevalue = distll[yueganzhi[1]]
                SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + changshengshiergongtianganyuevalue
            else:
                zhishigongtianpanganlist = zhishigongtianpan.split("\n")
                for key in tian_gan_dict:
                    if zhishigongtianpanganlist[0][-1] == key:
                        zhishigongdipanlist = []
                        if len(zhishigongdipan) == 1 or len(zhishigongdipan) == 3:
                            zhishigongdipanlist.append(zhishigongdipan[-1])
                        else:
                            zhishigongdipanganlist = zhishigongdipan.split("\n")
                            zhishigongdipanlist.append(zhishigongdipanganlist[0][-1])
                        if key == "乙" and "庚" in zhishigongdipanlist:
                            distll1 = {"子": 0, "丑": -2, "寅": 1, "卯": 1, "辰": -1, "巳": 1, "午": 1, "未": 0,
                                       "申": -1,
                                       "酉": 0,
                                       "戌": 0, "亥": 0}
                            changshengshiergongtianganyuevalue1 = distll1[yueganzhi[1]]
                        elif key == "庚" and "乙" in zhishigongdipanlist:
                            distll1 = {"子": 0, "丑": -2, "寅": 1, "卯": 1, "辰": -1, "巳": 1, "午": 1, "未": 0,
                                       "申": -1,
                                       "酉": 0,
                                       "戌": 0, "亥": 0}
                            changshengshiergongtianganyuevalue1 = distll1[yueganzhi[1]]
                        elif key == "丙" and "辛" in zhishigongdipanlist:
                            distll1 = {"子": -1, "丑": 1, "寅": 0, "卯": 0, "辰": 1, "巳": 2, "午": 1, "未": 0,
                                       "申": -1,
                                       "酉": 0,
                                       "戌": -1, "亥": -1}
                            changshengshiergongtianganyuevalue1 = distll1[yueganzhi[1]]
                        elif key == "辛" and "丙" in zhishigongdipanlist:
                            distll1 = {"子": -1, "丑": 1, "寅": 0, "卯": 0, "辰": 1, "巳": 2, "午": 1, "未": 0,
                                       "申": -1,
                                       "酉": 0,
                                       "戌": -1, "亥": -1}
                            changshengshiergongtianganyuevalue1 = distll1[yueganzhi[1]]
                        elif key == "戊" and "癸" in zhishigongdipanlist:
                            distll1 = {"子": 1, "丑": 0, "寅": -1, "卯": -1, "辰": 0, "巳": -1, "午": -1, "未": 0,
                                       "申": 1,
                                       "酉": 1,
                                       "戌": 1, "亥": 1}
                            changshengshiergongtianganyuevalue1 = distll1[yueganzhi[1]]
                        elif key == "癸" and "戊" in zhishigongdipanlist:
                            distll1 = {"子": 1, "丑": 0, "寅": -1, "卯": -1, "辰": 0, "巳": -1, "午": -1, "未": 0,
                                       "申": 1,
                                       "酉": 1,
                                       "戌": 1, "亥": 1}
                            changshengshiergongtianganyuevalue1 = distll1[yueganzhi[1]]
                        else:
                            distll1 = tian_gan_dict[key]
                            changshengshiergongtianganyuevalue1 = distll1[yueganzhi[1]]
                for key in tian_gan_dict:
                    if zhishigongtianpanganlist[1][-1] == key:
                        zhishigongdipanlist = []
                        if len(zhishigongdipan) == 1 or len(zhishigongdipan) == 3:
                            zhishigongdipanlist.append(zhishigongdipan[-1])
                        else:
                            zhishigongdipanganlist = zhishigongdipan.split("\n")
                            zhishigongdipanlist.append(zhishigongdipanganlist[1][-1])
                        if key == "乙" and "庚" in zhishigongdipanlist:
                            distll12 = {"子": 0, "丑": -2, "寅": 1, "卯": 1, "辰": -1, "巳": 1, "午": 1, "未": 0,
                                        "申": -1,
                                        "酉": 0,
                                        "戌": 0, "亥": 0}
                            changshengshiergongtianganyuevalue12 = distll12[yueganzhi[1]]
                        elif key == "庚" and "乙" in zhishigongdipanlist:
                            distll12 = {"子": 0, "丑": -2, "寅": 1, "卯": 1, "辰": -1, "巳": 1, "午": 1, "未": 0,
                                        "申": -1,
                                        "酉": 0,
                                        "戌": 0, "亥": 0}
                            changshengshiergongtianganyuevalue12 = distll12[yueganzhi[1]]
                        elif key == "丙" and "辛" in zhishigongdipanlist:
                            distll12 = {"子": -1, "丑": 1, "寅": 0, "卯": 0, "辰": 1, "巳": 2, "午": 1, "未": 0,
                                        "申": -1,
                                        "酉": 0,
                                        "戌": -1, "亥": -1}
                            changshengshiergongtianganyuevalue12 = distll12[yueganzhi[1]]
                        elif key == "辛" and "丙" in zhishigongdipanlist:
                            distll12 = {"子": -1, "丑": 1, "寅": 0, "卯": 0, "辰": 1, "巳": 2, "午": 1, "未": 0,
                                        "申": -1,
                                        "酉": 0,
                                        "戌": -1, "亥": -1}
                            changshengshiergongtianganyuevalue12 = distll12[yueganzhi[1]]
                        elif key == "戊" and "癸" in zhishigongdipanlist:
                            distll12 = {"子": 1, "丑": 0, "寅": -1, "卯": -1, "辰": 0, "巳": -1, "午": -1, "未": 0,
                                        "申": 1,
                                        "酉": 1,
                                        "戌": 1, "亥": 1}
                            changshengshiergongtianganyuevalue12 = distll12[yueganzhi[1]]
                        elif key == "癸" and "戊" in zhishigongdipanlist:
                            distll12 = {"子": 1, "丑": 0, "寅": -1, "卯": -1, "辰": 0, "巳": -1, "午": -1, "未": 0,
                                        "申": 1,
                                        "酉": 1,
                                        "戌": 1, "亥": 1}
                            changshengshiergongtianganyuevalue12 = distll12[yueganzhi[1]]
                        else:
                            distll12 = tian_gan_dict[key]
                            changshengshiergongtianganyuevalue12 = distll12[yueganzhi[1]]
                changshengshiergongtianganyuevalue = (
                                                             changshengshiergongtianganyuevalue1 + changshengshiergongtianganyuevalue12) / 2
                SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value + changshengshiergongtianganyuevalue
            changshenshiergongczuizhong = SpaDigiX_APPONE_Value - changshengshiergongchushi
            print(f"7 长生十二宫：{changshenshiergongczuizhong}")
            changshengshiergongSDX = SpaDigiX_APPONE_Value - bashenSDX
            jiaziwuchushi = SpaDigiX_APPONE_Value
            jimen = ["开使", "休使", "生使"]
            if zhishigongtianpan == "甲子戊" and zhishigongbamen in jimen:
                SpaDigiX_APPONE_Value = SpaDigiX_APPONE_Value - 1
                print("甲子戊+三吉门：-1")
            jiaziwusanjimenSDX = SpaDigiX_APPONE_Value - jiaziwuchushi
            # -----------------------------------------------------------------------------------------------------------------------
            print(
                "---------------------------------------------------------------------------------------------------------------\n---------------------------------------------------------------------------------------------------------------\n")
            print(f"全盘初判结果：{quanpanchupanjieguo}")
            print(f"后续结果：{SpaDigiX_APPONE_Value - quanpanchupanjieguo}")
            print(f"定位结果=全盘初判结果+后续结果={SpaDigiX_APPONE_Value}")
            return SpaDigiX_APPONE_Value, neiwaidunSDX, yimaSDX, tongbianyaosuSDX, kongwangSDX, zhichongSDX, jiaziwusanjimenSDX, jixionggejishuzuizhong, dangongtianpangandingshuzuizhong, dangongjiuxingliliangjishuzuizhong, dangongbamenliliangjishuzuizhong, dangongbashenliliangxiaozhangjishuzuizhong, changshenshiergongczuizhong
        year = self.yearEdit.text()
        month = self.monthEdit.text()
        day = self.dayEdit.text()
        hour = self.hourEdit.text()

        # 执行计算，这里只是示例，您需要根据您的实际计算规则来编写代码
        results = getSpaDigiXdingweideshu(year, month, day, hour)
        # 将第一个结果设置到self.largeEdit输出框中
        self.largeEdit.setText(str(results[0]))
        selected_results = results[1:14]
        # 将这些数字设置到十二个输出框中
        for i, result in enumerate(selected_results):
            self.outputEdits[i].setText(str(result))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DateCalculator()
    ex.show()
    sys.exit(app.exec())
