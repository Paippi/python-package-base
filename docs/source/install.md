# Installation

## Clone the Repository

```console
$ git clone git@github.com:Paippi/python-package-base.git
$ cd python-package-base
```

## Basic Install

% start-basic-install

```console
$ pipenv install
$ # or
$ pip install .
```

% end-basic-install

## Development Install

% start-development-install

```console
$ pipenv install --dev
$ # or
$ pip install -e ".[doc, test]"
```

% end-development-install

## Application Deployment Install

% start-application-deployment-install

Use this when your application is released and deployed to get the exact
versions that worked during development down to the hashes.

```
$ pipenv sync
```

% end-application-deployment-install
