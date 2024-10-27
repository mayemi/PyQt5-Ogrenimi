import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMenuBar, QAction
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("ajan.webp"))
        self.setWindowTitle("Qt5")

        menuBar = QMenuBar(self)

        fileMenu = menuBar.addMenu("File")
        editMenu = menuBar.addMenu("Edit")
        selectionMenu = menuBar.addMenu("Selection")

        newTextFileAction = QAction(QIcon("ajan.webp"), "New Text File", self)
        newTextFileAction.setShortcut("Ctrl+N")
        newTextFileAction.triggered.connect(self.actionClicked)

        fileMenu.addAction(newTextFileAction)
        fileMenu.addMenu(editMenu)

        undoAction = QAction(QIcon("ajan.webp"), "Undo", self)
        undoAction.setShortcut("Ctrl+B")
        undoAction.triggered.connect(self.actionClicked)

        editMenu.addAction(undoAction)

    def actionClicked(self):
        print("Tıklandı")

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
