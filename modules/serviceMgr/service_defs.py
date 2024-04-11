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

        Input: integer (0 to 2)

        0 = Win32OwnProcess (Default)

        1 = Win32ShareProcess

        2 = InteractiveProcess

        For details refer to the Microsoft Service Type Docs!

        https://learn.microsoft.com/en-us/dotnet/api/system.serviceprocess.servicetype?view=dotnet-plat-ext-8.0

        https://learn.microsoft.com/en-us/windows/win32/api/winsvc/nf-winsvc-createservicea
        """
        if type == 0:
            self.service_type = winS.SERVICE_WIN32_OWN_PROCESS
        elif type == 1:
            self.service_type = winS.SERVICE_WIN32_SHARE_PROCESS
        elif type == 2:
            self.service_type = winS.SERVICE_INTERACTIVE_PROCESS
        else:
            return

    def setServiceStartType(self, type: int) -> None:
        """
        Set service start Type

        Input: integer (0 to 2)

        0 = SERVICE_AUTO_START (Default)

        1 = SERVICE_DEMAND_START

        2 = SERVICE_DISABLED

        For details refer to the Microsoft Service Start Type Docs!

        https://learn.microsoft.com/en-us/dotnet/api/system.serviceprocess.servicestartmode?view=dotnet-plat-ext-8.0

        https://learn.microsoft.com/en-us/windows/win32/api/winsvc/nf-winsvc-createservicea
        """

        if type == 0:
            self.service_type = winS.SERVICE_AUTO_START
        elif type == 1:
            self.service_type = winS.SERVICE_DEMAND_START
        elif type == 2:
            self.service_type = winS.SERVICE_DISABLED
        else:
            return

    def setServiceErrorType(self, type: int) -> None:
        """
        Set service Error Type

        Input: integer (0 to 3)

        0 = SERVICE_ERROR_IGNORE

        1 = SERVICE_ERROR_NORMAL

        2 = SERVICE_ERROR_SEVERE (Default)

        3 = SERVICE_ERROR_CRITICAL

        For details refer to the Microsoft Service Error Type Docs!

        https://learn.microsoft.com/en-us/windows/win32/api/winsvc/nf-winsvc-createservicea
        """
        if type == 0:
            self.service_type = winS.SERVICE_ERROR_IGNORE
        elif type == 1:
            self.service_type = winS.SERVICE_ERROR_NORMAL
        elif type == 2:
            self.service_type = winS.SERVICE_ERROR_SEVERE
        elif type == 3:
            self.service_type = winS.SERVICE_ERROR_CRITICAL
        else:
            return
