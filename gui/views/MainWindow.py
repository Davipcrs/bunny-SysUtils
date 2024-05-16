from PySide6.QtWidgets import QMainWindow
from gui.qt.MainWindow_ui import Ui_MainWindow
from gui.models.data import getAllServicesName, getHostname, getAllBackupPathsToUI
from gui.views.AddServiceDialog import AddServiceDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._addBackupDataToBackupList()
        self._addServiceDataToServiceList()
        self.ui.endpointCountLabel.setText(str(0))
        self.ui.endpointNameLabel.setText(getHostname())
        self.ui.addServiceButton.clicked.connect(self._buttonAddService)
    # Backup Data/Functions

    def _addBackupDataToBackupList(self):
        self.ui.backupList.addItems(getAllBackupPathsToUI())

    # Service Data/Functions

    def _addServiceDataToServiceList(self):
        self.ui.serviceList.addItems(getAllServicesName())

    # Backup Buttons:

    def _buttonAddFolderToBackup():
        pass

    def _buttonStartBackup():
        pass

    def _buttonRemoveFromBackup():
        pass

    # Service Buttons:

    def _buttonStartService():
        pass

    def _buttonStopService():
        pass

    def _buttonAddService(self):
        self.addServiceDialog = AddServiceDialog()
        self.addServiceDialog.show()
