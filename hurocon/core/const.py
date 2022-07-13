from pathlib import Path


LOCAL_CONFIG_PATH = Path.home() / Path('.config/hurocon/config.json')
LOCAL_CONFIG_DEFAULT = {
    "config_version": 3,
    "connection": {
        "address": "http://192.168.8.1/",
        "timeout": 5.0
    },
    "auth": {
        "username": "admin",
        "password": "YWRtaW4="
    }
}
