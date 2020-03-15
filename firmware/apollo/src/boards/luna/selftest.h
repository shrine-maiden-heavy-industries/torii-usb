/**
 * Self-test & factory validation helpers.
 * This file is part of LUNA.
 */

#ifndef __SELFTEST_H__
#define __SELFTEST_H__

#include <sam.h>


/**
 * Initialize our self-test functionality.
 */
void selftest_init(void);

/**
 * Vendor request that reads the voltage on one of the supply rails.
 */
bool handle_get_rail_voltage(uint8_t rhport, tusb_control_request_t const* request);


#endif
