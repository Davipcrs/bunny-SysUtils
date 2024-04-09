from win32 import win32service as winS


class Service():
    def __init__(self, service_name: str, service_display_name: str, binary_path: str) -> None:
        self.service_name = service_name
        self.service_display_name = service_display_name
        self.service_type = winS.SERVICE_WIN32_OWN_PROCESS
        self.service_access = winS.SERVICE_START
        self.service_start_type = winS.SERVICE_AUTO_START
        self.service_error_type = winS.SERVICE_ERROR_SEVERE
        self.binary_path = binary_path

    def setServiceType(self, type: int) -> None:
        """
        Set service Type

        Input: integer (0 to 4)

        0 =

        1 =

        2 =

        3 =

        For details refer to the Microsoft Service Type Docs!

        https://learn.microsoft.com/en-us/dotnet/api/system.serviceprocess.servicetype?view=dotnet-plat-ext-8.0

        https://learn.microsoft.com/en-us/windows/win32/api/winsvc/nf-winsvc-createservicea
        """
        pass

    def setServiceStartType(self, type: int) -> None:
        """
        Set service start Type

        Input: integer (0 to 4)

        0 =

        1 =

        2 =

        3 =

        For details refer to the Microsoft Service Start Type Docs!

        https://learn.microsoft.com/en-us/dotnet/api/system.serviceprocess.servicestartmode?view=dotnet-plat-ext-8.0

        https://learn.microsoft.com/en-us/windows/win32/api/winsvc/nf-winsvc-createservicea
        """
        pass

    def setServiceErrorType(self, type: int) -> None:
        pass

    def setServiceAccessType(self, type: int) -> None:
        pass
