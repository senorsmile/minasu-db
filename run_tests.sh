#!/usr/bin/env bash

#TODO: is there a way to make tox run pipenv?
#pip list --format=legacy | grep pipenv >/dev/null || {
#  pip install pipenv
#}

pipenv run python tests/test_instance.py
