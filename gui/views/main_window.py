from PySide6.QtWidgets import QMainWindow, QFileDialog
from gui.qt.MainWindow_ui import Ui_MainWindow
from gui.models.data import getAllServicesName, getHostname, getAllBackupPathsToUI
from gui.models.interfaces.service_interface import startService, stopService
from gui.models.interfaces.backup_interface import startBackup
from gui.views.add_service_dialog import AddServiceDialog


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
        self.ui.searchFolderButton.clicked.connect(
            self._buttonAddDirectoryToBackup)
        self.ui.bkpOkButton.clicked.connect(
            self._buttonStartBackup)  # Refactor
        self.ui.startServiceButton.clicked.connect(self._buttonStartService)

    # ========================
    # Backup Data/Functions
    # ========================

    def _addBackupDataToBackupList(self):
        """Add the backup conf file in the backup list

        Format input_folder --> output.zip

        """
        self.ui.backupList.addItems(getAllBackupPathsToUI())

    # ========================
    # Service Data/Functions
    # ========================

    def _addServiceDataToServiceList(self):
        """Add the services names in the service list"""
        self.ui.serviceList.addItems(getAllServicesName())

    # ========================
    # Backup Buttons
    # ========================

    def _buttonAddDirectoryToBackup(self):
        """Show dialog file dialog for adding the backup input folder and the backup output zip file."""
        # https://stackoverflow.com/questions/74557955/how-to-get-a-directory-path-in-pyqt6-via-qfiledialog
        inputDir = QFileDialog.getExistingDirectory(
            self,  options=QFileDialog.Option.DontUseNativeDialog, caption="Select directory",)
        outputZip = QFileDialog.getSaveFileName(
            self, options=QFileDialog.Option.DontUseNativeDialog, caption="Save output zip")
        # Add Conf file Edit func.
        print(inputDir)
        print(outputZip)

    def _buttonStartBackup():
        """Calls the backup init func"""
        startBackup()
        pass

    def _buttonRemoveFromBackup():
        # Add Conf file Edit func
        pass

    # ========================
    # Service Buttons
    # ========================

    def _buttonStartService(self):
        """Start the currently selected service on Windows

        Require Admin Rights to start a service
        """
        # Needs to start a Dialog Window with the status
        # print(self.ui.serviceList.currentIndex().data())
        startService(serviceName=self.ui.serviceList.currentIndex().data())

    def _buttonStopService(self):
        """Stop the currently selected service on Windows

        Require Admin Rights to stop a service
        """
        # Needs to start a Dialog Window with the status
        stopService(serviceName=self.ui.serviceList.currentIndex().data())
        pass

    def _buttonAddService(self):
        """Show dialog to create the Service, with some defaults, for easy creation."""
        self.addServiceDialog = AddServiceDialog()
        self.addServiceDialog.show()
