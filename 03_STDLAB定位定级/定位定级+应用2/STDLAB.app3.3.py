from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, \
    QPushButton, QSizePolicy
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import math


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("STDLAB.app3_G3&G4_12时辰")  # 设置窗口标题
        self.output_rows = [[], [],[]]  # 保存输出框的引用
        self.final_score_rows = [[], [],[]]  # 保存最终得数的引用

        # 创建主窗口的中心部件和布局
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # 定义宋体加粗字体
        bold_song_font = QFont("宋体", pointSize=14, weight=QFont.Weight.Bold)

        # 第一行：标签
        self.label_hk = QLabel("香港定级G3-12时辰-HK(三级)", self)
        self.label_hk.setFont(bold_song_font)
        self.label_hk.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.label_hk)

        # 第二行：三个输入框及标签

        self.input_row_1 = self.create_input_row(main_layout, ["年", "月", "日","时"], self.calculate_results_1, 0)

        # 第三行：四个输出框及标签
        self.create_output_row(main_layout, ["日干：", "时干：","值符：", "值使：", "生门："], 0)

        # 最终得数行
        self.create_final_score_row(main_layout, 0)

        # 第四行：标签
        self.label_mc = QLabel("澳门定级G3-12时辰-MC(三级)", self)
        self.label_mc.setFont(bold_song_font)
        self.label_mc.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.label_mc)

        # 第五行：同第二行
        # 第五行：同第二行
        self.input_row_2 = self.create_input_row(main_layout, ["年", "月", "日","时"], self.calculate_results_2, 1)

        # 第六行：同第三行
        self.create_output_row(main_layout, ["日干：", "时干：", "值符：", "值使：", "生门："], 1)

        # 最终得数行（第二组）
        self.create_final_score_row(main_layout, 1)

        # MCG4
        self.label_mc_2 = QLabel("澳门定级G4-12时辰-MC(二级)", self)
        self.label_mc_2.setFont(bold_song_font)
        self.label_mc_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.label_mc_2)
        self.input_row_3 = self.create_input_row(main_layout, ["年", "月", "日","时"], self.calculate_results_3, 2)
        self.create_output_row(main_layout, ["日干：", "时干：", "值符：", "值使：", "生门："], 2)
        self.create_final_score_row(main_layout, 2)


    def create_input_row(self, layout, labels, result_func, group_index):
        row_layout = QHBoxLayout()
        line_edits = []
        for label_text in labels:
            line_edit = QLineEdit(self)
            line_edit.setFont(QFont("Arial", 15))
            line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)  # 居中文本
            line_edit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
            line_edits.append(line_edit)
            label = QLabel(label_text, self)
            row_layout.addWidget(line_edit)
            row_layout.addWidget(label)
        get_result_button = QPushButton("获取定级结果", self)
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
        get_result_button.setStyleSheet(button_style)
        get_result_button.clicked.connect(lambda: result_func(line_edits))
        clear_button = QPushButton("清除内容", self)
        button_style2 = """
                           QPushButton {
                               background-color: rgb(173, 216, 230);
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
        clear_button.setStyleSheet(button_style2)
        clear_button.clicked.connect(lambda: self.clear_inputs(line_edits, group_index))
        row_layout.addWidget(get_result_button)
        row_layout.addWidget(clear_button)
        layout.addLayout(row_layout)
        return line_edits

    def calculate_results_1(self, line_edits):
        # HKG3
        year, month, day,hour = [edit.text() for edit in line_edits]
        from functionSpadigiX_GetvaluefromFIVEthreeG_3_1_HK import gettheSpaDigiX_value
        from functionSpaDigiXAPPONE import getthebasicmessageofnineGrids
        riganzhi = getthebasicmessageofnineGrids(year, month, day, hour)[1][3]
        shichengganzhi = getthebasicmessageofnineGrids(year, month, day, hour)[1][4]
        if riganzhi == "甲子":
            rigan = "戊"
        elif riganzhi == "甲戌":
            rigan = "己"
        elif riganzhi == "甲辰":
            rigan = "壬"
        elif riganzhi == "甲寅":
            rigan = "癸"
        elif riganzhi == "甲申":
            rigan = "庚"
        elif riganzhi == "甲午":
            rigan = "辛"
        else:
            rigan = riganzhi[0]

        if shichengganzhi == "甲子":
            shigan = "戊"
        elif shichengganzhi == "甲戌":
            shigan = "己"
        elif shichengganzhi == "甲辰":
            shigan = "壬"
        elif shichengganzhi == "甲寅":
            shigan = "癸"
        elif shichengganzhi == "甲申":
            shigan = "庚"
        elif shichengganzhi == "甲午":
            shigan = "辛"
        else:
            shigan = shichengganzhi[0]
        # 时干
        print("SDXAPP3")
        print("时干：")
        shigandeshu = gettheSpaDigiX_value(year, month, day, hour, "时干", shigan, rigan)
        print(f"时干得数：{shigandeshu}")
        print(
            "---------------------------------------------------------------------------------------------------------------\n---------------------------------------------------------------------------------------------------------------\n")
        # 日干
        print("日干：")
        rigandeshu = gettheSpaDigiX_value(year, month, day, hour, "日干", shigan, rigan)
        print(f"日干得数：{rigandeshu}")
        print(
            "---------------------------------------------------------------------------------------------------------------\n---------------------------------------------------------------------------------------------------------------\n")
        # 值符
        print("值符：")
        zhifudeshu = gettheSpaDigiX_value(year, month, day, hour, "值符", shigan, rigan)
        print(f"值符得数：{zhifudeshu}")
        print(
            "---------------------------------------------------------------------------------------------------------------\n---------------------------------------------------------------------------------------------------------------\n")
        # 值使
        print("值使：")
        zhishideshu = gettheSpaDigiX_value(year, month, day, hour, "值使", shigan, rigan)
        print(f"值使得数：{zhishideshu}")
        print(
            "---------------------------------------------------------------------------------------------------------------\n---------------------------------------------------------------------------------------------------------------\n")
        # 生门
        print("生门：")
        shengmendeshu = gettheSpaDigiX_value(year, month, day, hour, "生门", shigan, rigan)
        print(f"生门得数：{shengmendeshu}")
        print(
            "---------------------------------------------------------------------------------------------------------------\n---------------------------------------------------------------------------------------------------------------\n")
        print(
            "-----------------------------------------------------------------------------------------------------------------")
        SpaDigiX_dingji_value = (shigandeshu + rigandeshu + zhifudeshu + zhishideshu + shengmendeshu) / 5
        while SpaDigiX_dingji_value < 0:
            SpaDigiX_dingji_value = SpaDigiX_dingji_value + 4
        while SpaDigiX_dingji_value > 4:
            SpaDigiX_dingji_value = SpaDigiX_dingji_value - 4
        print(f"G3-1HK定级结果：{SpaDigiX_dingji_value}")
        results = [rigandeshu,shigandeshu, zhifudeshu, zhishideshu, shengmendeshu, round(SpaDigiX_dingji_value,3)]
        self.fill_outputs(results, 0)

    def calculate_results_2(self, line_edits):
        # MCG3
        year, month, day,hour= [edit.text() for edit in line_edits]
        from functionSpadigiX_GetvaluefromFIVEthreeG_3_1_MC import gettheSpaDigiX_value
        from functionSpaDigiXAPPONE import getthebasicmessageofnineGrids
        riganzhi = getthebasicmessageofnineGrids(year, month, day, hour)[1][3]
        shichengganzhi = getthebasicmessageofnineGrids(year, month, day, hour)[1][4]
        if riganzhi == "甲子":
            rigan = "戊"
        elif riganzhi == "甲戌":
            rigan = "己"
        elif riganzhi == "甲辰":
            rigan = "壬"
        elif riganzhi == "甲寅":
            rigan = "癸"
        elif riganzhi == "甲申":
            rigan = "庚"
        elif riganzhi == "甲午":
            rigan = "辛"
        else:
            rigan = riganzhi[0]

        if shichengganzhi == "甲子":
            shigan = "戊"
        elif shichengganzhi == "甲戌":
            shigan = "己"
        elif shichengganzhi == "甲辰":
            shigan = "壬"
        elif shichengganzhi == "甲寅":
            shigan = "癸"
        elif shichengganzhi == "甲申":
            shigan = "庚"
        elif shichengganzhi == "甲午":
            shigan = "辛"
        else:
            shigan = shichengganzhi[0]
        # 时干
        print("SDXAPP3")
        print("时干：")
        shigandeshu = gettheSpaDigiX_value(year, month, day, hour, "时干", shigan, rigan)
        print(f"时干得数：{shigandeshu}")
        print(
            "---------------------------------------------------------------------------------------------------------------\n---------------------------------------------------------------------------------------------------------------\n")
        # 日干
        print("日干：")
        rigandeshu = gettheSpaDigiX_value(year, month, day, hour, "日干", shigan, rigan)
        print(f"日干得数：{rigandeshu}")
        print(
            "---------------------------------------------------------------------------------------------------------------\n---------------------------------------------------------------------------------------------------------------\n")
        # 值符
        print("值符：")
        zhifudeshu = gettheSpaDigiX_value(year, month, day, hour, "值符", shigan, rigan)
        print(f"值符得数：{zhifudeshu}")
        print(
            "---------------------------------------------------------------------------------------------------------------\n---------------------------------------------------------------------------------------------------------------\n")
        # 值使
        print("值使：")
        zhishideshu = gettheSpaDigiX_value(year, month, day, hour, "值使", shigan, rigan)
        print(f"值使得数：{zhishideshu}")
        print(
            "---------------------------------------------------------------------------------------------------------------\n---------------------------------------------------------------------------------------------------------------\n")
        # 生门
        print("生门：")
        shengmendeshu = gettheSpaDigiX_value(year, month, day, hour, "生门", shigan, rigan)
        print(f"生门得数：{shengmendeshu}")
        print(
            "---------------------------------------------------------------------------------------------------------------\n---------------------------------------------------------------------------------------------------------------\n")
        print(
            "-----------------------------------------------------------------------------------------------------------------")
        SpaDigiX_dingji_value = (shigandeshu + rigandeshu + zhifudeshu + zhishideshu + shengmendeshu) / 5
        while SpaDigiX_dingji_value < 0:
            SpaDigiX_dingji_value = SpaDigiX_dingji_value + 4
        while SpaDigiX_dingji_value > 4:
            SpaDigiX_dingji_value = SpaDigiX_dingji_value - 4
        print(f"G3-1MC定级结果：{SpaDigiX_dingji_value}")

        results = [rigandeshu,shigandeshu, zhifudeshu, zhishideshu, shengmendeshu, round(SpaDigiX_dingji_value,3)]
        self.fill_outputs(results, 1)
    def calculate_results_3(self, line_edits):
        # MCG4
        year, month, day,hour = [edit.text() for edit in line_edits]
        from functionSpadigiX_GetvaluefromFIVEthreeG_4_1_MC import gettheSpaDigiX_value
        from functionSpaDigiXAPPONE import getthebasicmessageofnineGrids
        riganzhi = getthebasicmessageofnineGrids(year, month, day, hour)[1][3]
        shichengganzhi = getthebasicmessageofnineGrids(year, month, day, hour)[1][4]
        if riganzhi == "甲子":
            rigan = "戊"
        elif riganzhi == "甲戌":
            rigan = "己"
        elif riganzhi == "甲辰":
            rigan = "壬"
        elif riganzhi == "甲寅":
            rigan = "癸"
        elif riganzhi == "甲申":
            rigan = "庚"
        elif riganzhi == "甲午":
            rigan = "辛"
        else:
            rigan = riganzhi[0]

        if shichengganzhi == "甲子":
            shigan = "戊"
        elif shichengganzhi == "甲戌":
            shigan = "己"
        elif shichengganzhi == "甲辰":
            shigan = "壬"
        elif shichengganzhi == "甲寅":
            shigan = "癸"
        elif shichengganzhi == "甲申":
            shigan = "庚"
        elif shichengganzhi == "甲午":
            shigan = "辛"
        else:
            shigan = shichengganzhi[0]

        # 时干
        print("SDXAPP3")
        print("时干：")
        shigandeshu = gettheSpaDigiX_value(year, month, day, hour, "时干", shigan, rigan)
        print(f"时干得数：{shigandeshu}")
        print(
            "---------------------------------------------------------------------------------------------------------------\n---------------------------------------------------------------------------------------------------------------\n")
        # 日干
        print("日干：")
        rigandeshu = gettheSpaDigiX_value(year, month, day, hour, "日干", shigan, rigan)
        print(f"日干得数：{rigandeshu}")
        print(
            "---------------------------------------------------------------------------------------------------------------\n---------------------------------------------------------------------------------------------------------------\n")
        # 值符
        print("值符：")
        zhifudeshu = gettheSpaDigiX_value(year, month, day, hour, "值符", shigan, rigan)
        print(f"值符得数：{zhifudeshu}")
        print(
            "---------------------------------------------------------------------------------------------------------------\n---------------------------------------------------------------------------------------------------------------\n")
        # 值使
        print("值使：")
        zhishideshu = gettheSpaDigiX_value(year, month, day, hour, "值使", shigan, rigan)
        print(f"值使得数：{zhishideshu}")
        print(
            "---------------------------------------------------------------------------------------------------------------\n---------------------------------------------------------------------------------------------------------------\n")
        # 生门
        print("生门：")
        shengmendeshu = gettheSpaDigiX_value(year, month, day, hour, "生门", shigan, rigan)
        print(f"生门得数：{shengmendeshu}")
        print(
            "---------------------------------------------------------------------------------------------------------------\n---------------------------------------------------------------------------------------------------------------\n")
        print(
            "-----------------------------------------------------------------------------------------------------------------")
        SpaDigiX_dingji_value = (shigandeshu + rigandeshu + zhifudeshu + zhishideshu + shengmendeshu) / 5
        while SpaDigiX_dingji_value < 0:
            SpaDigiX_dingji_value = SpaDigiX_dingji_value + 4
        while SpaDigiX_dingji_value > 4:
            SpaDigiX_dingji_value = SpaDigiX_dingji_value - 4
        print(f"G4-1MC定级结果：{SpaDigiX_dingji_value}")
        results = [rigandeshu,shigandeshu, zhifudeshu, zhishideshu, shengmendeshu, round(SpaDigiX_dingji_value,3)]
        self.fill_outputs(results, 2)
    def fill_outputs(self, results, group_index):
        for i, result in enumerate(results):
            self.output_rows[group_index][i].setText(str(result))
        final_score = math.ceil(results[-1])
        print(f"定级数：{final_score}")
        adjacent_numbers = self.get_adjacent_numbers(final_score)
        for i, num in enumerate(adjacent_numbers):
            self.final_score_rows[group_index][i].setText(self.number_to_chinese(num))

    def get_adjacent_numbers(self, num):
        adjacent = {1: [4, 1, 2], 2: [1, 2, 3], 3: [2, 3, 4], 4: [3, 4, 1]}
        return adjacent.get(num, [])

    def number_to_chinese(self, num):
        chinese_numbers = {1: "一", 2: "二", 3: "三", 4: "四"}
        return chinese_numbers.get(num, "")

    def create_output_row(self, layout, labels, group_index):
        row_layout = QHBoxLayout()
        for label_text in labels:
            line_edit = QLineEdit(self)
            line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)  # 居中文本
            line_edit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
            line_edit.setReadOnly(True)
            label = QLabel(label_text, self)
            row_layout.addWidget(label)
            row_layout.addWidget(line_edit)
            self.output_rows[group_index].append(line_edit)
        layout.addLayout(row_layout)

    def create_final_score_row(self, layout, group_index):
        row_layout = QHBoxLayout()

        # 最终得数标签和输出框
        final_score_label = QLabel("最终得数：", self)
        final_score_edit = QLineEdit(self)
        final_score_edit.setFont(QFont("KaiTi", 14, QFont.Weight.Bold))  # 设置加粗字体
        final_score_edit.setMinimumSize(200, 40)  # 设置最小尺寸
        final_score_edit.setMaximumSize(200, 40)  # 设置最大尺寸
        final_score_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)  # 居中文本
        final_score_edit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        final_score_edit.setReadOnly(True)
        row_layout.addWidget(final_score_label)
        row_layout.addWidget(final_score_edit)
        self.output_rows[group_index].append(final_score_edit)
        # 定级结果标签
        result_label = QLabel("定级结果：", self)
        row_layout.addWidget(result_label)
        # 三个并列的输出框
        for _ in range(3):
            line_edit = QLineEdit(self)
            line_edit.setAlignment(Qt.AlignmentFlag.AlignCenter)  # 居中文本
            line_edit.setFont(QFont("KaiTi", 18, QFont.Weight.Bold))  # 设置加粗字体
            line_edit.setMinimumSize(200, 40)  # 设置最小尺寸
            line_edit.setMaximumSize(200, 40)  # 设置最大尺寸
            line_edit.setStyleSheet("color: red; background-color: lightyellow;")  # 设置文本颜色为红色
            line_edit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
            line_edit.setReadOnly(True)
            row_layout.addWidget(line_edit)
            self.final_score_rows[group_index].append(line_edit)

        layout.addLayout(row_layout)

    def clear_inputs(self, line_edits, group_index):
        # 清除输入框内容
        for line_edit in line_edits:
            line_edit.clear()

        # 清除相关的输出框内容
        for output_edit in self.output_rows[group_index]:
            output_edit.clear()
        for output_edit in self.final_score_rows[group_index]:
            output_edit.clear()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()