# SPDX-License-Identifier: BSD-3-Clause

from unittest            import TestCase

from torii.hdl           import Module, Record, Signal
from torii.hdl.rec       import Direction

from torii_usb.test      import ToriiUSBGatewareTestCase, sync_test_case
from torii_usb.utils.cdc import stretch_strobe_signal, synchronize

class StrobeStretcherTest(ToriiUSBGatewareTestCase):
	''' Test case for our strobe stretcher function. '''

	def instantiate_dut(self):
		m = Module()

		# Create a module that only has our stretched strobe signal.
		m.strobe_in = Signal()
		m.stretched_strobe = stretch_strobe_signal(m, m.strobe_in, to_cycles = 2)

		return m

	def initialize_signals(self):
		yield self.dut.strobe_in.eq(0)

	@sync_test_case
	def test_stretch(self):

		# Ensure our stretched strobe stays 0 until it sees an input.
		yield
		self.assertEqual((yield self.dut.stretched_strobe), 0)
		yield
		self.assertEqual((yield self.dut.stretched_strobe), 0)

		# Apply our strobe, and validate that we immediately see a '1'...
		yield self.dut.strobe_in.eq(1)
		yield
		self.assertEqual((yield self.dut.stretched_strobe), 1)

		# ... ensure that 1 lasts for a second cycle ...
		yield self.dut.strobe_in.eq(0)
		yield
		self.assertEqual((yield self.dut.stretched_strobe), 1)

		# ... and then returns to 0.
		yield
		self.assertEqual((yield self.dut.stretched_strobe), 0)

		yield
		self.assertEqual((yield self.dut.stretched_strobe), 0)

class SynchronizedTest(TestCase):

	def test_signal(self):
		m = Module()
		m._MustUse__silence = True
		synchronize(m, Signal())

	def test_directional_record(self):
		m = Module()
		m._MustUse__silence = True

		record = Record([
			('sig_in',  1, Direction.FANIN),
			('sig_out', 1, Direction.FANOUT)
		])
		synchronize(m, record)

	def test_nested_record(self):
		m = Module()
		m._MustUse__silence = True

		record = Record([
			('sig_in',  1, Direction.FANIN),
			('sig_out', 1, Direction.FANOUT),
			('nested', [
				('subsig_in',  1, Direction.FANIN),
				('subsig_out', 1, Direction.FANOUT),
			])
		])
		synchronize(m, record)
