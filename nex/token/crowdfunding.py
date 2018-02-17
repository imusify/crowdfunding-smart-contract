from nex.common.storage import StorageAPI
from boa.code.builtins import concat
from boa.blockchain.vm.Neo.Runtime import CheckWitness, Notify


def crowdfunding_create(args):
    """ args:
     0: crowdfunding address
     1..n: member addresses
    """

    print("Create a crowdfunding")
    storage = StorageAPI()

    crowdfunding_address = args[0]
    crowdfunding_meta_key = storage.get_crowdfunding_members_key(crowdfunding_address)
    print(crowdfunding_meta_key)

    # Check for minimum number of arguments
    nargs = len(args)
    if nargs < 3:
        print("Error: need at least 3 arguments: (1) crowdfunding address, (2+3) member addresses")
        return False

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
    member_addresses = args[1]
    print(member_addresses)
    i = 2
    while i < nargs:
        member_address = args[i]
        print(member_address)
        i += 1
        member_addresses = concat(member_addresses, member_address)

    storage.put(crowdfunding_meta_key, member_addresses)
    print("Created the crowdfunding with those member addresses")
    print(member_addresses)


def is_crowdfunding_address(crowdfunding_address):
    storage = StorageAPI()
    crowdfunding_meta_key = storage.get_crowdfunding_members_key(crowdfunding_address)
    addresses = storage.get(crowdfunding_meta_key)
    if len(addresses) == 0:
        return False
    return True


def crowdfunding_get_members(crowdfunding_address):
    storage = StorageAPI()

    crowdfunding_meta_key = storage.get_crowdfunding_members_key(crowdfunding_address)
    print(crowdfunding_meta_key)

    # Check if this address or crowdfunding_meta already exists
    addresses = storage.get(crowdfunding_meta_key)
    if len(addresses) == 0:
        print("Error: address does not belong to a crowdfunding")
        return False

    n = len(addresses)
    num_addresses = n / 20

    msg = ["Crowdfunding found. Members:", num_addresses]
    Notify(msg)

    address_list = []
    i = 0
    while i < num_addresses:
        addr = addresses[0:20]
        addresses = addresses[20:]
        address_list.append(addr)
        i += 1

    return address_list


# def crowdfunding_test(args):
