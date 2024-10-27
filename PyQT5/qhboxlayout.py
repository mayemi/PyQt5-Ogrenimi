import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(500,200,400,400)
        self.setWindowIcon(QIcon("ajan.webp"))
        self.setWindowTitle("Qt5")

        hbox = QHBoxLayout()
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        button3 = QPushButton("Button 3")

        hbox.addWidget(button1)
        hbox.addWidget(button2)
        hbox.addWidget(button3)
        
        self.setLayout(hbox)
        
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
