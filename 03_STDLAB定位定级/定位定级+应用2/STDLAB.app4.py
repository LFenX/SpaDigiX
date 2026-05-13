from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QGridLayout, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor
import  pandas as pd
import os
import sys
from functionSpaDigiXAPPONE import getthebasicmessageofnineGrids
def resource_path(relative_path):
    """ 获取资源的绝对路径，用于 PyInstaller 打包后的环境 """
    try:
        # PyInstaller 创建的临时文件夹
        base_path = sys._MEIPASS
    except Exception:
        # 正常的 Python 环境
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
class ExampleApp(QWidget):
    def calculate_string8_matches(self, input_string, data):
        # 读取庄家数列
        zhuangjia_numbers = data['庄家数']

        # 初始化计数器和第九个数字的列表
        match_count = 0
        ninth_digits = []

        # 循环遍历数据，以每九行为一个窗口
        for i in range(len(zhuangjia_numbers) - 8):
            window_string = ''.join(map(str, zhuangjia_numbers[i:i + 8]))
            if window_string == input_string:
                match_count += 1
                ninth_digit = zhuangjia_numbers[i + 8]
                ninth_digits.append(ninth_digit)

        # 计算1的百分比和0的百分比
        one_percentage = ninth_digits.count(1) / len(ninth_digits) * 100 if ninth_digits else 0
        zero_percentage = ninth_digits.count(0) / len(ninth_digits) * 100 if ninth_digits else 0
        return match_count, one_percentage, zero_percentage

    def on_calculate_string8_clicked(self):
        # 获取用户输入的数串8
        input_string8 = self.input_dealer_8.text()
        input_stringHKorMC=self.input_dealer_HKorMC2.text()
        if input_stringHKorMC=="HK":
            # 执行计算
            matches, one_perc, zero_perc = self.calculate_string8_matches(input_string8, self.data1)
            # 显示结果
            self.output_dealer_8_count.setText(str(matches))
            self.output_1_percentage_2.setText(f"{one_perc:.2f}%")
            self.output_0_percentage_2.setText(f"{zero_perc:.2f}%")
        elif input_stringHKorMC=="MC":
            # 执行计算
            matches, one_perc, zero_perc = self.calculate_string8_matches(input_string8, self.data2)
            # 显示结果
            self.output_dealer_8_count.setText(str(matches))
            self.output_1_percentage_2.setText(f"{one_perc:.2f}%")
            self.output_0_percentage_2.setText(f"{zero_perc:.2f}%")

    def calculate_string9_matches(self, input_string, data):
        # 读取庄家数列
        zhuangjia_numbers = data['庄家数']

        # 初始化计数器和第十个数字的列表
        match_count = 0
        tenth_digits = []

        # 循环遍历数据，以每十行为一个窗口
        for i in range(len(zhuangjia_numbers) - 9):
            window_string = ''.join(map(str, zhuangjia_numbers[i:i + 9]))
            if window_string == input_string:
                match_count += 1
                tenth_digit = zhuangjia_numbers[i + 9]
                tenth_digits.append(tenth_digit)

        # 计算1的百分比和0的百分比
        one_percentage = tenth_digits.count(1) / len(tenth_digits) * 100 if tenth_digits else 0
        zero_percentage = tenth_digits.count(0) / len(tenth_digits) * 100 if tenth_digits else 0
        print(tenth_digits)
        return match_count, one_percentage, zero_percentage

    def on_calculate_string9_clicked(self):
        # 获取用户输入的数串9
        input_string9 = self.input_dealer_9.text()
        input_stringHKorMC=self.input_dealer_HKorMC1.text()
        if input_stringHKorMC=="HK":
            # 执行计算
            matches, one_perc, zero_perc = self.calculate_string9_matches(input_string9, self.data1)
            # 显示结果
            self.output_dealer_9_count.setText(str(matches))
            self.output_1_percentage_1.setText(f"{one_perc:.2f}%")
            self.output_0_percentage_1.setText(f"{zero_perc:.2f}%")
        elif input_stringHKorMC=="MC":
            # 执行计算
            matches, one_perc, zero_perc = self.calculate_string9_matches(input_string9, self.data2)
            # 显示结果
            self.output_dealer_9_count.setText(str(matches))
            self.output_1_percentage_1.setText(f"{one_perc:.2f}%")
            self.output_0_percentage_1.setText(f"{zero_perc:.2f}%")


    def __init__(self):
        super().__init__()
        # 使用 resource_path 函数来获取 Excel 文件的正确路径
        data1_path = resource_path('HK2010-2023_dataforAPP1.4.2prediction.xlsx')
        data2_path = resource_path('MC2021-2023_dataforAPP1.4.2prediction.xlsx')

        # 使用获得的路径来读取 Excel 文件
        self.data1 = pd.read_excel(data1_path)
        self.data2 = pd.read_excel(data2_path)
        self.initUI()

    def on_execute_clicked(self):
        # 从输入框读取数据
        year = self.year_input.text()
        month = self.month_input.text()
        day = self.day_input.text()
        branch = self.branch_input.text()
        date_str = f"{year}-{month}-{day}"

        # 调用 calculate_score 函数
        zhuangjia_number, shuanggan, values = self.calculate_score(date_str, branch)

        # 将结果显示在第二行的输出框中
        self.output_01.setText(str(zhuangjia_number))
        self.output_dual_dry.setText(shuanggan)
        self.output_dual_dry_palace.setText(values)

    def calculate_score(self, date_str, branch):
        data = pd.to_datetime(date_str, errors='coerce')
        year, month, day = data.year, data.month, data.day
        for i in range(0, 12):
            riganzhi = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][3]
            shichengganzhi = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][4]
            if riganzhi == "甲子" and shichengganzhi == "甲子":
                for j in range(0, 12):
                    panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][4][0]
                    if panduanwugan == "戊":
                        shuanggan = "戊"
                        hour = 2 * j
                        break
            elif riganzhi == "甲戌" and shichengganzhi == "甲戌":
                for j in range(0, 12):
                    panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][4][0]
                    if panduanwugan == "己":
                        shuanggan = "己"
                        hour = 2 * j
                        break
            elif riganzhi == "甲申" and shichengganzhi == "甲申":
                for j in range(0, 12):
                    panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][4][0]
                    if panduanwugan == "庚":
                        shuanggan = "庚"
                        hour = 2 * j
                        break
            elif riganzhi == "甲寅" and shichengganzhi == "甲子":
                for j in range(0, 12):
                    panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][4][0]
                    if panduanwugan == "癸":
                        shuanggan = "癸"
                        hour = 2 * j
                        break
            elif riganzhi == "甲午" and shichengganzhi == "甲午":
                for j in range(0, 12):
                    panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][4][0]
                    if panduanwugan == "辛":
                        shuanggan = "辛"
                        hour = 2 * j
                        break
            elif riganzhi == "甲辰" and shichengganzhi == "甲辰":
                for j in range(0, 12):
                    panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][4][0]
                    if panduanwugan == "壬":
                        shuanggan = "壬"
                        hour = 2 * j
                        break
            elif riganzhi[0] == "甲" and shichengganzhi[0] == "甲":
                if riganzhi == "甲子":
                    for j in range(0, 12):
                        panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                        if panduanwugan == "戊":
                            shuanggan = "戊"
                            hour = 2 * j
                            break
                elif riganzhi == "甲戌":
                    for j in range(0, 12):
                        panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                        if panduanwugan == "己":
                            shuanggan = "己"
                            hour = 2 * j
                            break
                elif riganzhi == "甲辰":
                    for j in range(0, 12):
                        panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                        if panduanwugan == "壬":
                            shuanggan = "壬"
                            hour = 2 * j
                            break
                elif riganzhi == "甲寅":
                    for j in range(0, 12):
                        panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                        if panduanwugan == "癸":
                            shuanggan = "癸"
                            hour = 2 * j
                            break
                elif riganzhi == "甲申":
                    for j in range(0, 12):
                        panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                        if panduanwugan == "庚":
                            shuanggan = "庚"
                            hour = 2 * j
                            break
                elif riganzhi == "甲午":
                    for j in range(0, 12):
                        panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                        if panduanwugan == "辛":
                            shuanggan = "辛"
                            hour = 2 * j
                            break
            else:
                if riganzhi[0] == shichengganzhi[0]:
                    shuanggan = riganzhi[0]
                    hour = 2 * i
                    break
        fanhuixinxi = getthebasicmessageofnineGrids(year, month, day, hour)  # 通过应用0获得排盘的基本信息
        ninegridsbasicmessage = fanhuixinxi[0]  # 九宫基本信息
        yinyangdun_ganzhi = fanhuixinxi[1]  # 阴阳遁和干支信息
        for i in range(0, 9):
            if i == 4:
                pass
            else:
                tianpanganshuju = ninegridsbasicmessage[i]["天盘"]
                if len(tianpanganshuju) == 1 or len(tianpanganshuju) == 3:
                    if shuanggan == tianpanganshuju[-1]:
                        zhishigongdingwei_index = i
                else:
                    tianpanganshuju_list = tianpanganshuju.split("\n")
                    if shuanggan == tianpanganshuju_list[0][-1] or shuanggan == tianpanganshuju_list[1][-1]:
                        zhishigongdingwei_index = i
        if zhishigongdingwei_index == 0:
            values = "坎一"
        elif zhishigongdingwei_index == 1:
            values = "坤二"
        elif zhishigongdingwei_index == 2:
            values = "震三"
        elif zhishigongdingwei_index == 3:
            values = "巽四"
        elif zhishigongdingwei_index == 5:
            values = "乾六"
        elif zhishigongdingwei_index == 6:
            values = "兑七"
        elif zhishigongdingwei_index == 7:
            values = "艮八"
        elif zhishigongdingwei_index == 8:
            values = "离九"

        dizhi = branch
        # 根据 values 和地支的组合判断庄家数
        if (values == "坎一" and dizhi in ["酉", "戌", "亥", "子", "丑", "寅"]) or \
                (values == "坤二" and dizhi in ["巳", "午", "未", "申", "酉", "戌"]) or \
                (values == "震三" and dizhi in ["子", "丑", "寅", "卯", "辰", "巳"]) or \
                (values == "巽四" and dizhi in ["寅", "卯", "辰", "巳", "午", "未"]) or \
                (values == "乾六" and dizhi in ["申", "酉", "戌", "亥", "子", "丑"]) or \
                (values == "兑七" and dizhi in ["午", "未", "申", "酉", "戌", "亥"]) or \
                (values == "艮八" and dizhi in ["亥", "子", "丑", "寅", "卯", "辰"]) or \
                (values == "离九" and dizhi in ["卯", "辰", "巳", "午", "未", "申"]):
            zhuangjia_number = 0
        else:
            zhuangjia_number = 1
        print(f"日期：{year}-{month}-{day}-{hour},地支: {dizhi}, 双干宫: {values},庄家数：{zhuangjia_number}")
        print("----------------------------------------------------------------------")
        return zhuangjia_number, shuanggan, values


    def initUI(self):
        # 主垂直布局
        main_layout = QVBoxLayout(self)

        # 第一行
        row1_layout = QHBoxLayout()
        self.year_input = QLineEdit()

        self.month_input = QLineEdit()

        self.day_input = QLineEdit()

        self.branch_input = QLineEdit()

        self.execute_button = QPushButton("执行")

        # 设置输入框内容居中
        self.year_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.month_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.day_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.branch_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # 添加标签
        row1_layout.addWidget(self.year_input)
        row1_layout.addWidget(QLabel("年"))
        row1_layout.addWidget(self.month_input)
        row1_layout.addWidget(QLabel("月"))
        row1_layout.addWidget(self.day_input)
        row1_layout.addWidget(QLabel("日"))
        row1_layout.addWidget(self.branch_input)
        row1_layout.addWidget(QLabel("地支"))
        row1_layout.addWidget(self.execute_button)
        # “执行”按钮的点击事件
        self.execute_button.clicked.connect(self.on_execute_clicked)

        # 第二行
        row2_layout = QHBoxLayout()
        self.output_01 = QLineEdit()
        self.output_01.setPlaceholderText("01输出")
        self.output_dual_dry = QLineEdit()
        self.output_dual_dry.setPlaceholderText("双干输出")
        self.output_dual_dry_palace = QLineEdit()
        self.output_dual_dry_palace.setPlaceholderText("双干宫输出")
        # 将输出框设置为只读
        self.output_01.setReadOnly(True)
        self.output_dual_dry.setReadOnly(True)
        self.output_dual_dry_palace.setReadOnly(True)
        # 设置输出框内容居中
        self.output_01.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.output_dual_dry.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.output_dual_dry_palace.setAlignment(Qt.AlignmentFlag.AlignCenter)

        row2_layout.addWidget(self.output_01)
        row2_layout.addWidget(self.output_dual_dry)
        row2_layout.addWidget(self.output_dual_dry_palace)
        # 网格布局
        grid_layout = QGridLayout()
        self.input_dealer_8 = QLineEdit()
        self.input_dealer_8.setPlaceholderText("庄家数串8")
        self.input_dealer_HKorMC1 = QLineEdit()
        self.input_dealer_HKorMC1.setPlaceholderText("HK/MC")
        self.input_dealer_9 = QLineEdit()
        self.input_dealer_9.setPlaceholderText("庄家数串9")
        self.input_dealer_HKorMC2 = QLineEdit()
        self.input_dealer_HKorMC2.setPlaceholderText("HK/MC")
        self.button_dealer_8_result = QPushButton("获取数串8结果")
        self.button_dealer_8_result.clicked.connect(self.on_calculate_string8_clicked)
        self.button_dealer_9_result = QPushButton("获取数串9结果")
        # 设置“获取数串9结果”按钮的点击事件
        self.button_dealer_9_result.clicked.connect(self.on_calculate_string9_clicked)
        self.output_dealer_8_count = QLineEdit()
        self.output_dealer_8_count.setPlaceholderText("数串8次数")
        self.output_dealer_9_count = QLineEdit()
        self.output_dealer_9_count.setPlaceholderText("数串9次数")

        # 创建两个“1的百分比”输出框和两个“0的百分比”输出框
        self.output_1_percentage_1 = QLineEdit()
        self.output_1_percentage_1.setPlaceholderText("1的百分比")
        self.output_1_percentage_2 = QLineEdit()
        self.output_1_percentage_2.setPlaceholderText("1的百分比")
        self.output_0_percentage_1 = QLineEdit()
        self.output_0_percentage_1.setPlaceholderText("0的百分比")
        self.output_0_percentage_2 = QLineEdit()
        self.output_0_percentage_2.setPlaceholderText("0的百分比")

        # 将输出框设置为只读
        self.output_dealer_8_count.setReadOnly(True)
        self.output_dealer_9_count.setReadOnly(True)
        self.output_1_percentage_1.setReadOnly(True)
        self.output_1_percentage_2.setReadOnly(True)
        self.output_0_percentage_1.setReadOnly(True)
        self.output_0_percentage_2.setReadOnly(True)

        # 设置网格布局的输入输出框内容居中
        self.input_dealer_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_dealer_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_dealer_HKorMC1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_dealer_HKorMC2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.output_dealer_8_count.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.output_dealer_9_count.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.output_1_percentage_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.output_1_percentage_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.output_0_percentage_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.output_0_percentage_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # 添加元素到网格布局
        grid_layout.addWidget(self.input_dealer_9, 0, 0)
        grid_layout.addWidget(self.input_dealer_HKorMC1, 0, 1)
        grid_layout.addWidget(self.input_dealer_8, 0, 2)
        grid_layout.addWidget(self.input_dealer_HKorMC2, 0, 3)
        grid_layout.addWidget(self.button_dealer_9_result, 1, 0, 1, 2)  # 横跨两列
        grid_layout.addWidget(self.button_dealer_8_result, 1, 2, 1, 2)  # 横跨两列
        grid_layout.addWidget(self.output_dealer_9_count, 2, 0, 1, 2)  # 横跨两列
        grid_layout.addWidget(self.output_dealer_8_count, 2, 2, 1, 2)  # 横跨两列
        grid_layout.addWidget(self.output_1_percentage_1, 3, 0, 1, 2)  # 横跨两列
        grid_layout.addWidget(self.output_1_percentage_2, 3, 2, 1, 2)  # 横跨两列
        grid_layout.addWidget(self.output_0_percentage_1, 4, 0, 1, 2)  # 横跨两列
        grid_layout.addWidget(self.output_0_percentage_2, 4, 2, 1, 2)  # 横跨两列

        # 添加行到主布局
        main_layout.addLayout(row1_layout)
        main_layout.addLayout(row2_layout)
        main_layout.addLayout(grid_layout)

        # 设置窗口属性
        self.setLayout(main_layout)
        self.setWindowTitle('STDLAB.app_4')

# 创建应用程序和主窗口
app = QApplication([])
ex = ExampleApp()
ex.show()
# 运行应用程序
app.exec()
