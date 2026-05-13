import sys
import random
import numpy as np
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel, QGridLayout

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
        self.probability_box.setPlaceholderText("欲望(百分制)")
        input_layout.addWidget(self.probability_box)

        main_layout.addLayout(input_layout)

        # Buttons for adding options and random selection
        add_button = QPushButton("添加选项", self)
        add_button.clicked.connect(self.add_option)
        main_layout.addWidget(add_button)

        choose_button = QPushButton("随机选择", self)
        choose_button.clicked.connect(self.choose_random)
        main_layout.addWidget(choose_button)

        # Layout for displaying options
        self.options_layout = QGridLayout()
        main_layout.addLayout(self.options_layout)

        # Label for displaying the chosen option
        self.result_label = QLabel("随机选项会显示在这里", self)
        main_layout.addWidget(self.result_label)

        self.setLayout(main_layout)

    def add_option(self):
        option = self.input_box.text().strip()
        probability_text = self.probability_box.text().strip()
        probability = float(probability_text) if probability_text else 1  # Default probability is 1

        if option:
            self.options.append((option, probability))
            option_label = QLabel(option, self)
            self.options_layout.addWidget(option_label, len(self.options) - 1, 0)

            self.input_box.clear()
            self.probability_box.clear()

    def choose_random(self):
        if self.options:
            options, probabilities = zip(*self.options)
            total = sum(probabilities)
            probabilities = [p / total for p in probabilities]  # Normalize probabilities
            chosen_option = np.random.choice(options, p=probabilities)
            self.result_label.setText(f'选择的选项: {chosen_option}')
        else:
            self.result_label.setText(f'没有选项可供选择')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EatWhatApp()
    ex.show()
    sys.exit(app.exec())
