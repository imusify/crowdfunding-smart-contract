from nex.common.storage import StorageAPI
from boa.code.builtins import concat
from boa.blockchain.vm.Neo.Runtime import CheckWitness, Notify
    

def level_of(address):
    """
    Return the level of the user who owns the address. 
    """
    
    level = 0
    
    storage = StorageAPI()
    
    level_key = storage.get_level_key(address)
    
    stored_level = storage.get_level_key(level_key)
    
    if stored_level:
        level = stored_level
        
    return level
    

def level_up(address):
    """
    """
    
    storage = StorageAPI()
    
    level_key = storage.get_level_key(address)
    
    level = level_of(address)
    
    new_level = level + 1
    
    storage.put(level_key, new_level)
    
    return new_level


def reward_user(address):
    """
    """
    
    ## to be called from Main upon 'operation == "reward"' if called by master wallet
    
    ## make use of 'calculate_reward' below
    
    storage = StorageAPI()
    
    """
    C# REFERENCE IMPLEMENTATION
    
                /// Reward user according to his or her user level
            
                byte[] owner = Storage.Get(Storage.CurrentContext, "owner");
            
                // if (Runtime.CheckWitness(owner)) // Enable this clause after CoZ contest
                BigInteger amount = RewardFunction(LevelUp(account));

                Transfer(owner, account, amount);

                return amount;
    """
    
    return True


def calculate_reward(address):
    """
    """
    
    ## make use of 'level_of' below
    
    """
    C# REFERENCE IMPLEMENTATION                 <====== WE DO IT BETTER THIS TIME, THOUGH
    
            /// Compute user reward depending on user level
            
            BigInteger basicReward = 100000000; 
            // TODO test if I can just use 'factor' here
            BigInteger bonusFactor = 1;

            /// Quick level up for demonstration purpose before official launch
            if (level > 1) bonusFactor = 2;
            if (level > 3) bonusFactor = 5;
            if (level > 9) bonusFactor = 20;

            return bonusFactor * basicReward;
    """
    
    return True
    
    