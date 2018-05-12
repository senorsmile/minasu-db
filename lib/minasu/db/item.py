import os


class bucket_item():
    ''' bucket_item exposes operation interfaces to the items in the bucket
    '''
    # not sure we need this yet
    # def __init__(
    #      self,
    #      bucket_name,
    #      bucket_path
    # ):
    #     self.bucket_name = bucket_name
    #     self.bucket_path = bucket_path

    def list(bucket_path):
        ''' list all the items in the bucket
        '''
        return [x for x in os.listdir(self.bucket_path)]

    def edit(bucket_path, item, content=0):
        ''' create or edit an item and its content
        '''
        f = open(item + ".yml", mode='a')
        if content != 0:
            f.write(content)
        else:
            f.write('---')
        f.close()

    def delete(bucket_path item):
        ''' delete item in the bucket
        '''
        os.remove(self.bucket_path + "/" + item)
        return True
