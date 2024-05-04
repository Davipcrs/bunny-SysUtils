from PySide6.QtWidgets import QMainWindow
from gui.qt.MainWindow_ui import Ui_MainWindow
import modules.confMgr.load_conf_file as conf


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._addBackupDataToList()

    def _addBackupDataToList(self):
        data = conf.getBackupDataFromConf()
        dataFolders = data.get("folders")
        dataOutputs = data.get("outputs")
        manipulatedData = []
        i = 0
        for i in range(len(dataFolders)):
            manipulatedData.append(dataFolders[i] + "  -->  " + dataOutputs[i])
            i = i + 1
        self.ui.backupList.addItems(manipulatedData)
