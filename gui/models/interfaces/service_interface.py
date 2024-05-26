from modules.serviceMgr.service_manager import ServiceManagement, Service


def startService(serviceName: str):
    srvMgr = ServiceManagement()
    rawData = srvMgr.getAllServicesStatus()
    servicesNames = []
    for data in rawData:
        servicesNames.append(data[1])

    serviceHandle = srvMgr.startService(
        rawData[servicesNames.index(serviceName)][0])

    return serviceHandle


def stopService(serviceName: str):
    srvMgr = ServiceManagement()
    rawData = srvMgr.getAllServicesStatus()
    servicesNames = []
    for data in rawData:
        servicesNames.append(data[1])

    serviceHandle = srvMgr.stopService(
        rawData[servicesNames.index(serviceName)][0])

    return serviceHandle


def serviceInfo(serviceName: str):
    srvMgr = ServiceManagement()
    return srvMgr.getServiceStatus(service_name=serviceName)


def createService():
    pass
