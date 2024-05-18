from modules.backup.backups import BackupUtils
import modules.confMgr.load_conf_file as conf
from modules.serviceMgr.service_manager import ServiceManagement, Service
from modules.sysInfo.sysinfo import SysInfo


def getAllServicesName():
    srvMgr = ServiceManagement()
    rawData = srvMgr.getAllServicesStatus()
    servicesNames = []
    for data in rawData:
        servicesNames.append(data[1])

    return servicesNames


def getAllBackupPathsToUI():
    data = conf.getBackupDataFromConf()
    dataFolders = data.get("folders")
    dataOutputs = data.get("outputs")
    manipulatedData = []
    i = 0
    for i in range(len(dataFolders)):
        manipulatedData.append(dataFolders[i] + "  -->  " + dataOutputs[i])
        i = i + 1
    return manipulatedData


def getHostname():
    return SysInfo().getHostname()


def startBackup():
    return BackupUtils().multiBackups()
