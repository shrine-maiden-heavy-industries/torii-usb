# Installation

```{warning}
The following instructions are a work-in-progress and may not be entirely up to date.
```

Torii-USB requires Python >= 3.10, and [Yosys] >= 0.30 except for 0.37 due to a Verilog backend bug. Torii-USB has been tested with [CPython], but might possibly run under [PyPy].

Torii-USB is built off of the [Torii] Hardware Definition Language, as such that is also required.

## Installing Prerequisites

Prior to installing Torii-USB, you must install all of its prerequisites and requirements.

### Installing Python

First off, install `python` and `pip` onto your system if the're not there already.


```{eval-rst}
.. tab:: Arch-like

	.. code-block:: console

		$ sudo pacman -S python python-pip

.. tab:: Other Linux

	.. warning:: These instructions may be incorrect or incomplete!

	.. tab:: Debian-like

		For `Debian <https://www.debian.org/>`_ based systems, use ``apt`` to install ``python3`` and ``python3-pip``

		.. code-block:: console

			$ sudo apt install python3 python3-pip

.. tab:: macOS

	Install `Homebrew <https://brew.sh/>`_ if not done already, then install the requirements.

	.. code-block:: console

		$ brew install python

.. tab:: Windows

	.. warning:: These instructions may be incorrect or incomplete!

	Download the latest Python installer from the `python downloads <https://www.python.org/downloads/>`_ page.

	Follow the instructions and ensure that the installer installs ``pip`` and puts the python executable in your ``%PATH%``
```


### Installing Yosys

```{eval-rst}
.. tab:: Arch-like

	On Arch Linux and Arch-likes, you can install nightly packages which are located in the `AUR <https://aur.archlinux.org/>`_ with an AUR helper or using ``makepkg`` directly.


	Via an AUR helper like ``yay``

	.. code-block:: console

		$ yay -S yosys-nightly nextpnr-ice40-nightly nextpnr-ecp5-nightly

	Via ``makepkg`` directly

	.. code-block:: console

		$ git clone https://aur.archlinux.org/yosys-nightly.git
		$ git clone https://aur.archlinux.org/prjtrellis-nightly.git
		$ git clone https://aur.archlinux.org/icestorm-nightly.git
		$ git clone https://aur.archlinux.org/nextpnr-ecp5-nightly.git
		$ git clone https://aur.archlinux.org/nextpnr-ice40-nightly.git
		$ (cd yosys-nightly && makepkg -sic)
		$ (cd prjtrellis-nightly && makepkg -sic)
		$ (cd icestorm-nightly && makepkg -sic)
		$ (cd nextpnr-ecp5-nightly && makepkg -sic)
		$ (cd nextpnr-ice40-nightly && makepkg -sic)


.. tab:: Other Linux

	.. warning:: These instructions may be incorrect or incomplete!

	With other Linux distributions, it is recommended to use the `OSS Cad Suite <https://github.com/YosysHQ/oss-cad-suite-build>`_ nightly build. It provides a full environment of all the tools needed built on a nightly basis.

	Simply download the latest `release <https://github.com/YosysHQ/oss-cad-suite-build/releases>`_ for your architecture, extract it to a good home, and then add it to your ``$PATH``

	.. code-block:: console

		$ curl -LOJ https://github.com/YosysHQ/oss-cad-suite-build/releases/download/2024-07-02/oss-cad-suite-linux-x64-20240702.tgz
		$ tar xfv oss-cad-suite-linux-x64-20240702.tgz
		$ export PATH="`pwd`/oss-cad-suite/bin:$PATH"


.. tab:: macOS

	For macOS systems, it is recommended to use the YoWASP distribution of the toolchain. However if you want to use the native tools, and you are using an Intel based Mac, then the `OSS Cad Suite <https://github.com/YosysHQ/oss-cad-suite-build>`_ has nightly builds for x86_64 versions of Darwin.

	Simply download the latest `release <https://github.com/YosysHQ/oss-cad-suite-build/releases>`_ for your architecture, extract it to a good home, and then add it to your ``$PATH``

	.. code-block:: console

		$ curl -LOJ https://github.com/YosysHQ/oss-cad-suite-build/releases/download/2024-07-02/oss-cad-suite-darwin-x64-20240702.tgz
		$ tar xfv oss-cad-suite-darwin-x64-20240702.tgz
		$ export PATH="`pwd`/oss-cad-suite/bin:$PATH"

.. tab:: Windows

	.. warning:: These instructions may be incorrect or incomplete!

	For Windows systems, it is recommended to use the YoWASP distribution of the toolchain. However if you want to use the native tools, and you are using an Intel based PC, then the `OSS Cad Suite <https://github.com/YosysHQ/oss-cad-suite-build>`_ has nightly builds for x86_64 versions of Windows.

	Simply download the latest `release <https://github.com/YosysHQ/oss-cad-suite-build/releases>`_ for your architecture, extract it to a good home, and then add it to your ``%PATH%``

	.. code-block:: console

		$ call %cd%\oss-cad-suite\environment.bat

```

### Installing Torii

Next, install the latest stable version of [Torii] from [PyPi].

```{eval-rst}
.. tab:: Arch-like

	.. code-block:: console

		$ pip install --user --upgrade torii

.. tab:: Other Linux

	.. code-block:: console

		$ pip install --user --upgrade torii

.. tab:: macOS

	.. code-block:: console

		$ pip install --user --upgrade torii

.. tab:: Windows

	.. code-block:: doscon

		> pip install --upgrade torii


.. platform-picker::

	.. platform-choice:: linux
		:title: Linux

		.. code-block:: console

			$ pip3 install --user --upgrade torii

```

## Installing Torii-USB

The [latest release] of Torii-USB is recommended for any new projects planning to use Torii-USB. It provides the most up-to-date stable version of the API. However, if needed, you can also install a [development snapshot] to get access to the bleeding-edge, however the API may be unstable.

### Latest release

```{eval-rst}
.. tab:: Arch-like

	.. code-block:: console

		$ pip install --user --upgrade torii-usb

.. tab:: Other Linux

	.. code-block:: console

		$ pip install --user --upgrade torii-usb

.. tab:: macOS

	.. code-block:: console

		$ pip install --user --upgrade torii-usb

.. tab:: Windows

	.. code-block:: doscon

		> pip install --upgrade torii-usb


```

### Development snapshot


```{eval-rst}

```{eval-rst}
.. tab:: Arch-like

	.. code-block:: console

		$ pip install --user --upgrade 'torii-usb @ git+https://github.com/shrine-maiden-heavy-industries/torii-usb.git'

.. tab:: Other Linux

	.. code-block:: console

		$ pip install --user --upgrade 'torii-usb @ git+https://github.com/shrine-maiden-heavy-industries/torii-usb.git'

.. tab:: macOS

	.. code-block:: console

		$ pip install --user --upgrade 'torii-usb @ git+https://github.com/shrine-maiden-heavy-industries/torii-usb.git'

.. tab:: Windows

	.. code-block:: doscon

		> pip install --upgrade "torii-usb @ git+https://github.com/shrine-maiden-heavy-industries/torii-usb.git"

```


```

### Editable development snapshot

To install an editable development snapshot of Torii-USB for the first time, run:

```{eval-rst}
.. tab:: Arch-like

	.. code-block:: console

		$ git clone https://github.com/shrine-maiden-heavy-industries/torii-usb
		$ cd torii-usb
		$ pip3 install --user --editable '.'

.. tab:: Other Linux

	.. code-block:: console

		$ git clone https://github.com/shrine-maiden-heavy-industries/torii-usb
		$ cd torii-usb
		$ pip3 install --user --editable '.'


.. tab:: macOS

	.. code-block:: console

		$ git clone https://github.com/shrine-maiden-heavy-industries/torii-usb
		$ cd torii-usb
		$ pip3 install --user --editable '.'


.. tab:: Windows

	.. code-block:: doscon

		> git clone https://github.com/shrine-maiden-heavy-industries/torii-usb
		> cd torii-usb
		> pip install --editable .
```

Any changes made to the `torii-usb` directory will immediately affect any code that uses Torii-USB. To update the snapshot, run:


```{eval-rst}
.. tab:: Arch-like

	.. code-block:: console

		$ cd tori-usb
		$ git pull --ff-only origin main
		$ pip3 install --user --editable '.'

.. tab:: Other Linux

	.. code-block:: console

		$ cd tori-usb
		$ git pull --ff-only origin main
		$ pip3 install --user --editable '.'


.. tab:: macOS

	.. code-block:: console

		$ cd tori-usb
		$ git pull --ff-only origin main
		$ pip3 install --user --editable '.'


.. tab:: Windows

	.. code-block:: doscon

		> cd sol
		> git pull --ff-only origin main
		> pip install --editable .

```

Run the `pip3 install --editable .` command each time the editable development snapshot is updated in case package dependencies have been added or changed. Otherwise, code using Torii-USB may misbehave or crash with an `ImportError`.

[Yosys]: https://github.com/YosysHQ/yosys
[CPython]: https://www.python.org/
[PyPy]: https://www.pypy.org/
[Torii]: https://github.com/shrine-maiden-heavy-industries/torii-hdl
[PyPi]: https://pypi.org/project/torii
[latest release]: #latest-release
[development snapshot]: #development-snapshot
