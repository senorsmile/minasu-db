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

# Set test data
test_data = dict(
  A='a',
  B='b',
  C='c'
)


class TestMinamu(unittest.TestCase):
    def setUp(self):
        self.instance_name = "testdb"
        self.instance_dir = "./tests"
        self.instance_path = self.instance_dir + "/" + self.instance_name

        self.test_instance = db(
            self.instance_name,
            self.instance_dir,
        )

    # def test_default_settings(self):
    #     print("****** Default settings")
    #     print(yaml.dump(settings.default_settings, default_flow_style=False))
    #     print()

    def test_instance_load_create_destroy(self):
        # Verify does NOT exist (yet)
        self.assertFalse(os.path.exists(self.instance_path))

        # Create a fresh instance
        self.test_instance.load()

        # Verify instance DOES exist
        self.assertTrue(os.path.exists(self.instance_path))

        # destroy the instance
        destroyed_data = self.test_instance.destroy()
        self.assertTrue(destroyed_data["destroyed"])

        # Verify does NOT exist (any more)
        self.assertFalse(os.path.exists(self.instance_path))


if __name__ == '__main__':
    unittest.main()
