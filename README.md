# gi

A tiny installable CLI that prints a ghost joke.

Installation

- Install locally: `pip install .`
- Install editable for development: `pip install -e .`

Usage

- Run the CLI: `gi` (prints the joke)
- Alternative subcommands: `gi tstatus`, `gi status`, `gi joke`
- Show version: `gi --version`
- Show help: `gi --help`

Packaging

This project uses a `pyproject.toml` with a console script entrypoint `gi = "gi.main:main"`.

License

MIT (check repository for license file)
