#!/usr/bin/env python3

# -----------------
# global vars
# -----------------
app_version = "v0.0.2"


# -----------------
# imports
# -----------------
import os
import sys


# -----------------
# app imports
# -----------------
# get realpath, go up dir then add lib to sys.path
sys.path.append(os.path.dirname(os.path.realpath(__file__)).rsplit("/",1)[0] + '/lib/')
from bovine_inventory import db


# -----------------
# main
# -----------------
if __name__ == "__main__":
    print("This is bovine-db version: " + app_version)
