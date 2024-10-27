import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 400, 400)
        self.setWindowTitle("Qt5")
        self.setWindowIcon(QIcon("ajan.webp"))
        
        table = QTableWidget(self)
        table.setGeometry(10, 10, 400, 400)
        table.setRowCount(3)
        table.setColumnCount(3)

        table.setEditTriggers(QTableWidget.NoEditTriggers)  # Dışardan müdahaleyi önleme
        
        ad = QTableWidgetItem("İsim")
        soyad = QTableWidgetItem("Soyisim")
        puan = QTableWidgetItem("Puan")

        table.setItem(0, 0, ad)
        table.setItem(0, 1, soyad)
        table.setItem(0, 2, puan)

        table.setItem(1, 0, QTableWidgetItem("Kayra"))
        table.setItem(1, 1, QTableWidgetItem("Kayıran"))
        table.setItem(1, 2, QTableWidgetItem("100"))

        table.setItem(2, 0, QTableWidgetItem("Ogün"))
        table.setItem(2, 1, QTableWidgetItem("Birinci"))
        table.setItem(2, 2, QTableWidgetItem("85"))

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
