# import time
# import modules.backup.backups as bkp
import multiprocessing
from modules.confMgr.create_conf_file import createConfFile
# import modules.confMgr.load_conf_file as loadConf
# import modules.confMgr.edit_conf_file as e
# import modules.serviceMgr.service_manager as SrvMgr
from gui.gui import gui
from modules.utils.uac import isAdmin, elevate
import os
from gui.models.interfaces.sysinfo_interface import getAllHardwareInfo

"""
def main():
    backup = bkp.BackupUtils()

    data, procs = backup.multiBackups()
    print(data)
    print(procs)
    print(procs[1])
    while True:

        time.sleep(0.3)
        print(backup.totalFiles)

"""


if __name__ == '__main__':
    multiprocessing.freeze_support()
    if isAdmin():
        pass
    else:
        elevate()
    if os.path.exists(".\\config.json"):
        gui()
    else:
        createConfFile()
        gui()
