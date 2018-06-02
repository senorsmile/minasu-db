import os
import yaml


class item():
    ''' item exposes operation interfaces to the items in the bucket
    '''
    def __init__(
         self,
         bucket_name,
         bucket_path,
         item_name,

    ):
        self.bucket_name = bucket_name
        self.bucket_path = bucket_path
        self.item_name = item_name
        self.item_path = self.bucket_path + "/" + self.item_name + ".yml"
        self.content = None # i.e. not yet read or written


    def list(self):
        ''' list all the items in the bucket
        '''
        return [x for x in os.listdir(self.bucket_path)]


    def read(self):
        ''' return the item content
        '''
        # TODO: implement me
        if os.path.isfile(self.item_path):
            f = open(self.item_path, mode='r')

            content = yaml.load(f)

            return content

        else:
            return None


    def edit(
            self,
            content=None,
    ):
        ''' create or edit an item and its content
        '''
        self.content = content

        f = open(self.item_path, mode='w')

        if self.content is None:
            # None means that we haven't read the item yet either
            #f.write('---') # do not overwrite the file
            pass
        else:
            f.write(
                yaml.dump(
                    self.content
                )
            )

        f.close()


    def delete(self):
        ''' delete item in the bucket
        '''
        os.remove(self.bucket_path + "/" + self.item_name + ".yml")
        return True
