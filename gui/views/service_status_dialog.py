from PySide6.QtWidgets import QDialog
from gui.qt.ServiceStatus_ui import Ui_ServiceStatusDialog


class ServiceStatusDialog(QDialog):
    def __init__(self):
        super(ServiceStatusDialog, self).__init__()
        self.ui = Ui_ServiceStatusDialog()
        self.ui.setupUi(self)
        self.ui.closeServiceStatusDialogButton.clicked.connect(self.close)
        self.ui.closeServiceStatusDialogButton.setText("Close")
