from PySide6.QtWidgets import QMainWindow, QFileDialog
from gui.qt.MainWindow_ui import Ui_MainWindow
from gui.models.data import getAllServicesName, getHostname, getAllBackupPathsToUI
from gui.models.interfaces.service_interface import startService, stopService, serviceInfo
from gui.models.interfaces.backup_interface import startBackup, addBackupFolderAndOutput, removeFromBackup
from gui.views.add_service_dialog import AddServiceDialog
from gui.views.service_status_dialog import ServiceStatusDialog


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
        self.ui.stopServiceButton.clicked.connect(self._buttonStopService)

    # ========================
    # Button Text
    # ========================

        self.ui.bkpOkButton.setText("Init Backup")
        self.ui.searchFolderButton.setText("Add Folders to Backup")
        self.ui.bkpCancelButton.setText("Remove Backup")

        self.ui.addServiceButton.setText("Add Service")
        self.ui.stopServiceButton.setText("Stop Service")
        self.ui.startServiceButton.setText("Start Service")

        self.ui.sysInfoGetHardwareInfoButton.setText("Hardware Info")
        self.ui.sysInfoGetInstalledSoftwareButton.setText(
            "Instelled Software (Program Files)")
        self.ui.sysInfoGetOsInfoButton.setText("OS info")

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
        if inputDir == '' or inputDir == None:
            return
        outputZip = QFileDialog.getSaveFileName(
            self, options=QFileDialog.Option.DontUseNativeDialog, caption="Save output zip")
        if outputZip == '' or outputZip == None:
            return
        # Add Conf file Edit func.
        addBackupFolderAndOutput(inputDir, outputZip[0])
        self.ui.backupList.clear()
        self._addBackupDataToBackupList()

    def _buttonStartBackup(self):
        """Calls the backup init func"""
        startBackup()

    def _buttonRemoveFromBackup():
        # Add Conf file Edit func
        removeFromBackup()

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
        self.serviceStatusDialog = ServiceStatusDialog()
        if serviceInfo(self.ui.serviceList.currentIndex().data())["CurrentState"] == 4:
            self.serviceStatusDialog.ui.serviceStatusLabel.setText("Service: " + str(self.ui.serviceList.currentIndex().data(
            )) + " Starting... \n" + "Service status: running PID: " + str(serviceInfo(self.ui.serviceList.currentIndex().data())["ProcessId"]))
        else:
            self.serviceStatusDialog.ui.serviceStatusLabel.setText(
                "Service" + str(self.ui.serviceList.currentIndex().data()) + "Starting...\n")
        # print(serviceInfo(self.ui.serviceList.currentIndex().data()))
        self.serviceStatusDialog.show()

    def _buttonStopService(self):
        """Stop the currently selected service on Windows

        Require Admin Rights to stop a service
        """
        # Needs to start a Dialog Window with the status
        # REFACTOR
        stopService(serviceName=self.ui.serviceList.currentIndex().data())
        self.serviceStatusDialog = ServiceStatusDialog()
        if serviceInfo(self.ui.serviceList.currentIndex().data())["CurrentState"] == 3:
            self.serviceStatusDialog.ui.serviceStatusLabel.setText("Service: " + str(self.ui.serviceList.currentIndex().data(
            )) + " Stoping... \n")
        else:
            self.serviceStatusDialog.ui.serviceStatusLabel.setText(
                "Service: " + str(self.ui.serviceList.currentIndex().data()) + " Stoping...\n")
        # print(serviceInfo(self.ui.serviceList.currentIndex().data()))
        self.serviceStatusDialog.show()

    def _buttonAddService(self):
        """Show dialog to create the Service, with some defaults, for easy creation."""
        self.addServiceDialog = AddServiceDialog()
        self.addServiceDialog.show()
