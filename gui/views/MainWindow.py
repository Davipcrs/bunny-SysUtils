from PySide6.QtWidgets import QMainWindow
from gui.qt.MainWindow_ui import Ui_MainWindow
from gui.models.data import getAllServicesName, getHostname
import modules.confMgr.load_conf_file as conf


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._addBackupDataToBackupList()
        self._addServiceDataToServiceList()
        self.ui.endpointCountLabel.setText(str(0))
        self.ui.endpointNameLabel.setText(getHostname())
    # Backup Data/Functions

    def _addBackupDataToBackupList(self):
        # Change Data manipulation to the models folder.
        data = conf.getBackupDataFromConf()
        dataFolders = data.get("folders")
        dataOutputs = data.get("outputs")
        manipulatedData = []
        i = 0
        for i in range(len(dataFolders)):
            manipulatedData.append(dataFolders[i] + "  -->  " + dataOutputs[i])
            i = i + 1
        self.ui.backupList.addItems(manipulatedData)

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
