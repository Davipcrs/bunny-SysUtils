import time
import modules.backup.backups as bkp
import modules.confMgr.create_conf_file as createConf
import modules.confMgr.load_conf_file as loadConf
import modules.serviceMgr.service_manager as SrvMgr
from gui.gui import gui

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
    gui()
    # main()
    # print(bkp.BackupUtils().multiBackups())
    # print("Compiled")

    # print(r"C:\Program Files (x86)\2DYTDownloader\main.exe")
    # SrvMgr.
    pass
