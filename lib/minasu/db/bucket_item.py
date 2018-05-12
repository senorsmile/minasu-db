import os


class bucket_item():
    ''' bucket_item exposes operation interfaces to the items in the bucket
    '''
    def __init__(
         self,
         bucket_name,
         bucket_path
    ):
        self.bucket_name = bucket_name
        self.bucket_path = bucket_path

    def item_list(bucket_path):
        ''' list all the items in the bucket
        '''
        return [x for x in os.listdir(bucket_path)]

    def item_read(bucket_path, item):
        ''' return the item content
        '''
        pass

    def item_edit(bucket_path, item, content=0):
        ''' create or edit an item and its content
        '''
        f = open(bucket_path + "/" + item + ".yml", mode='a')
        if content != 0:
            f.write(content)
        else:
            f.write('---')
        f.close()

    def item_delete(bucket_path, item):
        ''' delete item in the bucket
        '''
        os.remove(bucket_path + "/" + item + ".yml")
        return True
