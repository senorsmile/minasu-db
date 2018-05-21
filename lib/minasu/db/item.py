import os


class item():
    ''' bucket_item exposes operation interfaces to the items in the bucket
    '''
    def __init__(
         self,
         bucket_name,
         bucket_path,
         item_name,
         item_content

    ):
        self.bucket_name = bucket_name
        self.bucket_path = bucket_path
        self.item_name = item_name
        self.item_content = item_content

    def list(self):
        ''' list all the items in the bucket
        '''
        return [x for x in os.listdir(self.bucket_path)]

    def read(self):
        ''' return the item content
        '''
        pass

    def edit(self):
        ''' create or edit an item and its content
        '''
        f = open(self.bucket_path + "/" + self.item_name + ".yml", mode='a')
        if self.item_content is None:
            f.write('---')
        else:
            f.write(self.item_content)
        f.close()

    def delete(self):
        ''' delete item in the bucket
        '''
        os.remove(self.bucket_path + "/" + self.item_name + ".yml")
        return True