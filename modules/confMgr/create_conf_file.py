import json


def createConfFile():
    configDict = {
        "backup_conf": {
            "folders": [],
            "outputs": [],
            "day_bkp_frequency": 0,
            "enable": True,
            "init_date": "DD/MM/YYYY",
        },
    }
    with open("conf.json", "w") as config:
        json_obj = json.dumps(configDict, indent=4)
        config.write(json_obj)

        config.close()


# createConfFile()

def createServiceFile():
    pass
