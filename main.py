import json
from pathlib import Path

if __name__ == '__main__':

    # get block rewards
    home = str(Path.home())
    milestone = home + "/solar-core/packages/crypto/src/networks/mainnet/milestones.json"
    print(milestone)
    quit()
    f = open(milestone)
    data = json.load(f)
    
    print(data)
    quit()
       
    # get current voter information
    # do math and calculations
    # output something
    
 
