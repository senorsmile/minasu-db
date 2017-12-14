#!/usr/bin/env python3

# -----------------
# imports
# -----------------
import os,sys,yaml
import unittest


# -----------------
# app imports
# -----------------
# get realpath, go up dir then add lib to sys.path
sys.path.append(os.path.dirname(os.path.realpath(__file__)).rsplit("/",1)[0] + '/lib/')
from minasu.db import db
from minasu    import settings

# -----------------
# main tests
# -----------------


class TestMinamu(unittest.TestCase):
    def setUp(self):
        self.instance_name = "testdb"
        self.instance_dir = "./tests"

        self.test_instance = db(
            self.instance_name,
            self.instance_dir,
        )

    # def test_default_settings(self):
    #     print("****** Default settings")
    #     print(yaml.dump(settings.default_settings, default_flow_style=False))
    #     print()

    def test_create_instance(self):
        results = self.test_instance.load()
        # print(yaml.dump(results, default_flow_style=False))
        self.assertTrue(results["created"])

    def test_create_instance_exists(self):
        results = self.test_instance.load()
        self.assertFalse(results["created"])

    def test_destroy_instance(self):
        results = self.test_instance.destroy()
        self.assertTrue(results["destroyed"])

if __name__ == '__main__':
    unittest.main()
