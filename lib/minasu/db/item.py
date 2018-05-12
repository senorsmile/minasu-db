import bucket


class bucket_item():
    ''' bucket_list exposes operation interfaces to the items in the bucket
    '''
    def __init__(
         self,
         bucket_name
    ):
        self.bucket_name = bucket_name
        self.bucket = bucket.load(bucket_name) # bucket.load() is not working yet

    def list(self):
        ''' list all the items in the bucket
        '''
        return [x for x in os.listdir(self.buckets)]
