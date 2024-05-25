from modules.backup.backups import BackupUtils
from modules.confMgr.edit_conf_file import addBackupFolderAndOutput


def startBackup():
    return BackupUtils().multiBackups()


def removeFromBackup(index: int):
    # Remove the data from JSON based in the List index.
    return
