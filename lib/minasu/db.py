import os,shutil
from minasu import settings

class db():
    ## create a new db at folder location
    def create(
        instance_name, 
        instance_dir=settings.default_settings["instance_dir"]
    ):
        data = {}
        data["instance_name"] = instance_name
        data["instance_dir"]  = instance_dir + "/"
        instance_path = instance_dir + "/" + instance_name
        data["instance_path"] = instance_path + "/"


        if not os.path.exists(instance_path):
            try:
                os.mkdir(instance_path)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
            data["created"] = True

        else:
            data["created"] = False

        return data

    ## recursively remove a directory and all of its contents
    def destroy(
        instance_name, 
        instance_dir=settings.default_settings["instance_dir"]
    ):
        data = {}
        instance_path = instance_dir + "/" + instance_name

        if os.path.exists(instance_path):
            shutil.rmtree(instance_path)
            data["destroyed"] = True
        else:
            data["destroyed"] = False

        return data

    ## get group

    ## get host

