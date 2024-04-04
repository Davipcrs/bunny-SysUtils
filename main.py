import modules.confMgr.load_conf_file as conf
import modules.backup.backups as bkp
import multiprocessing


if __name__ == '__main__':
    # main()
    print(bkp.BackupUtils().multiBackups())
