from win32 import win32service as winS
from modules.serviceMgr.service_defs import Service
# from service_defs import Service

# Refactor later: Support remote computers management


class ServiceManagement():
    def getAllServicesStatus(self) -> tuple:
        """
        Function to list all services status on Windows
        """

        # service_handler: Permission to access the service database and enumarate
        # https://timgolden.me.uk/pywin32-docs/win32service__OpenSCManager_meth.html
        # https://timgolden.me.uk/pywin32-docs/win32service_SC_MANAGER_ENUMERATE_SERVICE.html
        service_handler = winS.OpenSCManager(
            None, None, winS.SC_MANAGER_ENUMERATE_SERVICE)

        # win32Api function to return the status.
        # https://timgolden.me.uk/pywin32-docs/win32service__EnumServicesStatus_meth.html
        return winS.EnumServicesStatus(service_handler)

    def getServiceStatus(self, service_name: str):
        """
        Function to return a service Status for one Specified service.
        """
        scHandle = winS.OpenSCManager(None, None, winS.SC_MANAGER_CONNECT)
        serviceHandle = winS.OpenService(
            scHandle, service_name, winS.SC_MANAGER_ENUMERATE_SERVICE)
        return winS.QueryServiceStatusEx(serviceHandle)

    def createService(self, Service: Service):
        """
        Recive a Service Object and Create the Service.
        """
        scHandle = winS.OpenSCManager(
            None, None, winS.SC_MANAGER_CREATE_SERVICE)
        # print(Service.binary_path)
        srvHandle = winS.CreateService(scHandle, Service.service_name, Service.service_display_name, winS.SERVICE_START, Service.service_type,
                                       Service.service_start_type, Service.service_error_type, Service.binary_path, None, False, None, None, None)

        # https://timgolden.me.uk/pywin32-docs/win32service__CreateService_meth.html
        # https://learn.microsoft.com/pt-br/windows/win32/api/winsvc/nf-winsvc-createservicea
        return srvHandle

    def deleteService(self, service_name: str):
        """
        Delete Service Fuction

        Input: service_name: str (The name of the service that you want to delete)
        """
        # https://timgolden.me.uk/pywin32-docs/win32service__DeleteService_meth.html
        SERVICE_DELETE_CONST = 65536
        # refeer to: https://learn.microsoft.com/pt-br/windows/win32/services/service-security-and-access-rights
        scHandle = winS.OpenSCManager(
            None, None, winS.SC_MANAGER_CONNECT)
        serviceHandle = winS.OpenService(
            scHandle, service_name, SERVICE_DELETE_CONST)
        winS.DeleteService(serviceHandle)

    def startService(self, service_name: str):
        """
        Start Service Fuction

        Input: service_name: str (The name of the service that you want to start)
        """
        scHandle = winS.OpenSCManager(None, None, winS.SC_MANAGER_CONNECT)
        serviceHandle = winS.OpenService(
            scHandle, service_name, winS.SERVICE_START)

        winS.StartService(serviceHandle)
        return

    def stopService(self,  service_name: str):
        scHandle = winS.OpenSCManager(None, None, winS.SC_MANAGER_CONNECT)
        serviceHandle = winS.OpenService(
            scHandle, service_name, winS.SERVICE_CHANGE_CONFIG)

        winS.ControlService(serviceHandle, winS.SERVICE_STOP)
        return

    def editService(self):
        pass


"""
ServiceManagement().createService(Service=Service(
    "Teste", "Teste de serviço", "E:\\src\\python\\Automation\\main.py"))
"""
# ServiceManagement().deleteService("Teste")
