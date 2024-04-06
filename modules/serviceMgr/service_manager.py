from win32 import win32service as winS


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

        To use this function is needed ADMIN RIGHTS or OWNERSHIP of The Service.
        """
        scHandle = winS.OpenSCManager(None, None, winS.SC_MANAGER_CONNECT)
        serviceHandle = winS.OpenService(
            scHandle, service_name, winS.SC_MANAGER_ALL_ACCESS)  # REQUIRE ADMIN RIGHTS
        return winS.QueryServiceStatusEx(serviceHandle)

    def createService(self):
        pass

    def removeService(self):
        pass

    def editService(self):
        pass

    def startService(self):
        pass

    def stopService(self):
        pass


print(ServiceManagement().getServiceStatus("BDAppSrv"))
