# SPDX-License-Identifier: BSD-3-Clause
#
# This file is part of Torii-USB.
#
# Copyright (c) 2020 Great Scott Gadgets <info@greatscottgadgets.com>
''' Import shortcuts for our most commonly used functionality. '''

# Create shorthands for the most common parts of the library's usb3 gateware.
from .usb.usb3.application.request import SuperSpeedRequestHandler, SuperSpeedRequestHandlerInterface
from .usb.usb3.device              import USBSuperSpeedDevice
from .usb.usb3.endpoints.stream    import SuperSpeedStreamInEndpoint

__all__ = (
	'SuperSpeedRequestHandler',
	'SuperSpeedRequestHandlerInterface',
	'USBSuperSpeedDevice',
	'SuperSpeedStreamInEndpoint',
)
