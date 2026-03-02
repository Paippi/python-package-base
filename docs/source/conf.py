# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

import toml

with open("../../pyproject.toml") as f:
    config = toml.load(f)

with open("../../LICENSE") as f:
    license = f.read()

project = config["project"]["name"]
copyright = license
author = config["project"]["maintainers"][0]["name"]

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx_autodoc_typehints",
    "sphinx.ext.napoleon",
    "myst_parser",
    "sphinx.ext.viewcode",
    "sphinx_argparse_cli",
    "sphinx.ext.autosummary",
]

autosummary_generate = True  # Turn on sphinx.ext.autosummary
autodoc_typehints = "both"

templates_path = ["_templates"]
exclude_patterns = ["*.inc.md", "*.inc.rst"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]
