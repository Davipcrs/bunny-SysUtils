from PySide6.QtWidgets import QDialog
from gui.qt.AddService_ui import Ui_addServiceDialog


class AddServiceDialog(QDialog):
    def __init__(self):
        super(AddServiceDialog, self).__init__()
        self.ui = Ui_addServiceDialog()
        self.ui.setupUi(self)
