from modules.backup.backups import BackupUtils


def startBackup():
    return BackupUtils().multiBackups()
