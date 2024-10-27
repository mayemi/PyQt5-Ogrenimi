import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton, QHBoxLayout
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 400, 400)
        self.setWindowTitle("Qt5")
        self.setWindowIcon(QIcon("ajan.webp"))
        
        hbox = QHBoxLayout()

        button1 = QPushButton("Uyarı")
        button2 = QPushButton("Bilgilendirme")
        button3 = QPushButton("Seçim")

        button1.clicked.connect(self.warningClicked)
        button2.clicked.connect(self.informClicked)
        button3.clicked.connect(self.decisionClicked)

        hbox.addWidget(button1)
        hbox.addWidget(button2)
        hbox.addWidget(button3)

        self.setLayout(hbox)

    def warningClicked(self):
        QMessageBox.warning(self, "Uyarı!", "Bu bir uyarıdır!")
    def informClicked(self):
        QMessageBox.information(self, "Bilgilendirme", "Bu bir bilgilendirmedir!")
    def decisionClicked(self):
        answer = QMessageBox.question(self, "Seçim", "Bu bir seçim ekrandır!", QMessageBox.Yes, QMessageBox.No)
        if answer == QMessageBox.Yes:
            print("Yes")
        else: 
            print("No")

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
