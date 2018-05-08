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

    def test_instance_load_create(self):
        '''
        Create a fresh instance
        '''
        self.test_instance.load()


    def test_instance_path_exists(self):
        '''
        Test that the instance's dir path exists
        '''
        instance_path_exists = os.path.exists(self.instance_path)
        self.assertTrue(instance_path_exists)


    def test_bucket_create(self):
        ###################
        # TODO:
        #   These lines should be a single api call, 
        #   instead of doing it directly in this test below?
        ###################

        bucket_path = self.instance_path + "/bucket1"

        # create the bucket dir
        if not os.path.exists(bucket_path):
            os.makedirs(bucket_path)

        # open file, and write test_data to it
        outfile = open(bucket_path + "/file1.yml", "w")
        yaml.dump(test_data, outfile, default_flow_style=False)

        ###################

        # reload
        results = self.test_instance.load()

        # verify test_data matches
        self.assertEqual(results['buckets']['bucket1']['file1.yml'], test_data)

    def test_destroy_instance(self):
        # first test that the instance path exists
        instance_exists_result = os.path.exists(self.instance_path)
        self.assertTrue(instance_exists_result)

        # then attempt to destroy the instance
            #TODO: this is not working... the subdirs remove but the main dir remains!
        destroyed_data = self.test_instance.destroy()
        self.assertTrue(destroyed_data["destroyed"])

        # finally test that the instance path does NOT exist
        instance_exists_result2 = os.path.exists(self.instance_path)
        self.assertFalse(instance_exists_result2)

if __name__ == '__main__':
    unittest.main()
