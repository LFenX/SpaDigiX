import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QCalendarWidget, QLabel,QMessageBox
from PyQt6.QtGui import QPixmap, QIcon, QFont, QPainter, QColor
from PyQt6.QtCore import QDate, Qt
import turtle
import time
class DayWindow(QWidget):
    def __init__(self, date):
        super().__init__()
        self.date = date
        self.initUI()

    def initUI(self):
        # Load the background image
        background_pixmap = QPixmap("BEIJING.jpg")

        # Set the window size to match the background image size
        self.setGeometry(100, 100, background_pixmap.width(), background_pixmap.height())
        self.setWindowTitle(f"{self.date.toString()}")

        # Background image that adapts to the window size
        background_label = QLabel(self)
        background_label.setPixmap(background_pixmap)
        background_label.setGeometry(self.rect())
        background_label.setScaledContents(True)

        # Define the starting date
        start_date = QDate(2024, 6, 26)

        # Calculate the difference in days between the current date and the start date
        days_difference = self.date.daysTo(start_date)

        if days_difference < 0:
            message = f"We've shared {-days_difference} days of togetherness and counting."
        elif days_difference == 0:
            message = f"On this day, we became one.！"
        else:
            message = f"In {days_difference} days, our love story will begin."

        # Text label
        label = QLabel(message, self)
        label.setGeometry(150, 200, 1000, 50)
        label.setFont(QFont("Gigi", 30))
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        if self.date == QDate(2024, 8, 10):
            # 修改按钮以运行Turtle绘图程序
            self.button = QPushButton("点我", self)
            self.button.setGeometry(200, 300, 1000, 30)
            self.button.setFont(QFont("KaiTi", 20))
            # 设置背景透明和无边框
            self.button.setStyleSheet("background-color: rgba(0, 0, 0, 0); border: none;")
            self.button.clicked.connect(self.run_turtle_graphics)
        elif days_difference < 0:
            # Add a button below the label
            self.button = QPushButton("点我", self)
            self.button.setGeometry(200, 300, 1000, 30)
            self.button.setFont(QFont("KaiTi", 20))
            # 设置背景透明和无边框
            self.button.setStyleSheet("background-color: rgba(0, 0, 0, 0); border: none;")

            self.button.clicked.connect(self.show_message)

            # Add a label to show the message after the button is clicked
            self.extra_label = QLabel("", self)
            self.extra_label.setGeometry(150, 340, 1000, 50)
            self.extra_label.setFont(QFont("KaiTi", 14))
            self.extra_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def show_message(self):
        self.extra_label.setText("平平淡淡想你的一天，LFen爱你又多了一点点")
    def run_turtle_graphics(self):
        turtle.clearscreen()
        turtle.speed(0)
        turtle.hideturtle()

        # 设置屏幕
        screen = turtle.Screen()
        screen.title("七夕快乐宝宝")
        screen.setup(width=1100, height=600)

        # 设置背景颜色
        screen.bgcolor("lightpink")  # 浅粉色背景

        def drawflower():
            # 设置初始位置
            turtle.penup()
            turtle.left(90)
            turtle.fd(200)
            turtle.pendown()
            turtle.right(90)
            turtle.speed(10)  # 调整速度为 3 (范围是 1 到 10, 越大越快)
            # 花蕊
            turtle.fillcolor("#CB002B")
            turtle.begin_fill()
            turtle.circle(10, 180)
            turtle.circle(25, 110)
            turtle.left(50)
            turtle.circle(60, 45)
            turtle.circle(20, 170)
            turtle.right(24)
            turtle.fd(30)
            turtle.left(10)
            turtle.circle(30, 110)
            turtle.fd(20)
            turtle.left(40)
            turtle.circle(90, 70)
            turtle.circle(30, 150)
            turtle.right(30)
            turtle.fd(15)
            turtle.circle(80, 90)
            turtle.left(15)
            turtle.fd(45)
            turtle.right(165)
            turtle.fd(20)
            turtle.left(155)
            turtle.circle(150, 80)
            turtle.left(50)
            turtle.circle(150, 90)
            turtle.end_fill()

            # 花瓣1
            turtle.left(150)
            turtle.circle(-90, 70)
            turtle.left(20)
            turtle.circle(75, 105)
            turtle.setheading(60)
            turtle.circle(80, 98)
            turtle.circle(-90, 40)  # 花瓣2
            turtle.left(180)
            turtle.circle(90, 40)
            turtle.circle(-80, 98)
            turtle.setheading(-83)

            # 叶子1
            turtle.fd(30)
            turtle.left(90)
            turtle.fd(25)
            turtle.left(45)
            turtle.fillcolor("#2CA46F")
            turtle.begin_fill()
            turtle.circle(-80, 90)
            turtle.right(90)
            turtle.circle(-80, 90)
            turtle.end_fill()

            turtle.right(135)
            turtle.fd(60)
            turtle.left(180)
            turtle.fd(85)
            turtle.left(90)
            turtle.fd(80)

            # 叶子2
            turtle.right(90)
            turtle.right(45)
            turtle.fillcolor("#2CA46F")
            turtle.begin_fill()
            turtle.circle(80, 90)
            turtle.left(90)
            turtle.circle(80, 90)
            turtle.end_fill()

            turtle.left(135)
            turtle.fd(60)
            turtle.left(180)
            turtle.fd(60)
            turtle.right(90)
            turtle.circle(200, 60)

        def draw_circle():
            for i in range(200):
                turtle.right(1)
                turtle.forward(1)

        def draw_love():
            turtle.color('#DA3261', '#CB002B')
            turtle.pensize(2)
            turtle.speed(1000)
            turtle.begin_fill()
            turtle.left(140)
            turtle.forward(112)
            draw_circle()
            turtle.left(120)
            draw_circle()
            turtle.forward(112)
            turtle.end_fill()  # 设置画笔颜色和大小

        turtle.color('#D2B48C')  # 画笔颜色
        turtle.pensize(3)
        turtle.penup()
        turtle.goto(-200, 0)
        turtle.pendown()

        # 绘制花
        drawflower()

        # 调整画笔
        turtle.penup()
        turtle.home()
        turtle.goto(200, -120)
        turtle.pendown()

        # 绘制爱心
        draw_love()

        # 调整画笔
        turtle.setheading(0)
        turtle.penup()
        turtle.backward(120)
        turtle.right(90)
        turtle.forward(80)
        turtle.pendown()
        turtle.write("    love    you", font=("Gigi", 28, "bold"))

        # 移动画笔，绘制时间
        turtle.penup()
        turtle.forward(60)
        turtle.left(90)
        turtle.forward(133)
        turtle.pendown()
        # date = time.strftime('%Y.%m.%d', time.localtime(time.time()))
        turtle.write("2024.08.10", font=("Gigi", 16, "bold"))

        turtle.pencolor('#FFDEAD')
        turtle.penup()
        turtle.goto(-80, 200)
        turtle.write("To my dearest love, ", font=("Gigi", 28, "bold"))
        # 移动画笔绘制姓名
        turtle.pencolor('#FFDEAD')
        turtle.penup()
        turtle.goto(-80, 100)
        turtle.write("Happy Double Seventh Day !", font=("Gigi", 28, "bold"))

        # 署名
        turtle.penup()
        turtle.goto(-450, 250)  # 右上角坐标
        turtle.pendown()
        turtle.pencolor('black')
        turtle.write("GRan:", align="left", font=("Gigi", 20, "bold"))
        # 署名
        turtle.penup()
        turtle.goto(220, -235)  # 右上角坐标
        turtle.pendown()
        turtle.pencolor('black')
        turtle.write("LFen", align="left", font=("Gigi", 20, "bold"))
        turtle.hideturtle()
        turtle.done()



class CalendarWidget(QCalendarWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGridVisible(True)
        self.setVerticalHeaderFormat(QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.setFont(QFont("KaiTi", 10))
        self.setHorizontalHeaderFormat(QCalendarWidget.HorizontalHeaderFormat.SingleLetterDayNames)

    def paintCell(self, painter, rect, date):
        super().paintCell(painter, rect, date)

        # Set the background image for each day cell
        background_pixmap = QPixmap("day_background.png").scaled(rect.size(), Qt.AspectRatioMode.IgnoreAspectRatio, Qt.TransformationMode.SmoothTransformation)

        # Calculate the difference in days between the current date and the start date
        start_date = QDate(2024, 6, 26)
        days_difference = date.daysTo(start_date)

        # Set custom background color for days_difference that are exact multiples of 100
        if days_difference % 100 == 0:
            painter.fillRect(rect, QColor(0, 0, 255))  # Blue background for multiples of 100
        else:
            painter.drawPixmap(rect, background_pixmap)

        # Increase the font size for the date number
        painter.setFont(QFont("Gigi", 16))

        # Draw the date number
        painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, str(date.day()))

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self.viewport())
        font = QFont("Gigi", 12)
        painter.setFont(font)
        painter.setPen(Qt.GlobalColor.black)

        for week in range(1, 54):  # There are usually a maximum of 53 weeks in a year
            rect = self.verticalHeader().sectionRect(week - 1)
            if not rect.isValid():
                continue
            text = f"Week {week}"
            painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, text)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('LFen写给GRan的日历情话')
        self.setGeometry(100, 100, 800, 600)

        main_layout = QVBoxLayout()

        # Top horizontal layout
        top_layout = QHBoxLayout()

        # Left button
        left_button = QPushButton(self)
        left_button.setFixedSize(50, 50)
        left_pixmap = QPixmap("LFen.jpg").scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        left_button.setIcon(QIcon(left_pixmap))
        left_button.setIconSize(left_button.size())
        left_button.setStyleSheet("border: none;")  # Make the button border transparent
        left_button.clicked.connect(self.show_popup)
        top_layout.addWidget(left_button)

        # Left image
        left_image_label = QLabel(self)
        left_image_pixmap = QPixmap("xindiantuICON.png").scaled(150, 50, Qt.AspectRatioMode.IgnoreAspectRatio, Qt.TransformationMode.SmoothTransformation)
        left_image_label.setPixmap(left_image_pixmap)
        left_image_label.setFixedSize(150, 50)
        top_layout.addWidget(left_image_label)

        # Center button
        center_button = QPushButton(self)
        center_button.setFixedSize(50, 50)
        center_pixmap = QPixmap("AIXIN.png").scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        center_button.setIcon(QIcon(center_pixmap))
        center_button.setIconSize(center_button.size())
        center_button.setStyleSheet("border: none;")  # Make the button border transparent
        center_button.clicked.connect(self.show_popup)
        top_layout.addWidget(center_button)

        # Right image
        right_image_label = QLabel(self)
        right_image_pixmap = QPixmap("xindiantuICON.png").scaled(150, 50, Qt.AspectRatioMode.IgnoreAspectRatio, Qt.TransformationMode.SmoothTransformation)
        right_image_label.setPixmap(right_image_pixmap)
        right_image_label.setFixedSize(150, 50)
        top_layout.addWidget(right_image_label)

        # Right button
        right_button = QPushButton(self)
        right_button.setFixedSize(50, 50)
        right_pixmap = QPixmap("GRan.jpg").scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        right_button.setIcon(QIcon(right_pixmap))
        right_button.setIconSize(right_button.size())
        right_button.setStyleSheet("border: none;")  # Make the button border transparent
        right_button.clicked.connect(self.show_popup)
        top_layout.addWidget(right_button)

        main_layout.addLayout(top_layout)

        # Calendar widget with custom day and week format
        self.calendar = CalendarWidget(self)
        self.calendar.clicked.connect(self.handle_calendar_click)
        main_layout.addWidget(self.calendar)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def show_popup(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("来不及喽")
        msg.setText("About.")
        msg.setGeometry(200, 200, 400, 300)
        msg.exec()

    def handle_calendar_click(self, date):
        self.show_day_window(date)

    def show_day_window(self, date):
        self.day_window = DayWindow(date)
        self.day_window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())