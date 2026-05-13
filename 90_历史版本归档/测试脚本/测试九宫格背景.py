import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QFrame
from PyQt5.QtGui import QPixmap
import os

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # 创建一个容器 QFrame
        frame_with_background = QFrame()
        base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
        image_path1 = os.path.join(base_path, 'TTB.png')

        # 设置容器的样式，包括背景图片
        st=f"background-image: url({image_path1});"
        frame_with_background.setStyleSheet(st)

        grid_layout = QGridLayout(frame_with_background)

        # 在容器中创建九宫格的内容
        for row in range(3):
            for col in range(3):
                label = QLabel(f"格子 {row + 1}-{col + 1}")
                grid_layout.addWidget(label, row, col)

        central_widget.setLayout(grid_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())