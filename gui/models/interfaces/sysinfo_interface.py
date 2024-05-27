from modules.sysInfo.sysinfo import SysInfo


def getAllHardwareInfo():
    sys = SysInfo()
    hardware_info = sys.getHardwareInfo()
    # treat the HardwareInfo
    treated_data = {
        "Hostname": hardware_info[0].Name,
        "Domain": hardware_info[0].Domain,
        "Current User": hardware_info[0].UserName,
        "Computer Model": hardware_info[0].Model,
        "Manufacturer": hardware_info[0].Manufacturer,
        "Serial Number": hardware_info[1].SerialNumber,
        "Processor Name": hardware_info[2].Name,
        "Cores": hardware_info[2].NumberOfCores,
        "Threads": hardware_info[2].NumberOfLogicalProcessors,
        "BIOS Manufacturer": hardware_info[3].Manufacturer,
        "BIOS Serial Number": hardware_info[3].SerialNumber,
        "SMBIOSVERSION": hardware_info[3].SMBIOSBIOSVersion,
    }
    return treated_data


def getAllOSInfo():
    sys = SysInfo()
    os_info = sys.getOSInfo()
    pass


def getAllSoftwareInstalledInfo():
    sys = SysInfo()
    installed_software = sys.getSoftwareInstalledInfo()
    treated_data = []
    for data in installed_software:
        treated_data.append(
            str(data.Name) + " -- Win-Version: " + str(data.Version))
    return treated_data
