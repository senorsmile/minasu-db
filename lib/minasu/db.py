from minasu import settings
import os, shutil, yaml


class db():
    def __init__(
        self,
        instance_name,
        instance_dir=settings.default_settings["instance_dir"]
    ):
        self.instance_name = instance_name
        self.instance_dir  = instance_dir
        self.instance_path = self.instance_dir + "/" + self.instance_name

    # create a new db at folder location
    # def load(self) -> results[JSON]:
    # create path if doesn't exist
    # for each dir (bucket)
    #     for each yml file
    #         yaml.load()
    # mkdir lockdir

    def load(self):
        data = {}
        # data["instance_name"] = self.instance_name
        # data["instance_dir"]  = self.instance_dir + "/"
        # data["instance_path"] = self.instance_path + "/"

        if not os.path.exists(self.instance_path):
            try:
                os.mkdir(self.instance_path)
                # temporary bucket creation until write method is working
                os.mkdir(self.instance_path + "/test_dir1")
                os.mkdir(self.instance_path + "/test_dir2")
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
            data["created"] = True

        else:
            data["created"] = False
            print(self.instance_path)

        self.load_all_buckets()

        return data

    # recursively remove a directory and all of its contents
    def destroy(self):
        data = {}

        if os.path.exists(self.instance_path):
            shutil.rmtree(self.instance_path)
            data["destroyed"] = True
        else:
            data["destroyed"] = False

        return data

    def load_all_buckets(self):
        '''Load all files within buckets

        Walk the instance path directory,
        loading all yml/yaml within every bucket
        '''

        buckets = {}
        list_of_buckets = os.listdir(self.instance_path)
        print(list_of_buckets)
        for bucket in list_of_buckets:
            if bucket.lower().endswith(('.yml', '.yaml')): #ignore non yaml files
                with open(self.instance_path + bucket, 'r') as stream:
                    try:
                        buckets[bucket] = yaml.safe_load(stream)
                    except yaml.YAMLError as exc:
                        print(exc)
            else:
                pass


    ## get group

    ## get host
