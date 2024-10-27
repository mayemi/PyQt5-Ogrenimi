import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 400, 400)
        self.setWindowTitle("Qt5")
        self.setWindowIcon(QIcon("ajan.webp"))

        grid = QGridLayout()
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        button3 = QPushButton("Button 3")
        button4 = QPushButton("Button 4")
        button5 = QPushButton("Button 5")
        button6 = QPushButton("Button 6")

        grid.addWidget(button1, 0, 0)  # Widget, row, column
        grid.addWidget(button2, 0, 1)
        grid.addWidget(button3, 0, 2)
        grid.addWidget(button4, 1, 0)
        grid.addWidget(button5, 1, 1)
        grid.addWidget(button6, 1, 2)

        self.setLayout(grid)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())