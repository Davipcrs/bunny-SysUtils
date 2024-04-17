# https://learn.microsoft.com/en-us/windows/win32/wmisdk/wmi-tasks-for-scripts-and-applications
# https://medium.com/@marcovit87/pywin32-and-wmi-windows-mangement-instrumentation-navigating-windows-os-with-python-4a73bfcce59a#:~:text=Windows%20Management%20Instrumentation%20(WMI)%20is,of%20the%20Windows%20API%20functions.
import wmi


class SysInfo():
    def __init__(self, hostname: str = ""):
        self.c = wmi.WMI(hostname)

    def getNetworkInfo(self):

        pass

    def getHardwareInfo():
        pass

    def getOSInfo(self) -> wmi._wmi_object:
        """
        Return a _wmi_object that return a dictonary like data type

        For accessing the data you can use the ."Function"
        Example: SysInfo().getOSInfo().Caption -> Microsoft Windows 11 Home Single Language (Or your OS Type)
        """
        info = []
        for os in self.c.Win32_OperatingSystem():
            # print(os)
            # print(os.Caption)
            info.append(os)
            # print(info)
        return info[0]

    def getSoftwareInstalledInfo():
        pass

    def getUsersInfo():
        pass

    def getSysInfo(self):
        self.getNetworkInfo()
        self.getHardwareInfo()
        self.getOSInfo()
        self.getSoftwareInstalledInfo()
        self.getUsersInfo()

        pass


print(SysInfo().getOSInfo())
# SysInfo().getOSInfo()
