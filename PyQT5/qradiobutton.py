import sys
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QHBoxLayout
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(500,200,400,400)
        self.setWindowIcon(QIcon("ajan.webp"))
        self.setWindowTitle("Qt5")

        hbox = QHBoxLayout()

        radioButton1 = QRadioButton(text = "Python")
        radioButton1.setChecked(True)
        radioButton1.toggled.connect(self.secildi)
        radioButton2 = QRadioButton(text = "C++")
        radioButton2.toggled.connect(self.secildi)
        radioButton3 = QRadioButton(text = "JavaScript")
        radioButton3.toggled.connect(self.secildi)

        hbox.addWidget(radioButton1)
        hbox.addWidget(radioButton2)
        hbox.addWidget(radioButton3)

        self.setLayout(hbox)

    def secildi(self):
        button = self.sender()
        if not button.isChecked():
            print(f"{button.text()} seçimi kaldırıldı!")
        else:
            print(f"{button.text()} seçildi!")

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
