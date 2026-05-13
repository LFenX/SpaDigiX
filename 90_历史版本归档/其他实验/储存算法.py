from PyQt5.QtWidgets import QApplication, QMainWindow, QScrollArea, QWidget, QVBoxLayout, QHBoxLayout, QLabel

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        scroll_area = QScrollArea()

        central_widget = QWidget()
        central_layout = QHBoxLayout()  # 主布局，水平布局
        central_widget.setLayout(central_layout)

        # 原始布局，垂直布局
        original_layout = QVBoxLayout()
        label1 = QLabel("原始布局1")
        label2 = QLabel("原始布局2")
        original_layout.addWidget(label1)
        original_layout.addWidget(label2)

        # 新布局，垂直布局
        new_layout = QVBoxLayout()
        label3 = QLabel("新布局1")
        label4 = QLabel("新布局2")
        new_layout.addWidget(label3)
        new_layout.addWidget(label4)

        # 在主布局中添加原始布局和新布局
        central_layout.addLayout(original_layout)
        central_layout.addLayout(new_layout)

        # 将内容窗口设置为可滚动区域的小部件
        scroll_area.setWidget(central_widget)
        # 将可滚动区域设置为主窗口的中央部件
        self.setCentralWidget(scroll_area)

        self.setWindowTitle('布局示例')
        self.setGeometry(100, 100, 400, 300)
        self.show()

if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    app.exec_()
