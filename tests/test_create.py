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

    def test_load_instance_create(self):
        '''Create a fresh instance

        Testing if instance directory is create on load
        '''
        self.test_instance.load()
        result = os.path.exists(self.instance_path)
        self.test_instance.destroy()
        self.assertTrue(result)

    def test_load_instance_exists(self):
        os.makedirs(self.instance_path + "/bucket1")
        outfile = open(self.instance_path + "/bucket1/" + "file1.yml", "w")
        yaml.dump(test_data, outfile, default_flow_style=False)
        results = self.test_instance.load()
        self.test_instance.destroy()
        self.assertEqual(results['buckets']['bucket1']['file1.yml'], test_data)

    def test_destroy_instance(self):
        self.test_instance.load()
        result = os.path.exists(self.instance_path)
        self.test_instance.destroy()
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
