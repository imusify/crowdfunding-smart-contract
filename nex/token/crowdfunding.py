from nex.common.storage import StorageAPI
from boa.code.builtins import concat


def crowdfunding_create(args):
    """ args:
     0: crowdfunding address
     1..n: member addresses
    """

    print("Create a crowdfunding")
    storage = StorageAPI()

    crowdfunding_address = args[0]
    crowdfunding_meta_key = storage.get_crowdfunding_meta_key(crowdfunding_address)
    print(crowdfunding_meta_key)

    # Check if this address or crowdfunding_meta already exists
    balance = storage.get(crowdfunding_address)
    if len(balance) > 0:
        print("Error: address is already in use")
        return False

    meta = storage.get(crowdfunding_meta_key)
    if len(meta) > 0:
        print("Error: crowdfunding is already setup")
        return False

    # Build list of addresses to store in meta key
    print("Build list of addresses")
    nargs = len(args)
    member_addresses = ''
    i = 1
    while i < nargs:
        # print(i)
        member_address = args[i]
        # print(member_address)
        i += 1
        member_addresses = concat(member_addresses, member_address)

    storage.put(crowdfunding_meta_key, member_addresses)
    print("Created the crowdfunding with those member addresses")
    print(member_addresses)
