import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt5.QtGui import QIcon, QIntValidator

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(500,200,400,400)
        self.setWindowIcon(QIcon("ajan.webp"))
        self.setWindowTitle("Qt5")

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(80, 80, 150, 40)

        #  self.lineEdit.textChanged.connect(self.printText)

        self.lineEdit.editingFinished.connect(self.printText)

        #  Validator
        self.lineEdit.setValidator(QIntValidator())

        #  Maksimum uzunluk
        self.lineEdit.setMaxLength(8)

        #  Şifreyi gizleme
        self.lineEdit.setEchoMode(QLineEdit.Password)

        #  Placeholder
        self.lineEdit.setPlaceholderText("Şifreyi giriniz.")

        #  Telefon numarası
        #  self.lineEdit.setInputMask('+99-999-999-9999')

    def printText(self):
        print(f"İçerik: {self.lineEdit.text()}")
        print(f"Uzunluk: {self.lineEdit.text().__len__()}")
        
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
