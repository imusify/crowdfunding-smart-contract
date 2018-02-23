from nex.common.storage import StorageAPI
from boa.code.builtins import concat
from boa.blockchain.vm.Neo.Runtime import CheckWitness, Notify


def reward_user(address):
    """
    """
    
    ## to be called from Main upon 'operation == "reward"' if called by master wallet
    
    ## make use of 'calculate_reward' below
    
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
    

def level_up(address):
    """
    """
    
    ## make use of 'level_up' below
    
    """
    C# REFERENCE IMPLEMENTATION
    
            BigInteger newLevel = LevelOf(account) + 1;
            
            Storage.Put(Storage.CurrentContext, Key("L", account), newLevel);
            
            return newLevel;
    """
    
    return True
    

def level_of(address):
    """
    """
    
    ## to be called from Main upon 'operation == "level"' if called by master wallet
    
    """
    C# REFERENCE IMPLEMENTATION
    
            BigInteger nLevel = 0;

            byte[] level = Storage.Get(Storage.CurrentContext, Key("L", account));

            if (level != null)
                nLevel = level.AsBigInteger();

            return nLevel;
    """
    
    return True
    