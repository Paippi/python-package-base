This repository provides a ready-made scaffold for new Python projects
(application & library development). It bundles the most commonly required
development tools and configuration files, so you can start coding immediately
without assembling the environment from scratch.

Included capabilities:

* **Documentation authoring** - Write project documentation in Markdown or
  reStructuredText.
* **Doc generation** - Build HTML (or other) docs with Sphinx + MyST.
* **API reference** - Automatic API pages are created from the source tree.
* **Docstring formats** - Support for reStructuredText, NumPy, and Google style
  docstrings via the napoleon extension.
* **Testing** - Run unit and integration tests with pytest.
* **Linting** - Code style enforcement and automatic formatting.
* **Multi-environment support** - Use tox together with pyenv to test against
  several Python versions.
* **Package building** - Produce PEP 517-compliant wheels and source
  distributions.
* **Build-time dependencies** - Declare build requirements per PEP 518 (via
  `pyproject.toml`).
* **Binary compilation** - Compile your code to binary with Nuitka integration
  for optimzed speed and to obfuscate business logic.
     
How to use 

1. Clone the repository or copy the package skeleton into your project
   directory. 
2. Adjust the metadata in `pyproject.toml` (name, author, etc.).
3. Add your source code under `src/` and write docstrings/documentation in the
   supported formats.
4. Run tests during development via `pytest` or `pipenv run test` during CI for
   multi-python support.
5. Build docs with `pipenv build-docs`.
5. Format and lint your code with `black` and `pylint`.
6. Build the distribution with `python -m build` or `pip wheel .`.
7. Configure your code for binary distribution by configuring Nuitka backend in
   your `pyproject.toml`.

For step-by-step guide see [getting started](getting-started.md).

```{tip}
The package is intended as a baseline; you can extend or replace any component
to suit particular project needs while preserving the overall structure. 
```

