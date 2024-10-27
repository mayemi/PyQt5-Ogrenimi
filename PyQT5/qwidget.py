import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(800, 300, 400, 400)  # Konumu, boyutlar.
        self.setWindowTitle("QWindow")  # Başlık.
        self.setWindowIcon(QIcon("ajan.webp"))  # Ikon.

        self.setFixedHeight(400)  # Sabit, büyümez.
        self.setFixedWidth(400)  # Sabit, büyümez.
        self.setStyleSheet("background-color: purple;")  # Biçimlendirme

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
