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


def instance_load(obj):
    # Verify does NOT exist (yet)
    obj.assertFalse(os.path.exists(obj.instance_path))

    # Create a fresh instance
    obj.test_instance.load()

    # Verify instance DOES exist
    obj.assertTrue(os.path.exists(obj.instance_path))


def instance_destroy(obj):
    # destroy the instance
    destroyed_data = obj.test_instance.destroy()
    obj.assertTrue(destroyed_data["destroyed"])

    # Verify does NOT exist (any more)
    obj.assertFalse(os.path.exists(obj.instance_path))


def bucket_create(obj):
        # Verify bucket does NOT exist
        obj.assertFalse(os.path.exists(obj.bucket_path))

        # create bucket
        obj.test_instance.bucket(obj.bucket_name).create()

        # Verify bucket DOES exist
        obj.assertTrue(os.path.exists(obj.bucket_path))


def item_create(obj):
        # Verify item does NOT exist
        obj.assertFalse(os.path.exists(obj.item_path))

        # create bucket
        obj.test_instance.bucket(obj.bucket_name).create()
        # create item
        obj.test_instance.bucket().item(obj.item_name).create()

        # Verify bucket DOES exist
        obj.assertTrue(os.path.exists(obj.bucket_path.item_path))


def bucket_destroy(obj):
        # destroy bucket
        obj.test_instance.bucket(obj.bucket_name).destroy()

        # Verify bucket does NOT exist
        obj.assertFalse(os.path.exists(obj.bucket_path))


class TestMinamu(unittest.TestCase):
    def setUp(self):
        self.instance_name = "test_instance"
        self.instance_dir = "./tests"
        self.instance_path = self.instance_dir + "/" + self.instance_name

        self.test_instance = db(
            self.instance_name,
            self.instance_dir,
        )

        self.bucket_name = "bucket1"
        self.bucket_path = self.instance_path + "/" + self.bucket_name
        self.bucket_item = "file1"
        self.item_path = self.bucket_path + "/" + self.bucket_item + ".yml"


    def test_instance_load_create_destroy(self):
        instance_load(self)
        instance_destroy(self)


    def test_bucket_create_destroy(self):
        instance_load(self)

        # create the bucket dir
        ##if not os.path.exists(self.bucket_path):
        ##    os.makedirs(self.bucket_path)
        bucket_create(self)
        bucket_destroy(self)


    # TODO: refactor below into item method testing
#        # open file, and write test_data to it
#        #   TODO: move file writing to "item" methods testing
#        outfile = open(self.bucket_path + "/file1.yml", "w")
#        yaml.dump(test_data, outfile, default_flow_style=False)
#
#        # reload
#        results = self.test_instance.load()
#
#        print("****** bucket test results")
#        print(results)
#
#        # verify test_data matches
#        self.assertEqual(results['buckets']['bucket1']['file1.yml'], test_data)

        instance_destroy(self)

    def test_item_create_destroy(self):
        instance_load(self)

        bucket_create(self)

        item_create(self)
        #item_destroy(self)
        bucket_destroy(self)
        instance_destroy(self)


if __name__ == '__main__':
    unittest.main()
