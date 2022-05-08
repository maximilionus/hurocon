# Hurocon Changelog
This project uses [semantic versioning](https://semver.org/)


## 0.3.0dev
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
