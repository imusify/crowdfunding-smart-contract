from boa.blockchain.vm.Neo.Storage import GetContext, Get, Put, Delete
from boa.code.builtins import concat


class StorageAPI():
    """
    Wrapper for the storage api
    """
    ctx = GetContext()

    def get(self, key):

        return Get(self.ctx, key)

    def put(self, key, value):

        Put(self.ctx, key, value)

    def delete(self, key):

        Delete(self.ctx, key)

    def get_crowdfunding_members_key(self, address):
        key = concat(address, "crowdfunding_meta")
        return key

    def get_crowdfunding_total_key(self, address):
        key = concat(address, "crowdfunding_total")
        return key

    def get_crowdfunding_numcontrib_key(self, address):
        key = concat(address, "crowdfunding_numcontrib")
        return key
