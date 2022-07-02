# Hurocon Changelog
This project uses [semantic versioning](https://semver.org/). Note that semver principles for this tool are only reflected on public part of it - `cli`. Code of this project may be changed in any **not backwards compatible** way without `MAJOR` version incrementation.


## 0.5.0 : dev
### Added
- `net` commands group
  - `lan` - LAN connection controls
  - `cellular` - Cellular connection controls (Replacement for deprecated `lte` commands group)

### Deprecated
- `lte` commands group deprecated, will be removed in version `1.0.0`


## 0.4.5 : 2022.06.29
### Added
- `device info` command:
  - Export all information in json format by passing the `--json` flag
  - Formatted default mode output

### Changed
- More consistent output for cli help messages


## 0.4.4 : 2022.06.25
### Added
- `sms view` command will not automatically mark viewed message as read. This behavior can be disabled by passing the new `--dont-mark-read` (`-M`) flag to CLI call.

### Changed
- Project structure enhanced

### Fixed
- Help message for the `sms view` command corrected


## 0.4.3 : 2022.05.29
### Fixed
- Added help messages to `sms`: `send` and `view` commands


## 0.4.2 : 2022.05.27
### Fixed
- The last added features are now stated in [README](./README.md)


## 0.4.1 : 2022.05.26
### Fixed
- Project version meta fixed. This version should be considered as version `0.4.0` stable release.


## 0.4.0 : 2022.05.26
### Added
- Inbox SMS messages handling with new commands:
  - `list`
  - `view`
  - `count`
- "Did you mean..." prompt on cli command misspelling

### Changed
- Enhanced `auth login` visualization


## 0.3.1 : 2022.05.09
### Fixed
- Stated new features from `0.3.0` release in project `README`


## 0.3.0 : 2022.05.09
### Added
- New `device info` command to get device information
- New `lte` group with cellular network controls
  - Get current connection status with `status` command
  - Enable or disable connection with `set` command

### Changed
- Project structure enhanced to be more modular

### Fixed
- Misspelling issues in output


## 0.2.0 : 2022.05.03
### Added
- Now any valid `url` address can be used to connect to router, not just `ip`

### Changed
- Authentication password now will be stored more safely
- Configuration file updated to version `2` - automatic merge supported
- License changed to [MIT](./LICENSE)

### Fixed
- Output for `config exist` command will now be displayed properly


## 0.1.0 : 2022.04.25
Package released
