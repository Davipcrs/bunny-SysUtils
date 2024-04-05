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

    def getServiceStatus(self):
        pass

    def setServiceStatus(self):
        pass

    def createService(self):
        pass

    def removeService(self):
        pass

    def editService(self):
        pass
