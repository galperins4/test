import json
from pathlib import Path
from util.util import Util

if __name__ == '__main__':
    delegate_number = 53
    utility = Util()
    client = utility.get_client(6003)
    
    # get block rewards
    home = str(Path.home())
    milestone = home + "/solar-core/packages/crypto/src/networks/mainnet/milestones.json"
    f = open(milestone)
    data = json.load(f)
    reward_dict = {int(k):v for k, v in data[2]['dynamicReward']['ranks'].items()}
    print(reward_dict)
    
    # get delegate order
    delegates = client.delegates.all()
    for i in delegates['data'][:delegate_number]:
        print(i['username'])
        print(i['rank'])
        print(i['votes'])
        
    # get current voter information
    # do math and calculations
    # output something
    
 
