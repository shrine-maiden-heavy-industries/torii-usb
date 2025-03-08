# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

<!--
Unreleased template stuff

## [Unreleased]
### Added
### Changed
### Deprecated
### Removed
### Fixed
### Security
-->

## [Unreleased]

### Added

### Changed

### Deprecated

### Removed

### Fixed

## [v0.7.0]

> [!IMPORTANT]
> This is the first release after the split from [SOL](https://github.com/shrine-maiden-heavy-industries/sol), This is primarily a release to set things up

### Changed

- `sol_usb` and `sol_usb.gateware` are now just `torii_usb`

### Removed

- Built in `StreamInterface` and `StreamArbiter` in favor of Torii's
- Existing examples (for now)
- SoC components
- ILA components
- Platform components
- USB Analyzer component
- Applet components
- cli runner
- `eptri` interface
- flash interface
- jtag interface
- psram interface
- spi interface
- uart interface

[Unreleased]: https://github.com/shrine-maiden-heavy-industries/torii-usb/compare/main...main
[v0.7.0]: https://github.com/shrine-maiden-heavy-industries/torii-usb/compare/e84197f...v0.7.0
