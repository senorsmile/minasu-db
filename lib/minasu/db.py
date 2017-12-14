from minasu import settings
import os,shutil


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
    def create(self):
        data = {}
        # data["instance_name"] = self.instance_name
        # data["instance_dir"]  = self.instance_dir + "/"
        # data["instance_path"] = self.instance_path + "/"

        if not os.path.exists(self.instance_path):
            try:
                os.mkdir(self.instance_path)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
            data["created"] = True

        else:
            data["created"] = False

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

    ## get group

    ## get host
