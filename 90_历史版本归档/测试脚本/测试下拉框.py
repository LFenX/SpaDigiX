from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QLineEdit, QComboBox
import sys

class InputWithComboBox(QWidget):
    def __init__(self, options=None):
        super().__init__()

        self.layout = QVBoxLayout()

        self.input_text = QLineEdit()
        self.combo_box = QComboBox()

        if options:
            self.combo_box.addItems(options)

        self.layout.addWidget(self.input_text)
        self.layout.addWidget(self.combo_box)

        self.combo_box.currentTextChanged.connect(self.update_input_text)

        self.setLayout(self.layout)

    def update_input_text(self, text):
        self.input_text.setText(text)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        central_widget = QWidget()
        layout = QVBoxLayout()

        input_combo = InputWithComboBox(options=["Option 1", "Option 2", "Option 3"])
        layout.addWidget(input_combo)


        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def show_input_text(self):
        # 获取输入框中的文本
        input_text = self.centralWidget().findChild(QLineEdit, "input_text")
        print("Input Text:", input_text.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
