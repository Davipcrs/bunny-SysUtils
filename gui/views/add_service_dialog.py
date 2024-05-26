from PySide6.QtWidgets import QDialog
from gui.qt.AddService_ui import Ui_addServiceDialog
from gui.models.interfaces.service_interface import createService


class AddServiceDialog(QDialog):
    def __init__(self):
        super(AddServiceDialog, self).__init__()
        self.ui = Ui_addServiceDialog()
        self.ui.setupUi(self)
        self.ui.selectExe.clicked.connect(self._selectExeFileButton)
        self.ui.confirmAddService.clicked.connect(self._createServiceButton)
        self.ui.cancelAddService.clicked.connect(self._cancelAddServiceButton)

        self.ui.displayNameLineEdit.setText("Display name (Visual)")
        self.ui.nameLineEdit.setText("Service name (Internal Name)")
        self.ui.pathLineEdit.setText("c:/path/to/exe")
        self.ui.errorTypeComboBox.addItem("Error Type")
        self.ui.startTypeComboBox.addItem("Start Type")
        self.ui.serviceTypeComboBox.addItem("Service Type")

    def _createServiceButton(self):
        self.ui.displayNameLineEdit
        self.ui.nameLineEdit
        self.ui.pathLineEdit
        self.ui.errorTypeComboBox
        self.ui.startTypeComboBox
        self.ui.serviceTypeComboBox
        createService()

    def _selectExeFileButton():
        pass

    def _cancelAddServiceButton(self):
        self.close()
