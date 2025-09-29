<!-- markdownlint-disable MD024 -->
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

> [!IMPORTANT]
> The minimum Python version for Torii and Torii USB is now 3.11

### Added

### Changed

- Switched from using the old setuptools `setup.py` over to setuptools via `pyproject.toml`

### Deprecated

### Removed

### Fixed

## [0.8.1] - 2025-09-29

### Fixed

- Fixed the WindowsRequestHandler not synthesising due to a signed-unsigned conversion error, and having not been updated for an API change in the request handler system (`handlerCondition` -> `handler_condition`)

## [0.8.0] - 2025-06-26

This is a maintenance release, syncs the minimum [Torii] version to `0.8.0` in preparation for
the Torii `1.0.0` release in the future.

### Changed

- Bumped Torii minimum version from `0.7.7` to `0.8.0`

### Deprecated

- Preemptively deprecated `torii_usb.stream.generator` as the contents will be merged into the [Torii] `torii.lib.streams.simple` library in the near future.

### Removed

- Removed the `torii_usb.utils.io` module, as the only member `delay` was FPGA specific, and not used elsewhere within the codebase, it was moved over to [SOL], where it was the only known consumer.

## [0.7.1] - 2025-03-11

## Changed

- Bumped Torii minimum version from `0.7.6` to `0.7.7`

## [0.7.0] - 2025-03-07

> [!IMPORTANT]
> This is the first release after the split from [SOL], This is primarily a release to set things up

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

[Unreleased]: https://github.com/shrine-maiden-heavy-industries/torii-usb/compare/v0.8.1...main
[0.8.1]: https://github.com/shrine-maiden-heavy-industries/torii-usb/compare/v0.8.0..v0.8.1
[0.8.0]: https://github.com/shrine-maiden-heavy-industries/torii-usb/compare/v0.7.1..v0.8.0
[0.7.1]: https://github.com/shrine-maiden-heavy-industries/torii-usb/compare/v0.7.0..v0.7.1
[0.7.0]: https://github.com/shrine-maiden-heavy-industries/torii-usb/compare/e84197f...v0.7.0
[SOL]: https://github.com/shrine-maiden-heavy-industries/sol
[Torii]: https://github.com/shrine-maiden-heavy-industries/torii-hdl
