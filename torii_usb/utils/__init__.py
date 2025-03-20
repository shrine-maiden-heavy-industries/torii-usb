# SPDX-License-Identifier: BSD-3-Clause
#
# This file is part of Torii-USB.
#

''' Simple utility constructs for Torii-USB. '''

from warnings  import warn

from torii.hdl import Signal

from .cdc      import synchronize

__all__ = [
	'rising_edge_detected', 'falling_edge_detected', 'any_edge_detected',
	'past_value_of', 'synchronize'
]

def _single_edge_detector(m, signal, *, domain, edge = 'rising'):
	''' Generates and returns a signal that goes high for a cycle upon a given edge of a given signal. '''

	# Create a one-cycle delayed version of our input signal.
	delayed = Signal()
	m.d[domain] += delayed.eq(signal)

	# And create a signal that detects edges on the relevant signal.
	edge_detected = Signal()
	if edge == 'falling':
		m.d.comb += edge_detected.eq(delayed & ~signal)
	elif edge == 'rising':
		m.d.comb += edge_detected.eq(~delayed & signal)
	elif edge == 'any':
		m.d.comb += edge_detected.eq(delayed != signal)
	else:
		raise ValueError('edge must be one of {rising,falling,any}')

	return edge_detected

def past_value_of(m, signal, *, domain):
	''' Generates and returns a signal that represents the value of another signal a cycle ago. '''

	warn(
		'past_value_of has been deprecated and will be removed in a future release, '
		'please use the \'torii.hdl.Past\' construct instead',
		DeprecationWarning,
		stacklevel = 2
	)
	# Create a one-cycle delayed version of our input signal.
	delayed = Signal()
	m.d[domain] += delayed.eq(signal)

	return delayed

def rising_edge_detected(m, signal, *, domain = 'sync'):
	''' Generates and returns a signal that goes high for a cycle each rising edge of a given signal. '''

	warn(
		'rising_edge_detected has been deprecated and will be removed in a future release, '
		'please use the \'torii.hdl.Rose\' construct instead',
		DeprecationWarning,
		stacklevel = 2
	)
	return _single_edge_detector(m, signal, edge = 'rising', domain = domain)

def falling_edge_detected(m, signal, *, domain = 'sync'):
	''' Generates and returns a signal that goes high for a cycle each rising edge of a given signal. '''

	warn(
		'falling_edge_detected has been deprecated and will be removed in a future release, '
		'please use the \'torii.hdl.Fell\' construct instead',
		DeprecationWarning,
		stacklevel = 2
	)
	return _single_edge_detector(m, signal, edge = 'falling', domain = domain)

def any_edge_detected(m, signal, *, domain = 'sync'):
	''' Generates and returns a signal that goes high for a cycle each rising edge of a given signal. '''

	warn(
		'any_edge_detected has been deprecated and will be removed in a future release, '
		'please use the \'torii.hdl.Edge\' construct instead',
		DeprecationWarning,
		stacklevel = 2
	)
	return _single_edge_detector(m, signal, edge = 'any', domain = domain)
