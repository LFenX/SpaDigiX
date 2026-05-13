from PyQt6.QtWidgets import QMessageBox,QComboBox,QApplication,QGraphicsDropShadowEffect, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QGridLayout, QLabel
from PyQt6.QtCore import Qt
import os
import shutil
import sys
from PyQt6.QtGui import QPalette, QColor
import  pandas as pd
from datetime import  datetime
import os
import sys
from functionSpaDigiXAPPONE import getthebasicmessageofnineGrids
import random
from PyQt6.QtGui import QFont
import sys
from PyQt6.QtWidgets import QMainWindow,QTextEdit,QApplication, QWidget, QHBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox,QDialog
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QTimer, QDateTime
import pandas as pd
from datetime import datetime,time,timedelta
class DetailWindow(QDialog):
    def __init__(self, parent, content):
        super().__init__(parent)
        self.setWindowTitle("数串源信息")
        self.resize(700, 450)

        layout = QVBoxLayout(self)
        text_edit = QTextEdit(self)
        text_edit.setReadOnly(True)
        text_edit.setText(content)
        layout.addWidget(text_edit)
class SubWindow(QMainWindow):
    def __init__(self, match_data):
        super().__init__()
        self.setWindowTitle("Matched Data Display")
        self.setGeometry(100, 100, 800, 600)

        # 创建并设置文本框
        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(10, 10, 780, 580)
        self.text_edit.setReadOnly(True)
        self.text_edit.setText(match_data)
def open_sub_window(main_window, matches):
    formatted_data = ""
    for index, match in enumerate(matches):
        formatted_data += f"第 {index + 1} 个匹配数串：\n"

        # 添加列名称，每列宽度为10个字符，居中对齐
        column_names = "{:^22}{:^12}{:^8}{:^6}{:^8}{:^6}".format("日期", "特", "地支", "庄家数", "双干", "双干宫")
        formatted_data += column_names + "\n"

        for row_index, row in match.iterrows():
            # 格式化每一行数据，确保居中对齐
            date_str = row['日期'] if isinstance(row['日期'], str) else row['日期'].strftime('%Y-%m-%d')
            # 处理 '特' 列的数据，确保为两位数字
            te_str = str(int(row['特'])).zfill(2)
            row_data = "{:^20}{:^12}{:^10}{:^10}{:^10}{:^10}".format(
                date_str, te_str, row['地支'], row['庄家数'], row['双干'], row['双干宫']
            )
            if row_index == match.index[-1]:  # 检查是否为最后一行
                row_data += " （预测行）"
            formatted_data += row_data + "\n"

        formatted_data += "\n"

    # 创建并显示副窗口
    sub_window = SubWindow(formatted_data)
    sub_window.show()

    # 将副窗口存储在主窗口的属性中，防止被Python的垃圾回收机制回收
    main_window.sub_window = sub_window




class InputWithComboBox(QWidget):
    def __init__(self, options=None):
        super().__init__()
        base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
        # 访问数据文件的路径
        image_path1 = os.path.join(base_path, 'XLJT.png')

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
        # 增加数字
        current_index = self.combo_box.currentIndex()
        if current_index < self.combo_box.count() - 1:
            self.combo_box.setCurrentIndex(current_index + 1)

    def decrement_value(self):
        # 减少数字
        current_index = self.combo_box.currentIndex()
        if current_index > 0:
            self.combo_box.setCurrentIndex(current_index - 1)

def resource_path(relative_path):
    """ 获取资源的绝对路径，用于 PyInstaller 打包后的环境 """
    try:
        # PyInstaller 创建的临时文件夹
        base_path = sys._MEIPASS
    except Exception:
        # 正常的 Python 玐境
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def get_storage_path():
    """ 获取存储路径 """
    d_drive = 'D:\\'
    c_drive = 'C:\\'
    folder_name = 'LFendata'

    if os.path.exists(d_drive):
        storage_path = os.path.join(d_drive, folder_name)
    else:
        storage_path = os.path.join(c_drive, folder_name)

    if not os.path.exists(storage_path):
        os.makedirs(storage_path)

    return storage_path

def copy_to_storage_location(relative_path):
    """ 将文件复制到存储位置 """
    storage_path = get_storage_path()
    target_path = os.path.join(storage_path, relative_path)

    # 如果目标路径上的文件不存在，则复制
    if not os.path.exists(target_path):
        source_path = resource_path(relative_path)
        shutil.copy(source_path, target_path)

    return target_path

class ExampleApp(QWidget):
    def calculate_string8_matches(self, input_string, data):
        # 读取庄家数列
        zhuangjia_numbers = data['庄家数']

        # 初始化计数器、第九个数字的列表和匹配数据列表
        match_count = 0
        ninth_digits = []
        matched_details = []

        # 循环遍历数据，以每九行为一个窗口
        for i in range(len(zhuangjia_numbers) - 8):
            window_string = ''.join(map(str, zhuangjia_numbers[i:i + 8]))
            if window_string == input_string:
                match_count += 1
                ninth_digit = zhuangjia_numbers[i + 8]
                ninth_digits.append(ninth_digit)

                # 收集匹配的详细信息
                matched_row = data.iloc[i:i + 9]  # 包括第九行
                matched_details.append(matched_row)

        # 计算1的百分比和0的百分比
        one_percentage = ninth_digits.count(1) / len(ninth_digits) * 100 if ninth_digits else 0
        zero_percentage = ninth_digits.count(0) / len(ninth_digits) * 100 if ninth_digits else 0

        return match_count, one_percentage, zero_percentage, matched_details

    def on_calculate_string8_clicked(self):
        # 获取用户输入的数串8
        input_string8 = self.input_dealer_8.text()
        input_stringHKorMC = self.input_dealer_HKorMC2.text()
        # 如果 input_string9 为空，则从 self.jutishuchuan 获取后9位数字
        jutishuchuan_text = self.jutishuchuan.text()  # 获取数串文本
        if jutishuchuan_text:
            if len(jutishuchuan_text) >= 8:
                input_string8 = jutishuchuan_text[-8:]  # 提取后10位数字
                self.input_dealer_8.setText(input_string8)  # 填入数串
            else:
                self.output_dealer_8_count.setText("数串长度不足8位")
                return
        # 使用获得的路径来读取 Excel 文件
        self.data1 = pd.read_excel(self.data1_path)
        self.data2 = pd.read_excel(self.data2_path)
        if input_stringHKorMC == "HK":
            # 执行计算
            matches, one_perc, zero_perc, matched_details = self.calculate_string8_matches(input_string8, self.data1)
        elif input_stringHKorMC == "MC":
            # 执行计算
            matches, one_perc, zero_perc, matched_details = self.calculate_string8_matches(input_string8, self.data2)
        else:
            # 如果输入不是"HK"或"MC"，显示错误或返回
            self.output_dealer_8_count.setText("请输入城市")
            return

        # 显示基础结果
        self.output_dealer_8_count.setText(str(matches))
        self.output_1_percentage_2.setText(f"{one_perc:.2f}%")
        self.output_0_percentage_2.setText(f"{zero_perc:.2f}%")

        # 如果有匹配的数据，可以在此处处理或显示 matched_details
        # 例如，打开一个新窗口来显示详细信息
        if matched_details:
            open_sub_window(self, matched_details)  # 假设您已经定义了这个函数

    def calculate_string9_matches(self, input_string, data):
        # 读取庄家数列
        zhuangjia_numbers = data['庄家数']

        # 初始化计数器、第十个数字的列表和匹配数据列表
        match_count = 0
        tenth_digits = []
        matched_details = []

        # 循环遍历数据，以每十行为一个窗口
        for i in range(len(zhuangjia_numbers) - 9):
            window_string = ''.join(map(str, zhuangjia_numbers[i:i + 9]))
            if window_string == input_string:
                match_count += 1
                tenth_digit = zhuangjia_numbers[i + 9]
                tenth_digits.append(tenth_digit)

                # 收集匹配的详细信息
                matched_row = data.iloc[i:i + 10]  # 包括第十行
                matched_details.append(matched_row)

        # 计算1的百分比和0的百分比
        one_percentage = tenth_digits.count(1) / len(tenth_digits) * 100 if tenth_digits else 0
        zero_percentage = tenth_digits.count(0) / len(tenth_digits) * 100 if tenth_digits else 0

        return match_count, one_percentage, zero_percentage, matched_details

    def on_calculate_string9_clicked(self):
        # 获取用户输入的数串9
        input_string9 = self.input_dealer_9.text()
        input_stringHKorMC = self.input_dealer_HKorMC1.text()
        # 如果 input_string9 为空，则从 self.jutishuchuan 获取后9位数字
        jutishuchuan_text = self.jutishuchuan.text()  # 获取数串文本
        if  jutishuchuan_text:
            if len(jutishuchuan_text) >= 9:
                input_string9 = jutishuchuan_text[-9:]  # 提取后10位数字
                self.input_dealer_9.setText(input_string9)  # 填入数串
            else:
                self.output_dealer_9_count.setText("数串长度不足9位")
                return
        # 使用获得的路径来读取 Excel 文件
        self.data1 = pd.read_excel(self.data1_path)
        self.data2 = pd.read_excel(self.data2_path)
        if input_stringHKorMC == "HK":
            # 执行计算
            matches, one_perc, zero_perc, matched_details = self.calculate_string9_matches(input_string9, self.data1)
        elif input_stringHKorMC == "MC":
            # 执行计算
            matches, one_perc, zero_perc, matched_details = self.calculate_string9_matches(input_string9, self.data2)
        else:
            # 如果输入不是"HK"或"MC"，显示错误或返回
            self.output_dealer_9_count.setText("请输入城市")
            return

        # 显示基础结果
        self.output_dealer_9_count.setText(str(matches))
        self.output_1_percentage_1.setText(f"{one_perc:.2f}%")
        self.output_0_percentage_1.setText(f"{zero_perc:.2f}%")

        # 如果有匹配的数据，打开副窗口显示详细信息
        if matched_details:
            open_sub_window(self, matched_details)

    def calculate_string10_matches(self, input_string, data):
        zhuangjia_numbers = data['庄家数']
        match_count = 0
        eleventh_digits = []
        matched_details = []

        for i in range(len(zhuangjia_numbers) - 10):
            window_string = ''.join(map(str, zhuangjia_numbers[i:i + 10]))
            if window_string == input_string:
                match_count += 1
                eleventh_digit = zhuangjia_numbers[i + 10]
                eleventh_digits.append(eleventh_digit)

                # 收集匹配的详细信息
                matched_row = data.iloc[i:i + 11]  # 包括第十一行
                matched_details.append(matched_row)

        one_percentage = eleventh_digits.count(1) / len(eleventh_digits) * 100 if eleventh_digits else 0
        zero_percentage = eleventh_digits.count(0) / len(eleventh_digits) * 100 if eleventh_digits else 0
        return match_count, one_percentage, zero_percentage, matched_details

    def calculate_string11_matches(self, input_string, data):
        zhuangjia_numbers = data['庄家数']
        match_count = 0
        twelfth_digits = []
        matched_details = []

        for i in range(len(zhuangjia_numbers) - 11):
            window_string = ''.join(map(str, zhuangjia_numbers[i:i + 11]))
            if window_string == input_string:
                match_count += 1
                twelfth_digit = zhuangjia_numbers[i + 11]
                twelfth_digits.append(twelfth_digit)

                # 收集匹配的详细信息
                matched_row = data.iloc[i:i + 12]  # 包括第十二行
                matched_details.append(matched_row)

        one_percentage = twelfth_digits.count(1) / len(twelfth_digits) * 100 if twelfth_digits else 0
        zero_percentage = twelfth_digits.count(0) / len(twelfth_digits) * 100 if twelfth_digits else 0
        return match_count, one_percentage, zero_percentage, matched_details

    def on_calculate_string10_clicked(self):
        input_string10 = self.input_dealer_10.text()
        input_stringHKorMC = self.input_dealer_HKorMC10.text()
        # 如果 input_string10 为空，则从 self.jutishuchuan 获取后10位数字
        jutishuchuan_text = self.jutishuchuan.text()  # 获取数串文本
        if jutishuchuan_text:

            if len(jutishuchuan_text) >= 10:
                input_string10 = jutishuchuan_text[-10:]  # 提取后10位数字
                self.input_dealer_10.setText(input_string10)  # 填入数串
            else:
                self.output_dealer_10_count.setText("数串长度不足10位")
                return
        # 使用获得的路径来读取 Excel 文件
        self.data1 = pd.read_excel(self.data1_path)
        self.data2 = pd.read_excel(self.data2_path)
        if input_stringHKorMC == "HK":
            matches, one_perc, zero_perc, matched_details = self.calculate_string10_matches(input_string10, self.data1)
        elif input_stringHKorMC == "MC":
            matches, one_perc, zero_perc, matched_details = self.calculate_string10_matches(input_string10, self.data2)
        else:
            self.output_dealer_10_count.setText("请输入城市")
            return

        self.output_dealer_10_count.setText(str(matches))
        self.output_1_percentage_10.setText(f"{one_perc:.2f}%")
        self.output_0_percentage_10.setText(f"{zero_perc:.2f}%")


        if matched_details:
            open_sub_window(self, matched_details)

    def on_calculate_string11_clicked(self):
        input_string11 = self.input_dealer_11.text()
        input_stringHKorMC = self.input_dealer_HKorMC11.text()
        # 如果 input_string11 为空，则从 self.jutishuchuan 获取后11位数字
        jutishuchuan_text = self.jutishuchuan.text()  # 获取数串文本
        if jutishuchuan_text:

            if len(jutishuchuan_text) >= 11:
                input_string11 = jutishuchuan_text[-11:]  # 提取后11位数字
                self.input_dealer_11.setText(input_string11)  # 填入数串
            else:
                self.output_dealer_11_count.setText("数串长度不足11位")
                return
        # 使用获得的路径来读取 Excel 文件
        self.data1 = pd.read_excel(self.data1_path)
        self.data2 = pd.read_excel(self.data2_path)
        if input_stringHKorMC == "HK":
            matches, one_perc, zero_perc, matched_details = self.calculate_string11_matches(input_string11, self.data1)
        elif input_stringHKorMC == "MC":
            matches, one_perc, zero_perc, matched_details = self.calculate_string11_matches(input_string11, self.data2)
        else:
            self.output_dealer_11_count.setText("请输入城市")
            return

        self.output_dealer_11_count.setText(str(matches))
        self.output_1_percentage_11.setText(f"{one_perc:.2f}%")
        self.output_0_percentage_11.setText(f"{zero_perc:.2f}%")

        # 如果有匹配的数据，可以在此处处理或显示 matched_details
        # 例如，打开一个新窗口来显示详细信息
        if matched_details:
            open_sub_window(self, matched_details)  # 假设您已经定义了这个函数

    def __init__(self):
        super().__init__()
        # 使用 resource_path 函数来获取 Excel 文件的正确路径
        # 使用示例
        self.data1_path = copy_to_storage_location('HK2010-2023_dataforAPP1.4.2prediction.xlsx')
        self.data2_path = copy_to_storage_location('MC2021-2023_dataforAPP1.4.2prediction.xlsx')


        self.initUI()

    def set_current_time2(self):
        current_date = datetime.now().strftime("%Y-%m-%d")
        self.input_jiezhiriqi.setText(current_date)
        self.input_shuchuanchangdu.setText("11")
        self.hkormc.setText("HK")

    def get_string_sequence(self):
        input_date= self.input_jiezhiriqi.text()
        xianzaishuju=self.hkormc.text()
        # 使用获得的路径来读取 Excel 文件
        self.data1 = pd.read_excel(self.data1_path)
        self.data2 = pd.read_excel(self.data2_path)
        try:
            input_date = datetime.strptime(input_date, "%Y-%m-%d").date()
            sequence_length = int(self.input_shuchuanchangdu.text())
            if xianzaishuju=="HK":
                data_source = self.data1
                self.data1['日期'] = pd.to_datetime(self.data1['日期']).dt.date
                if input_date in self.data1['日期'].values:
                    # 定位到相应日期的行
                    index = self.data1[self.data1['日期'] == input_date].index[0]
                    start_index = max(index - sequence_length + 1, 0)
                    dealer_sequence = self.data1['庄家数'][start_index:index + 1].astype(str).str.cat()
                    self.jutishuchuan.setText(dealer_sequence)
                    # 判断是否需要新窗口显示
                    if sequence_length > 65:
                        self.display_in_new_window2(dealer_sequence)
                    else:
                        self.jutishuchuan.setText(dealer_sequence)

                else:
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
                    reply.setStyleSheet("QLabel { alignment: AlignCenter; }")
                    reply.setStyleSheet(style_sheet)
                    reply.setIcon(QMessageBox.Icon.Critical)
                    reply.setWindowTitle("温馨提示")
                    reply.setText("日期不存在，请补充数据，确保至少更新到您输入的截至日期")
                    reply.setStandardButtons(QMessageBox.StandardButton.Ok)
                    reply.exec()  #
            elif xianzaishuju=="MC":
                data_source = self.data2
                self.data2['日期'] = pd.to_datetime(self.data2['日期']).dt.date
                if input_date in self.data2['日期'].values:
                    # 定位到相应日期的行
                    index = self.data2[self.data2['日期'] == input_date].index[0]
                    start_index = max(index - sequence_length + 1, 0)
                    dealer_sequence = self.data2['庄家数'][start_index:index + 1].astype(str).str.cat()
                    self.jutishuchuan.setText(dealer_sequence)
                    # 判断是否需要新窗口显示
                    if sequence_length > 65:
                        self.display_in_new_window2(dealer_sequence)
                    else:
                        self.jutishuchuan.setText(dealer_sequence)
                else:
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
                    reply.setStyleSheet("QLabel { alignment: AlignCenter; }")
                    reply.setStyleSheet(style_sheet)
                    reply.setIcon(QMessageBox.Icon.Critical)
                    reply.setWindowTitle("温馨提示")
                    reply.setText("日期不存在，请补充数据，确保至少更新到您输入的截至日期")
                    reply.setStandardButtons(QMessageBox.StandardButton.Ok)
                    reply.exec()  #
        except ValueError:
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
            reply.setStyleSheet("QLabel { alignment: AlignCenter; }")
            reply.setStyleSheet(style_sheet)
            reply.setIcon(QMessageBox.Icon.Critical)
            reply.setWindowTitle("温馨提示")
            reply.setText("数串长度输入不是有效的数字")
            reply.setStandardButtons(QMessageBox.StandardButton.Ok)
            reply.exec()  # 阻塞应用程序直到用户关闭警告框
            return

        data_source['日期'] = pd.to_datetime(data_source['日期']).dt.date
        if input_date in data_source['日期'].values:
            index = data_source[data_source['日期'] == input_date].index[0]
            start_index = max(index - sequence_length + 1, 0)
            match = data_source[start_index:index + 1]
            # 格式化匹配的数据
            formatted_data = self.format_data(match)
            self.display_in_new_window(formatted_data)

    def format_data(self, match):
        formatted_data = ""
        # 调整格式标识符以实现居中对齐
        column_names = "{:^22}{:^12}{:^8}{:^6}{:^8}{:^6}".format("  日期", "   特", "  地支", "庄家数", "双干", "双干宫")
        formatted_data += column_names + "\n"

        for row_index, row in match.iterrows():
            date_str = row['日期'] if isinstance(row['日期'], str) else row['日期'].strftime('%Y-%m-%d')
            te_str = str(int(row['特'])).zfill(2)
            # 确保数据行格式与列头格式匹配
            row_data = "{:^20}{:^12}{:^10}{:^10}{:^10}{:^10}".format(
                date_str, te_str, row['地支'], row['庄家数'], row['双干'], row['双干宫']
            )
            formatted_data += row_data + "\n"

        return formatted_data

    def display_in_new_window(self, content):
        dialog = DetailWindow(self, content)
        dialog.show()
        # 将非模态窗口存储在某个属性中以防止其被自动销毁
        self.detail_window = dialog

    def display_in_new_window2(self, content):
        dialog = QDialog(self)
        dialog.setWindowTitle("所有数串")
        dialog.resize(1000, 100)
        layout = QVBoxLayout(dialog)

        text_edit = QTextEdit(dialog)
        text_edit.setReadOnly(True)
        text_edit.setText(content)
        layout.addWidget(text_edit)

        dialog.show()
    def on_execute_clicked(self):
        # 从输入框读取数据
        if 1900<=int(self.year_input.input_text.text())<=2101  and 1<=int(self.month_input.input_text.text())<=12 and 1<=int(self.day_input.input_text.text())<=31 :
            year = int(self.year_input.input_text.text())
            month = int(self.month_input.input_text.text())
            day = int(self.day_input.input_text.text())
            date_str = f"{year}-{month}-{day}"
            # 调用 calculate_score 函数
            ling, yi, shuanggan, values = self.calculate_score(date_str)
            # 将结果显示在第二行的输出框中
            self.output_ling_dry.setText(ling)
            self.output_yi_dry_palace.setText(yi)
            self.output_dual_dry.setText(shuanggan)
            self.output_dual_dry_palace.setText(values)

    def calculate_score(self, date_str):
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


        # 根据 values 和地支的组合判断庄家数
        '''
        if (values == "坎一" and dizhi in ["酉", "戌", "亥", "子", "丑", "寅"]) or \
                (values == "坤二" and dizhi in ["巳", "午", "未", "申", "酉", "戌"]) or \
                (values == "震三" and dizhi in ["子", "丑", "寅", "卯", "辰", "巳"]) or \
                (values == "巽四" and dizhi in ["寅", "卯", "辰", "巳", "午", "未"]) or \
                (values == "乾六" and dizhi in ["申", "酉", "戌", "亥", "子", "丑"]) or \
                (values == "兑七" and dizhi in ["午", "未", "申", "酉", "戌", "亥"]) or \
                (values == "艮八" and dizhi in ["亥", "子", "丑", "寅", "卯", "辰"]) or \
                (values == "离九" and dizhi in ["卯", "辰", "巳", "午", "未", "申"]):
            zhuangjia_number = 0
        elif (values == "坎一" and dizhi in ["卯", "辰", "巳", "午", "未", "申"]) or \
                (values == "坤二" and dizhi in ["亥", "子", "丑", "寅", "卯", "辰"]) or \
                (values == "震三" and dizhi in ["午", "未", "申", "酉", "戌", "亥"]) or \
                (values == "巽四" and dizhi in ["申", "酉", "戌", "亥", "子", "丑"]) or \
                (values == "乾六" and dizhi in ["寅", "卯", "辰", "巳", "午", "未"]) or \
                (values == "兑七" and dizhi in ["子", "丑", "寅", "卯", "辰", "巳"]) or \
                (values == "艮八" and dizhi in ["巳", "午", "未", "申", "酉", "戌"]) or \
                (values == "离九" and dizhi in ["酉", "戌", "亥", "子", "丑", "寅"]):
            zhuangjia_number = 1
        '''
        if values=="坎一":
            ling="酉鸡🐓-戌狗🐕-亥猪🐖-子鼠🐀-丑牛🐂-寅虎🐅"
            yi="卯兔🐇-辰龙🐉-巳蛇🐍-午马🐎-未羊🐏-申猴🐒"
        elif values=="坤二":
            ling="巳蛇🐍-午马🐎-未羊🐏-申猴🐒-酉鸡🐓-戌狗🐕"
            yi="亥猪🐖-子鼠🐀-丑牛🐂-寅虎🐅-卯兔🐇-辰龙🐉"
        elif values == "震三":
            ling = "子鼠🐀-丑牛🐂-寅虎🐅-卯兔🐇-辰龙🐉-巳蛇🐍"
            yi = "午马🐎-未羊🐏-申猴🐒-酉鸡🐓-戌狗🐕-亥猪🐖"
        elif values == "巽四":
            ling = "寅虎🐅-卯兔🐇-辰龙🐉-巳蛇🐍-午马🐎-未羊🐏"
            yi = "申猴🐒-酉鸡🐓-戌狗🐕-亥猪🐖-子鼠🐀-丑牛🐂"
        elif values == "乾六":
            ling = "申猴🐒-酉鸡🐓-戌狗🐕-亥猪🐖-子鼠🐀-丑牛🐂"
            yi = "寅虎🐅-卯兔🐇-辰龙🐉-巳蛇🐍-午马🐎-未羊🐏"
        elif values == "兑七":
            ling = "午马🐎-未羊🐏-申猴🐒-酉鸡🐓-戌狗🐕-亥猪🐖"
            yi = "子鼠🐀-丑牛🐂-寅虎🐅-卯兔🐇-辰龙🐉-巳蛇🐍"
        elif values == "艮八":
            ling = "亥猪🐖-子鼠🐀-丑牛🐂-寅虎🐅-卯兔🐇-辰龙🐉"
            yi = "巳蛇🐍-午马🐎-未羊🐏-申猴🐒-酉鸡🐓-戌狗🐕"
        elif values == "离九":
            ling = "卯兔🐇-辰龙🐉-巳蛇🐍-午马🐎-未羊🐏-申猴🐒"
            yi = "酉鸡🐓-戌狗🐕-亥猪🐖-子鼠🐀-丑牛🐂-寅虎🐅"
        print(f"日期：{year}-{month}-{day}-{hour} , 双干宫: {values}")
        print("----------------------------------------------------------------------")
        return ling,yi , shuanggan, values

    def toggle_HKMC_8(self):
        current_text = self.input_dealer_HKorMC2.text()
        if current_text == "":
            self.input_dealer_HKorMC2.setText(random.choice(["HK", "MC"]))
        elif current_text == "HK":
            self.input_dealer_HKorMC2.setText("MC")
        else:
            self.input_dealer_HKorMC2.setText("HK")

    def toggle_HKMC_9(self):
        current_text = self.input_dealer_HKorMC1.text()
        if current_text == "":
            self.input_dealer_HKorMC1.setText(random.choice(["HK", "MC"]))
        elif current_text == "HK":
            self.input_dealer_HKorMC1.setText("MC")
        else:
            self.input_dealer_HKorMC1.setText("HK")

    def toggle_HKMC_10(self):
        current_text = self.input_dealer_HKorMC10.text()
        if current_text == "":
            self.input_dealer_HKorMC10.setText(random.choice(["HK", "MC"]))
        elif current_text == "HK":
            self.input_dealer_HKorMC10.setText("MC")
        else:
            self.input_dealer_HKorMC10.setText("HK")

    def toggle_HKMC_11(self):
        current_text = self.input_dealer_HKorMC11.text()
        if current_text == "":
            self.input_dealer_HKorMC11.setText(random.choice(["HK", "MC"]))
        elif current_text == "HK":
            self.input_dealer_HKorMC11.setText("MC")
        else:
            self.input_dealer_HKorMC11.setText("HK")
    def toggle_HKMC_hkmc(self):
        current_text = self.hkormc.text()
        if current_text == "":
            self.hkormc.setText(random.choice(["HK", "MC"]))
        elif current_text == "HK":
            self.hkormc.setText("MC")
        else:
            self.hkormc.setText("HK")
    def toggle_HKMC_shujuku(self):
        current_text = self.city_input2.input_text.text()
        if current_text == "":
            self.city_input2.input_text.setText(random.choice(["HK", "MC"]))
        elif current_text == "HK":
            self.city_input2.input_text.setText("MC")
        else:
            self.city_input2.input_text.setText("HK")
    def clear_outputs(self):

        self.year_input.input_text.clear()
        self.month_input.input_text.clear()
        self.day_input.input_text.clear()
        self.output_dual_dry.clear()
        self.output_dual_dry_palace.clear()
        self.output_ling_dry.clear()
        self.output_yi_dry_palace.clear()
        self.input_jiezhiriqi.clear()
        self.input_shuchuanchangdu.clear()
        self.hkormc.clear()
        self.jutishuchuan.clear()
        self.input_dealer_8.clear()
        self.input_dealer_HKorMC2.clear()
        self.input_dealer_9.clear()
        self.input_dealer_HKorMC1.clear()
        self.input_dealer_10.clear()
        self.input_dealer_HKorMC10.clear()
        self.input_dealer_11.clear()
        self.input_dealer_HKorMC11.clear()
        self.output_dealer_8_count.clear()
        self.output_dealer_9_count.clear()
        self.output_dealer_10_count.clear()
        self.output_dealer_11_count.clear()
        self.output_1_percentage_2.clear()
        self.output_1_percentage_1.clear()
        self.output_1_percentage_10.clear()
        self.output_1_percentage_11.clear()
        self.output_0_percentage_2.clear()
        self.output_0_percentage_1.clear()
        self.output_0_percentage_10.clear()
        self.output_0_percentage_11.clear()
    def clear_outputs2(self):

        self.year_input2.input_text.clear()
        self.month_input2.input_text.clear()
        self.day_input2.input_text.clear()
        self.riqicahzhaoxiugai.clear()
        self.riqixiugai.clear()
        self.riqizengjia.clear()
        self.tamacahzhaoxiugai.clear()
        self.tamaxiugai.clear()
        self.tamazengjia.clear()
        self.dizhicahzhaoxiugai.clear()
        self.dizhixiugai.clear()
        self.dizhizengjia.clear()
        self.zhuangjiashucahzhaoxiugai.clear()
        self.zhuangjiashuxiugai.clear()
        self.zhuangjiashuzengjia.clear()
        self.shuanggancahzhaoxiugai.clear()
        self.shuangganxiugai.clear()
        self.shuangganzengjia.clear()
        self.shuanggangongcahzhaoxiugai.clear()
        self.shuanggangongxiugai.clear()
        self.shuanggangongzengjia.clear()

    def on_search_clicked(self):
        # 获取输入的年、月、日和城市
        year = self.year_input2.input_text.text()
        month = self.month_input2.input_text.text()
        day = self.day_input2.input_text.text()
        city = self.city_input2.input_text.text()

        try:
            search_date = datetime.strptime(f"{year}-{month}-{day}", "%Y-%m-%d").date()
        except ValueError:
            QMessageBox.warning(self, "错误", "无效的日期格式")
            return

        data_path = self.data1_path if city == "HK" else self.data2_path
        try:
            data = pd.read_excel(data_path)
            data['日期'] = pd.to_datetime(data['日期']).dt.date  # 转换日期列为 datetime.date 对象
        except FileNotFoundError:
            QMessageBox.warning(self, "错误", f"无法找到文件: {data_path}")
            return
        except Exception as e:
            QMessageBox.warning(self, "错误", str(e))
            return

        # 打印调试信息
        print("用户输入日期:", search_date)
        print("数据中的日期列:", data['日期'])

        # 查找数据
        try:
            result = data[data['日期'] == search_date]

            if not result.empty:
                # 将找到的数据显示在界面上
                print("找到的数据:", result)  # 添加调试输出
                self.riqicahzhaoxiugai.setText(str(result.iloc[0]['日期'].strftime("%Y-%m-%d")))
                self.tamacahzhaoxiugai.setText(str(result.iloc[0]['特']))
                self.dizhicahzhaoxiugai.setText(str(result.iloc[0]['地支']))
                self.zhuangjiashucahzhaoxiugai.setText(str(result.iloc[0]['庄家数']))
                self.shuanggancahzhaoxiugai.setText(str(result.iloc[0]['双干']))
                self.shuanggangongcahzhaoxiugai.setText(str(result.iloc[0]['双干宫']))
            else:
                # 显示未找到数据的消息
                print("未找到数据")  # 添加调试输出
                QMessageBox.information(self, "查找结果", "未找到数据")
        except Exception as e:
            # 捕获异常并输出错误信息
            print(f"查找数据时出错: {e}")
            QMessageBox.warning(self, "错误", f"查找数据时出错: {e}")

    def on_add_clicked(self):
        # 获取增加数据的输入
        print("开始执行 on_add_clicked 方法")

        date = self.riqizengjia.text()
        tema = self.tamazengjia.text()
        dizhi = self.dizhizengjia.text()
        zhuangjiashu = self.zhuangjiashuzengjia.text()
        shuanggan = self.shuangganzengjia.text()
        shuanggangong = self.shuanggangongzengjia.text()
        city = self.city_input2.input_text.text()
        print(f"收集到的输入数据: 日期={date}, 特={tema},...")
        # 将用户输入的日期字符串转换为 datetime.date 对象
        # 将用户输入的日期字符串转换为 YYYY-MM-DD 格式
        try:
            year, month, day = map(int, date.split('-'))
            add_date_str = f"{year:04d}-{month:02d}-{day:02d}"
            print(f"转换后的日期字符串: {add_date_str}")
        except ValueError as e:
            print(f"日期转换错误: {e}")
            QMessageBox.warning(self, "错误", "无效的日期格式")
            return

        # 根据城市选择数据集
        data_path = self.data1_path if city == "HK" else self.data2_path
        print(f"选择的数据路径: {data_path}")
        try:
            if os.path.exists(data_path):
                data = pd.read_excel(data_path)
                # 将日期列转换为仅日期的字符串格式
                if pd.api.types.is_datetime64_any_dtype(data['日期']):
                    data['日期'] = data['日期'].dt.strftime('%Y-%m-%d')
            else:
                data = pd.DataFrame()  # 如果文件不存在，创建一个空的 DataFrame

        except FileNotFoundError as e:
            print(f"读取或处理数据时出错: {e}")
            QMessageBox.warning(self, "错误", f"无法找到文件: {data_path}")
            return
        except Exception as e:
            print(f"读取或处理数据时出错: {e}")
            QMessageBox.warning(self, "错误", str(e))
            return

        # 检查数据是否已存在
        if add_date_str in data['日期'].values:
            QMessageBox.warning(self, "添加结果", "相同日期的数据已存在")
            return
        print("尝试追加数据到 DataFrame")
        # 创建新记录并尝试添加到 DataFrame
        # 创建新记录
        date_obj = datetime.strptime(add_date_str, "%Y-%m-%d")
        new_row = pd.DataFrame([{'日期': add_date_str, '特': tema, '地支': dizhi, '庄家数': zhuangjiashu,
                                 '双干': shuanggan, '双干宫': shuanggangong}])

        # 使用 concat 合并原始 DataFrame 和新行
        try:
            data = pd.concat([data, new_row], ignore_index=True)
        except Exception as e:
            print(f"合并数据时出错: {e}")
            QMessageBox.warning(self, "错误", "合并数据时出错: " + str(e))
            return

        # 打印新追加的数据行进行检查
        print("新追加的数据行:", new_row)
        print("追加后的 DataFrame 最后几行:")
        print(data.tail())

        # 保存数据
        try:
            print("尝试保存数据到 Excel")
            data.sort_values(by=['日期'], inplace=True)
            data.to_excel(data_path, index=False)
            QMessageBox.information(self, "添加结果", "数据添加成功")
        except Exception as e:
            print(f"保存文件时出错: {e}")
            QMessageBox.warning(self, "错误", "保存文件时出错: " + str(e))

    def on_modify_clicked(self):
        # 获取输入的日期和其他要修改的数据
        print("开始执行 on_modify_clicked 方法")

        date_to_modify = self.riqixiugai.text()
        new_tema = self.tamaxiugai.text()
        new_dizhi = self.dizhixiugai.text()
        new_zhuangjiashu = self.zhuangjiashuxiugai.text()
        new_shuanggan = self.shuangganxiugai.text()
        new_shuanggangong = self.shuanggangongxiugai.text()
        city = self.city_input2.input_text.text()
        print(f"收集到的输入数据: 修改日期={date_to_modify}, 新特={new_tema},...")

        # 将用户输入的日期字符串转换为 datetime.date 对象
        # 将用户输入的日期字符串转换为 YYYY-MM-DD 格式
        try:
            year, month, day = map(int, date_to_modify.split('-'))
            date_to_modify_str = f"{year:04d}-{month:02d}-{day:02d}"
            print(f"转换后的日期字符串: {date_to_modify_str}")
        except ValueError as e:
            print(f"日期转换错误: {e}")
            QMessageBox.warning(self, "错误", "无效的日期格式")
            return

        # 根据城市选择数据集
        data_path = self.data1_path if city == "HK" else self.data2_path
        print(f"选择的数据路径: {data_path}")
        try:
            if os.path.exists(data_path):
                data = pd.read_excel(data_path)
                # 将日期列转换为仅日期的字符串格式
                if pd.api.types.is_datetime64_any_dtype(data['日期']):
                    data['日期'] = data['日期'].dt.strftime('%Y-%m-%d')
            else:
                print(f"文件不存在: {data_path}")
                QMessageBox.warning(self, "错误", f"无法找到文件: {data_path}")
                return

        except Exception as e:
            print(f"读取或处理数据时出错: {e}")
            QMessageBox.warning(self, "错误", str(e))
            return

            # 查找要修改的行
        matching_rows = data[data['日期'] == date_to_modify_str]

        if not matching_rows.empty:
            index_to_modify = matching_rows.index[0]
            original_row = data.loc[index_to_modify].copy()  # 保存原始行的副本以进行比较

            # 检查每个字段，如果用户输入了数据，则更新，否则保留原数据
            # 更新数据（如果有新的输入）
            if new_tema:
                data.at[index_to_modify, '特'] = new_tema if new_tema else original_row['特']
            if new_dizhi:
                data.at[index_to_modify, '地支'] = new_dizhi if new_dizhi else original_row['地支']
            if new_zhuangjiashu:
                data.at[index_to_modify, '庄家数'] = new_zhuangjiashu if new_zhuangjiashu else original_row['庄家数']
            if new_shuanggan:
                data.at[index_to_modify, '双干'] = new_shuanggan if new_shuanggan else original_row['双干']
            if new_shuanggangong:
                data.at[index_to_modify, '双干宫'] = new_shuanggangong if new_shuanggangong else original_row['双干宫']
            modified_row = data.loc[index_to_modify]
            if modified_row.equals(original_row):
                QMessageBox.information(self, "提示", "数据并没有改变")
                return
            # 保存修改后的数据
            try:
                print("尝试保存数据到 Excel")
                data.to_excel(data_path, index=False)
                QMessageBox.information(self, "修改结果", "数据修改成功")
            except Exception as e:
                print(f"保存文件时出错: {e}")
                QMessageBox.warning(self, "错误", "保存文件时出错: " + str(e))
                return
        else:
            print("未找到要修改的日期")
            QMessageBox.warning(self, "错误", "未找到要修改的日期")

    def on_delete_clicked(self):
        # 获取输入的日期和城市
        date_to_delete = self.riqicahzhaoxiugai.text()
        city = self.city_input2.input_text.text()

        # 将用户输入的日期字符串转换为 YYYY-MM-DD 格式
        try:
            year, month, day = map(int, date_to_delete.split('-'))
            date_to_delete_str = f"{year:04d}-{month:02d}-{day:02d}"
        except ValueError as e:
            QMessageBox.warning(self, "错误", "无效的日期格式")
            return

        # 根据城市选择数据集
        data_path = self.data1_path if city == "HK" else self.data2_path

        try:
            if os.path.exists(data_path):
                data = pd.read_excel(data_path)
                # 将日期列转换为仅日期的字符串格式
                if pd.api.types.is_datetime64_any_dtype(data['日期']):
                    data['日期'] = data['日期'].dt.strftime('%Y-%m-%d')
            else:
                data = pd.DataFrame()  # 如果文件不存在，创建一个空的 DataFrame
        except FileNotFoundError:
            QMessageBox.warning(self, "错误", f"无法找到文件: {data_path}")
            return
        except Exception as e:
            QMessageBox.warning(self, "错误", str(e))
            return

        # 查找要删除的行
        matching_rows = data[data['日期'] == date_to_delete_str]

        if not matching_rows.empty:
            # 如果找到匹配的日期，选择第一行或其他策略
            index_to_delete = matching_rows.index[0]

            # 删除数据
            data = data.drop(index_to_delete)

            # 保存修改后的数据
            try:
                data.to_excel(data_path, index=False)
                QMessageBox.information(self, "删除结果", "数据删除成功")
            except Exception as e:
                QMessageBox.warning(self, "错误", "保存文件时出错: " + str(e))
                return
        else:
            QMessageBox.warning(self, "错误", "未找到要删除的日期")

    def updateTime(self):
        # 获取当前日期和时间
        current_datetime = QDateTime.currentDateTime()
        formatted_datetime = current_datetime.toString("yyyy-MM-dd hh:mm:ss")

        # 更新 QLabel 上显示的文本
        self.label.setText(f"{formatted_datetime}")
    def set_current_time(self):
        current_time = datetime.now()
        self.year_input.input_text.setText(str(current_time.year))
        self.month_input.input_text.setText(str(current_time.month))
        self.day_input.input_text.setText(str(current_time.day))

    def set_current_time3(self):
        current_time = datetime.now()
        self.year_input2.input_text.setText(str(current_time.year))
        self.month_input2.input_text.setText(str(current_time.month))
        self.day_input2.input_text.setText(str(current_time.day))
        self.city_input2.input_text.setText("HK")
    def initUI(self):
        # 主垂直布局
        main_layout = QVBoxLayout(self)

        # 第一行
        row1_layout = QHBoxLayout()
        self.year_input = InputWithComboBox(options=[str(i) for i in range(1900, 2101)])
        self.month_input = InputWithComboBox(options=[str(i) for i in range(1, 13)])
        self.day_input = InputWithComboBox(options=[str(i) for i in range(1, 32)])
        self.current_time_button = QPushButton("获取当前时间")
        self.current_time_button.clicked.connect(self.set_current_time)
        self.execute_button = QPushButton("获取零一生肖")
        self.output_dual_dry = QLineEdit()
        self.output_dual_dry.setPlaceholderText("双干输出")
        self.output_dual_dry_palace = QLineEdit()
        self.output_dual_dry_palace.setPlaceholderText("双干宫输出")
        self.output_dual_dry_palace.setFixedSize(145, 40)
        self.output_dual_dry .setFixedSize(135, 40)
        # 将输出框设置为只读
        self.output_dual_dry.setReadOnly(True)
        self.output_dual_dry_palace.setReadOnly(True)
        # 设置输出框内容居中
        for entry in [self.year_input, self.month_input, self.day_input]:
            entry.input_text.setStyleSheet("border: 2px solid gray;")
            entry.input_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.output_dual_dry.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.output_dual_dry_palace.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_entry1label = QLabel('年')
        self.time_entry2label = QLabel('月')
        self.time_entry3label = QLabel('日')
        self.time_entry1label.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.time_entry2label.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.time_entry3label.setAlignment(Qt.AlignmentFlag.AlignTop)
        margin = 12
        self.time_entry1label.setMargin(margin)
        self.time_entry2label.setMargin(margin)
        self.time_entry3label.setMargin(margin)
        FONT=QFont("KaiTi",15)
        FONT.setBold(True)
        font = QFont('SimSun', 10)
        font.setBold(True)
        self.current_time_button.setFont(font)
        self.execute_button.setFont(font)
        self.output_dual_dry.setFont(FONT)
        self.output_dual_dry_palace.setFont(FONT)
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
        self.execute_button.setStyleSheet(button_style)
        # 添加标签
        row1_layout.addWidget(self.year_input)
        row1_layout.addWidget(self.time_entry1label)
        row1_layout.addWidget(self.month_input)
        row1_layout.addWidget(self.time_entry2label)
        row1_layout.addWidget(self.day_input)
        row1_layout.addWidget(self.time_entry3label)
        row1_layout.addWidget( self.output_dual_dry)
        row1_layout.addWidget(self.output_dual_dry_palace)
        row1_layout.addWidget(self.current_time_button )
        row1_layout.addWidget(self.execute_button)

        self.execute_button.clicked.connect(self.on_execute_clicked)

        row3_layout = QHBoxLayout()
        self.output_ling_dry = QLineEdit()
        self.output_ling_dry.setFixedHeight(30)
        bold_song_font = QFont("宋体", pointSize=13, weight=QFont.Weight.Bold)
        self.output_ling_dry.setFont(bold_song_font)
        self.output_ling_dry.setPlaceholderText("零-地支")
        self.output_yi_dry_palace = QLineEdit()

        self.output_yi_dry_palace.setFixedHeight(30)
        self.output_yi_dry_palace.setFont(bold_song_font)
        self.output_yi_dry_palace.setPlaceholderText("一-地支")
        # 将输出框设置为只读
        self.output_ling_dry.setReadOnly(True)
        self.output_yi_dry_palace.setReadOnly(True)
        # 设置输出框内容居中

        self.output_ling_dry.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.output_yi_dry_palace.setAlignment(Qt.AlignmentFlag.AlignCenter)
        row3_layout.addWidget(self.output_ling_dry)
        row3_layout.addWidget(self.output_yi_dry_palace)

        row4_layout = QHBoxLayout()
        bold_song_font = QFont("宋体", pointSize=14, weight=QFont.Weight.Bold)
        # 第一行：标签
        self.label_ling = QLabel("0", self)
        self.label_ling.setFont(bold_song_font)
        self.label_ling.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_yi = QLabel("1", self)
        self.label_yi.setFont(bold_song_font)
        self.label_yi.setAlignment(Qt.AlignmentFlag.AlignCenter)
        row4_layout.addWidget(self.label_ling)
        row4_layout.addWidget(self.label_yi)
        row5_layout = QHBoxLayout()
        self.input_jiezhiriqi = QLineEdit()
        self.input_shuchuanchangdu=QLineEdit()
        self.input_jiezhiriqi.setPlaceholderText("请输入截至时间(格式：2024-1-1)")
        self.input_jiezhiriqi.setFixedWidth(255)
        self.input_jiezhiriqi.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_shuchuanchangdu.setPlaceholderText("长度")
        self.input_shuchuanchangdu.setFixedWidth(40)
        self.input_shuchuanchangdu.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.huoqudangqianshijian=QPushButton("获取当前时间")
        self.huoqushuchuan=QPushButton("获取数串")
        self.jutishuchuan=QLineEdit()
        self.jutishuchuan.setPlaceholderText("具体数串在此显示")
        self.jutishuchuan.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.huoqudangqianshijian.clicked.connect(self.set_current_time2)
        self.huoqushuchuan.clicked.connect(self.get_string_sequence)
        self.hkormc=QLineEdit()
        self.hkormc.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hkormc.setPlaceholderText("HK/MC")
        self.hkormc.setFixedWidth(60)
        self.qiehuanchengshi=QPushButton("切换城市")
        self.qiehuanchengshi.clicked.connect(self.toggle_HKMC_hkmc)
        row5_layout.addWidget(self.input_jiezhiriqi)
        row5_layout.addWidget(self.input_shuchuanchangdu)
        row5_layout.addWidget(self.hkormc)
        row5_layout.addWidget(self.huoqudangqianshijian)
        row5_layout.addWidget(self.qiehuanchengshi)
        row5_layout.addWidget(self.huoqushuchuan)
        row5_layout.addWidget(self.jutishuchuan)



        #网格布局
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
        self.input_dealer_10 = QLineEdit()
        self.input_dealer_10.setPlaceholderText("庄家数串10")
        self.input_dealer_11 = QLineEdit()
        self.input_dealer_11.setPlaceholderText("庄家数串11")
        self.button_dealer_10_result = QPushButton("获取数串10结果")
        self.button_dealer_11_result = QPushButton("获取数串11结果")
        self.button_dealer_10_result.clicked.connect(self.on_calculate_string10_clicked)
        self.button_dealer_11_result.clicked.connect(self.on_calculate_string11_clicked)
        self.output_dealer_10_count = QLineEdit()
        self.output_dealer_10_count.setPlaceholderText("数串10次数")
        self.output_dealer_11_count = QLineEdit()
        self.output_dealer_11_count.setPlaceholderText("数串11次数")
        self.output_1_percentage_10 = QLineEdit()
        self.output_1_percentage_10.setPlaceholderText("1的百分比")
        self.output_0_percentage_10 = QLineEdit()
        self.output_0_percentage_10.setPlaceholderText("0的百分比")
        self.output_1_percentage_11 = QLineEdit()
        self.output_1_percentage_11.setPlaceholderText("1的百分比")
        self.output_0_percentage_11 = QLineEdit()
        self.output_0_percentage_11.setPlaceholderText("0的百分比")
        self.input_dealer_HKorMC10 = QLineEdit()
        self.input_dealer_HKorMC10.setPlaceholderText("HK/MC")
        self.input_dealer_HKorMC11 = QLineEdit()
        self.input_dealer_HKorMC11.setPlaceholderText("HK/MC")
        self.button_HKMC_8 = QPushButton("切换城市")
        self.button_HKMC_9 = QPushButton("切换城市")
        self.button_HKMC_10 = QPushButton("切换城市")
        self.button_HKMC_11 = QPushButton("切换城市")
        self.button_HKMC_8.clicked.connect(self.toggle_HKMC_8)
        self.button_HKMC_9.clicked.connect(self.toggle_HKMC_9)
        self.button_HKMC_10.clicked.connect(self.toggle_HKMC_10)
        self.button_HKMC_11.clicked.connect(self.toggle_HKMC_11)
        self.lingyi8_0=  QLabel("零")
        self.lingyi9_0 = QLabel("零")
        self.lingyi10_0 = QLabel("零")
        self.lingyi11_0 = QLabel("零")
        self.lingyi8_1 = QLabel("壹")
        self.lingyi9_1 = QLabel("壹")
        self.lingyi10_1 = QLabel("壹")
        self.lingyi11_1 = QLabel("壹")
        FONT = QFont("KaiTi", 15)
        FONT.setBold(True)
        self.lingyi8_0.setFont(FONT)
        self.lingyi10_0.setFont(FONT)
        self.lingyi9_0.setFont(FONT)
        self.lingyi11_0.setFont(FONT)
        self.lingyi10_1.setFont(FONT)
        self.lingyi8_1.setFont(FONT)
        self.lingyi9_1.setFont(FONT)
        self.lingyi11_1.setFont(FONT)
        self.lingyi8_0.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lingyi9_0.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lingyi10_0.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lingyi11_0.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lingyi8_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lingyi9_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lingyi10_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lingyi11_1.setAlignment(Qt.AlignmentFlag.AlignCenter)


        button_style = """
                  QPushButton {
                      background-color: white;  /* 设置背景颜色为灰色 */
                      color: black;  /* 设置文字颜色为红色 */
                      border: 1px solid gray;  /* 设置边框样式 */
                      border-radius: 10px;  /* 设置边框圆角 */      
                      padding: 2px;   /* 设置内边距 */                 
                       border-style: outset; /* 设置内边距 */           
                  }

                  QPushButton:hover {
                      background-color: purple;  /* 设置鼠标悬停时的背景颜色 */color: white;  /* 设置文字颜色为白色 */
                  }
              """
        self.button_HKMC_8.setStyleSheet(button_style)
        self.button_HKMC_9.setStyleSheet(button_style)
        self.button_HKMC_10.setStyleSheet(button_style)
        self.button_HKMC_11.setStyleSheet(button_style)
        self.button_dealer_8_result.setStyleSheet(button_style)
        self.button_dealer_9_result.setStyleSheet(button_style)
        self.button_dealer_10_result.setStyleSheet(button_style)
        self.button_dealer_11_result.setStyleSheet(button_style)
        self.huoqushuchuan.setStyleSheet(button_style)
        self.huoqudangqianshijian.setStyleSheet(button_style)
        self.qiehuanchengshi.setStyleSheet(button_style)
        # 将输出框设置为只读
        self.output_dealer_8_count.setReadOnly(True)
        self.output_dealer_9_count.setReadOnly(True)
        self.output_1_percentage_1.setReadOnly(True)
        self.output_1_percentage_2.setReadOnly(True)
        self.output_0_percentage_1.setReadOnly(True)
        self.output_0_percentage_2.setReadOnly(True)
        self.output_dealer_10_count.setReadOnly(True)
        self.output_dealer_11_count.setReadOnly(True)
        self.output_1_percentage_10.setReadOnly(True)
        self.output_0_percentage_10.setReadOnly(True)
        self.output_1_percentage_11.setReadOnly(True)
        self.output_0_percentage_11.setReadOnly(True)
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
        self.output_dealer_10_count.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.output_dealer_11_count.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.output_1_percentage_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.output_0_percentage_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.output_1_percentage_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.output_0_percentage_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_dealer_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_dealer_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_dealer_HKorMC11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_dealer_HKorMC10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # 添加元素到网格布局
        grid_layout.addWidget(self.input_dealer_8, 0, 1)
        grid_layout.addWidget(self.input_dealer_HKorMC2, 0, 0)

        grid_layout.addWidget(self.input_dealer_9, 0, 3)
        grid_layout.addWidget(self.input_dealer_HKorMC1, 0, 2)

        grid_layout.addWidget(self.input_dealer_10, 0, 5)
        grid_layout.addWidget(self.input_dealer_HKorMC10, 0, 4)

        grid_layout.addWidget(self.input_dealer_11, 0, 7)
        grid_layout.addWidget(self.input_dealer_HKorMC11, 0, 6)

        grid_layout.addWidget(self.button_dealer_8_result, 1, 1)
        grid_layout.addWidget(self.button_HKMC_8, 1, 0)

        grid_layout.addWidget(self.button_dealer_9_result, 1, 3)
        grid_layout.addWidget(self.button_HKMC_9, 1, 2)

        grid_layout.addWidget(self.button_dealer_10_result, 1, 5)
        grid_layout.addWidget(self.button_HKMC_10, 1, 4)

        grid_layout.addWidget(self.button_dealer_11_result, 1, 7)
        grid_layout.addWidget(self.button_HKMC_11, 1, 6)
        
        grid_layout.addWidget(self.output_dealer_8_count, 2, 0, 1, 2)  # 横跨两列
        grid_layout.addWidget(self.output_dealer_9_count, 2, 2, 1, 2)  # 横跨两列
        grid_layout.addWidget(self.output_dealer_10_count, 2, 4, 1, 2)  # 横跨两列
        grid_layout.addWidget(self.output_dealer_11_count, 2, 6, 1, 2)  # 横跨两列
        grid_layout.addWidget(self.lingyi8_1, 3, 1, 1, 1)  # 横跨两列
        grid_layout.addWidget(self.lingyi9_1, 3, 3, 1, 1)  # 横跨两列
        grid_layout.addWidget(self.lingyi10_1,3, 5, 1, 1)  # 横跨两列
        grid_layout.addWidget(self.lingyi11_1, 3, 7, 1, 1)  # 横跨两列
        grid_layout.addWidget(self.lingyi8_0, 3, 0, 1, 1)  # 横跨两列
        grid_layout.addWidget(self.lingyi9_0, 3, 2, 1, 1)  # 横跨两列
        grid_layout.addWidget(self.lingyi10_0,3, 4, 1, 1)  # 横跨两列
        grid_layout.addWidget(self.lingyi11_0, 3, 6, 1, 1)  # 横跨两列


        grid_layout.addWidget(self.output_1_percentage_2, 4, 1, 1, 1)  # 横跨两列
        grid_layout.addWidget(self.output_1_percentage_1, 4, 3, 1, 1)  # 横跨两列
        grid_layout.addWidget(self.output_1_percentage_10, 4, 5, 1, 1)  # 横跨两列
        grid_layout.addWidget(self.output_1_percentage_11, 4, 7, 1, 1)  # 横跨两列
        grid_layout.addWidget(self.output_0_percentage_2, 4, 0, 1, 1)  # 横跨两列
        grid_layout.addWidget(self.output_0_percentage_1, 4, 2, 1, 1)  # 横跨两列
        grid_layout.addWidget(self.output_0_percentage_10, 4, 4, 1, 1)  # 横跨两列
        grid_layout.addWidget(self.output_0_percentage_11, 4, 6, 1, 1)  # 横跨两列
        row6_layout = QHBoxLayout()
        self.clear_button = QPushButton("清除内容-庄家模型")
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
        self.clear_button.clicked.connect(self.clear_outputs)
        row6_layout.addWidget(self.clear_button)
        row7_layout = QHBoxLayout()
        self.label_dataoperation = QLabel("数据库", self)
        self.label_dataoperation.setFont(bold_song_font)
        self.label_dataoperation.setAlignment(Qt.AlignmentFlag.AlignCenter)
        row7_layout.addWidget(self.label_dataoperation)
        row8_layout = QHBoxLayout()
        self.year_input2 = InputWithComboBox(options=[str(i) for i in range(1900, 2101)])
        self.month_input2 = InputWithComboBox(options=[str(i) for i in range(1, 13)])
        self.day_input2 = InputWithComboBox(options=[str(i) for i in range(1, 32)])
        self.city_input2=InputWithComboBox(options=["HK","MC"])
        # 设置输出框内容居中
        for entry in [self.year_input2, self.month_input2, self.day_input2,self.city_input2]:
            entry.input_text.setStyleSheet("border: 2px solid gray;")
            entry.input_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.zhuanhuanhkmc=QPushButton("切换城市")
        self.zhuanhuanhkmc.clicked.connect(self.toggle_HKMC_shujuku)
        self.chazhao=QPushButton("查找")
        self.chazhao.clicked.connect(self.on_search_clicked)
        self.zengjia=QPushButton("增加")
        self.xiugai=QPushButton("修改")
        self.shanchu=QPushButton("删除")
        self.huoqushijianshujukuandhk=QPushButton("获取当前时间")
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
        self.chazhao.setFixedWidth(75)
        self.zengjia.setFixedWidth(75)
        self.xiugai.setFixedWidth(75)
        self.shanchu.setFixedWidth(75)
        self.huoqushijianshujukuandhk.setFixedWidth(120)
        self.zhuanhuanhkmc.setFixedWidth(80)
        self.time_entry1label2 = QLabel('年')
        self.time_entry2label2 = QLabel('月')
        self.time_entry3label2 = QLabel('日')
        self.city_entry3label2=QLabel("城市")
        self.time_entry1label2.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.time_entry2label2.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.time_entry3label2.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.city_entry3label2.setAlignment(Qt.AlignmentFlag.AlignTop)
        margin = 12
        self.time_entry1label2.setMargin(margin)
        self.time_entry2label2.setMargin(margin)
        self.time_entry3label2.setMargin(margin)
        self.city_entry3label2.setMargin(margin)
        self.chazhao.setStyleSheet(button_style)
        self.zengjia.setStyleSheet(button_style)
        self.xiugai.setStyleSheet(button_style)
        self.shanchu.setStyleSheet(button_style)
        self.zhuanhuanhkmc.setStyleSheet(button_style)
        self.huoqushijianshujukuandhk.setStyleSheet(button_style)
        self.zengjia.clicked.connect(self.on_add_clicked)
        self.xiugai.clicked.connect(self.on_modify_clicked)
        self.shanchu.clicked.connect(self.on_delete_clicked)
        self.huoqushijianshujukuandhk.clicked.connect(self.set_current_time3)
        row8_layout.addWidget(self.year_input2)
        row8_layout.addWidget(self.time_entry1label2)
        row8_layout.addWidget(self.month_input2)
        row8_layout.addWidget(self.time_entry2label2)
        row8_layout.addWidget(self.day_input2)
        row8_layout.addWidget(self.time_entry3label2)
        row8_layout.addWidget(self.city_input2)
        row8_layout.addWidget(self.city_entry3label2)
        row8_layout.addWidget(self.zhuanhuanhkmc)
        row8_layout.addWidget(self.huoqushijianshujukuandhk)
        row8_layout.addWidget(self.chazhao)
        row8_layout.addWidget(self.zengjia)
        row8_layout.addWidget(self.xiugai)
        row8_layout.addWidget(self.shanchu)
        row9_layout = QHBoxLayout()
        self.riqi = QLabel('日期')
        self.tema = QLabel('特码')
        self.dizhi = QLabel('地支')
        self.zhuangjiashu = QLabel('庄家数')
        self.shuagngan = QLabel('双干')
        self.shuanggangong = QLabel('双干宫')
        self.riqi.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dizhi.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.zhuangjiashu.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.shuagngan.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.shuanggangong.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tema.setAlignment(Qt.AlignmentFlag.AlignCenter)
        row9_layout.addWidget(self.riqi)
        row9_layout.addWidget(self.tema)
        row9_layout.addWidget(self.dizhi)
        row9_layout.addWidget(self.zhuangjiashu)
        row9_layout.addWidget(self.shuagngan)
        row9_layout.addWidget(self.shuanggangong)
        row10_layout = QHBoxLayout()
        self.riqicahzhaoxiugai=QLineEdit()
        self.tamacahzhaoxiugai = QLineEdit()
        self.dizhicahzhaoxiugai = QLineEdit()
        self.zhuangjiashucahzhaoxiugai = QLineEdit()
        self.shuanggancahzhaoxiugai = QLineEdit()
        self.shuanggangongcahzhaoxiugai = QLineEdit()
        self.riqicahzhaoxiugai.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tamacahzhaoxiugai.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dizhicahzhaoxiugai.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.zhuangjiashucahzhaoxiugai.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.shuanggancahzhaoxiugai.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.shuanggangongcahzhaoxiugai.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.riqicahzhaoxiugai.setPlaceholderText("查找/删除")
        self.tamacahzhaoxiugai.setPlaceholderText("查找/删除")
        self.dizhicahzhaoxiugai.setPlaceholderText("查找/删除")
        self.zhuangjiashucahzhaoxiugai.setPlaceholderText("查找/删除")
        self.shuanggancahzhaoxiugai.setPlaceholderText("查找/删除")
        self.shuanggangongcahzhaoxiugai.setPlaceholderText("查找/删除")
        row10_layout.addWidget(self.riqicahzhaoxiugai)
        row10_layout.addWidget(self.tamacahzhaoxiugai)
        row10_layout.addWidget(self.dizhicahzhaoxiugai)
        row10_layout.addWidget(self.zhuangjiashucahzhaoxiugai)
        row10_layout.addWidget(self.shuanggancahzhaoxiugai)
        row10_layout.addWidget(self.shuanggangongcahzhaoxiugai)

        row11_layout = QHBoxLayout()
        self.riqixiugai = QLineEdit()
        self.tamaxiugai = QLineEdit()
        self.dizhixiugai = QLineEdit()
        self.zhuangjiashuxiugai = QLineEdit()
        self.shuangganxiugai = QLineEdit()
        self.shuanggangongxiugai = QLineEdit()
        self.riqixiugai.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tamaxiugai.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dizhixiugai.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.zhuangjiashuxiugai.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.shuangganxiugai.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.shuanggangongxiugai.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.riqixiugai.setPlaceholderText("修改")
        self.tamaxiugai.setPlaceholderText("修改")
        self.dizhixiugai.setPlaceholderText("修改")
        self.zhuangjiashuxiugai.setPlaceholderText("修改")
        self.shuangganxiugai.setPlaceholderText("修改")
        self.shuanggangongxiugai.setPlaceholderText("修改")
        row11_layout.addWidget(self.riqixiugai)
        row11_layout.addWidget(self.tamaxiugai)
        row11_layout.addWidget(self.dizhixiugai)
        row11_layout.addWidget(self.zhuangjiashuxiugai)
        row11_layout.addWidget(self.shuangganxiugai)
        row11_layout.addWidget(self.shuanggangongxiugai)


        row12_layout = QHBoxLayout()
        self.riqizengjia = QLineEdit()
        self.tamazengjia = QLineEdit()
        self.dizhizengjia = QLineEdit()
        self.zhuangjiashuzengjia = QLineEdit()
        self.shuangganzengjia = QLineEdit()
        self.shuanggangongzengjia = QLineEdit()
        self.riqizengjia.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tamazengjia.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dizhizengjia.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.zhuangjiashuzengjia.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.shuangganzengjia.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.shuanggangongzengjia.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.riqizengjia.setPlaceholderText("增加")
        self.tamazengjia.setPlaceholderText("增加")
        self.dizhizengjia.setPlaceholderText("增加")
        self.zhuangjiashuzengjia.setPlaceholderText("增加")
        self.shuangganzengjia.setPlaceholderText("增加")
        self.shuanggangongzengjia.setPlaceholderText("增加")
        row12_layout.addWidget(self.riqizengjia)
        row12_layout.addWidget(self.tamazengjia)
        row12_layout.addWidget(self.dizhizengjia)
        row12_layout.addWidget(self.zhuangjiashuzengjia)
        row12_layout.addWidget(self.shuangganzengjia)
        row12_layout.addWidget(self.shuanggangongzengjia)
        row13_layout = QHBoxLayout()
        self.clear_button2 = QPushButton("清除内容-数据库")
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
        self.clear_button2.setStyleSheet(button_style)
        self.clear_button2.clicked.connect(self.clear_outputs2)
        row13_layout.addWidget(self.clear_button2)

        row0_layout=QHBoxLayout()
        self.biaoti_app4_Ultra=QLabel("SDTLAB_庄家模型APP4.Ultra")
        self.biaoti_app4_Ultra.setAlignment(Qt.AlignmentFlag.AlignCenter)
        bold_song_font = QFont("宋体", pointSize=14, weight=QFont.Weight.Bold)
        self.biaoti_app4_Ultra.setFont(bold_song_font)
        row0_layout.addWidget(self.biaoti_app4_Ultra)

        row14_layout=QHBoxLayout()
        self.label = QLabel(self)
        FONT = QFont("KaiTi", 12)
        FONT.setBold(True)
        self.label.setFont(FONT)
        self.timer = QTimer(self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)  # 1秒更新一次
        row14_layout.addWidget(self.label)
        # 添加行到主布局
        main_layout.addLayout(row0_layout)
        main_layout.addLayout(row14_layout)
        main_layout.addLayout(row1_layout)
        main_layout.addLayout(row4_layout)
        main_layout.addLayout(row3_layout)
        main_layout.addLayout(row5_layout)
        main_layout.addLayout(grid_layout)
        main_layout.addLayout(row6_layout)
        main_layout.addLayout(row7_layout)
        main_layout.addLayout(row8_layout)
        main_layout.addLayout(row9_layout)
        main_layout.addLayout(row10_layout)
        main_layout.addLayout(row11_layout)
        main_layout.addLayout(row12_layout)
        main_layout.addLayout(row13_layout)
        # 设置窗口属性
        self.setLayout(main_layout)
        self.setWindowTitle('STDLAB.app_4')

# 创建应用程序和主窗口
app = QApplication([])
ex = ExampleApp()
ex.show()
# 运行应用程序
app.exec()