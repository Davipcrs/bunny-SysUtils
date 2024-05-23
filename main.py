# import time
# import modules.backup.backups as bkp
from modules.confMgr.create_conf_file import createConfFile
# import modules.confMgr.load_conf_file as loadConf
# import modules.confMgr.edit_conf_file as e
# import modules.serviceMgr.service_manager as SrvMgr
from gui.gui import gui
import os

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
    # e.addBackupFolderAndOutput("E:/src/sh-scripts", "E:/src/sh-scripts.zip")
    if os.path.exists(".\\config.json"):
        gui()
    else:
        createConfFile()

    # main()
    # print(bkp.BackupUtils().multiBackups())
    # print("Compiled")

    # print(r"C:\Program Files (x86)\2DYTDownloader\main.exe")
    # SrvMgr.
