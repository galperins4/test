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
    
    # get delegate order
    delegates = client.delegates.all()
    delegate_list = {}
    for i in delegates['data'][:delegate_number]:
        delegate_list[i['rank']] = {'username': i['username'], 'votes': i['votes'],
                                   'block reward': reward_dict[i['rank']]}

    print(delegate_list)        
    # get current voter information
    # do math and calculations
    # output something
    
 
