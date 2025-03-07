# SPDX-License-Identifier: BSD-3-Clause
#
# This file is part of Torii-USB.
#
# Copyright (c) 2020 Great Scott Gadgets <info@greatscottgadgets.com>

''' Clock and reset (CAR) controllers for Torii-USB. '''

from torii.hdl import Elaboratable, Module, Signal

class PHYResetController(Elaboratable):
	'''
	Gateware that implements a short power-on-reset pulse to reset an attached PHY.

	I/O ports:

		I: trigger   -- A signal that triggers a reset when high.
		O: phy_reset -- The signal to be delivered to the target PHY.
	'''

	def __init__(self, *, clock_frequency = 60e6, reset_length = 2e-6, stop_length = 2e-6, power_on_reset = True):
		'''

		Parameters
		----------
		reset_length
			The length of a reset pulse, in seconds.

		stop_length
			The length of time STP should be asserted after reset.

		power_on_reset
			If True or omitted, the reset will be applied once the firmware is configured.

		'''

		from math import ceil

		self.power_on_reset = power_on_reset

		# Compute the reset length in cycles.
		clock_period = 1 / clock_frequency
		self.reset_length_cycles = ceil(reset_length / clock_period)
		self.stop_length_cycles  = ceil(stop_length  / clock_period)

		#
		# I/O port
		#
		self.trigger   = Signal()
		self.phy_reset = Signal()
		self.phy_stop  = Signal()

	def elaborate(self, platform):
		m = Module()

		# Counter that stores how many cycles we've spent in reset.
		cycles_in_reset = Signal(range(0, self.reset_length_cycles))

		reset_state = 'RESETTING' if self.power_on_reset else 'IDLE'
		with m.FSM(reset = reset_state, domain = 'sync') as fsm:

			# Drive the PHY reset whenever we're in the RESETTING cycle.
			m.d.comb += [
				self.phy_reset.eq(fsm.ongoing('RESETTING')),
				self.phy_stop.eq(~fsm.ongoing('IDLE'))
			]

			with m.State('IDLE'):
				m.d.sync += cycles_in_reset.eq(0)

				# Wait for a reset request.
				with m.If(self.trigger):
					m.next = 'RESETTING'

			# RESETTING: hold the reset line active for the given amount of time
			with m.State('RESETTING'):
				m.d.sync += cycles_in_reset.eq(cycles_in_reset + 1)

				with m.If(cycles_in_reset + 1 == self.reset_length_cycles):
					m.d.sync += cycles_in_reset.eq(0)
					m.next = 'DEFERRING_STARTUP'

			# DEFERRING_STARTUP: Produce a signal that will defer startup for
			# the provided amount of time. This allows line state to stabilize
			# before the PHY will start interacting with us.
			with m.State('DEFERRING_STARTUP'):
				m.d.sync += cycles_in_reset.eq(cycles_in_reset + 1)

				with m.If(cycles_in_reset + 1 == self.stop_length_cycles):
					m.d.sync += cycles_in_reset.eq(0)
					m.next = 'IDLE'

		return m
