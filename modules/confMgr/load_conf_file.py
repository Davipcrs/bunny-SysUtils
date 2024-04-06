import json


def loadConfFile() -> dict:
    with open("config.json", "r") as conf:
        data = json.load(conf)
        conf.close()
    return data


def getBackupDataFromConf() -> dict:
    data = loadConfFile()
    return data.get("backup_conf")
