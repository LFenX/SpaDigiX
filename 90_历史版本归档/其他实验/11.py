scroll_area = QScrollArea()
central_widget = QWidget()
layout = QVBoxLayout()
horizontal_layout = QHBoxLayout()
central_widget.setStyleSheet("background-image: url(AAA.png); background-repeat: no-repeat;")
layout.setContentsMargins(0, 0, 0, 0)
for row in range(3):
    for col in range(3):
        frame = QFrame()
        frame.setFrameShape(QFrame.Shape.Box)
        frame.setLineWidth(2)
        frame.setMidLineWidth(2)
        frame.setFixedSize(235, 175)
        frame.setStyleSheet("border: none;background-color: transparent;")
        label = QLabel(f"格子 {row + 1}-{col + 1}")
        if row == 1 and col == 1:
            # 创建一个内部的二维布局
            inner_layout = QGridLayout()

            output1 = QLineEdit()
            output1.setStyleSheet("background-color: white; border: 2px solid black;")
            output1.setFixedSize(53, 30)  # 设置宽度和高度
            output1.setAlignment(Qt.AlignmentFlag.AlignCenter)
            output2 = QLineEdit()
            output2.setStyleSheet("background-color: white; border: 2px solid black;")
            output2.setAlignment(Qt.AlignmentFlag.AlignCenter)
            output2.setFixedSize(53, 45)  # 设置宽度和高度
            output1.setReadOnly(True)
            output2.setReadOnly(True)
            font = QFont('SimSun', 11)
            output1.setAlignment(Qt.AlignmentFlag.AlignCenter)
            output1.setFont(font)
            output2.setAlignment(Qt.AlignmentFlag.AlignCenter)
            output2.setFont(font)
            output1.setStyleSheet("border: none;color:red")
            output2.setStyleSheet("border: none;")
            box_names = [f"output_{row}_{col}_1", f"output_{row}_{col}_2"]
            self.output_boxes.update(
                {name: output for name, output in zip(box_names, [output1, output2])})
            '''
            out1 = QLineEdit()
            out2 = QLineEdit()
            out2.setReadOnly(True)
            out1.setReadOnly(True)
            out1.setFixedSize(33, 30)  # 设置宽度和高度
            out2.setFixedSize(33, 40)  # 设置宽度和高度
            out2.setSt