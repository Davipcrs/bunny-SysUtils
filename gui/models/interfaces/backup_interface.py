from modules.backup.backups import BackupUtils
from modules.confMgr.edit_conf_file import addBackupFolderAndOutput


def startBackup():
    return BackupUtils().multiBackups()
