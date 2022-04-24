# Hurocon
Hurocon *(**hu**awei **ro**uter **con**trol)* - command line interface tool for interacting with Huawei LTE routers


## Features
### Released
- Device Control
  - Reboot
- SMS Control
  - Send

### Planned
- Device Control
  - Information
  - Signal Level
- SMS Control
  - List
  - View


## Supported Devices
Full list of supported devices is available on [this link](https://github.com/Salamek/huawei-lte-api#tested-on).


## Installation
Currently this tool can only be installed with `pip` on `python` >= 3.7. You can install it from PyPi:

```bash
python3 -m pip install hurocon
```

Or directly from this Github repo:

```bash
pip install git+https://github.com/maximilionus/hurocon.git
```

> Built executable mode *(with [pyinstaller](https://pyinstaller.org/))* is planned but no ETA yet


## Special
Big thanks to @Salamek for his [`huawei-lte-api`](https://github.com/Salamek/huawei-lte-api). This api made the whole thing possible.
