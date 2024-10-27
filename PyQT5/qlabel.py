import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QGridLayout
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qt5")
        self.setWindowIcon(QIcon("ajan.webp"))

        grid = QGridLayout()

        label = QLabel(self)
        label.setText("QLabel")
        label.resize(80, 80)
        label.setStyleSheet("border: 4px solid red; border-radius: 90%;")

        grid.addWidget(label, 0, 0)

        self.setLayout(grid)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())