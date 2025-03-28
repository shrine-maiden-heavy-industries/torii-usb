# Status & Support

The Torii-USB library is a work in progress; but many of its features are usable enough for inclusion in your own designs.
More testing of our work -- and more feedback -- is always appreciated!

## Support for Device Mode

```{eval-rst}

+-------------------------------------+---------------------------------------+-----------------------------+
| Feature                                                                     | Status                      |
+=====================================+=======================================+=============================+
| **USB Communications**              | High/Full-Speed w/ ``UTMI`` PHY       | Complete; Needs Testing     |
+-------------------------------------+---------------------------------------+-----------------------------+
|                                     | High/Full-Speed w/ ``ULPI`` PHY       | Feature Complete            |
+-------------------------------------+---------------------------------------+-----------------------------+
|                                     | Full-Speed w/ raw ``GPIO``/Resistors  | Feature Complete            |
+-------------------------------------+---------------------------------------+-----------------------------+
|                                     | Super-Speed w/ ``PIPE`` PHY           | Experimental                |
+-------------------------------------+---------------------------------------+-----------------------------+
|                                     | Super-Speed w/ ``SerDes`` PHY         | In-Progress                 |
+-------------------------------------+---------------------------------------+-----------------------------+
|                                     | Low-Speed w/ ``UTMI``/``ULPI`` PHY    | Untested                    |
+-------------------------------------+---------------------------------------+-----------------------------+
|                                     | Low-Speed w/ raw ``GPIO``/Resistors   | Unsupported                 |
+-------------------------------------+---------------------------------------+-----------------------------+
| **Control Transfers / Endpoints**   | User-Defined                          | Feature Complete            |
+-------------------------------------+---------------------------------------+-----------------------------+
|                                     | Full-gateware w/ User Request Handler | Complete; Needs Improvement |
+-------------------------------------+---------------------------------------+-----------------------------+
| **Bulk Transfers / Endpoints**      | User-Defined                          | Feature Complete            |
+-------------------------------------+---------------------------------------+-----------------------------+
|                                     | ``IN`` Stream Helpers                 | Feature Complete            |
+-------------------------------------+---------------------------------------+-----------------------------+
|                                     | ``OUT`` Stream Helpers                | Feature Complete            |
+-------------------------------------+---------------------------------------+-----------------------------+
| **Interrupt Transfers / Endpoints** | User-Defined                          | Feature Complete            |
+-------------------------------------+---------------------------------------+-----------------------------+
|                                     | Status-to-Host Helpers                | Feature Complete            |
+-------------------------------------+---------------------------------------+-----------------------------+
|                                     | Status-from-Host Helpers              | Planned                     |
+-------------------------------------+---------------------------------------+-----------------------------+
|**Isochronous Transfers / Endpoints**| User-Defined                          | Planned                     |
+-------------------------------------+---------------------------------------+-----------------------------+
|                                     | ``IN`` Transfer Helpers               | Completed; Needs Testing    |
+-------------------------------------+---------------------------------------+-----------------------------+
|                                     | ``OUT`` Transfer Helpers              | Planned                     |
+-------------------------------------+---------------------------------------+-----------------------------+



```

## Support for Host Mode

The Torii-USB library currently does not provide any support for operating as a USB host; though the low-level USB
communications interfaces have been designed to allow for eventual host support. Host support is not currently
a priority, but contributions are welcome.
