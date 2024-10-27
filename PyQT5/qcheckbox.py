import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QHBoxLayout
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(500,200,400,400)
        self.setWindowIcon(QIcon("ajan.webp"))
        self.setWindowTitle("Qt5")

        hbox = QHBoxLayout()
        checkbox1 = QCheckBox(text="Python")
        checkbox1.stateChanged.connect(self.picked)
        checkbox2 = QCheckBox(text="C++")
        checkbox2.stateChanged.connect(self.picked)
        checkbox3 = QCheckBox(text="JavaScript")
        checkbox3.stateChanged.connect(self.picked)

        hbox.addWidget(checkbox1)
        hbox.addWidget(checkbox2)
        hbox.addWidget(checkbox3)

        self.setLayout(hbox)

    def picked(self):
        checkbox = self.sender()
        if checkbox.isChecked():
            print(f"{checkbox.text()} seçildi.")
        else:
            print(f"{checkbox.text()} seçimi kaldırıldı.")

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
