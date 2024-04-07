from win32 import win32service as winS
from modules.serviceMgr.service_defs import Service
# from service_defs import Service


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
        print(Service.binary_path)
        winS.CreateService(scHandle, Service.service_name, Service.service_display_name, winS.SERVICE_ALL_ACCESS, Service.service_type,
                           Service.service_start_type, Service.service_error_type, Service.binary_path, None, False, None, None, None)

        # https://timgolden.me.uk/pywin32-docs/win32service__CreateService_meth.html
        # Create a ServiceDefine Class to input use for creating the service.
        pass

    def removeService(self):
        pass

    def editService(self):
        pass

    def startService(self):
        pass

    def stopService(self):
        pass


"""
ServiceManagement().createService(Service=Service(
    "Teste", "Teste de serviço", "E:\\src\\python\\Automation\\main.py"))
"""
