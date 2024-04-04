import json


def createConfFile():
    configDict = {
        "backup_conf": {
            "folders": ["E:\Teste"],
            "outputs": [],
            "bkp_frequency": 0,
            "enable": False,

        },
        "service_manager_conf": {},
    }
    with open("config.json", "w") as config:
        json_obj = json.dumps(configDict, indent=4)
        config.write(json_obj)

        config.close()


createConfFile()
