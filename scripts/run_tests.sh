#!/usr/bin/env bash

pushd $(pipenv --where) 1> /dev/null
pipenv requirements --dev > requirements.txt
tox $@
rm requirements.txt
popd 1> /dev/null
