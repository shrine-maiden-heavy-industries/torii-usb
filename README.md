# Torii-USB

> [!IMPORTANT]
> Please see the Torii-USB to SOL [migration guide] for information on migrating from SOL
> to Torii-USB.

Torii-USB is a fork of the [Luna] USB platform for [Amaranth], it was ported to [Torii] originally under the name [SOL] where it retained all of the platform and SoC machinery.

Later it was broken out into Torii-USB which is just purely the USB gateware, all of the hardware and SoC support has been retained by [SOL], but breaking it out into it's own dedicated library allows for isolating dependencies as needed.

## Installation

Please see the [installation instructions] on the [online documentation]

## License

The Torii-USB gateware is released under the [BSD-3-Clause], the full text of which can be found in the [`LICENSE`] file.

The Torii-USB documentation is released under the [CC-BY-4.0], the full text of which can be found in the [`LICENSE.docs`] file.

[migration guide]: https://torii-usb.shmdn.link/migration.html
[Luna]: https://github.com/greatscottgadgets/luna/
[Amaranth]: https://github.com/amaranth-lang
[Torii]: https://github.com/shrine-maiden-heavy-industries/torii-hdl
[SOL]: https://github.com/shrine-maiden-heavy-industries/sol
[installation instructions]: https://torii-usb.shmdn.link/install.html
[online documentation]: https://torii-usb.shmdn.link/
[BSD-3-Clause]: https://spdx.org/licenses/BSD-3-Clause.html
[`LICENSE`]: ./LICENSE
[CC-BY-4.0]: https://creativecommons.org/licenses/by/4.0/
[`LICENSE.docs`]: ./LICENSE.docs
