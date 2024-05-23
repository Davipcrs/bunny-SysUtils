# Needs implementation.
from modules.confMgr.load_conf_file import loadConfFile
import json

def addBackupFolderAndOutput(folder: str, output: str):
    conf = loadConfFile()
    conf["backup_conf"]["folders"].append(folder)
    conf["backup_conf"]["outputs"].append(output)

    with open("config.json", "w") as config:
        json_obj = json.dumps(conf, indent=4)
        config.write(json_obj)

        config.close()
    
    return

def removeBackupFolderAndOutput(index: int):
    conf = loadConfFile()
    return
