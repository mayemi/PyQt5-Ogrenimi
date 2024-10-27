import sys
from PyQt5.QtWidgets import QWidget, QApplication, QComboBox
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qt5")
        self.setWindowIcon(QIcon("ajan.webp"))

        self.comboBox = QComboBox(self)
        self.comboBox.setGeometry(80, 80, 150, 50)
        self.comboBox.addItem("Seçiniz")
        self.comboBox.addItem("Python")
        self.comboBox.addItem("C++")
        self.comboBox.addItem("JavaScript")

        self.comboBox.model().item(0).setEnabled(False)

        self.comboBox.currentIndexChanged.connect(self.secildi)

    def secildi(self):
        item = self.comboBox.currentText()
        index = self.comboBox.currentIndex()
        print(item, "-" ,index)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
