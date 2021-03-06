#from minasu import settings
from ..db import item as item_module
import os, shutil


class bucket():
    def __init__(
        self,
        instance_object,
        bucket_name,
    ):
        self.instance_object = instance_object
        self.buckets = self.instance_object.instance_path
        self.bucket_name = bucket_name
        self.bucket_path = self.instance_object.instance_path + "/" + self.bucket_name


    def list(self):
        # get all buckets
        return [x for x in os.listdir(self.buckets)]


    def create(self):
        bucket_path = self.instance_object.instance_path + "/" + self.bucket_name
        if os.path.exists(bucket_path):
            # not creating anything if it's already there
            return False
        else:
            # create folder representing bucket
            os.makedirs(bucket_path)
            return True


    def destroy(self):
        bucket_path = self.instance_object.instance_path + "/" + self.bucket_name

        if os.path.exists(bucket_path):
            shutil.rmtree(bucket_path)
            return True
        else:
            return False


    def item(
        self,
        item_name=None,
        #item_content=None
    ):
        return item_module.item(
            self.bucket_name,
            self.bucket_path,
            item_name,
            #item_content,
        )
