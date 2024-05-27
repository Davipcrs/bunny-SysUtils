from PySide6.QtWidgets import QDialog, QFileDialog
from PySide6.QtCore import QDir
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

        self._initUIText()

    def _initUIText(self):
        self.ui.displayNameLineEdit.setText("Display name (Visual)")
        self.ui.nameLineEdit.setText("Service name (Internal Name)")
        self.ui.pathLineEdit.setText("c:/path/to/exe")
        self.ui.errorTypeComboBox.addItem("Error Type")
        self.ui.startTypeComboBox.addItem("Start Type")
        self.ui.serviceTypeComboBox.addItem("Service Type")

        self.ui.errorTypeComboBox.setEditable(False)
        self.ui.startTypeComboBox.setEditable(False)
        self.ui.serviceTypeComboBox.setEditable(False)

        self.ui.startTypeComboBox.addItem("0. Auto Start - (Default)")
        self.ui.startTypeComboBox.addItem("1. Demand Start")
        self.ui.startTypeComboBox.addItem("2. Disabled Start")

        self.ui.errorTypeComboBox.addItem("0. Ignore Error")
        self.ui.errorTypeComboBox.addItem("1. Normal Error")
        self.ui.errorTypeComboBox.addItem("2. Severe Error - (Default)")
        self.ui.errorTypeComboBox.addItem("3. Critical Error")

        self.ui.serviceTypeComboBox.addItem("0. Own Process - (Default)")
        self.ui.serviceTypeComboBox.addItem("1. Shared Process")
        self.ui.serviceTypeComboBox.addItem("2. Interactive Process")

    def _createServiceButton(self):
        display_name = self.ui.displayNameLineEdit.text()
        srv_name = self.ui.nameLineEdit.text()
        exe_path = self.ui.pathLineEdit.text()

        if self.ui.errorTypeComboBox.currentIndex() != 0:
            error_type = int(
                self.ui.errorTypeComboBox.currentText().split(".")[0])
        else:
            error_type = 2

        if self.ui.startTypeComboBox.currentIndex() != 0:
            start_type = int(
                self.ui.startTypeComboBox.currentText().split(".")[0])
        else:
            start_type = 0

        if self.ui.serviceTypeComboBox.currentIndex() != 0:
            service_type = int(
                self.ui.serviceTypeComboBox.currentText().split(".")[0])
        else:
            service_type = 0

        # createService(service_name=srv_name, service_display_name=display_name, binary_path=exe_path,
        #              error_type=error_type, start_type=start_type, service_type=service_type)

    def _selectExeFileButton(self):
        file_selector = QFileDialog.getOpenFileName(
            self, caption="Select Service Binary", options=QFileDialog.Option.DontUseNativeDialog, filter="Executables (*.exe *.bat)")
        self.ui.pathLineEdit.setText(file_selector[0])
        return

    def _cancelAddServiceButton(self):
        self.close()
