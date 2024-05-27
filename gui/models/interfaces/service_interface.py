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


def createService(service_name: str, service_display_name: str, binary_path: str, error_type: int, start_type: int,  service_type: int):
    srvMgr = ServiceManagement()
    service = Service(service_name=service_name,
                      service_display_name=service_display_name, binary_path=binary_path)
    service.setServiceStartType(start_type)
    service.setServiceType(service_type)
    service.setServiceErrorType(error_type)
    srvMgr.createService(Service=service)
    pass
