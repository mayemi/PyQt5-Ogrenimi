import sys
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("ajan.webp"))
        self.setWindowTitle("Qt5")

        self.listWidget = QListWidget(self)       
        self.listWidget.insertItem(0, "Python")
        self.listWidget.insertItem(1, "C++")
        self.listWidget.insertItem(2, "JavaScript")
        self.listWidget.clicked.connect(self.onClick)

    def onClick(self):
        item = self.listWidget.currentItem()
        print(item.text())

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())