from click import echo

from ..core.local_cfg import LocalConfig
from ..core.const import LOCAL_CONFIG_PATH


def config_init_impl():
    cfg = LocalConfig(auto_file_creation=False)

    if not cfg.file_exists():
        if cfg.create_file():
            echo('Configuration file successfully generated at "{}"'
                 .format(LOCAL_CONFIG_PATH)
                 )
        else:
            echo('Can not generate configuration file at "{}"'
                 .format(LOCAL_CONFIG_PATH)
                 )
    else:
        echo('Configuration file already exists on path: "{}"'
             .format(LOCAL_CONFIG_PATH)
             )


def config_remove_impl():
    if LocalConfig.erase_config() is True:
        echo("All local configuration files and dirs successfully erased")
    else:
        echo("No local configuration files detected")


def config_get_path_impl():
    echo(LOCAL_CONFIG_PATH)


def config_exist_impl():
    if LOCAL_CONFIG_PATH.exists() is True:
        echo("Configuration file do exist")
    else:
        echo("Configuration file doesn't exist")
