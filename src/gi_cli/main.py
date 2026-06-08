#!/usr/bin/env python3
"""gi - tiny ghost-joke CLI entrypoint."""
from __future__ import annotations

import sys
from . import __version__

# ANSI Escape Codes for Colors
CYAN = "\033[36m"
YELLOW = "\033[33m"
RED = "\033[31m"
BOLD = "\033[1m"
RESET = "\033[0m"


def print_ghost_joke() -> None:
    """Print a colorful ASCII art ghost joke."""
    ghost = f"""
{CYAN}     .-.
    (o o) {YELLOW}boo!{CYAN}
    | O |
     \\ /    {YELLOW}"I am the ghost of commands that
      {CYAN}`      {YELLOW}almost made sense. Try again."{RESET}
"""
    print(ghost)


def show_help() -> None:
    print("gi: simple ghost joke CLI\n")
    print("Usage:\n  gi [tstatus|status|joke]\n")
    print("Options:\n  -h, --help   Show this message\n  --version    Show version")


def main(argv: list[str] | None = None) -> None:
    """Main entrypoint. If no args or known subcommands are provided, print the joke.

    Designed to be installed as a console_script entrypoint (gi -> gi_cli.main:main).
    """
    if argv is None:
        argv = sys.argv[1:]

    if not argv:
        print_ghost_joke()
        return

    cmd = argv[0].lower()
    if cmd in ("tstatus", "status", "joke"):
        print_ghost_joke()
        return

    if cmd in ("-h", "--help"):
        show_help()
        return

    if cmd == "--version":
        print(__version__)
        return

    # Unknown command
    print(f"{RED}gi: unknown command: {cmd}{RESET}", file=sys.stderr)
    sys.exit(2)


if __name__ == "__main__":
    main()
