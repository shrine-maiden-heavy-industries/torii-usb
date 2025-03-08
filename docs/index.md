```{toctree}
:hidden:

intro
features
install
migration
getting_started
tutorials/index
gateware/index

changelog

Source Code <https://github.com/shrine-maiden-heavy-industries/torii-usb/>
```

# Torii-USB: USB Gateware Library

```{warning}
   This documentation is a work in progress and is seriously incomplete!
```

Torii-USB is a fork of the [Luna] USB platform for [Amaranth], it was ported to [Torii] originally under the name [SOL] where it retained all of the platform and SoC machinery.

Later it was broken out into Torii-USB which is just purely the USB gateware, all of the hardware and SoC support has been retained by [SOL], but breaking it out into it's own dedicated library allows for isolating dependencies as needed.

See the Torii-USB to SOL [migration guide] for information on migrating from SOL to Torii-USB.

For more information on Torii-USB, see the [Introduction] and check out the [Getting Started] guide for how to get up and running with Torii-USB.

[Torii]: https://github.com/shrine-maiden-heavy-industries/torii-hdl
[SOL]: https://github.com/shrine-maiden-heavy-industries/sol
[LUNA]: https://github.com/greatscottgadgets/luna
[Amaranth]: https://github.com/amaranth-lang/amaranth
[migration guide]: ./migration.md
[Introduction]: ./intro.md
[Getting Started]: ./getting_started.md
