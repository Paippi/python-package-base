# Building your code

Instructions on how to create distribution packages from your code

## Requirements

* gcc (For windows mingw64 works) (only required if compiling the code)
* build frontend

```
$ pipenv run pip install --group build-tools
```

## Setup (Windows)

Set path to your gcc to CC environment variable (only required if compiling the code).

    $ set CC=C:\mingw64\bin\gcc.exe

## How to build your code

    $ python -m build
    $ # The files will be built in a folder called `build`.

For more options see:

    python -m build --help

Distribution types:

* [wheel](https://wheel.readthedocs.io/en/stable/) (binary distribution)
* [sdist](https://docs.python.org/3.6/distutils/sourcedist.html) (source distribution default gztar)
