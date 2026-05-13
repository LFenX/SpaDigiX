import sys,os
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit,QComboBox
)
import ast
import shutil
from PyQt6.QtCore import QDateTime, Qt  # 导入 Qt
from PyQt6.QtGui import QFont
from functionSpaDigiXONEANDSEVEN import  getSpaDigiXdingweideshu
from functionSpaDigiXAPPONE import getthebasicmessageofnineGrids
from functionSpaDigiXONEANDSEVEN_P3MC_240515 import getSpaDigiXdingweideshu1
import pandas as pd
import re
from datetime import datetime
from lunarcalendar import Converter, Solar
class OutputBasicMessage(QWidget):
    def __init__(self, label_text, output_width, fixed_height, parent=None):
        super().__init__(parent)

        # 垂直布局
        layout = QVBoxLayout()

        # Label
        self.label = QLabel(label_text)
        font = QFont("KaiTi", 12)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(self.label)

        # Output 部件
        self.output = QTextEdit()
        self.output.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.output.setFixedWidth(output_width)  # 设置 QTextEdit 的宽度
        layout.addWidget(self.output)

        self.setLayout(layout)

        # 固定高度
        self.setFixedHeight(fixed_height)
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

class InputWithComboBox(QWidget):
    def __init__(self, options=None):
        super().__init__()

        layout = QVBoxLayout()

        self.input_text = QLineEdit()
        self.combo_box = QComboBox()
        self.combo_box.setFixedSize(50,23)
        self.combo_box.setStyleSheet("""
            QComboBox {
                background-color: white; /* 设置背景颜色 */
                color: black; /* 设置文本颜色 */
                border: 1px solid #CCC; /* 设置边框样式 */
                padding: 0px; /* 设置内边距 */
            }
            QComboBox::drop-down {
                width: 10px; /* 设置下拉箭头的宽度 */

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
        self.right_arrow_button.setFixedWidth(10)
        self.left_arrow_button.setFixedWidth(10)
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
    def set_p_text(self,text):
        self.input_text.setPlaceholderText(text)
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

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        # 使用 resource_path 函数来获取 Excel 文件的正确路径
        # 使用示例
        self.data_path = copy_to_storage_location('1080局实数确定版本.xlsx')
        self.setGeometry(100, 100, 600, 600)  # 初始大小为800x600
        # 主布局
        self.setWindowTitle("01-新尾号模型-排干-高")
        main_layout = QVBoxLayout()

        # 第一个水平布局：Label
        layout1 = QHBoxLayout()
        self.label = QLabel('O1软件测试')
        font=QFont("KaiTi",15)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout1.addWidget(self.label)
        main_layout.addLayout(layout1)

        # 第二个水平布局：四个输入框和三个按钮
        layout2 = QHBoxLayout()
        self.input_year = InputWithComboBox(options=[str(i) for i in range(1900, 2101)])
        self.input_month = InputWithComboBox(options=[str(i) for i in range(1, 13)])
        self.input_day =InputWithComboBox(options=[str(i) for i in range(1, 32)])
        self.input_city = InputWithComboBox(options=[str(i) for i in ["澳门","香港"]])
        for entry in [self.input_year, self.input_month, self.input_day,self.input_city]:
            entry.input_text.setStyleSheet("border: 2px solid gray;")
            entry.input_text.setAlignment(Qt.AlignmentFlag.AlignCenter)


        self.time_entry1label = QLabel('年')
        self.time_entry2label = QLabel('月')
        self.time_entry3label = QLabel('日')
        self.city_label=QLabel("城市")
        font = QFont('Microsoft YaHei', 10)
        self.time_entry1label.setFont(font)
        self.time_entry2label.setFont(font)
        self.time_entry3label.setFont(font)
        self.city_label.setFont(font)
        layout2.addWidget(self.input_year)
        layout2.addWidget(self.time_entry1label)
        layout2.addWidget(self.input_month)
        layout2.addWidget(self.time_entry2label)
        layout2.addWidget(self.input_day)
        layout2.addWidget(self.time_entry3label)
        layout2.addWidget(self.input_city)
        layout2.addWidget(self.city_label)

        self.time_entry1label.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.time_entry2label.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.time_entry3label.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.city_label.setAlignment(Qt.AlignmentFlag.AlignTop)
        margin = 15
        self.time_entry1label.setMargin(margin)
        self.time_entry2label.setMargin(margin)
        self.time_entry3label.setMargin(margin)
        self.city_label.setMargin(margin)

        self.yinyangdun = QLineEdit()
        self.yinyangdun.setPlaceholderText("阴阳遁")
        self.hour = QLineEdit()
        self.hour.setPlaceholderText("时辰")
        self.hour.setFixedSize(60, 40)
        self.yinyangdun.setFixedSize(80, 40)
        # 将输出框设置为只读
        self.hour.setReadOnly(True)
        self.yinyangdun.setReadOnly(True)
        self.hour.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.yinyangdun.setAlignment(Qt.AlignmentFlag.AlignCenter)
        FONT = QFont("KaiTi", 15)
        FONT.setBold(True)
        self.hour.setFont(FONT)
        self.yinyangdun.setFont(FONT)

        self.button_get_time = QPushButton('获取当前时间')
        self.button_clear = QPushButton('清空数据')
        self.button_predict = QPushButton('执行预测')
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
        self.button_clear.setStyleSheet(button_style)
        self.button_predict.setStyleSheet(button_style)
        self.button_get_time.setStyleSheet(button_style)
        layout2.addWidget(self.yinyangdun)
        layout2.addWidget(self.hour)
        layout2.addWidget(self.button_get_time)
        layout2.addWidget(self.button_clear)
        layout2.addWidget(self.button_predict)

        main_layout.addLayout(layout2)

        # 第三个水平布局：四个 OutputBasicMessage 部件
        layout3 = QHBoxLayout()
        self.basicmessage1 = OutputBasicMessage('双干宫', output_width=120, fixed_height=80)
        self.basicmessage2 = OutputBasicMessage('年月日干支时间', output_width=320, fixed_height=80)
        self.basicmessage3 = OutputBasicMessage('程序得数', output_width=120, fixed_height=80)
        self.basicmessage4 = OutputBasicMessage('实数', output_width=120, fixed_height=80)

        layout3.addWidget(self.basicmessage1)
        layout3.addWidget(self.basicmessage2)
        layout3.addWidget(self.basicmessage3)
        layout3.addWidget(self.basicmessage4)



        # 第四个水平布局：三个 OutputBasicMessage 部件
        layout4 = QHBoxLayout()
        self.imformation1 = OutputBasicMessage('预测生肖', output_width=120, fixed_height=80)
        self.imformation2 = OutputBasicMessage('预测01', output_width=120, fixed_height=80)
        self.imformation3 = OutputBasicMessage('预测生肖串', output_width=300, fixed_height=80)

        layout3.addWidget(self.imformation1)
        layout3.addWidget(self.imformation2)
        layout3.addWidget(self.imformation3)
        main_layout.addLayout(layout3)
        #main_layout.addLayout(layout4)
        layout5=QHBoxLayout()
        lunar_date = self.get_lunar_date()
        self.weihaobiaoqian=QLabel(f"新尾号模型(今天是{lunar_date})")
        font = QFont("KaiTi", 15)
        self.weihaobiaoqian.setFont(font)
        self.weihaobiaoqian.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout5.addWidget(self.weihaobiaoqian)
        main_layout.addLayout(layout5)

        layout6 = QHBoxLayout()
        self.shang1 = InputWithComboBox(options=[str(i) for i in range(0, 10)])
        self.shang2 = InputWithComboBox(options=[str(i) for i in range(0, 10)])
        self.shang3= InputWithComboBox(options=[str(i) for i in range(0, 10)])
        self.shang4 = InputWithComboBox(options=[str(i) for i in range(0, 10)])
        self.shang5 = InputWithComboBox(options=[str(i) for i in range(0, 10)])
        self.shang6 = InputWithComboBox(options=[str(i) for i in range(0, 10)])
        self.shangte = InputWithComboBox(options=[str(i) for i in range(0, 10)])
        self.nongli = InputWithComboBox(options=[str(i) for i in range(0, 10)])
        self.gongli = InputWithComboBox(options=[str(i) for i in range(0, 10)])
        self.shang1.input_text.setPlaceholderText("上一")
        self.shang2.input_text.setPlaceholderText("上二")
        self.shang3.input_text.setPlaceholderText("上三")
        self.shang4.input_text.setPlaceholderText("上四")
        self.shang5.input_text.setPlaceholderText("上五")
        self.shang6.input_text.setPlaceholderText("上六")
        self.shangte.input_text.setPlaceholderText("上特")
        self.nongli.input_text.setPlaceholderText("农历")
        self.gongli.input_text.setPlaceholderText("公历")
        self.input_city2 = InputWithComboBox(options=[str(i) for i in ["澳门", "香港"]])
        self.input_city2.input_text.setPlaceholderText("城市")
        for entry in [self.shang1, self.shang2, self.shang3, self.shang4,self.shang4,self.shang5,self.shang6,self.shangte,self.nongli,self.gongli,self.input_city2]:
            entry.input_text.setStyleSheet("border: 2px solid gray;")
            entry.input_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
            entry.input_text.setFixedSize(90, 25)
        layout6.addWidget(self.shang1)
        layout6.addWidget(self.shang2)
        layout6.addWidget(self.shang3)
        layout6.addWidget(self.shang4)
        layout6.addWidget(self.shang5)
        layout6.addWidget(self.shang6)
        layout6.addWidget(self.shangte)
        layout6.addWidget(self.nongli)
        layout6.addWidget(self.gongli)
        layout6.addWidget(self.input_city2)

        self.button_clear2 = QPushButton('清空数据')
        self.button_predict2 = QPushButton('执行预测')
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
        self.button_clear2.setStyleSheet(button_style)
        self.button_predict2.setStyleSheet(button_style)
        layout6.addWidget(self.button_clear2)
        layout6.addWidget(self.button_predict2)
        main_layout.addLayout(layout6)
        layout7=QHBoxLayout()
        self.shang1yuce=QLineEdit()
        self.shang2yuce=QLineEdit()
        self.shang3yuce=QLineEdit()
        self.shang4yuce=QLineEdit()
        self.shang5yuce=QLineEdit()
        self.shang6yuce=QLineEdit()
        self.shangteyuce=QLineEdit()
        self.shang1yuce.setPlaceholderText("下一")
        self.shang2yuce.setPlaceholderText("下二")
        self.shang3yuce.setPlaceholderText("下三")
        self.shang4yuce.setPlaceholderText("下四")
        self.shang5yuce.setPlaceholderText("下五")
        self.shang6yuce.setPlaceholderText("下六")
        self.shangteyuce.setPlaceholderText("下特")


        FONT = QFont("KaiTi", 11)
        FONT.setBold(True)
        self.shang1yuce.setFont(FONT)
        self.shang2yuce.setFont(FONT)
        self.shang3yuce.setFont(FONT)
        self.shang4yuce.setFont(FONT)
        self.shang5yuce.setFont(FONT)
        self.shang6yuce.setFont(FONT)
        self.shangteyuce.setFont(FONT)
        self.shang1yuce.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.shang2yuce.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.shang3yuce.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.shang4yuce.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.shang5yuce.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.shang6yuce.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.shangteyuce.setAlignment(Qt.AlignmentFlag.AlignCenter)



        layout7.addWidget(self.shang1yuce)
        layout7.addWidget(self.shang2yuce)
        layout7.addWidget(self.shang3yuce)
        layout7.addWidget(self.shang4yuce)
        layout7.addWidget(self.shang5yuce)
        layout7.addWidget(self.shang6yuce)
        layout7.addWidget(self.shangteyuce)

        main_layout.addLayout(layout7)



        layout8=QHBoxLayout()
        self.weihaobiaoqian=QLabel("排干模型")
        font = QFont("KaiTi", 15)
        self.weihaobiaoqian.setFont(font)
        self.weihaobiaoqian.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout8.addWidget(self.weihaobiaoqian)
        main_layout.addLayout(layout8)
        layout00=QHBoxLayout()
        self.shang123 = InputWithComboBox(
            options=[str(i) for i in range(0,50)])
        self.shang223 = InputWithComboBox(
            options=[str(i) for i in range(0,50)])
        self.shang323 = InputWithComboBox(
            options=[str(i) for i in range(0,50)])
        self.shang423 = InputWithComboBox(
            options=[str(i) for i in range(0,50)])
        self.shang523 = InputWithComboBox(
            options=[str(i) for i in range(0,50)])
        self.shang623 = InputWithComboBox(
            options=[str(i) for i in range(0,50)])
        self.shangte23 = InputWithComboBox(
            options=[str(i) for i in range(0,50)])
        self.niangan3 = InputWithComboBox(
            options=[str(i) for i in range(2024,2049)])
        self.yuegan3 = InputWithComboBox(
            options=[str(i) for i in range(1,13)])
        self.rigan3 = InputWithComboBox(
            options=[str(i) for i in range(1,31)])
        self.shang123.input_text.setPlaceholderText("一")
        self.shang223.input_text.setPlaceholderText("二")
        self.shang323.input_text.setPlaceholderText("三")
        self.shang423.input_text.setPlaceholderText("四")
        self.shang523.input_text.setPlaceholderText("五")
        self.shang623.input_text.setPlaceholderText("六")
        self.shangte23.input_text.setPlaceholderText("特码")
        self.niangan3.input_text.setPlaceholderText("年")
        self.yuegan3.input_text.setPlaceholderText("月")
        self.rigan3.input_text.setPlaceholderText("日")
        for entry in [self.shang123, self.shang223, self.shang323, self.shang423,self.shang423,self.shang523,self.shang623,self.shangte23,self.niangan3,self.yuegan3,self.rigan3]:
            entry.input_text.setStyleSheet("border: 2px solid gray;")
            entry.input_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
            entry.input_text.setFixedSize(90, 25)
        layout00.addWidget(self.shang123)
        layout00.addWidget(self.shang223)
        layout00.addWidget(self.shang323)
        layout00.addWidget(self.shang423)
        layout00.addWidget(self.shang523)
        layout00.addWidget(self.shang623)
        layout00.addWidget(self.shangte23)
        layout00.addWidget(self.niangan3)
        layout00.addWidget(self.yuegan3)
        layout00.addWidget(self.rigan3)
        self.button_time33 = QPushButton('获取当前时间')
        self.button_predict33 = QPushButton('填入数据')
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
        self.button_time33.setStyleSheet(button_style)
        self.button_predict33.setStyleSheet(button_style)
        layout00.addWidget(self.button_time33)
        layout00.addWidget(self.button_predict33)
        main_layout.addLayout(layout00)





        layout9 = QHBoxLayout()
        self.shang12 = InputWithComboBox(options=[str(i) for i in ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']])
        self.shang22 = InputWithComboBox(options=[str(i) for i in ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']])
        self.shang32= InputWithComboBox(options=[str(i) for i in ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']])
        self.shang42 = InputWithComboBox(options=[str(i) for i in ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']])
        self.shang52 = InputWithComboBox(options=[str(i) for i in ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']])
        self.shang62 = InputWithComboBox(options=[str(i) for i in ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']])
        self.shangte2 = InputWithComboBox(options=[str(i) for i in ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']])
        self.niangan = InputWithComboBox(options=[str(i) for i in ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']])
        self.yuegan = InputWithComboBox(options=[str(i) for i in ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']])
        self.rigan=InputWithComboBox(options=[str(i) for i in['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸'] ])
        self.shang12.input_text.setPlaceholderText("上一")
        self.shang22.input_text.setPlaceholderText("上二")
        self.shang32.input_text.setPlaceholderText("上三")
        self.shang42.input_text.setPlaceholderText("上四")
        self.shang52.input_text.setPlaceholderText("上五")
        self.shang62.input_text.setPlaceholderText("上六")
        self.shangte2.input_text.setPlaceholderText("上特")
        self.niangan.input_text.setPlaceholderText("年干")
        self.yuegan.input_text.setPlaceholderText("月干")
        self.rigan.input_text.setPlaceholderText("日干")
        self.input_city3 = InputWithComboBox(options=[str(i) for i in ["澳门", "香港"]])
        self.input_city3.input_text.setPlaceholderText("城市")
        for entry in [self.shang12, self.shang22, self.shang32, self.shang42,self.shang42,self.shang52,self.shang62,self.shangte2,self.niangan,self.yuegan,self.rigan,self.input_city3,]:
            entry.input_text.setStyleSheet("border: 2px solid gray;")
            entry.input_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
            entry.input_text.setFixedSize(90, 25)
        layout9.addWidget(self.shang12)
        layout9.addWidget(self.shang22)
        layout9.addWidget(self.shang32)
        layout9.addWidget(self.shang42)
        layout9.addWidget(self.shang52)
        layout9.addWidget(self.shang62)
        layout9.addWidget(self.shangte2)
        layout9.addWidget(self.niangan)
        layout9.addWidget(self.yuegan)
        layout9.addWidget(self.rigan)
        layout9.addWidget(self.input_city3)

        self.button_clear3 = QPushButton('清空数据')
        self.button_predict3 = QPushButton('执行预测')
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
        self.button_clear3.setStyleSheet(button_style)
        self.button_predict3.setStyleSheet(button_style)
        layout9.addWidget(self.button_clear3)
        layout9.addWidget(self.button_predict3)
        main_layout.addLayout(layout9)
        layout10=QHBoxLayout()
        self.shang1yuce2=QLineEdit()
        self.shang2yuce2=QLineEdit()
        self.shang3yuce2=QLineEdit()
        self.shang4yuce2=QLineEdit()
        self.shang5yuce2=QLineEdit()
        self.shang6yuce2=QLineEdit()
        self.shangteyuce2=QLineEdit()
        self.shang1yuce2.setPlaceholderText("下一")
        self.shang2yuce2.setPlaceholderText("下二")
        self.shang3yuce2.setPlaceholderText("下三")
        self.shang4yuce2.setPlaceholderText("下四")
        self.shang5yuce2.setPlaceholderText("下五")
        self.shang6yuce2.setPlaceholderText("下六")
        self.shangteyuce2.setPlaceholderText("下特")
        FONT = QFont("KaiTi", 6)
        FONT.setBold(True)
        self.shang1yuce2.setFont(FONT)
        self.shang2yuce2.setFont(FONT)
        self.shang3yuce2.setFont(FONT)
        self.shang4yuce2.setFont(FONT)
        self.shang5yuce2.setFont(FONT)
        self.shang6yuce2.setFont(FONT)
        self.shangteyuce2.setFont(FONT)
        self.shang1yuce2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.shang2yuce2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.shang3yuce2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.shang4yuce2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.shang5yuce2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.shang6yuce2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.shangteyuce2.setAlignment(Qt.AlignmentFlag.AlignCenter)



        layout10.addWidget(self.shang1yuce2)
        layout10.addWidget(self.shang2yuce2)
        layout10.addWidget(self.shang3yuce2)
        layout10.addWidget(self.shang4yuce2)
        layout10.addWidget(self.shang5yuce2)
        layout10.addWidget(self.shang6yuce2)
        layout10.addWidget(self.shangteyuce2)

        main_layout.addLayout(layout10)
        layout11=QHBoxLayout()
        self.shang1yuce24 = QTextEdit()
        self.shang2yuce24 = QTextEdit()
        self.shang3yuce24 = QTextEdit()
        self.shang4yuce24 = QTextEdit()
        self.shang5yuce24 = QTextEdit()
        self.shang6yuce24 = QTextEdit()
        self.shangteyuce24 = QTextEdit()
        FONT = QFont("KaiTi", 12)
        FONT.setBold(True)
        self.shang1yuce24.setFont(FONT)
        self.shang2yuce24.setFont(FONT)
        self.shang3yuce24.setFont(FONT)
        self.shang4yuce24.setFont(FONT)
        self.shang5yuce24.setFont(FONT)
        self.shang6yuce24.setFont(FONT)
        self.shangteyuce24.setFont(FONT)
        self.shang1yuce24.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.shang2yuce24.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.shang3yuce24.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.shang4yuce24.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.shang5yuce24.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.shang6yuce24.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.shangteyuce24.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.shang1yuce24.setFixedHeight(110)
        self.shang2yuce24.setFixedHeight(110)
        self.shang3yuce24.setFixedHeight(110)
        self.shang4yuce24.setFixedHeight(110)
        self.shang5yuce24.setFixedHeight(110)
        self.shang6yuce24.setFixedHeight(110)
        self.shangteyuce24.setFixedHeight(110)





        layout11.addWidget(self.shang1yuce24)
        layout11.addWidget(self.shang2yuce24)
        layout11.addWidget(self.shang3yuce24)
        layout11.addWidget(self.shang4yuce24)
        layout11.addWidget(self.shang5yuce24)
        layout11.addWidget(self.shang6yuce24)
        layout11.addWidget(self.shangteyuce24)
        main_layout.addLayout(layout11)
        self.setLayout(main_layout)

        # 链接信号和槽
        self.button_get_time.clicked.connect(self.get_current_time)
        self.button_clear.clicked.connect(self.clear_data)
        self.button_predict.clicked.connect(self.predict)
        self.button_clear2.clicked.connect(self.clear_data2)
        self.button_clear3.clicked.connect(self.clear_data3)
        self.button_predict2.clicked.connect(self.predict2)
        self.button_predict3.clicked.connect(self.predict3)
        self.button_time33.clicked.connect(self.get_current_time2)
        self.button_predict33.clicked.connect(self.tianrushuju)

        # 设置按钮样式

    def get_lunar_date(self):
        today = datetime.today()
        solar = Solar(today.year, today.month, today.day)
        lunar = Converter.Solar2Lunar(solar)
        return f"农历 {lunar.year}年{lunar.month}月{lunar.day}日"
    def tianrushuju(self):
        yi=int(self.shang123.input_text.text())
        er = int(self.shang223.input_text.text())
        san = int(self.shang323.input_text.text())
        si = int(self.shang423.input_text.text())
        wu = int(self.shang523.input_text.text())
        liu = int(self.shang623.input_text.text())
        qi = int(self.shangte23.input_text.text())
        nian = int(self.niangan3.input_text.text())
        yue = int(self.yuegan3.input_text.text())
        ri = int(self.rigan3.input_text.text())
        base_sequence = ['己', '戊', '丁', '丙', '乙', '甲', '癸', '壬', '辛', '庚']
        def generate_tian_gan_for_year(base_sequence, start_year, target_year):
            # Calculate the number of shifts based on the year difference
            shift = (target_year - start_year) % 10
            shifted_sequence = base_sequence[-shift:] + base_sequence[:-shift]  # Apply the shift

            # Generate the Tian Gan for 49 numbers
            tian_gan_list = []
            for i in range(49):
                tian_gan_list.append(shifted_sequence[i % 10])

            # Create a dictionary mapping numbers to Tian Gan
            tian_gan_dict = {i + 1: tian_gan_list[i] for i in range(49)}
            return tian_gan_dict
        # Function to allow user input for a year and generate the Tian Gan sequence
        def tian_gan_for_input_year(target_year):
            tian_gan_dict = generate_tian_gan_for_year(base_sequence, 2009, target_year)
            return tian_gan_dict
        tiangandist=tian_gan_for_input_year(nian)
        for i in tiangandist:
            if i==yi:
                yigan=tiangandist[i]
            if i==er:
                ergan=tiangandist[i]
            if i==san:
                sangan=tiangandist[i]
            if i==si:
                sigan=tiangandist[i]
            if i==wu:
                wugan=tiangandist[i]
            if i==liu:
                liugan=tiangandist[i]
            if i==qi:
                qigan=tiangandist[i]
        list=getSpaDigiXdingweideshu1(nian,yue,ri)
        niangan=list[9]
        yuegan=list[10]
        rigan=list[11]
        self.shang12.input_text.setText(str(yigan))
        self.shang22.input_text.setText(str(ergan))
        self.shang32.input_text.setText(str(sangan))
        self.shang42.input_text.setText(str(sigan))
        self.shang52.input_text.setText(str(wugan))
        self.shang62.input_text.setText(str(liugan))
        self.shangte2.input_text.setText(str(qigan))
        self.niangan.input_text.setText(str(niangan))
        self.yuegan.input_text.setText(str(yuegan))
        self.rigan.input_text.setText(str(rigan))

    def set_button_styles(self):
        button_style = """
            QPushButton {
                font-size: 14px;
                padding: 8px 16px;
            }
            QPushButton:hover {
                background-color: #d0d0d0;
            }
        """
        self.button_get_time.setStyleSheet(button_style)
        self.button_clear.setStyleSheet(button_style)
        self.button_predict.setStyleSheet(button_style)

    def get_current_time(self):
        current_time = QDateTime.currentDateTime()
        self.input_year.input_text.setText(current_time.toString("yyyy"))
        self.input_month.input_text.setText(current_time.toString("MM"))
        self.input_day.input_text.setText(current_time.toString("dd"))
        self.input_city.input_text.setText("澳门")

    def get_current_time2(self):
        current_time = QDateTime.currentDateTime()
        self.niangan3.input_text.setText(current_time.toString("yyyy"))
        self.yuegan3.input_text.setText(current_time.toString("MM"))
        self.rigan3.input_text.setText(current_time.toString("dd"))
        self.input_city3.input_text.setText("澳门")


    def clear_data(self):
        self.input_year.input_text.clear()
        self.input_month.input_text.clear()
        self.input_day.input_text.clear()

        self.input_city.input_text.clear()
        self.hour.clear()
        self.yinyangdun.clear()
        self.basicmessage1.output.clear()
        self.basicmessage2.output.clear()
        self.basicmessage3.output.clear()
        self.basicmessage4.output.clear()


        self.imformation1.output.clear()
        self.imformation2.output.clear()
        self.imformation3.output.clear()

    def clear_data2(self):
        self.shang1.input_text.clear()
        self.shang2.input_text.clear()
        self.shang3.input_text.clear()
        self.shang4.input_text.clear()
        self.shang5.input_text.clear()
        self.shang6.input_text.clear()
        self.shangte.input_text.clear()
        self.nongli.input_text.clear()
        self.gongli.input_text.clear()
        self.input_city2.input_text.clear()

        self.shang1yuce.clear()
        self.shang2yuce.clear()
        self.shang3yuce.clear()
        self.shang4yuce.clear()
        self.shang5yuce.clear()
        self.shang6yuce.clear()
        self.shangteyuce.clear()
    def clear_data3(self):
        self.shang12.input_text.clear()
        self.shang22.input_text.clear()
        self.shang32.input_text.clear()
        self.shang42.input_text.clear()
        self.shang52.input_text.clear()
        self.shang62.input_text.clear()
        self.shangte2.input_text.clear()
        self.niangan.input_text.clear()
        self.yuegan.input_text.clear()
        self.rigan.input_text.clear()
        self.input_city3.input_text.clear()

        self.shang1yuce2.clear()
        self.shang2yuce2.clear()
        self.shang3yuce2.clear()
        self.shang4yuce2.clear()
        self.shang5yuce2.clear()
        self.shang6yuce2.clear()
        self.shangteyuce2.clear()
    def predict(self):
        year = int(self.input_year.input_text.text())
        month = int(self.input_month.input_text.text())
        day = int(self.input_day.input_text.text())

        city=self.input_city.input_text.text()
        # 规则映射
        rules_MC = {
            "坎一": {"阳遁": ("子时", "子卯辰午未申-酉丑巳戌寅亥"), "阴遁": ("巳时", "子丑寅卯酉戌-辰申亥未午巳")},
            "巽四": {"阳遁": ("寅时", "子寅巳午未亥-卯申丑辰酉戌"), "阴遁": ("卯时", "卯辰巳午酉戌-寅亥未申子丑")},
            "坤二": {"阳遁": ("酉时", "子寅辰巳午未-丑申戌亥酉卯"), "阴遁": ("丑时", "子卯巳未申酉-辰戌亥午寅丑")},
            "兑七": {"阳遁": ("卯时", "子丑巳申酉亥-卯戌寅未午辰"), "阴遁": ("戌时", "巳未申酉戌亥-子辰午卯丑寅")},
            "艮八": {"阳遁": ("酉时", "丑巳午未戌亥-申子卯酉辰寅"), "阴遁": ("未时", "子丑卯未酉戌-辰申亥巳午寅")},
            "离九": {"阳遁": ("巳时", "丑卯辰午未酉-申亥子寅戌巳"), "阴遁": ("卯时", "寅卯辰巳申酉-戌亥未午子丑")},
            "乾六": {"阳遁": ("亥时", "丑寅巳午未酉-戌卯亥辰子申"), "阴遁": ("酉时", "丑辰巳午未申-戌子亥酉卯寅")},
            "震三": {"阳遁": ("辰时", "丑寅巳午申亥-辰子酉卯未戌"), "阴遁": ("辰时", "丑寅巳午未亥-辰子申卯酉戌")}
        }
        rules_HK = {
            "坎一": {"阳遁": ("辰时", "丑卯辰巳午戌-未寅申亥酉子"), "阴遁": ("午时", "子丑寅辰巳未-卯申酉戌亥午")},
            "巽四": {"阳遁": ("亥时", "子卯辰巳午酉-申戌亥未寅丑"), "阴遁": ("寅时", "子丑卯辰午亥-申寅未戌巳酉")},
            "坤二": {"阳遁": ("卯时", "丑寅辰未申酉-亥子戌午卯巳"), "阴遁": ("申时", "丑巳午未申亥-子辰戌寅酉卯")},
            "兑七": {"阳遁": ("卯时", "子丑辰午申亥-未酉寅戌卯巳"), "阴遁": ("酉时", "丑卯辰巳午戌-申子亥酉未寅")},
            "艮八": {"阳遁": ("酉时", "丑寅巳午未申-亥子辰酉戌卯"), "阴遁": ("酉时", "丑巳午申戌亥-子辰酉未卯寅")},
            "离九": {"阳遁": ("子时", "巳午申酉戌亥-卯丑子未辰寅"), "阴遁": ("卯时", "辰巳午申戌亥-未子丑酉寅卯")},
            "乾六": {"阳遁": ("亥时", "丑寅卯巳申酉-戌子亥未辰午"), "阴遁": ("戌时", "丑辰申酉戌亥-子午未卯寅巳")},
            "震三": {"阳遁": ("卯时", "寅辰巳午未戌-亥丑子酉卯申"), "阴遁": ("寅时", "丑寅卯午申亥-未酉戌子巳辰")}
        }
        # 时辰对应数字
        time_to_number = {
            "子时": 0, "丑时": 2, "寅时": 4, "卯时": 6,
            "辰时": 8, "巳时": 10, "午时": 12, "未时": 14,
            "申时": 16, "酉时": 18, "戌时": 20, "亥时": 22
        }
        basic1 = getSpaDigiXdingweideshu1(year,month,day)[1]
        basic2 = getSpaDigiXdingweideshu1(year,month,day)[2]
        yinyangdun=getSpaDigiXdingweideshu1(year,month,day)[8]

        if city=="澳门":
            for i in rules_MC:
                if basic1==i:

                   for j in rules_MC[i]:
                       if yinyangdun==j:

                            shicheng = rules_MC[i][j][0]
                            yi=rules_MC[i][j][1][0:6]
                            ling=rules_MC[i][j][1][7:]
                       else:
                           pass
                else:
                    pass
        elif city=="香港":
            for i in rules_HK:
                if basic1 == i:

                    for j in rules_HK[i]:

                        if yinyangdun == j:

                            shicheng = rules_HK[i][j][0]
                            yi = rules_HK[i][j][1][0:6]
                            ling = rules_HK[i][j][1][7:]
                        else:
                            pass
                else:
                    pass

        for i in time_to_number:
            if shicheng==i:
                hour=time_to_number[i]
            else:
                pass
        self.hour.setText(shicheng)
        self.yinyangdun.setText(yinyangdun)
        basic3 = getSpaDigiXdingweideshu(year,month,day,hour)
        excel_data = pd.read_excel(self.data_path, sheet_name='Sheet1')
        # Replace with the actual value of basic1
        labels = getthebasicmessageofnineGrids(year, month, day, hour)[0]
        # Generate label string
        label = ''
        for i in range(9):
            if i == 4:
                item = labels[i]
                label += item['地盘'] + item['九星'] + '-'
            else:
                item = labels[i]
                label += item['地盘'] + item['八神'] + item['天盘'] + item['九星'] + item['八门'] + '-'
        label = label.rstrip('-')
        # Compare the first column with 'basic1' and extract the corresponding value from the "实数数据" column
        matched_row = excel_data[excel_data.iloc[:, 0] == label]
        edata = matched_row['实数数据'].values[0] if not matched_row.empty else None
        dizhiduiyingshicheng={0:"子",2:"丑",4:"寅",6:"卯",8:"辰",10:"巳",12:"午",14:"未",16:"申",18:"酉",20:"戌",22:"亥",1:"子",3:"丑",5:"寅",7:"卯",9:"辰",11:"巳",13:"午",15:"未",17:"申",19:"酉",21:"戌",23:"亥"}
        for i in dizhiduiyingshicheng:
            if i==hour:
                basic4=dizhiduiyingshicheng[i]+str(edata)
            else:
                pass

        self.basicmessage1.output.setPlainText(str(basic1))
        self.basicmessage2.output.setPlainText(str(basic2))
        self.basicmessage3.output.setPlainText(str(basic3))
        self.basicmessage4.output.setPlainText(str(basic4))
        zodiac_to_number = {
            '子': 1, '丑': 2, '寅': 3, '卯': 4,
            '辰': 5, '巳': 6, '午': 7, '未': 8,
            '申': 9, '酉': 10, '戌': 11, '亥': 12
        }
        real_number = str(basic4)  # 强制转换为字符串
        digit_match = re.search(r'\d+\.?\d*', real_number)
        shengxiao_match = re.search(r'[^\d]+', real_number)

        if digit_match and shengxiao_match:
            digit_part = float(digit_match.group())
            shengxiao = shengxiao_match.group().strip()
            combined_value = digit_part + int(basic3)

            if combined_value > 1:
                new_number = round(combined_value - 1)
            elif -1 < combined_value <= 1:
                new_number = -1 if -1 < combined_value < 0 else 0
            else:
                new_number = round(combined_value)

            SSSX = zodiac_to_number.get(shengxiao, 0)
            new_number = new_number + SSSX

            # 新的BIAOQIAN计算方法
            if new_number > 12:
                BIAOQIAN = new_number % 12 if new_number % 12 != 0 else 12
            elif new_number == 0:
                BIAOQIAN = 12
            elif new_number < 0:
                BIAOQIAN = 12 - ((-new_number) % 12)
            else:
                BIAOQIAN = new_number

            label_zodiac = {v: k for k, v in zodiac_to_number.items()}.get(BIAOQIAN, '')
            info1=label_zodiac
        #根据 basicmessage3 和 basicmessage4 计算 imformation1
        self.imformation1.output.setPlainText(str(info1))
        palace_animal_groups = {
            '坎一': (['酉', '戌', '亥', '子', '丑', '寅'], ['卯', '辰', '巳', '午', '未', '申']),
            '坤二': (['巳', '午', '未', '申', '酉', '戌'], ['亥', '子', '丑', '寅', '卯', '辰']),
            '震三': (['子', '丑', '寅', '卯', '辰', '巳'], ['午', '未', '申', '酉', '戌', '亥']),
            '巽四': (['寅', '卯', '辰', '巳', '午', '未'], ['申', '酉', '戌', '亥', '子', '丑']),
            '乾六': (['申', '酉', '戌', '亥', '子', '丑'], ['寅', '卯', '辰', '巳', '午', '未']),
            '兑七': (['午', '未', '申', '酉', '戌', '亥'], ['子', '丑', '寅', '卯', '辰', '巳']),
            '艮八': (['亥', '子', '丑', '寅', '卯', '辰'], ['巳', '午', '未', '申', '酉', '戌']),
            '离九': (['卯', '辰', '巳', '午', '未', '申'], ['酉', '戌', '亥', '子', '丑', '寅'])
        }
        palace = basic1
        animal = info1
        group0, group1 = palace_animal_groups.get(palace, ([], []))
        if animal in group0:
            compare_01_data=0
        elif animal in group1:
            compare_01_data=1
        else:
            compare_01_data=2
        # 根据 imformation1 计算 imformation2 和 imformation3
        info2 = compare_01_data

        if info2==1:
            info3 = yi
        elif info2==0:
            info3=ling
        self.imformation2.output.setPlainText(str(info2))
        self.imformation3.output.setPlainText(str(info3))
        font=QFont("KaiTi",20)
        self.basicmessage1.output.setFont(font)
        self.basicmessage2.output.setFont(font)
        self.basicmessage3.output.setFont(font)
        self.basicmessage4.output.setFont(font)
        self.imformation1.output.setFont(font)
        self.imformation2.output.setFont(font)

        self.basicmessage1.output.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.basicmessage2.output.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.basicmessage3.output.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.basicmessage4.output.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.imformation1.output.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.imformation2.output.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.imformation3.output.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont("KaiTi", 20)
        self.imformation3.output.setFont(font)

    def predict2(self):
        # 获取输入值
        shang1 = int(self.shang1.input_text.text())
        shang2 = int(self.shang2.input_text.text())
        shang3 = int(self.shang3.input_text.text())
        shang4 = int(self.shang4.input_text.text())
        shang5 = int(self.shang5.input_text.text())
        shang6 = int(self.shang6.input_text.text())
        shangte = int(self.shangte.input_text.text())
        nongliweihao = int(self.nongli.input_text.text())
        gongliweihao = int(self.gongli.input_text.text())
        chengshi = self.input_city2.input_text.text()  # 澳门或香港

        # 五行属性分类
        wuxing_dict = {
            "水": [1, 6],
            "火": [2, 7],
            "木": [3, 8],
            "金": [4, 9],
            "土": [5, 0]
        }

        # 五行生克关系
        sheng_ke_dict = {
            "水": {"生": "木", "克": "火", "被生": "金", "被克": "土", "本我": "水"},
            "火": {"生": "土", "克": "金", "被生": "木", "被克": "水", "本我": "火"},
            "木": {"生": "火", "克": "土", "被生": "水", "被克": "金", "本我": "木"},
            "金": {"生": "水", "克": "木", "被生": "土", "被克": "火", "本我": "金"},
            "土": {"生": "金", "克": "水", "被生": "火", "被克": "木", "本我": "土"}
        }

        # 获取五行属性函数
        def get_wuxing(value):
            for wuxing, numbers in wuxing_dict.items():
                if value in numbers:
                    return wuxing
            return None

        # 根据规则计算预测值
        def calculate_yuce(relations):
            possible_values = []
            for upper_value, relation in relations:
                upper_wuxing = get_wuxing(upper_value)
                if upper_wuxing and relation in sheng_ke_dict[upper_wuxing]:
                    related_wuxing = sheng_ke_dict[upper_wuxing][relation]
                    # 获取该五行对应的数字
                    possible_values.append(wuxing_dict[related_wuxing])
            return possible_values

        if chengshi == "澳门":
            shang1yuce_relations = [(shang2, "被克"), (shang4, "克"), (shang6, "克")]
            shang2yuce_relations = [(shang3, "克"), (shang5, "被克"), (shang6, "本我")]
            shang3yuce_relations = [(shang4, "被克"), (shang6, "克"), (nongliweihao, "被克")]
            shang4yuce_relations = [(shang2, "被生"), (shang1, "被生"), (shangte, "被克")]
            shang5yuce_relations = [(shang2, "被克"), (shang5, "被生"), (shang4, "被生")]
            shang6yuce_relations = [(shang3, "本我"), (gongliweihao, "被克"), (shang6, "被生")]
            shangteyuce_relations = [(shang2, "本我"), (nongliweihao, "被生"), (shang1, "被克")]

            # 香港规则
        elif chengshi == "香港":
            shang1yuce_relations = [(shangte, "被生"), (shang6, "生"), (shang2, "被克")]
            shang2yuce_relations = [(nongliweihao, "生"), (shang2, "被克"), (gongliweihao, "被生")]
            shang3yuce_relations = [(shang5, "被克"), (shang6, "生"), (shangte, "被克")]
            shang4yuce_relations = [(gongliweihao, "克"), (nongliweihao, "克"), (shang1, "被克")]
            shang5yuce_relations = [(shang3, "生"), (nongliweihao, "被生"), (shang5, "被生")]
            shang6yuce_relations = [(shang6, "生"), (nongliweihao, "本我"), (shang1, "生")]
            shangteyuce_relations = [(shang4, "克"), (nongliweihao, "生"), (shang3, "克")]
        # if chengshi == "澳门":
        #     shang1yuce_relations = [(shang2, "被克")]
        #     shang2yuce_relations = [(shang3, "克")]
        #     shang3yuce_relations = [(shang4, "被克")]
        #     shang4yuce_relations = [(shang2, "被生")]
        #     shang5yuce_relations = [(shang2, "被克")]
        #     shang6yuce_relations = [(shang3, "本我")]
        #     shangteyuce_relations = [(shang2, "本我")]
        #
        #     # 香港规则
        # elif chengshi == "香港":
        #     shang1yuce_relations = [(shangte, "被生")]
        #     shang2yuce_relations = [(nongliweihao, "生")]
        #     shang3yuce_relations = [(shang5, "被克")]
        #     shang4yuce_relations = [(gongliweihao, "克")]
        #     shang5yuce_relations = [(shang3, "生")]
        #     shang6yuce_relations = [(shang6, "生")]
        #     shangteyuce_relations = [(shang4, "克")]
        # 计算预测值
        shang1yuce = calculate_yuce(shang1yuce_relations)
        shang2yuce = calculate_yuce(shang2yuce_relations)
        shang3yuce = calculate_yuce(shang3yuce_relations)
        shang4yuce = calculate_yuce(shang4yuce_relations)
        shang5yuce = calculate_yuce(shang5yuce_relations)
        shang6yuce = calculate_yuce(shang6yuce_relations)
        shangteyuce = calculate_yuce(shangteyuce_relations)

        # 输出预测值到 QLineEdit
        self.shang1yuce.setText(str(shang1yuce))
        self.shang2yuce.setText(str(shang2yuce))
        self.shang3yuce.setText(str(shang3yuce))
        self.shang4yuce.setText(str(shang4yuce))
        self.shang5yuce.setText(str(shang5yuce))
        self.shang6yuce.setText(str(shang6yuce))
        self.shangteyuce.setText(str(shangteyuce))



    # 主函数：根据输入数据进行预测
    def predict3(self):
        # 获取输入值
        print("1")
        # 定义天干分组
        tianganjiayi = [['甲', '乙'], ['丙', '丁'], ['戊', '己'], ['庚', '辛'], ['壬', '癸']]
        tianganbingding = [['丙', '丁'], ['戊', '己'], ['庚', '辛'], ['壬', '癸'], ['甲', '乙']]
        tianganwuji = [['戊', '己'], ['庚', '辛'], ['壬', '癸'], ['甲', '乙'], ['丙', '丁']]
        tiangangengxin = [['庚', '辛'], ['壬', '癸'], ['甲', '乙'], ['丙', '丁'], ['戊', '己']]
        tianganrengui = [['壬', '癸'], ['甲', '乙'], ['丙', '丁'], ['戊', '己'], ['庚', '辛']]

        # 获取对应天干列表的函数
        def get_tian_gan_list(tian_gan):
            if tian_gan in ['甲', '乙']:
                return tianganjiayi
            elif tian_gan in ['丙', '丁']:
                return tianganbingding
            elif tian_gan in ['戊', '己']:
                return tianganwuji
            elif tian_gan in ['庚', '辛']:
                return tiangangengxin
            elif tian_gan in ['壬', '癸']:
                return tianganrengui
            return []

        # 反向推算第二个天干的函数
        def find_second_tian_gan(tian_gan_1, angle):
            tian_gan_list = get_tian_gan_list(tian_gan_1)
            group_count = len(tian_gan_list)

            # 找到第一个天干的位置
            group_1, index_1 = next(
                (group_index, group.index(tian_gan_1)) for group_index, group in enumerate(tian_gan_list) if
                tian_gan_1 in group)

            # 计算角度对应的组间差值
            group_diff = (angle // 60) % group_count
            group_2 = (group_1 + group_diff) % group_count

            # 返回可能的天干
            return tian_gan_list[group_2]
        shang12 = self.shang12.input_text.text()
        shang22 = self.shang22.input_text.text()
        shang32 = self.shang32.input_text.text()
        shang42 = self.shang42.input_text.text()
        shang52 = self.shang52.input_text.text()
        shang62 = self.shang62.input_text.text()
        shangte2 = self.shangte2.input_text.text()
        niangan = self.niangan.input_text.text()
        yuegan = self.yuegan.input_text.text()
        rigan = self.rigan.input_text.text()
        chengshi2 = self.input_city3.input_text.text()
        print("2")
        # 澳门和香港的规则
        aomen_rules = [
            [(shang42, 240), (yuegan, 120), (shang32, 120)],
            [(niangan, 180), (shang32, 240), (shang12, 0)],
            [(rigan, 60), (shang22, 60), (shang32, 180)],
            [(shang32, 0), (shang12, 120), (shang12, 240)],
            [(shang12, 0), (niangan, 180), (shang52, 120)],
            [(shang52, 180), (shang32, 120), (shang52, 0)],
            [(shang22, 0), (shangte2, 120), (shang32, 120)]
        ]

        xianggang_rules = [
            [(shang62, 240), (shang42, 180), (shang42, 0)],
            [(yuegan, 0), (shangte2, 60), (shang52, 180)],
            [(shang52, 120), (shang12, 60), (yuegan, 60)],
            [(niangan, 120), (yuegan, 0), (shang62, 240)],
            [(shang12, 240), (niangan, 240), (shangte2, 0)],
            [(niangan, 240), (shang12, 180), (rigan, 120)],
            [(shang52, 120), (yuegan, 60), (shang42, 240)]
        ]

        # 根据输入的城市选择规则
        if chengshi2 == "澳门":
            selected_rules = aomen_rules
        elif chengshi2 == "香港":
            selected_rules = xianggang_rules
        else:
            return  # 如果城市不匹配，直接退出
        # 计算预测值的函数
        # 计算预测天干的函数
        # def predict_tian_gan(rule):
        #     possible_values = set()  # 初始化为空
        #     for input_value, angle in rule:
        #         predicted_values = find_second_tian_gan(input_value, angle)
        #         print(predicted_values)
        #         print(input_value,angle)
        #         if possible_values is None:
        #             # 第一次预测的天干值用来初始化集合
        #             possible_values = set(predicted_values)
        #         else:
        #             # 后续进行交集操作
        #             possible_values |= set(predicted_values)
        #     # 如果有可能的天干值，返回列表，否则返回 '无预测结果'
        #     return list(possible_values) if possible_values else ['无预测结果']
        def predict_tian_gan(rule):
            possible_values = []  # 初始化为空
            for input_value, angle in rule:
                predicted_values = find_second_tian_gan(input_value, angle)
                possible_values.append(predicted_values)
            # 如果有可能的天干值，返回列表，否则返回 '无预测结果'
            return possible_values


        # # 执行预测并设置结果
        # self.shang1yuce2.setText(",".join(predict_tian_gan(selected_rules[0])))
        #
        # self.shang2yuce2.setText(",".join(predict_tian_gan(selected_rules[1])))
        # self.shang3yuce2.setText(",".join(predict_tian_gan(selected_rules[2])))
        # self.shang4yuce2.setText(",".join(predict_tian_gan(selected_rules[3])))
        # self.shang5yuce2.setText(",".join(predict_tian_gan(selected_rules[4])))
        # self.shang6yuce2.setText(",".join(predict_tian_gan(selected_rules[5])))
        # self.shangteyuce2.setText(",".join(predict_tian_gan(selected_rules[6])))
        self.shang1yuce2.setText(str(predict_tian_gan(selected_rules[0])))
        self.shang2yuce2.setText(str(predict_tian_gan(selected_rules[1])))
        self.shang3yuce2.setText(str(predict_tian_gan(selected_rules[2])))
        self.shang4yuce2.setText(str(predict_tian_gan(selected_rules[3])))
        self.shang5yuce2.setText(str(predict_tian_gan(selected_rules[4])))
        self.shang6yuce2.setText(str(predict_tian_gan(selected_rules[5])))
        self.shangteyuce2.setText(str(predict_tian_gan(selected_rules[6])))
        # Define the base Tian Gan sequence for 2009
        base_sequence = ['己', '戊', '丁', '丙', '乙', '甲', '癸', '壬', '辛', '庚']

        # Function to generate the Tian Gan sequence for a given year
        def generate_tian_gan_for_year(base_sequence, start_year, target_year):
            # Calculate the number of shifts based on the year difference
            shift = (target_year - start_year) % 10
            shifted_sequence = base_sequence[-shift:] + base_sequence[:-shift]  # Apply the shift

            # Generate the Tian Gan for 49 numbers
            tian_gan_list = []
            for i in range(49):
                tian_gan_list.append(shifted_sequence[i % 10])

            # Create a reverse mapping of Tian Gan to all number positions
            tian_gan_to_numbers = {gan: [] for gan in shifted_sequence}
            for i in range(49):
                tian_gan_to_numbers[tian_gan_list[i]].append(i + 1)

            return tian_gan_to_numbers



        # Function to convert a Tian Gan string into the first two Tian Gan's possible number sequences
        def convert_tian_gan_to_first_two_numbers(tian_gan_string, tian_gan_to_numbers):
            list_of_lists = ast.literal_eval(tian_gan_string)
            tian_gan_string=[item for sublist in list_of_lists for item in sublist]
            tian_gan_string=",".join(tian_gan_string)
            tian_gan_list = tian_gan_string.split(',')

            result = {}

            # Take only the first two Tian Gan
            for gan in tian_gan_list[:6]:
                if gan in tian_gan_to_numbers:
                    result[gan] = tian_gan_to_numbers[gan]

            # Format the result as a string
            output = ""
            for gan, numbers in result.items():
                output += f"{numbers}\n"

            return output.strip()  # Remove trailing newline

        target_year=int(self.niangan3.input_text.text())
        # New function to allow user input for converting Tian Gan to only the first two numbers
        # Generate Tian Gan mapping for the given year
        tian_gan_to_numbers = generate_tian_gan_for_year(base_sequence, 2009, target_year)

        tian_gan_string1 = self.shang1yuce2.text()
        tian_gan_string2 = self.shang2yuce2.text()
        tian_gan_string3 = self.shang3yuce2.text()
        tian_gan_string4 = self.shang4yuce2.text()
        tian_gan_string5 = self.shang5yuce2.text()
        tian_gan_string6 = self.shang6yuce2.text()
        tian_gan_string7 = self.shangteyuce2.text()
        try:
            result1 = convert_tian_gan_to_first_two_numbers(tian_gan_string1, tian_gan_to_numbers)
            result2 = convert_tian_gan_to_first_two_numbers(tian_gan_string2, tian_gan_to_numbers)
            result3 = convert_tian_gan_to_first_two_numbers(tian_gan_string3, tian_gan_to_numbers)
            result4 = convert_tian_gan_to_first_two_numbers(tian_gan_string4, tian_gan_to_numbers)
            result5 = convert_tian_gan_to_first_two_numbers(tian_gan_string5, tian_gan_to_numbers)
            result6 = convert_tian_gan_to_first_two_numbers(tian_gan_string6, tian_gan_to_numbers)
            result7 = convert_tian_gan_to_first_two_numbers(tian_gan_string7, tian_gan_to_numbers)
            self.shang1yuce24.setText(result1)

            self.shang2yuce24.setText(result2)

            self.shang3yuce24.setText(result3)

            self.shang4yuce24.setText(result4)

            self.shang5yuce24.setText(result5)

            self.shang6yuce24.setText(result6)

            self.shangteyuce24.setText(result7)
        except:
            print("出错了")






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())