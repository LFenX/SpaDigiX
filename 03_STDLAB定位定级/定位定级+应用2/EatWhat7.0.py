import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel
from PyQt6.QtGui import QPainter, QPolygonF, QColor, QPen, QBrush
from PyQt6.QtCore import Qt, QTimer, QPoint, QPointF
from PyQt6.QtCore import QSize

class WheelOfFortune(QWidget):
    def __init__(self, options):
        super().__init__()
        self.options = options





    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Set up the pen and brush for drawing
        pen = QPen(Qt.GlobalColor.black, 2)
        painter.setPen(pen)
        painter.setBrush(QBrush(QColor(255, 255, 255)))

        rect = self.contentsRect()
        wheel_size = min(rect.width(), rect.height()) - 20
        painter.translate(rect.center().x(), rect.center().y())  # Translate to center
        painter.drawEllipse(QPoint(0, 0), wheel_size // 2, wheel_size // 2)

        # Draw the options on the wheel
        angle_step = 360 / len(self.options)
        for i, option in enumerate(self.options):
            painter.save()
            painter.rotate(angle_step * i)
            # Draw the individual pie slice
            painter.setBrush(QBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))))
            points = [QPointF(0, 0), QPointF(0, -wheel_size // 2), QPointF(angle_step, -wheel_size // 2)]
            polygon = QPolygonF(points)
            painter.drawConvexPolygon(polygon)
            painter.restore()


class EatWhatApp(QWidget):
    def __init__(self):
        super().__init__()

        self.options = []  # Store options and probabilities
        self.initUI()

    def initUI(self):
        # Main layout
        main_layout = QVBoxLayout()
        # Input layout for options and probabilities
        input_layout = QHBoxLayout()
        self.input_box = QLineEdit(self)
        self.input_box.setPlaceholderText("输入选项")
        input_layout.addWidget(self.input_box)

        self.probability_box = QLineEdit(self)
        self.probability_box.setPlaceholderText("概率")
        input_layout.addWidget(self.probability_box)

        add_button = QPushButton("添加选项", self)
        add_button.clicked.connect(self.add_option)
        input_layout.addWidget(add_button)

        main_layout.addLayout(input_layout)

        # Wheel of Fortune
        self.wheel = WheelOfFortune(self.options)
        main_layout.addWidget(self.wheel)

        # Button to start the wheel spinning
        choose_button = QPushButton("选择", self)
        choose_button.clicked.connect(self.spin_wheel)
        main_layout.addWidget(choose_button)

        self.setLayout(main_layout)

    def add_option(self):
        option = self.input_box.text().strip()
        probability_text = self.probability_box.text().strip()
        probability = float(probability_text) if probability_text else 1  # Default probability is 1

        if option:
            self.options.append((option, probability))
            self.wheel.update()  # Redraw the wheel with the new option

    def spin_wheel(self):
        # TODO: Implement the spinning of the wheel and selection of an option
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EatWhatApp()
    ex.show()
    sys.exit(app.exec())
