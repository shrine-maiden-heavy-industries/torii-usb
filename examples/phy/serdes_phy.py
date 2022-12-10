#!/usr/bin/env python3
# SPDX-License-Identifier: BSD-3-Clause
#
# This file is part of SOL.
#
# Copyright (c) 2020 Great Scott Gadgets <info@greatscottgadgets.com>

''' Incomplete example for working the SerDes-based a PIPE PHY. '''

from torii                        import *

from sol_usb.cli                      import cli
from sol_usb.gateware.usb.devices.ila import (
	USBIntegratedLogicAnalyzer, USBIntegratedLogicAnalyzerFrontend
)

WITH_ILA = False

class PIPEPhyExample(Elaboratable):
	''' Hardware module that demonstrates grabbing a PHY resource with gearing. '''

	def __init__(self):
		if WITH_ILA:
			self.serdes_rx = Signal(32)
			self.ctrl      = Signal(4)
			self.valid     = Signal()
			self.rx_gpio   = Signal()

			self.ila = USBIntegratedLogicAnalyzer(
				bus = 'usb',
				domain = 'ss',
				signals = [
					self.serdes_rx,
					self.ctrl,
					self.valid,
					self.rx_gpio,
				],
				sample_depth = 128,
				max_packet_size = 64
			)

	def emit(self):
		frontend = USBIntegratedLogicAnalyzerFrontend(ila = self.ila)
		frontend.emit_vcd('/tmp/output.vcd')

	def elaborate(self, platform):
		m = Module()
		if WITH_ILA:
			m.submodules.ila = self.ila


		# Generate our domain clocks/resets.
		m.submodules.car = platform.clock_domain_generator()

		# Create our core PIPE PHY. Since PHY configuration is per-board, we'll just ask
		# our platform for a pre-configured USB3 PHY.
		m.submodules.phy = phy = platform.create_usb3_phy()

		if WITH_ILA:

			# Grab the SerDes from our PHY, for debugging.
			serdes = phy.serdes

			m.d.comb += [
				# ILA
				self.serdes_rx.eq(serdes.source.data),
				self.ctrl.eq(serdes.source.ctrl),
				self.valid.eq(serdes.source.valid),
				self.rx_gpio.eq(serdes.rx_gpio),
				self.ila.trigger.eq(~serdes.rx_gpio)
			]

		# Return our elaborated module.
		return m


if __name__ == '__main__':
	ex = cli(PIPEPhyExample)
	if WITH_ILA:
		ex.emit()
