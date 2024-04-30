from PySide6.QtWidgets import QApplication
import sys
from gui.views.MainWindow import MainWindow


def gui():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
