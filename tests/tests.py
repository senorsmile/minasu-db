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
        self.instance_name = "test_instance"
        self.instance_dir = "./tests"
        self.instance_path = self.instance_dir + "/" + self.instance_name

        self.test_instance = db(
            self.instance_name,
            self.instance_dir,
        )

        self.bucket_path = self.instance_path + "/bucket1"


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

    def test_bucket_create(self):
        # Verify does NOT exist (yet)
        self.assertFalse(os.path.exists(self.instance_path))

        # Create a fresh instance
        self.test_instance.load()

        # Verify instance DOES exist
        self.assertTrue(os.path.exists(self.instance_path))

        # create the bucket dir
        #   TODO: use method instead of manual creation here
        if not os.path.exists(self.bucket_path):
            os.makedirs(self.bucket_path)

        # open file, and write test_data to it
        #   TODO: move file writing to "item" methods testing
        outfile = open(self.bucket_path + "/file1.yml", "w")
        yaml.dump(test_data, outfile, default_flow_style=False)

        # reload
        results = self.test_instance.load()

        print("****** bucket test results")
        print(results)

        # verify test_data matches
        self.assertEqual(results['buckets']['bucket1']['file1.yml'], test_data)






        # destroy the instance
        destroyed_data = self.test_instance.destroy()
        self.assertTrue(destroyed_data["destroyed"])

        # Verify does NOT exist (any more)
        self.assertFalse(os.path.exists(self.instance_path))

if __name__ == '__main__':
    unittest.main()
