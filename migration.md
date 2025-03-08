# Migration Guide

The migration from [SOL] `v0.5.0` to Torii-USB is very simple. There are just a few minor differences.

* Updated name from `sol_usb` to `torii_usb`.
* Dropping the `.gateware` module.
* Dropping SoC support.
* Removal of a chunk of the `streams` module.

## Updating Imports

If you were not doing anything super involved, then replacing all instances of `sol_usb` and `sol_usb.gateware` with `torii_usb` will be enough.

For instance, the code below:

```py
from sol_usb.usb2                      import USBDevice
from sol_usb.gateware.usb.usb2.request import USBRequestHandler, SetupPacket
from sol_usb.gateware.usb.stream       import USBInStreamInterface, USBOutStreamInterface
from sol_usb.gateware.stream.generator import StreamSerializer
```

Becomes:

```py
from torii_usb.usb2             import USBDevice
from torii_usb.usb.usb2.request import USBRequestHandler, SetupPacket
from torii_usb.usb.stream       import USBInStreamInterface, USBOutStreamInterface
from torii_usb.stream.generator import StreamSerializer

```

## SoC Support

If you were using the SoC support parts of SOL, then continue to do so, SOL is being updated to use `torii_usb` on the backend, but it will retain all public facing API for the SoC components.

## The `streams` Module

The built-in streams module has mostly been subsumed by [Torii]'s [`torii.lib.streams.simple`].

For the most part it's a drop-in replacement, it has `StreamInterface` and `StreamArbiter`, so the `.stream.arbiter` module has been dropped.

For the moment, we still retain the `.stream.generators` module and it's contents, as they have yet to be integrated into Torii.

[SOL]: https://github.com/shrine-maiden-heavy-industries/sol
[Torii]: https://github.com/shrine-maiden-heavy-industries/torii-hdl
[`torii.lib.streams.simple`]: https://github.com/shrine-maiden-heavy-industries/torii-hdl/blob/main/torii/lib/stream/simple.py
