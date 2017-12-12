#!/usr/bin/env python3

#-----------------
# imports
#-----------------
import os
import sys


#-----------------
# app imports
#-----------------
## get realpath, go up dir then add lib to sys.path
sys.path.append(os.path.dirname(os.path.realpath(__file__)).rsplit("/",1)[0] + '/lib/')
from minasu.db import db



#-----------------
# main tests
#-----------------

instance_name="testdb"
db.create(instance_name)
