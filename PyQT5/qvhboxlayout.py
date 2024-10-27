import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(500,200,400,400)
        self.setWindowIcon(QIcon("ajan.webp"))
        self.setWindowTitle("Qt5")

        vbox = QVBoxLayout()  # Dikey
        hbox = QHBoxLayout()  # Yatay
        hbox2 = QHBoxLayout()

        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        hbox.addWidget(button1)
        hbox.addWidget(button2)

        button3 = QPushButton("Button 3")
        button4 = QPushButton("Button 4")
        hbox2.addWidget(button3)
        hbox2.addWidget(button4)

        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)
        self.setLayout(vbox)
        
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
