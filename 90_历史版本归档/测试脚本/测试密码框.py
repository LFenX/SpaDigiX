from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QPushButton
from PyQt6.QtCore import Qt
import sys

def createLineEditRightButton(edit):
    button = QPushButton()
    layout = QHBoxLayout()
    button.setCursor(Qt.CursorShape.ArrowCursor)
    layout.addStretch()
    layout.addWidget(button)
    layout.setContentsMargins(0, 0, 0, 0)
    edit.setLayout(layout)

    return button

def togglePasswordVisibility(password_edit):
    if password_edit.echoMode() == QLineEdit.EchoMode.Normal:
        password_edit.setEchoMode(QLineEdit.EchoMode.Password)
    else:
        password_edit.setEchoMode(QLineEdit.EchoMode.Normal)

app = QApplication(sys.argv)

widget = QWidget()
password_edit = QLineEdit(widget)
password_button = createLineEditRightButton(password_edit)
password_edit.setGeometry(20, 20, 200, 26)
widget.resize(400, 100)
widget.show()

password_button.clicked.connect(lambda: togglePasswordVisibility(password_edit))

# 设置样式
style = """
QLineEdit {
    border: 1px solid #EEE;
    border-radius: 4px;
    padding-right: 30px; /* 增加右侧按钮的宽度 */
}

QLineEdit:focus {
    border-color: #bbbec4;
}

QLineEdit QPushButton {
    width:  16px;
    height: 16px;
    qproperty-flat: true;
    margin-right: 4px;
    border: none;
    border-width: 0;
    background-image: url('your_image_path.png'); /* 替换成您的按钮图像路径 */
    background-position: center;
    background-repeat: no-repeat;
}
"""

widget.setStyleSheet(style)

sys.exit(app.exec())
