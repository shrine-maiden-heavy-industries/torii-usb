# Contribution Guidelines

> [!NOTE]
> Contributions that were generated in whole or in-part from any
> language model or AI, such as GitHub Copilot, ChatGPT, BARD, or any other such tool
> are explicitly forbidden and will result in your permanent ban from contributing
> to this project.

## Contributing

Contributions to Torii-USB are released under the following licenses depending on the component:

* [BSD-3-Clause] - Software
* [CC-BY-4.0] - Documentation

Please note that Torii-USB is released with a [Contributor Code of Conduct]. By participating in this project you agree to abide by its terms.

## Development and Testing

Prior working on Torii-USB, ensure you understand have have followed the general [Installation] guide, when installing Torii-USB make sure to add `[dev]` do the package name to ensure the needed development tools are installed along with Torii-USB.

Alternatively, use `pip` to install [nox], like so:

```
$ pip install nox
```

General testing and linting of Torii-USB is done with nox, as such there are some session names to know about:

* `test` - Run the test suite
* `lint` - Run the linter
* `typecheck` - Run the type-checker

Bye default these are configured to run one right after another when invoking `nox` with no arguments, to run a single check, you can run it with passing `-s <session>` to nox, like so:

```
$ nox -s lint
```

[BSD-3-Clause]: ./LICENSE
[CC-BY-4.0]: ./LICENSE.docs
[Contributor Code of Conduct]: ./CODE_OF_CONDUCT.md
[Installation]: https://torii-usb.shmdn.link/install.html
[nox]: https://nox.thea.codes/
