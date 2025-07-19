<!-- markdownlint-disable MD041 -->
```{toctree}
:hidden:

intro
features
install
migration
getting_started
tutorials/index
gateware/index
```

```{toctree}
:caption: Development
:hidden:

Source Code <https://github.com/shrine-maiden-heavy-industries/torii-usb/>
Contributing <https://github.com/shrine-maiden-heavy-industries/torii-usb/blob/main/CONTRIBUTING.md>
changelog
license
```

# Torii-USB: USB Gateware Library

```{warning}
   This documentation is a work in progress and is seriously incomplete!
```

Torii-USB is a fork of the [Luna] USB platform for [Amaranth], it was ported to [Torii] originally under the name [SOL] where it retained all of the platform and SoC machinery.

Later it was broken out into Torii-USB which is just purely the USB gateware, all of the hardware and SoC support has been retained by [SOL], but breaking it out into it's own dedicated library allows for isolating dependencies as needed.

See the Torii-USB to SOL [migration guide] for information on migrating from SOL to Torii-USB.

For more information on Torii-USB, see the [Introduction] and check out the [Getting Started] guide for how to get up and running with Torii-USB.

## Community

The two primary community spots for Torii and by extension Torii USB are the `#torii` IRC channel on [libera.chat] (`irc.libera.chat:6697`) which you can join via your favorite IRC client or the [web chat], and the [discussion forum] on GitHub.

Please do join and share your projects using Torii, ask questions, get help with problems, or discuss development.

[Torii]: https://github.com/shrine-maiden-heavy-industries/torii-hdl
[SOL]: https://github.com/shrine-maiden-heavy-industries/sol
[LUNA]: https://github.com/greatscottgadgets/luna
[Amaranth]: https://github.com/amaranth-lang/amaranth
[migration guide]: ./migration.md
[Introduction]: ./intro.md
[Getting Started]: ./getting_started.md
[libera.chat]: https://libera.chat/
[web chat]: https://web.libera.chat/#torii
[discussion forum]: https://github.com/shrine-maiden-heavy-industries/torii-usb/discussions
