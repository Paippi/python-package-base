# Getting Started
 
## Introduction

The project base is intended to be used with `pipenv`, though other tools, such
as `pip`, may be used as well. See [pipenv quick start
guide](https://pipenv.pypa.io/en/latest/quick_start.html). Also
[pyenv](https://github.com/pyenv/pyenv) is recommended to be installed for easy
access of different python environments.

(setup-package)=
## Setup Your Package

```{important}
Before diving into the package-setup instructions, it's important to
distinguish between library and application requirements. This is also stated
in the third bullet point in the list below this note:

* **If you're building a library**, list its dependencies in the
  `pyproject.toml` file
* **If you're building an application**, use the `Pipfile.lock` file that
  `pipenv` creates when you install the package. One can then install the
  dependencies using `pipenv sync`.

Consequently, when you're developing an application, the `Pipfile.lock` should
be committed to version control. When you're developing a library, you should
**not** commit `Pipfile.lock`.
```

1. Copy this repository and rename it with your package name (exclude `.git/`)
   or simply fork.
2. from `src` directory rename `package_name` with the name of your package

   ```console
   $ mv src/package_name src/my_packet
   ```
3. Open `pyproject.toml`
    * Search for the following string `# ! CHANGE` and replace the lines below
      them with suitable information.
    * **IF** your package is a library define its dependencies in the
      `"project.dependencies"`.

      ```python
      [project]
      ...
      dependencies = [
          "my_dependency",
          "my_other_dep < 2",
      ]
      ...
      ```
    * **IF** your package is an application install the dependencies using
      `pipenv` and commit the `Pipfile.lock` 
4. Open `src/your_package/__init__.py`
    * fix the author on line 10
    ```python
    # Author: Firstname Lastname <email>
    ```
5. Open `Pipfile` and change the `package-name` to match yours.

    ```
    [packages]
    package-name = {file = "."}
    ^^^^^^^^^^^^

    [dev-packages]
    package-name = {extras = ["doc", "test"], file = ".", editable = true}
    ^^^^^^^^^^^^
    ```

    ```{warning}
    As of when this documentation was written, `pipenv` has changed `path`
    attribute to `file`. This attribute isn't documented but can potentially cause
    issues for older versions of `pipenv`. If that's the case consider renaming the
    attirbute as `path`.
    See [pypa/pipenv#6505](https://github.com/pypa/pipenv/issues/6505).
    ```

---

## Packet Installation Test

After changing the package details in [setup package](#setup-package) the
package name should be changed and the packet can be installed with either:

(development-install)=
```{include} install.md
:start-after: "% start-development-install"
:end-before: "% end-development-install"
```

Or if you just need the basic installation you can use:

(install)=
```{include} install.md
:start-after: "% start-basic-install"
:end-before: "% end-basic-install"
```

After installing the packet, test that you can import it.

```
$ python
>>> import package_name
```

If your package has some functionality that can be tested try to use it, or
better if it has tests, [run the tests](#run-tests).

```python
>>> package_name.__version__
'<package version>'
>>> package_name.foo()
'foo'
```

---

## Setup Automated Documentation

The documentation is mainly automatic, but requires some manual changes, and the
`doc` extras defined in `pyproject.toml`.

From `docs/source/index.md` change the title to fit your needs.

```markdown
# package-name documentation
```

From the same document change the package name to match with your package's name.

````markdown
## API Reference

```{eval-rst}
.. autosummary::
   :toctree: _autosummary
   :template: custom-module-template.rst
   :recursive:

   <package_name>     <---- This line
```
````

See [autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html) for more details.

## Document Generation

```console
$ pipenv run build-docs
```

Open the webpage in your browser `$ xdg-open docs/build/html/index.html`.

---

## Testing

Testing is performed with `pytest` & `tox`, which make it easy to work with
several Python versions. The tests are located at `tests/` folder.

[pytest documentation](https://docs.pytest.org/en/stable/contents.html)  \
[tox documentation](https://tox.wiki/en/latest/user_guide.html)

**Running the tests**

(run-tests)=
```console
$ # To run test for multiple python versions run.
$ pipenv run test
$ # To run specific environments
$ pipenv run test -- -e build,docs
$ # List all envs with
$ pipenv run test -- -l
$ # Or simply run within your environment with.
$ pytest
```

Typically you run the test suite while you're developing. See the [development
installation](#development-install) section for details.

## Binary Compilation

The code can be compiled to binary utilizing `nuitka` by commenting and
uncommenting the following lines in `pyproject.toml`. This is useful if you
want the performance increase from compiled code or if you want to protect your
codebase when distributed.

```toml
[build-system]
requires = [
    # The minimum setuptools version is specific to the PEP 517 backend,
    # and may be stricter than the version required in `setup.py`
    "setuptools >= 77.0.3",
    "wheel",

    # To build with nuitka (binary) uncomment the following line.
    # "nuitka", <------------------ Uncomment
]
build-backend = "setuptools.build_meta" # <--------- Remove/comment out

# To build with nuitka (binary) uncomment the following line.
# build-backend = "nuitka.distutils.Build" <------------ Uncomment
```

That's it now you should be able to [install the packet](#install) normally or [build distribution files](build-instructions.md).
