from modules.backup.backups import BackupUtils
from modules.serviceMgr.service_manager import ServiceManagement, Service
from modules.sysInfo.sysinfo import SysInfo


def getAllServicesName():
    srvMgr = ServiceManagement()
    rawData = srvMgr.getAllServicesStatus()
    servicesNames = []
    for data in rawData:
        servicesNames.append(data[1])

    return servicesNames


def getHostname():
    return SysInfo().getHostname()
