# Python CLI Template Standards

This document defines the architectural patterns, development workflows, and engineering standards for Python CLI applications. When starting a new project from this template, the following structure and standards **must** be implemented.

## Tech Stack
- **Language:** Python 3.10+
- **Testing:** [pytest](https://docs.pytest.org/)
- **Linting/Formatting:** [ruff](https://github.com/astral-sh/ruff)
- **CI/CD:** GitHub Actions

## Mandatory Project Structure
Every project derived from this template must adhere to this layout:

```text
project_root/
├── src/
│   └── <project_name>/       # Project-specific package name
│       ├── __init__.py
│       └── main.py           # CLI entry point
├── tests/
│   ├── __init__.py
│   └── test_main.py          # Corresponding tests
├── .github/
│   └── workflows/
│       └── test.yml          # GitHub Actions CI workflow
├── GEMINI.md                 # This standards document
├── requirements.txt          # Production and dev dependencies
└── README.md                 # User documentation
```

## Engineering Standards

### 1. Code Style & Linting
- Follow PEP 8 conventions.
- Use `ruff` for both linting and formatting.
- **Rule:** Never suppress linting errors with `# noqa` unless there is a documented architectural reason.

### 2. Testing Requirements
- All new features must include unit tests in the `tests/` directory.
- Use `pytest` as the test runner.
- Aim for high test coverage of core CLI logic.
- Tests must be passing in CI before merging.

### 3. CLI Design
- Use `argparse` (standard library) or `click` for command-line argument parsing.
- Ensure the application provides helpful `--help` output.
- Follow standard exit codes (0 for success, non-zero for errors).

### 4. Dependency Management
- All dependencies must be pinned in `requirements.txt`.
- Development-only dependencies should be clearly separated if the project grows large.

### 5. Documentation
- Maintain an up-to-date `README.md` with installation and usage instructions.
- Use type hints for all function signatures.
- Write docstrings (Google or NumPy style) for public modules and functions.

## Workflows

### Running Tests
```bash
pytest
```

### Linting
```bash
ruff check .
```

### Formatting
```bash
ruff format .
```
