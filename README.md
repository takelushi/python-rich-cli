# Python Rich CLI

You can quickly start development rich Python CLI application with this repository.

## Requirements

* Poetry

## Setup

```sh
poetry install
```

## Run command

```sh
poetry shell
# Simple command
command1
# Click simple command
command2 --help
# Click group command.
command3 --help
# Rich command.
command4 --help
```

## Testing

```sh
poetry run pytest
```

## Ecosystem

* Poetry
   * Python environment management.
* Click
   * CLI development kit.
* pytest
   * Testing framework.
* Loguru
   * Simple logger.
