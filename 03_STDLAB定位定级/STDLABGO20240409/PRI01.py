import sys,os
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit,QComboBox
)
import shutil
from PyQt6.QtCore import QDateTime, Qt  # 导入 Qt
from PyQt6.QtGui import QFont
from functionSpaDigiXONEANDSEVEN import  getSpaDigiXdingweideshu
from functionSpaDigiXAPPONE import getthebasicmessageofnineGrids
from functionSpaDigiXONEANDSEVEN_P3MC_240515 import getSpaDigiXdingweideshu1
import pandas as pd
import re
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

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        # 使用 resource_path 函数来获取 Excel 文件的正确路径
        # 使用示例
        self.data_path = copy_to_storage_location('1080局实数确定版本.xlsx')

        # 主布局
        self.setWindowTitle("01软件")
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
        self.basicmessage1 = OutputBasicMessage('双干宫', output_width=300, fixed_height=80)
        self.basicmessage2 = OutputBasicMessage('年月日干支时间', output_width=400, fixed_height=80)
        self.basicmessage3 = OutputBasicMessage('程序得数', output_width=200, fixed_height=80)
        self.basicmessage4 = OutputBasicMessage('实数', output_width=200, fixed_height=80)

        layout3.addWidget(self.basicmessage1)
        layout3.addWidget(self.basicmessage2)
        layout3.addWidget(self.basicmessage3)
        layout3.addWidget(self.basicmessage4)

        main_layout.addLayout(layout3)

        # 第四个水平布局：三个 OutputBasicMessage 部件
        layout4 = QHBoxLayout()
        self.imformation1 = OutputBasicMessage('预测生肖', output_width=300, fixed_height=80)
        self.imformation2 = OutputBasicMessage('预测01', output_width=300, fixed_height=80)
        self.imformation3 = OutputBasicMessage('预测生肖串', output_width=500, fixed_height=80)

        layout4.addWidget(self.imformation1)
        layout4.addWidget(self.imformation2)
        layout4.addWidget(self.imformation3)

        main_layout.addLayout(layout4)

        self.setLayout(main_layout)

        # 链接信号和槽
        self.button_get_time.clicked.connect(self.get_current_time)
        self.button_clear.clicked.connect(self.clear_data)
        self.button_predict.clicked.connect(self.predict)

        # 设置按钮样式



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

    def predict(self):
        year = int(self.input_year.input_text.text())
        month = int(self.input_month.input_text.text())
        day = int(self.input_day.input_text.text())

        city=self.input_city.input_text.text()
        # 规则映射
        rules_MC = {
            "坎一": {"阳遁": ("子时", "子卯辰午未申-酉丑巳戌寅亥"), "阴遁": ("巳时", "子丑寅卯酉戌-辰申亥未午巳")},
            "巽四": {"阳遁": ("寅时", "子寅巳午未亥-卯申丑辰酉戌"), "阴遁": ("酉时", "子卯辰巳未戌-丑申亥午酉寅")},
            "坤二": {"阳遁": ("酉时", "子寅辰巳午未-丑申戌亥酉卯"), "阴遁": ("丑时", "子卯巳未申酉-辰戌亥午寅丑")},
            "兑七": {"阳遁": ("卯时", "子丑巳申酉亥-卯戌寅未午辰"), "阴遁": ("戌时", "巳未申酉戌亥-子辰午卯丑寅")},
            "艮八": {"阳遁": ("酉时", "丑巳午未戌亥-申子卯酉辰寅"), "阴遁": ("未时", "子丑卯未酉戌-辰申亥巳午寅")},
            "离九": {"阳遁": ("巳时", "丑卯辰午未酉-申亥子寅戌巳"), "阴遁": ("卯时", "寅卯辰巳申酉-戌亥未午子丑")},
            "乾六": {"阳遁": ("亥时", "丑寅巳午未酉-戌卯亥辰子申"), "阴遁": ("酉时", "丑辰巳午未申-戌子亥酉卯寅")},
            "震三": {"阳遁": ("辰时", "丑寅巳午申亥-辰子酉卯未戌"), "阴遁": ("辰时", "丑寅巳午未亥-辰子申卯酉戌")}
        }
        rules_HK = {
            "坎一": {"阳遁": ("辰时", "丑卯辰巳午戌-未寅申亥酉子"), "阴遁": ("丑时", "子丑寅酉戌亥-辰卯巳未午申")},
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
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
