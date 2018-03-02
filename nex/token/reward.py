from nex.common.storage import StorageAPI
from nex.token.mytoken import Token
from nex.token.nep5 import NEP5Handler
from boa.code.builtins import concat
from boa.blockchain.vm.Neo.Runtime import CheckWitness, Notify


def level_of(address):
    """
    Return the level of the user who owns the address.
    """
    storage = StorageAPI()
    level_key = storage.get_level_key(address)
    stored_level = storage.get(level_key)
    return stored_level


def level_up(address):
    """
    Loop up the level of the owner of address. Then raise it
    by 1, put it back into storage and return the new value.
    """
    storage = StorageAPI()
    level_key = storage.get_level_key(address)
    level = level_of(level_key)
    new_level = level + 1
    storage.put(level_key, new_level)
    return new_level


def calculate_reward(address):
    """
    Apply the calculation function for the user reward.
    """
    storage = StorageAPI()
    level_key = storage.get_level_key(address)
    level = level_of(address)
    bonus_factor = 1

    if level > 1:
        bonus_factor = 2
    if level > 3:
        bonus_factor = 5
    if level > 9:
        bonus_factor = 20

    basic_reward = 100000000
    reward = basic_reward * bonus_factor
    return reward


def reward_user(address):
    """
    Raise the user level corresponding to address and reward him/her.
    """
    token = Token()
    if not CheckWitness(token.owner):
        print("Must be owner to reward")
        return False

    nep = NEP5Handler()
    storage = StorageAPI()
    level = level_up(address) ### you might wanna just set this constant for debugging purposes
    reward = calculate_reward(level)
    success = nep.do_transfer(storage, token.owner, address, reward)
    return success
