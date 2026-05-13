import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import QTimer

def close_loading_window():
    loading_window.close()

# 创建应用程序对象
app = QApplication(sys.argv)

# 创建加载窗口
loading_window = QWidget()
loading_window.setWindowTitle("加载中...")

# 创建布局
layout = QVBoxLayout()

# 创建标签并设置图片
image_label = QLabel()
image = QPixmap("QMDJ.png")  # 替换成您的图片文件路径
image_label.setPixmap(image)

# 将标签添加到布局
layout.addWidget(image_label)


# 将布局设置为加载窗口的主布局
loading_window.setLayout(layout)

# 调整加载窗口大小
loading_window.resize(400, 300)

# 显示加载窗口
loading_window.show()

# 创建定时器，一定时间后关闭加载窗口（例如3秒后）
timer = QTimer()
timer.timeout.connect(close_loading_window)
timer.start(3000)  # 3000毫秒（3秒）

# 在加载完成后执行您的主程序逻辑
# ...

# 运行应用程序
sys.exit(app.exec_())
