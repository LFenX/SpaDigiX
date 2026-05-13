import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QCalendarWidget, QLabel
from PyQt5.QtCore import QDate
import matplotlib.pyplot as plt
import numpy as np


class GreetingCardWindow(QWidget):
    def __init__(self, date):
        super().__init__()
        self.date = date
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Greeting Card")
        self.setGeometry(200, 200, 400, 300)

        # Using Matplotlib to create a dynamic greeting card
        self.create_greeting_card()

    def create_greeting_card(self):
        # Create a plot
        fig, ax = plt.subplots()
        t = np.arange(0.0, 2.0, 0.01)
        s = 1 + np.sin(2 * np.pi * t)

        ax.plot(t, s)

        ax.set(xlabel='time (s)', ylabel='voltage (mV)',
               title=f'Greeting Card for {self.date.toString()}')
        ax.grid()

        # Save the plot to a file
        fig.savefig("greeting_card.png")

        # Display the plot in a QLabel
        label = QLabel(self)
        label.setGeometry(10, 10, 380, 280)
        label.setPixmap(QtGui.QPixmap("greeting_card.png"))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Important Dates')
        self.setGeometry(100, 100, 300, 400)

        layout = QVBoxLayout()

        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)
        layout.addWidget(self.calendar)

        self.important_dates = [QDate(2024, 8, 1), QDate(2024, 12, 25)]  # Example important dates

        for date in self.important_dates:
            button = QPushButton(date.toString(), self)
            button.clicked.connect(lambda checked, date=date: self.show_greeting_card(date))
            layout.addWidget(button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def show_greeting_card(self, date):
        self.greeting_card_window = GreetingCardWindow(date)
        self.greeting_card_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
