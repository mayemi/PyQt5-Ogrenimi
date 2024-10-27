import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(500,200,400,400)
        self.setWindowIcon(QIcon("ajan.webp"))
        self.setWindowTitle("Qt5")
        
        button = QPushButton(self)
        button.setText("Tıkla")
        #button.move(200, 200)
        button.setGeometry(20, 20, 100, 100)
        button.setIcon(QIcon("ajan.webp"))
        button.setIconSize(QSize(50, 50))
        button.setFont(QFont("Sanserif", 14))
        button.setStyleSheet("background-color: red; border: 2px solid gray; border-radius: 12px;")
        button.clicked.connect(self.onClick)

        button2 = QPushButton(self)
        button2.setText("Tıkla")
        #button2.move(200, 200)
        button2.setGeometry(300, 300, 100, 100)
        button2.setIcon(QIcon("ajan.webp"))
        button2.setIconSize(QSize(50, 50))
        button2.setFont(QFont("Sanserif", 14))
        button2.setStyleSheet("background-color: black; border: 2px solid gray; border-radius: 12px; color: white;")
        button2.clicked.connect(self.second_onClick)

    def onClick(self):
        print("Butona tıklandı!")

    def second_onClick(self):
        print("İkinci butona tıklandı!")

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())